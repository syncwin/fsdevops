# Lean coding: the lean ladder (write less, finish everything)

Method adapted from [Ponytail](https://github.com/dietrichgebert/ponytail) by Dietrich Gebert (MIT); wording and structure here are original. See `CREDITS.md`.

Be lazy about the solution, never about completeness: every part the task needs is done.

## 1. Read, then list touch points (before any code)
- Read the task and the code it touches.
- List every place the change must reach: callers, tests, fixtures, config, exports, docs, generated files.
- Ask what could break for users: data loss, exposure, callers that stop working. This list is the scope; extras are not.

## 2. The ladder (take the first rung that fully works)
1. **Does it need to exist?** If the plan or request does not require it, skip it and report "skipped: X, add when Y". A vague request gets the smallest version that does the core job.
2. **Reuse what the project has** (widgets, extensions, providers, helpers), in the surrounding style. Search before writing.
3. **Dart or Flutter already provides it** (Material/Cupertino widgets, `ThemeData` component themes, `LayoutBuilder`, `Intl`, `dart:collection`). See `flutter-shortcuts.md`.
4. **An installed dependency provides it** (Riverpod, go_router, drift, freezed). A new package never for a few lines; otherwise only with the user's OK after the `fsdevops-security` licence and health check, one package per need.
5. **One readable line** beats a helper.
6. **Minimum working code**, nothing speculative.

## 3. Rules while changing
- One way per repo (one state library, router, HTTP client, model generator). No speculative interface, wrapper, option or flag; no commented-out code. Deleting code beats adding it.
- Config over code (`ThemeData`, `analysis_options.yaml`). Generated code (freezed, json_serializable, riverpod_generator) once three or more models need it.
- Bug fix: grep every caller first, then fix the root cause once in the shared code, not at each call site.
- Moved or merged code keeps its error handling and validation. Between equally short options pick the one that handles edge cases.
- New non-trivial logic (branches, loops, parsers, money, security) gets one small test. Trivial changes do not.

## 4. Never cut
Validation at trust boundaries, error handling that prevents data loss, security (`fsdevops-security`), accessibility (`accessibility.md`), and anything the user explicitly asked for.

## 5. Shortcut notes
A deliberate shortcut with a known limit gets a code comment: `// shortcut: <limit>, upgrade when <condition>`. The reviewer's debt mode collects them.

## 6. Levels and modes
- **lite**: apply the ladder silently. **full** (default): also list skipped items in the summary. **ultra**: also challenge the request, report lines added versus removed, and justify each new file.
- **review**: lean lens over a diff or folder. Flag code a higher rung covers, duplicated utilities, one-use abstractions, a second library, root causes patched per caller. Name the rung and the smaller form.
- **audit**: same lens over the whole repo, ranked by lines saved.
- **debt**: list every `shortcut:` note with its limit and upgrade trigger; flag ones whose trigger has now been met or that lack a limit.
