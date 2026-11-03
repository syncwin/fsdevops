---
name: fs-developer-maintainer
description: Change stage for existing app code in Full-Stack Developer. Fixes bugs, refactors, upgrades Flutter, Dart and packages, and migrates state, routing or data layers without breaking behaviour, respecting paths owned by visual builders or code generators. Covers reading before changing, parity lists, small diffs, migrations and rollback. Invoked by fs-developer after an approved change brief. Use when the user asks directly for safe-change or upgrade questions.
license: MIT
metadata:
  displayName: "FS Maintainer"
  version: "0.2.0"
  author: "@wasimness"
  company: "SyncWin"
---

# FS Maintainer

## Before changing
1. Read the files the brief names and their tests. Run the gate once to get a baseline (`fs-developer-qa`); record what already fails so you don't take the blame for it or hide it.
2. Check `.claude/ownership.md` (`fs-developer/references/ownership.md`). Builder-owned path: commit first, then follow the builder-safe rules. Generated path: change the source and regenerate.
3. Write the parity list (behaviour that must stay) into the brief if missing.

## Changing
- Smallest diff that meets the brief; match the surrounding code's style and libraries.
- A failing test first for bugs, then the fix.
- No drive-by refactors; list them as follow-ups.
- Keep public APIs; when one must change, deprecate (`@Deprecated('Use X; removed in N')`) before removing.

## Upgrades (`references/upgrades.md`)
Flutter/Dart SDK, packages, Riverpod 2→3, go_router majors, Gradle/AGP, Windows runner changes.

## After
Gate, scenarios from the parity list, reviewer. Report lines added versus removed.

Finish with a scratchpad: baseline, changes, parity results, follow-ups.
