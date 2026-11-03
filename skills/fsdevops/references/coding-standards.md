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

## Documentation
- `///` doc comments on public APIs only; explain why, not what.
- README per package: purpose, public API, how to test.

## Tests
- Every behaviour change has a test (unit for logic, widget for UI, golden only for stable visuals).
- Test names describe behaviour: `'shows empty state when feed has no cards'`.
