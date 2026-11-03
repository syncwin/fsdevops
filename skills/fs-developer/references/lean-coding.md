# Lean coding (foundational: write less)

Principle credited in `CREDITS.md` (Ponytail's minimal-code order of operations); wording and rules here are original.

## Decision ladder (stop at the first yes)
1. **Does the plan require it?** If not, don't write it. Report it as "skipped: X, add when Y".
2. **Does the project already have it?** Search the repo (widgets, extensions, providers, helpers) and reuse.
3. **Does Flutter or Dart already provide it?** Material/Cupertino widgets, `ThemeData` component themes, `LayoutBuilder`, `Intl`, `dart:collection`, `Future`/`Stream` utilities. See `flutter-shortcuts.md`.
4. **Does an already-approved dependency provide it?** Riverpod, go_router, drift, freezed.
5. **Is a well-maintained package worth it?** Only with the user's OK (`fs-developer-security` licence and health check). One package per need.
6. **Write the smallest code that works**, with tests for its behaviour.

## Habits
- One way to do a thing per repo (one state library, one router, one HTTP client, one model generator).
- No speculative abstractions: no interface with one implementation unless a test or the module registry needs it.
- No dead parameters, flags or commented-out code.
- Configuration over code when a setting does the job (`ThemeData` over custom painting; `analysis_options.yaml` over ad-hoc rules).
- Generated code beats hand-written boilerplate (freezed, json_serializable, riverpod_generator) once three or more models need it; before that, plain classes.

## Effort levels
- **lite**: apply the ladder silently.
- **full** (default): apply it and list skipped items in the summary.
- **ultra**: also report lines added versus removed and justify each new file.

## Shortcut marker
When you deliberately take a shortcut to ship (a deliberate gap with a reason), mark it `// SHORTCUT(fs): <reason>, remove when <condition>`. `fs-developer-qa` lists every marker.
