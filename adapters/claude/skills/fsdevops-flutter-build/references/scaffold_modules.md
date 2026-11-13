# Recipe: scaffold a Flutter workspace app, part 2 (modules, shell, secure defaults)

Contents: 6 one package per module, 7 shell, 8 secure defaults. Placeholders as in `scaffold_app.md`. Never overwrite existing files.

## 6. One package per module
`packages/{pkg}/lib/{pkg}.dart`: `export 'src/{m}_module.dart';`

`packages/{pkg}/lib/src/{m}_module.dart`:
```dart
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:{p}_core/{p}_core.dart';

class {M}Module extends AppModule {
  const {M}Module();

  @override
  String get id => '{m-slug}';

  @override
  String get title => '{M}';

  @override
  IconData get icon => Icons.dashboard_outlined;

  @override
  List<RouteBase> get routes => [
        GoRoute(
          path: '/$id',
          builder: (context, state) => const _{M}Screen(),
        ),
      ];
}

class _{M}Screen extends StatelessWidget {
  const _{M}Screen();

  @override
  Widget build(BuildContext context) =>
      const Center(child: Text('{M}'));
}
```

## 7. Shell (`<app_dir>/lib/`)
`registry.dart` (one import per module package; `<list>` = `{M}Module()` joined with `, `):
```dart
import 'package:{p}_core/{p}_core.dart';
import 'package:{pkg}/{pkg}.dart';

/// Every module the app ships. Enabled ones come from enabledModuleIdsProvider.
const List<AppModule> allModules = [<list>];
```
`router.dart`:
```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:{p}_core/{p}_core.dart';

import 'registry.dart';

final enabledModulesProvider = Provider<List<AppModule>>((ref) {
  final ids = ref.watch(enabledModuleIdsProvider);
  return allModules.where((m) => ids.contains(m.id)).toList();
});

final routerProvider = Provider<GoRouter>((ref) {
  final modules = ref.watch(enabledModulesProvider);
  return GoRouter(
    initialLocation: modules.isEmpty ? '/empty' : '/${modules.first.id}',
    routes: [
      GoRoute(
        path: '/empty',
        builder: (context, state) =>
            const Scaffold(body: Center(child: Text('No modules enabled'))),
      ),
      for (final m in modules) ...m.routes,
    ],
  );
});
```
`app.dart` (`<ids>` = the module slugs quoted and comma-joined, `{AppName}` = CamelCase of `{name}`):
```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:{p}_core/{p}_core.dart';
import 'package:{p}_ui/{p}_ui.dart';

import 'router.dart';

const defaultEnabledModules = {<ids>};

final appOverrides = [
  enabledModuleIdsProvider.overrideWithValue(defaultEnabledModules),
];

class App extends ConsumerWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) => MaterialApp.router(
        title: '{AppName}',
        theme: buildTheme(Brightness.light),
        darkTheme: buildTheme(Brightness.dark),
        routerConfig: ref.watch(routerProvider),
      );
}
```
`<app_dir>/test/app_test.dart` (`{M0}` = CamelCase of the first module):
```dart
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:{name}/app.dart';

void main() {
  testWidgets('starts on the first enabled module', (tester) async {
    await tester.pumpWidget(ProviderScope(overrides: appOverrides, child: const App()));
    await tester.pumpAndSettle();
    expect(find.text('{M0}'), findsOneWidget);
  });
}
```

## 8. Secure by default
`<root>/.gitignore`:
```
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
```
`<root>/.pre-commit-config.yaml`:
```yaml
# Run `pre-commit install` once. `rev` is pinned to a full commit SHA (tag in the comment); review it when updating.
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: d5c275d6b2140fcb59bc3f58b8dd5350f5b19df6  # v8.24.2
    hooks:
      - id: gitleaks
```
With a visual builder owning the UI package, also `<root>/.claude/ownership.md`:
```
| Path | Owner | Rule for code edits |
|---|---|---|
| packages/{p}_ui/** | Visual builder | Builder-safe rules in fsdevops/references/ownership.md; commit before and after |
| **/*.g.dart, **/*.freezed.dart | build_runner | Never edit; regenerate |
```
