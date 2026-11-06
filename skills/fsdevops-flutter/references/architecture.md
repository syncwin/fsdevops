# Architecture

Based on the official app architecture guide (UI, logic and data layers; `official-docs.md`) plus house rules.

## Workspace layout
```
<app>/
├─ pubspec.yaml                  # name: <app>_workspace, workspace: [apps/<app>, packages/*]
├─ analysis_options.yaml
├─ .claude/ownership.md          # when a builder or generator owns paths
├─ apps/<app>/                   # shell: main.dart, bootstrap, router, registry, platform folders
└─ packages/
   ├─ <prefix>_core/             # models, repositories, API client, local db, flags, logging
   ├─ <prefix>_ui/               # theme, tokens, shared widgets; builder-owned when a builder is used
   └─ <prefix>_<module>/         # one per module: screens, providers, routes
```
Each package's `pubspec.yaml` has `resolution: workspace`. Dependency direction: shell → modules → core and ui; modules never import each other (communicate through core).

Small app (one or two screens, no modules): a single package with `lib/src/<feature>/` folders. Move to a workspace when a second module appears.

## Module contract
```dart
abstract class AppModule {
  String get id;                       // stable, kebab-case
  String get title;                    // localized in UI, not here
  IconData get icon;
  List<RouteBase> get routes;          // go_router routes, mounted under '/<id>'
  Widget? settingsPage(BuildContext context) => null;
}
```
- The shell holds `const modules = <AppModule>[...]`.
- `enabledModuleIdsProvider` (Riverpod) reads config: a local default, then a cached remote or user value.
- The router builds from `modules.where(enabled)`; navigation lists only enabled modules.
- Extra contribution points (feed cards, search, background jobs) are added to the contract only when a second module needs them.

## Layers inside a module
- `data/`: repository implementations, DTOs.
- `domain/`: plain models and use-case functions when logic is non-trivial.
- `presentation/`: screens, widgets, providers.

## Errors and logging
Repositories return values or throw typed exceptions; providers expose `AsyncValue`; screens render loading, error (with retry) and empty states. One logger in core.

## Product decisions (user, 2026-11-06)
- One monorepo per product with shared packages: Flutter pub workspace with `apps/`, `packages/ui` (design system with a Widgetbook catalog; check it before building any widget) and `packages/core`.
- Rust via `flutter_rust_bridge` only for proven hot spots (crypto, sync, search, files); measure first.
- Python only for desktop or server helpers, never inside mobile apps.
- Public parts are published from the monorepo by a release workflow, not by separate source repos.
