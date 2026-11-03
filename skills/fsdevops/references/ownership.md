# Ownership of paths

Some paths in a repo are written by something other than a developer: a visual builder (for example Nowa owning `packages/ui`), a code generator (`*.g.dart`, `*.freezed.dart`), or a platform tool.

## The ownership file
If `.claude/ownership.md` exists, read it before editing. Format (create it in new apps that use a builder):

```
| Path | Owner | Rule for code edits |
|---|---|---|
| packages/ui/** | Visual builder | Edit only with the builder-safe rules below; commit before and after |
| **/*.g.dart, **/*.freezed.dart | build_runner | Never edit; regenerate |
```

## Builder-safe rules (any visual builder that round-trips real Dart)
1. Commit (or confirm the builder saved) before editing; edit on a branch.
2. Keep widget trees declarative. Prefer small widget classes over `_buildX()` helper methods, which builders treat as opaque.
3. Keep builder-owned packages free of state libraries: widgets take plain values and callbacks; state lives in the shell or module packages.
4. Keep generated code (freezed, drift, riverpod_generator) out of builder-owned packages.
5. After a builder save, run the gate (`fsdevops-qa`): builders may rewrite syntax.
6. Do not hand-edit platform manifests while the builder is editing them.
7. A `pubspec.yaml` change usually needs a new run in the builder; tell the user.

No ownership file and no builder in use: the developer owns every path except generated files.
