# Coding standards (foundational)

Source of truth: Effective Dart and the Dart linter (`official-docs.md`). These are the house rules on top.

## Formatting and lints
- `dart format` always; never hand-format.
- Lints: the project's `analysis_options.yaml` wins. New apps use `flutter_lints` plus these rules enabled: `prefer_const_constructors`, `prefer_final_locals`, `avoid_print`, `require_trailing_commas`, `unawaited_futures`, `use_build_context_synchronously`. Stricter sets (very_good_analysis) only if the user picks them.
- `flutter analyze --fatal-infos` must be clean.

## Naming
- Files `snake_case.dart`; types `UpperCamelCase`; members `lowerCamelCase`; constants `lowerCamelCase`.
- Packages in a workspace: `<app>_core`, `<app>_ui`, `<app>_<module>`; ask the owner for the app prefix in the architect question round (no built-in default).
- Providers end in `Provider`; repositories in `Repository`; widgets are nouns, not `Widget`-suffixed.

## Structure
- Feature-first folders inside packages: `lib/src/<feature>/{data,domain,presentation}`; export a small public API from `lib/<package>.dart`.
- One public widget per file; private helpers as small widget classes, not `_buildX()` methods.
- `const` constructors wherever possible.
- No `BuildContext` across async gaps without a `mounted` check.
- Errors: typed results or exceptions caught at the boundary (repository); never swallow; log through one logger.

## Documentation standard (single source; other skills link here)
Every project this plugin builds has these files from the first scaffold and keeps them current. A change that touches code updates the matching docs in the same change, never later. The docs gate recipe (`fsdevops-qa/references/docs_gate.md`) enforces it.

- **`README.md` + `docs/`**: short. `README.md` = what it is, quick start, link to `docs/`. `docs/setup.md` (install, run, test), `docs/architecture.md` (packages, modules, state, routing, data flow), `docs/ops.md` (build, release, config, troubleshooting). `///` doc comments on public APIs only (why, not what). Package READMEs: purpose, public API, how to test.
- **`CHANGELOG.md`**: Keep a Changelog 1.1.0 + Semantic Versioning 2.0.0. Starts at `0.0.1`. Top section `## [Unreleased]`; released sections `## [X.Y.Z] - YYYY-MM-DD`; categories only `### Added`, `### Changed`, `### Deprecated`, `### Removed`, `### Fixed`, `### Security`. One line per user-visible change, written for users. Pre-1.0 (`0.y.z`) = beta. `1.0.0` only when the owner says so.
- **`docs/features/`**: one file per feature, `docs/features/<feature-slug>.md` (slug = lowercase, hyphens; the folder under `lib/src/` or `lib/features/`, or the module package name), plus `docs/features/README.md`, an index table:

  `| Feature | Status | Since | File |` (one row per feature; Status and Since equal the feature file's)

- **Feature file template.** Lean, no fluff, ASCII only, understandable with no visual reference, so a new agent or user can learn the feature from it alone:

```
# <Title>

**Status:** planned|beta|stable|deprecated | **Since:** X.Y.Z | **Updated:** X.Y.Z

## Context
Why it exists, who uses it.

## Behaviour
What the user sees and does; states; edge cases; errors; permissions.

## How it works
Flow, components and files, data, APIs, config.

## UI
Text description, no screenshots needed: layout, controls, states.

## Limits & known issues

## History
- X.Y.Z: one-line change
```
- **When code changes** (anything under `lib/` or `src/`): add a line under `## [Unreleased]`; update the feature file of every touched feature (body, `Updated`, a History line) and the index row if Status or Since changed; add file + index row for a new feature. Shared code (core, ui, theme, root files) needs the changelog line only. Pure refactors skip the feature-file update: a new `### Changed` line or a line containing `docs: none` under `[Unreleased]` waives it (the changelog line is still required).
- **Release** (`fsdevops-release`): `[Unreleased]` becomes `## [X.Y.Z] - date`, a fresh empty `[Unreleased]` stays on top, `pubspec.yaml` version matches.
- **Evidence for AI+ contract adoption** (no `contract.yaml` here yet): `changelog_unreleased_updated`, `feature_docs_updated`, `feature_index_current`, `docs_gate_exit_code` = the rows and overall result of the docs gate recipe.

## Tests
- Every behaviour change has a test (unit for logic, widget for UI, golden only for stable visuals).
- Test names describe behaviour: `'shows empty state when feed has no cards'`.
