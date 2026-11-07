---
name: fsdevops-maintainer
description: Change stage for existing app code in Full-Stack DevOps. Fixes bugs, refactors, upgrades Flutter, Dart and packages, and migrates state, routing or data layers without breaking behaviour, respecting paths owned by visual builders or code generators. Covers reading before changing, parity lists, small diffs, migrations and rollback. Invoked by fsdevops after an approved change brief. Use when the user asks directly for safe-change or upgrade questions.
license: MIT
metadata:
  displayName: "FSDevOps Maintainer"
  version: "0.5.0"
  author: "@wasimness"
  company: "SyncWin"
---

# FSDevOps Maintainer

## Before changing
1. Read the files the brief names and their tests. Run the gate once to get a baseline (`fsdevops-qa`); record what already fails so you don't take the blame for it or hide it.
2. Check `.claude/ownership.md` (`fsdevops/references/ownership.md`). Builder-owned path: commit first, then follow the builder-safe rules. Generated path: change the source and regenerate.
3. Write the parity list (behaviour that must stay) into the brief if missing.
4. Research before building: apply the router's Official first rule.

## Changing
- Apply the lean ladder (`fsdevops/references/lean-coding.md`): list touch points first, fix root causes once in shared code, note shortcuts.
- Smallest diff that meets the brief; match the surrounding code's style and libraries.
- A failing test first for bugs, then the fix.
- No drive-by refactors; list them as follow-ups.
- Keep public APIs; when one must change, deprecate (`@Deprecated('Use X; removed in N')`) before removing.

## Upgrades (`references/upgrades.md`)
Flutter/Dart SDK, packages, Riverpod 2→3, go_router majors, Gradle/AGP, Windows runner changes.

## After
Docs in the same change (`fsdevops/references/coding-standards.md`): `[Unreleased]` line, touched feature files, index. Gate, scenarios from the parity list, reviewer. Report lines added versus removed.

Finish with a scratchpad: baseline, changes, parity results, follow-ups.
