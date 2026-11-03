---
name: fsdevops-flutter
description: Flutter build skill of Full-Stack DevOps. Creates new Flutter apps and adds new modules or features to existing ones - pub-workspace monorepo, module registry with runtime on/off, Riverpod 3 state, go_router routing, Material 3 theme tokens, adaptive layouts - verified on Windows desktop first, then Android, iOS and web. Invoked by fsdevops after an approved PRD. Use when the user asks directly for Flutter structure, state, routing, theming or platform questions.
license: MIT
metadata:
  displayName: "FSDevOps Flutter Developer"
  version: "0.3.0"
  author: "@wasimness"
  company: "SyncWin"
---

# FSDevOps Flutter Developer

Build what the approved PRD says, nothing more (`fsdevops/references/lean-coding.md`). Standards: `fsdevops/references/coding-standards.md`.

## New app
1. Check the toolchain: `flutter --version`, `flutter doctor -v`, `flutter devices`. Missing Windows toolchain → `fsdevops-ci`.
2. Scaffold with `python scripts/scaffold_app.py <dir> --name <app> --prefix <prefix> [--modules feed,tasks] [--builder-ui]`. It runs `flutter create` for the shell (all platforms, org from the user) and writes the workspace, packages, module registry, router, theme, lints, an ownership file when `--builder-ui` is set, and a first widget test. Review what it wrote; it never overwrites existing files.
3. Fill the modules from the PRD: each module package exposes one `AppModule` (`references/architecture.md`).
4. Run the app on the first target: `flutter run -d windows`.
5. Hand to `fsdevops-qa`.

## New feature or module
1. Detect (`fsdevops-architect`): existing state and routing libraries win, even if they differ from the defaults below. Never introduce a second state or routing library.
2. Add a module package or feature folder, register it, add routes and tests.
3. Builder-owned paths: follow `fsdevops/references/ownership.md`.

## Defaults (when the project has none)
| Concern | Default | Reference |
|---|---|---|
| Repo | Pub workspace; single package for small apps | `references/architecture.md` |
| State and DI | Riverpod 3 (`flutter_riverpod`), codegen optional | `references/state-and-routing.md` |
| Routing | go_router, `StatefulShellRoute` for main sections | `references/state-and-routing.md` |
| Theme | Material 3, `ColorScheme.fromSeed`, `ThemeExtension` tokens | `references/theming.md` |
| Layout | Window size classes: compact <600, medium <840, expanded >=840 | `fsdevops-ui` |
| Data | Repositories; API and offline per `fsdevops-api` | `fsdevops-api` |
| Platforms | Windows first | `references/platforms.md` |

## Module registry (runtime on/off)
Every module implements the same contract and is listed once in the shell. The enabled set comes from config (local file, remote flags, or user settings), is cached, and is exposed as a provider. A disabled module contributes no routes, no navigation entry, no background work, and keeps its data. Details and code shape: `references/architecture.md`.

Finish with a scratchpad: what was created, commands run with results, open items.
