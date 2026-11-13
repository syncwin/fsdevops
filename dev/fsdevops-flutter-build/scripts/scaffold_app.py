#!/usr/bin/env python3
"""Scaffold a Flutter pub-workspace app with a module registry. Never overwrites files.

Usage:
  python scaffold_app.py <dir> --name <app> --prefix <prefix> [--org com.example]
         [--modules feed,tasks] [--platforms windows,android,ios,web] [--builder-ui] [--no-create]

Needs the Flutter SDK on PATH for `flutter create` (skip with --no-create).
"""
import argparse
import datetime
import re
import shutil
import subprocess
import sys
from pathlib import Path

WRITTEN, SKIPPED = [], []


def write(path: Path, text: str):
    if path.exists():
        SKIPPED.append(str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.lstrip("\n"), encoding="utf-8")
    WRITTEN.append(str(path))


def pkg_pubspec(name, deps, flutter=True):
    lines = [f"name: {name}", "publish_to: none", "resolution: workspace", "",
             "environment:", "  sdk: ^3.6.0", "", "dependencies:"]
    if flutter:
        lines += ["  flutter:", "    sdk: flutter"]
    lines += [f"  {d}" for d in deps]
    lines += ["", "dev_dependencies:", "  flutter_test:", "    sdk: flutter", ""]
    if flutter:
        lines += ["flutter:", "  uses-material-design: true", ""]
    return "\n".join(lines)


def camel(s):
    return "".join(p.capitalize() for p in re.split(r"[_\-]", s))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    ap.add_argument("--name", required=True)
    ap.add_argument("--prefix", required=True)
    ap.add_argument("--org", default="com.example")
    ap.add_argument("--modules", default="home")
    ap.add_argument("--platforms", default="windows,android,ios,web")
    ap.add_argument("--builder-ui", action="store_true")
    ap.add_argument("--no-create", action="store_true")
    a = ap.parse_args()

    for v in (a.name, a.prefix):
        if not re.fullmatch(r"[a-z][a-z0-9_]*", v):
            sys.exit(f"Use lower_snake_case: {v}")
    if not re.fullmatch(r"[a-z][a-z0-9]*(\.[a-z][a-z0-9_]*)+", a.org):
        sys.exit(f"--org must be a reverse-domain id such as com.example: {a.org}")
    if not re.fullmatch(r"[a-z][a-z0-9_]*(,\s*[a-z][a-z0-9_]*)*", a.modules):
        sys.exit(f"--modules must be comma-separated lower_snake_case: {a.modules}")
    if not re.fullmatch(r"(windows|android|ios|web|linux|macos)(,(windows|android|ios|web|linux|macos))*", a.platforms):
        sys.exit(f"--platforms must be a comma list of windows,android,ios,web,linux,macos: {a.platforms}")
    root = Path(a.dir).resolve()
    app_dir = root / "apps" / a.name
    p = a.prefix
    modules = [m.strip() for m in a.modules.split(",") if m.strip()]
    mod_pkgs = [f"{p}_{m}" for m in modules]

    created = False
    if not a.no_create:
        flutter = shutil.which("flutter")
        if not flutter:
            sys.exit("Flutter SDK not on PATH. Install it or pass --no-create.")
        if not (app_dir / "pubspec.yaml").exists():
            subprocess.run([flutter, "create", "--org", a.org, "--project-name", a.name,
                            "--platforms", a.platforms, "--empty", str(app_dir)],
                           check=True)
            created = True
    if created:
        # Only files flutter create just made are changed here.
        pub = app_dir / "pubspec.yaml"
        text = pub.read_text(encoding="utf-8")
        extra = "".join(f"  {d}: any\n" for d in [f"{p}_core", f"{p}_ui", *mod_pkgs])
        text = re.sub(r"^(environment:)", "resolution: workspace\n\n\\1", text, count=1, flags=re.M)
        text = re.sub(r"(^dependencies:\n  flutter:\n    sdk: flutter\n)",
                      "\\1  flutter_riverpod: ^3.0.0\n  go_router: ^16.0.0\n" + extra, text, count=1, flags=re.M)
        text = re.sub(r"^version:.*$", "version: 0.0.1+1", text, count=1, flags=re.M)
        pub.write_text(text, encoding="utf-8")
        (app_dir / "lib/main.dart").write_text(
            "import 'package:flutter/material.dart';\n"
            "import 'package:flutter_riverpod/flutter_riverpod.dart';\n\n"
            "import 'app.dart';\n\n"
            "void main() => runApp(ProviderScope(overrides: appOverrides, child: const App()));\n",
            encoding="utf-8")
        for t in (app_dir / "test").glob("widget_test.dart"):
            t.unlink()

    write(root / "pubspec.yaml", "\n".join(
        [f"name: {a.name}_workspace", "publish_to: none", "", "environment:", "  sdk: ^3.6.0", "",
         "workspace:", f"  - apps/{a.name}", f"  - packages/{p}_core", f"  - packages/{p}_ui"]
        + [f"  - packages/{m}" for m in mod_pkgs] + ["", "dev_dependencies:", "  flutter_lints: ^5.0.0", ""]))
    write(root / "analysis_options.yaml", """
include: package:flutter_lints/flutter.yaml

linter:
  rules:
    - prefer_const_constructors
    - prefer_final_locals
    - avoid_print
    - require_trailing_commas
    - unawaited_futures
    - use_build_context_synchronously

analyzer:
  exclude:
    - "**/*.g.dart"
    - "**/*.freezed.dart"
""")

    # core
    write(root / f"packages/{p}_core/pubspec.yaml", pkg_pubspec(f"{p}_core", ["flutter_riverpod: ^3.0.0", "go_router: ^16.0.0"]))
    write(root / f"packages/{p}_core/lib/{p}_core.dart", f"""
export 'src/app_module.dart';
export 'src/enabled_modules.dart';
""")
    write(root / f"packages/{p}_core/lib/src/app_module.dart", """
import 'package:flutter/widgets.dart';
import 'package:go_router/go_router.dart';

/// Contract every module package implements; the shell lists them once.
abstract class AppModule {
  const AppModule();

  /// Stable id, also the route prefix: '/<id>'.
  String get id;
  String get title;
  IconData get icon;
  List<RouteBase> get routes;
}
""")
    write(root / f"packages/{p}_core/lib/src/enabled_modules.dart", """
import 'package:flutter_riverpod/flutter_riverpod.dart';

/// Ids of enabled modules. Override in the shell with the real source
/// (local default, cached remote flags or user settings).
final enabledModuleIdsProvider = Provider<Set<String>>((ref) => const {});
""")

    # ui
    ui_owner = "builder-owned: edit with ownership rules" if a.builder_ui else "developer-owned"
    write(root / f"packages/{p}_ui/pubspec.yaml", pkg_pubspec(f"{p}_ui", []))
    write(root / f"packages/{p}_ui/lib/{p}_ui.dart", f"""
// {ui_owner}
export 'src/theme.dart';
""")
    write(root / f"packages/{p}_ui/lib/src/theme.dart", """
import 'package:flutter/material.dart';

@immutable
class AppTokens extends ThemeExtension<AppTokens> {
  const AppTokens({this.space = 8, this.radius = 12});

  final double space;
  final double radius;

  @override
  AppTokens copyWith({double? space, double? radius}) =>
      AppTokens(space: space ?? this.space, radius: radius ?? this.radius);

  @override
  AppTokens lerp(AppTokens? other, double t) => other == null
      ? this
      : AppTokens(
          space: lerpDouble(space, other.space, t),
          radius: lerpDouble(radius, other.radius, t),
        );

  static double lerpDouble(double a, double b, double t) => a + (b - a) * t;
}

ThemeData buildTheme(Brightness brightness) => ThemeData(
      useMaterial3: true,
      colorScheme: ColorScheme.fromSeed(
        seedColor: const Color(0xFF3F51B5),
        brightness: brightness,
      ),
      visualDensity: VisualDensity.adaptivePlatformDensity,
      extensions: const [AppTokens()],
    );
""")

    # modules
    for m, pkg in zip(modules, mod_pkgs):
        cls = camel(m) + "Module"
        write(root / f"packages/{pkg}/pubspec.yaml", pkg_pubspec(pkg, [
            f"{p}_core: any", f"{p}_ui: any", "flutter_riverpod: ^3.0.0", "go_router: ^16.0.0"]))
        write(root / f"packages/{pkg}/lib/{pkg}.dart", f"export 'src/{m}_module.dart';\n")
        write(root / f"packages/{pkg}/lib/src/{m}_module.dart", f"""
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:{p}_core/{p}_core.dart';

class {cls} extends AppModule {{
  const {cls}();

  @override
  String get id => '{m.replace('_', '-')}';

  @override
  String get title => '{camel(m)}';

  @override
  IconData get icon => Icons.dashboard_outlined;

  @override
  List<RouteBase> get routes => [
        GoRoute(
          path: '/$id',
          builder: (context, state) => const _{camel(m)}Screen(),
        ),
      ];
}}

class _{camel(m)}Screen extends StatelessWidget {{
  const _{camel(m)}Screen();

  @override
  Widget build(BuildContext context) =>
      const Center(child: Text('{camel(m)}'));
}}
""")

    # shell
    imports = "\n".join(f"import 'package:{pkg}/{pkg}.dart';" for pkg in mod_pkgs)
    mod_list = ", ".join(f"{camel(m)}Module()" for m in modules)
    write(app_dir / "lib/registry.dart", f"""
import 'package:{p}_core/{p}_core.dart';
{imports}

/// Every module the app ships. Enabled ones come from enabledModuleIdsProvider.
const List<AppModule> allModules = [{mod_list}];
""")
    write(app_dir / "lib/router.dart", f"""
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:{p}_core/{p}_core.dart';

import 'registry.dart';

final enabledModulesProvider = Provider<List<AppModule>>((ref) {{
  final ids = ref.watch(enabledModuleIdsProvider);
  return allModules.where((m) => ids.contains(m.id)).toList();
}});

final routerProvider = Provider<GoRouter>((ref) {{
  final modules = ref.watch(enabledModulesProvider);
  return GoRouter(
    initialLocation: modules.isEmpty ? '/empty' : '/${{modules.first.id}}',
    routes: [
      GoRoute(
        path: '/empty',
        builder: (context, state) =>
            const Scaffold(body: Center(child: Text('No modules enabled'))),
      ),
      for (final m in modules) ...m.routes,
    ],
  );
}});
""")
    default_ids = ", ".join(f"'{m.replace('_', '-')}'" for m in modules)
    write(app_dir / "lib/app.dart", f"""
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:{p}_core/{p}_core.dart';
import 'package:{p}_ui/{p}_ui.dart';

import 'router.dart';

const defaultEnabledModules = {{{default_ids}}};

final appOverrides = [
  enabledModuleIdsProvider.overrideWithValue(defaultEnabledModules),
];

class App extends ConsumerWidget {{
  const App({{super.key}});

  @override
  Widget build(BuildContext context, WidgetRef ref) => MaterialApp.router(
        title: '{camel(a.name)}',
        theme: buildTheme(Brightness.light),
        darkTheme: buildTheme(Brightness.dark),
        routerConfig: ref.watch(routerProvider),
      );
}}
""")
    write(app_dir / "test/app_test.dart", f"""
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:{a.name}/app.dart';

void main() {{
  testWidgets('starts on the first enabled module', (tester) async {{
    await tester.pumpWidget(ProviderScope(overrides: appOverrides, child: const App()));
    await tester.pumpAndSettle();
    expect(find.text('{camel(modules[0])}'), findsOneWidget);
  }});
}}
""")
    # Secure by default (rules: fsdevops-security): secrets never committed, scanned before every commit.
    write(root / ".gitignore", """
.dart_tool/
build/
.env
.env.*
!.env.example
*.jks
*.keystore
*.p12
*.pfx
*.pem
key.properties
secrets*.json
!secrets*.example.json
""")
    write(root / ".pre-commit-config.yaml", """
# Run `pre-commit install` once. `rev` is pinned to a full commit SHA (tag in the comment); review it when updating.
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: d5c275d6b2140fcb59bc3f58b8dd5350f5b19df6  # v8.24.2
    hooks:
      - id: gitleaks
""")
    if a.builder_ui:
        write(root / ".claude/ownership.md", f"""
| Path | Owner | Rule for code edits |
|---|---|---|
| packages/{p}_ui/** | Visual builder | Builder-safe rules in fsdevops/references/ownership.md; commit before and after |
| **/*.g.dart, **/*.freezed.dart | build_runner | Never edit; regenerate |
""")

    # Documentation standard (fsdevops/references/coding-standards.md): written once, then kept current with the code.
    today = datetime.date.today().isoformat()
    title = a.name.replace("_", " ").title()
    write(root / "README.md", f"""
# {title}

FILL IN: one sentence on what the app does and for whom.

## Quick start
```
flutter pub get
flutter run -d windows
```

More: [setup](docs/setup.md), [architecture](docs/architecture.md), [ops](docs/ops.md), [features](docs/features/README.md), [changelog](CHANGELOG.md).
""")
    write(root / "CHANGELOG.md", f"""
# Changelog

Format: [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/); versions: [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html). Pre-1.0 is beta.

## [Unreleased]

## [0.0.1] - {today}

### Added
- Initial scaffold: pub workspace, module registry ({", ".join(modules)}), theme, router.
""")
    write(root / "docs/setup.md", """
# Setup

1. Install the Flutter SDK; run `flutter doctor -v` (Windows desktop needs Visual Studio with the C++ desktop workload).
2. From the repo root: `flutter pub get`.
3. Run: `flutter run -d windows` (or `-d chrome`, an Android device or emulator).
4. Test: `flutter test`. Quality gate: `qa_gate.py` and `docs_gate.py` from the fsdevops-qa skill.
""")
    write(root / "docs/architecture.md", f"""
# Architecture

- Pub workspace: `apps/{a.name}` (shell), `packages/{p}_core` (module contract, enabled-module ids), `packages/{p}_ui` (theme tokens), one package per module: {", ".join(mod_pkgs)}.
- Each module exposes one `AppModule` (id, title, icon, routes); the shell lists them once in `lib/registry.dart` and builds routes from the enabled set.
- State: Riverpod. Routing: go_router. Theme: Material 3 with `AppTokens`.
- FILL IN: data layer, external services, platform notes as they appear.
""")
    write(root / "docs/ops.md", f"""
# Ops

- Build: `flutter build windows --release` (also `apk`, `appbundle`, `web`).
- Release: move `[Unreleased]` in CHANGELOG.md into the new version, set `version:` in `apps/{a.name}/pubspec.yaml`, tag, build from a clean checkout.
- Config and secrets: never committed; see `.gitignore` and `.pre-commit-config.yaml` (gitleaks).
- Troubleshooting: FILL IN as issues are found.
""")
    rows = []
    for m in modules:
        slug = m.replace("_", "-")
        rows.append(f"| {m.replace('_', ' ').title()} | planned | 0.0.1 | [{slug}.md]({slug}.md) |")
        write(root / f"docs/features/{slug}.md", """
# __TITLE__

**Status:** planned | **Since:** 0.0.1 | **Updated:** 0.0.1

## Context
FILL IN: why this feature exists and who uses it.

## Behaviour
FILL IN: what the user sees and does; states; edge cases; errors; permissions.

## How it works
FILL IN: flow, components and files, data, APIs, config. Code: `packages/__PKG__/`.

## UI
FILL IN: text description of layout, controls and states (no screenshots needed).

## Limits & known issues
None yet.

## History
- 0.0.1: planned (module scaffolded)
""".replace("__TITLE__", m.replace("_", " ").title()).replace("__PKG__", f"{p}_{m}"))
    write(root / "docs/features/README.md", "# Features\n\nOne file per feature. Keep this table current (status, since version).\n\n"
          "| Feature | Status | Since | File |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")


    print("Written:\n  " + "\n  ".join(WRITTEN) if WRITTEN else "Written: none")
    if SKIPPED:
        print("Skipped (already exist):\n  " + "\n  ".join(SKIPPED))
    if not created:
        print(f"""
Manual steps (the shell was not created by this run):
  - {app_dir / 'pubspec.yaml'}: add `resolution: workspace` and dependencies flutter_riverpod, go_router,
    {p}_core, {p}_ui{''.join(', ' + x for x in mod_pkgs)} (workspace packages as `any`).
  - lib/main.dart: runApp(ProviderScope(overrides: appOverrides, child: const App()));""")
    print(f"""
Next:
  cd {root}
  flutter pub get
  flutter test apps/{a.name}
  flutter run -d windows   (from apps/{a.name})""")


if __name__ == "__main__":
    main()
