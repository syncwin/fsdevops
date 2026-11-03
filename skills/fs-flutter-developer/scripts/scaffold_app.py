#!/usr/bin/env python3
"""Scaffold a Flutter pub-workspace app with a module registry. Never overwrites files.

Usage:
  python scaffold_app.py <dir> --name <app> --prefix <prefix> [--org com.example]
         [--modules feed,tasks] [--platforms windows,android,ios,web] [--builder-ui] [--no-create]

Needs the Flutter SDK on PATH for `flutter create` (skip with --no-create).
"""
import argparse
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
    root = Path(a.dir).resolve()
    app_dir = root / "apps" / a.name
    p = a.prefix
    modules = [m.strip() for m in a.modules.split(",") if m.strip()]
    mod_pkgs = [f"{p}_{m}" for m in modules]

    created = False
    if not a.no_create:
        if not shutil.which("flutter"):
            sys.exit("Flutter SDK not on PATH. Install it or pass --no-create.")
        if not (app_dir / "pubspec.yaml").exists():
            subprocess.run(["flutter", "create", "--org", a.org, "--project-name", a.name,
                            "--platforms", a.platforms, "--empty", str(app_dir)],
                           check=True, shell=sys.platform == "win32")
            created = True
    if created:
        # Only files flutter create just made are changed here.
        pub = app_dir / "pubspec.yaml"
        text = pub.read_text(encoding="utf-8")
        extra = "".join(f"  {d}: any\n" for d in [f"{p}_core", f"{p}_ui", *mod_pkgs])
        text = re.sub(r"^(environment:)", "resolution: workspace\n\n\\1", text, count=1, flags=re.M)
        text = re.sub(r"(^dependencies:\n  flutter:\n    sdk: flutter\n)",
                      "\\1  flutter_riverpod: ^3.0.0\n  go_router: ^16.0.0\n" + extra, text, count=1, flags=re.M)
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
    if a.builder_ui:
        write(root / ".claude/ownership.md", f"""
| Path | Owner | Rule for code edits |
|---|---|---|
| packages/{p}_ui/** | Visual builder | Builder-safe rules in fs-developer/references/ownership.md; commit before and after |
| **/*.g.dart, **/*.freezed.dart | build_runner | Never edit; regenerate |
""")

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
