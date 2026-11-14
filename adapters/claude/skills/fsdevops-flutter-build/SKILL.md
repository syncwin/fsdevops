---
name: fsdevops-flutter-build
description: Use when the user asks directly for Flutter structure, state, routing, theming or platform questions. Flutter build skill of Full-Stack DevOps. Creates new Flutter apps and adds new modules or features to existing ones - pub-workspace monorepo, module registry with runtime on/off, Riverpod 3 state, go_router routing, Material 3 theme tokens, adaptive layouts - verified on Windows desktop first, then Android, iOS and web. Invoked by fsdevops after an approved PRD.
---

# FSDevOps Flutter Developer

Build what the approved PRD says, nothing more: apply the lean ladder (`fsdevops/references/lean-coding.md`) and record shortcuts as `shortcut:` notes. Standards: `fsdevops/references/coding-standards.md`. Research before building: apply the router's Official first rule.

## New app
1. Check the toolchain: `flutter --version`, `flutter doctor -v`, `flutter devices`. Missing Windows toolchain → `fsdevops-ci`.
2. Scaffold by following the recipe `references/scaffold_app.md`, then `references/scaffold_modules.md` and `references/scaffold_docs.md` (inputs: dir, app name, prefix, modules, builder-ui yes or no). It runs `flutter create` for the shell (all platforms, org from the user) and writes the workspace, packages, module registry, router, theme, lints, an ownership file when `--builder-ui` is set, and a first widget test. It also writes the documentation standard (`README.md`, `CHANGELOG.md` at 0.0.1, `docs/` setup, architecture, ops, `docs/features/` index and one planned feature file per module; `FILL IN:` markers). Review what it wrote; it never overwrites existing files.
3. Fill the modules from the PRD: each module package exposes one `AppModule` (`references/architecture.md`).
4. Format every Dart file you created or changed (required step, recipe `fsdevops-qa/references/format_dart.md`).
5. Run the app on the first target: `flutter run -d windows`.
6. Hand to `fsdevops-qa`.

## New feature or module
0. Check `packages/ui` (and its Widgetbook catalog) before building any widget.
1. Detect (`fsdevops-plan`): existing state and routing libraries win, even if they differ from the defaults below. Never introduce a second state or routing library.
2. Add a module package or feature folder, register it, add routes and tests, and a feature file plus index row in `docs/features/` (`fsdevops/references/coding-standards.md`). Every code change adds an `[Unreleased]` line and updates its feature file in the same change.
3. Builder-owned paths: follow `fsdevops/references/ownership.md`.
4. Format every Dart file you created or changed (required step, recipe `fsdevops-qa/references/format_dart.md`).

## Defaults (when the project has none)
| Concern | Default | Reference |
|---|---|---|
| Repo | Pub workspace; single package for small apps | `references/architecture.md` |
| State and DI | Riverpod 3 (`flutter_riverpod`), codegen optional | `references/state-and-routing.md` |
| Routing | go_router, `StatefulShellRoute` for main sections | `references/state-and-routing.md` |
| Theme | Material 3, `ColorScheme.fromSeed`, `ThemeExtension` tokens | `references/theming.md` |
| Layout | Window size classes: compact <600, medium <840, expanded >=840 | `fsdevops-design` |
| Data | Repositories; API and offline per `fsdevops-api` | `fsdevops-api` |
| Platforms | Windows first | `references/platforms.md` |

## Module registry (runtime on/off)
Every module implements the same contract and is listed once in the shell. The enabled set comes from config (local file, remote flags, or user settings), is cached, and is exposed as a provider. A disabled module contributes no routes, no navigation entry, no background work, and keeps its data. Details and code shape: `references/architecture.md`.

Finish with a scratchpad: what was created, commands run with results, open items.
