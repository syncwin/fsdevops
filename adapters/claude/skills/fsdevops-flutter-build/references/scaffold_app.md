# Recipe: scaffold a Flutter pub-workspace app

Create the files below with Write (never overwrite a file that exists: list it as skipped). Placeholders: `{name}` app name, `{p}` package prefix, `{org}` reverse-domain id (default `com.example`), `{modules}` list (default `home`), `{Title}` the app name as Title Case words, and per module `{m}` (lower_snake_case), `{m-slug}` (`{m}` with `_` as `-`), `{M}` (CamelCase of `{m}`), `{pkg}` = `{p}_{m}`.

Contents: 0 inputs, 1 Flutter shell, 2 root files, 3 package pubspec, 4 core, 5 UI (this file); 6 modules, 7 shell, 8 secure defaults (`scaffold_modules.md`); 9 documentation files, 10 report (`scaffold_docs.md`). Do all steps in order.

## 0. Validate inputs first
- `{name}` and `{p}`: lower_snake_case (`[a-z][a-z0-9_]*`).
- `{org}`: reverse-domain id such as `com.example`.
- modules: comma-separated lower_snake_case. platforms: comma list of `windows,android,ios,web,linux,macos` (default `windows,android,ios,web`).
- Layout: root = the target folder, `app_dir` = `<root>/apps/{name}`.

## 1. Create the Flutter shell
Needs the Flutter SDK (skip this step and do the manual steps at the end when it is missing; report NOT RUN). If `<app_dir>/pubspec.yaml` does not exist, run `flutter create --org {org} --project-name {name} --platforms <platforms> --empty <app_dir>`. Only when this run created the shell:
- In `<app_dir>/pubspec.yaml` insert `resolution: workspace` plus a blank line before the first `environment:` line; after `dependencies:` / `flutter:` / `sdk: flutter` add `flutter_riverpod: ^3.0.0`, `go_router: ^16.0.0`, and `{p}_core: any`, `{p}_ui: any`, `{p}_<m>: any` for each module (two-space indent); set `version: 0.0.1+1`.
- Replace `<app_dir>/lib/main.dart` with:
  ```dart
  import 'package:flutter/material.dart';
  import 'package:flutter_riverpod/flutter_riverpod.dart';

  import 'app.dart';

  void main() => runApp(ProviderScope(overrides: appOverrides, child: const App()));
  ```
- Delete `<app_dir>/test/widget_test.dart` if present.

## 2. Root files
`<root>/pubspec.yaml`:
```yaml
name: {name}_workspace
publish_to: none

environment:
  sdk: ^3.6.0

workspace:
  - apps/{name}
  - packages/{p}_core
  - packages/{p}_ui
  - packages/{p}_<m>    # one line per module

dev_dependencies:
  flutter_lints: ^5.0.0
```
`<root>/analysis_options.yaml`:
```yaml
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
```

## 3. Package pubspec shape
Every package pubspec (`packages/{p}_core`, `packages/{p}_ui`, each module) uses this shape; `<deps>` is the per-package list below, one per line with two-space indent:
```yaml
name: <package name>
publish_to: none
resolution: workspace

environment:
  sdk: ^3.6.0

dependencies:
  flutter:
    sdk: flutter
  <deps>

dev_dependencies:
  flutter_test:
    sdk: flutter

flutter:
  uses-material-design: true
```
- `{p}_core` deps: `flutter_riverpod: ^3.0.0`, `go_router: ^16.0.0`
- `{p}_ui` deps: none
- module `{pkg}` deps: `{p}_core: any`, `{p}_ui: any`, `flutter_riverpod: ^3.0.0`, `go_router: ^16.0.0`

## 4. Core package
`packages/{p}_core/lib/{p}_core.dart`:
```dart
export 'src/app_module.dart';
export 'src/enabled_modules.dart';
```
`packages/{p}_core/lib/src/app_module.dart`:
```dart
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
```
`packages/{p}_core/lib/src/enabled_modules.dart`:
```dart
import 'package:flutter_riverpod/flutter_riverpod.dart';

/// Ids of enabled modules. Override in the shell with the real source
/// (local default, cached remote flags or user settings).
final enabledModuleIdsProvider = Provider<Set<String>>((ref) => const {});
```

## 5. UI package
`packages/{p}_ui/lib/{p}_ui.dart` (first line is `// builder-owned: edit with ownership rules` when a visual builder owns the UI package, else `// developer-owned`):
```dart
// developer-owned
export 'src/theme.dart';
```
`packages/{p}_ui/lib/src/theme.dart`:
```dart
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
```

Continue with `scaffold_modules.md`, then `scaffold_docs.md`. Same placeholders.
