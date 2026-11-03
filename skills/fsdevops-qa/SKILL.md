---
name: fsdevops-qa
description: Verification stage of Full-Stack DevOps. Runs the mechanical gate for Flutter and Dart projects (dart format, dart fix dry run, flutter analyze, flutter test, codegen check, a release build for the current target), the scope check against the approved brief, scenario tests and the shortcut-marker list. Reports PASS, FAIL or NOT RUN and never implies a skipped check passed. Invoked by fsdevops after a build and before delivery. Use when the user asks directly to audit any Flutter project.
license: MIT
metadata:
  displayName: "FSDevOps QA Engineer"
  version: "0.3.0"
  author: "@wasimness"
  company: "SyncWin"
---

# FSDevOps QA Engineer

Verify; do not fix while gating. Report first, then fix in the router's fix loop.

## 1. Mechanical gate
```
python scripts/qa_gate.py <dir> [--target windows|apk|appbundle|web|none] [--fix]
```
Runs at the workspace root (or package): `flutter pub get`, `dart format --output=none --set-exit-if-changed .`, `dart fix --dry-run`, `flutter analyze --fatal-infos`, `flutter test`, `build_runner` check when codegen is used, then `flutter build <target> --release` for the current target (default `windows` on Windows). `--fix` runs `dart format .` and `dart fix --apply` first; review the diff. Prefer the Dart MCP server's tools (`analyze`, `run_tests`, `dart_format`) when connected; same reporting rules.

**Reporting:** every step is PASS, FAIL or NOT RUN, with tool versions. NOT RUN (no SDK, no Visual Studio, iOS on Windows) is never a pass and never "clean"; name the command that would run it.

## 2. Scope check
Compare the diff with the approved brief. Files, packages, permissions or dependencies the plan did not ask for are scope creep. Count lines added versus removed. List every `SHORTCUT(fsdevops)` marker (`fsdevops/references/lean-coding.md`).

## 3. Scenarios
Turn each "Done when" and parity item into a check: an automated test where possible, otherwise numbered manual steps on the current target with expected results. Desktop: keyboard-only pass, window resize to the minimum width, 200% text scale.

## 4. Pre-release
Before `fsdevops-release`: gate green on the release target, version bumped, changelog entry, no debug flags, no `print`.

Finish with a scratchpad: the gate table, scope findings, scenario results.
