---
name: fsdevops-architect
description: Planning stage of Full-Stack DevOps. Detects the project (stack, workspace, packages, targets, state and routing libraries, builder-owned paths), runs one question round, researches official docs, and writes a PRD for new apps and features or a change brief for updates, ending in the single approval gate before any code is written. Invoked by fsdevops first. Use when the user asks directly for "plan this app", "write a PRD" or "what would this change touch".
license: MIT
metadata:
  displayName: "FSDevOps Architect"
  version: "0.3.3"
  author: "@wasimness"
  company: "SyncWin"
---

# FSDevOps Architect

## 1. Triage (once)
Run `python scripts/detect_project.py <dir>` (standard library only). It prints the stack, workspace packages, Flutter/Dart constraints, targets present (`windows/`, `android/`, `ios/`, `web/`, `macos/`, `linux/`), state, routing, model and database libraries, codegen use, lints, tests count, an ownership file, and a `.nowa/` folder (visual builder in use). No Python: read `pubspec.yaml` files and folder names yourself.

## 2. One question round
Ask only what the user alone knows, at most five questions, with your default filled in:
- App name and a short code prefix for packages (propose candidates from the name).
- Targets and order (default: Windows desktop first, then Android, iOS, web).
- Backend: existing API/OpenAPI spec, or none yet (mock repositories).
- Is a visual builder editing part of the UI? Which package?
- Anything they must use or must avoid (packages, licences).

## 3. Research
Link the official pages the plan depends on (`fsdevops/references/official-docs.md`); re-fetch any page whose rule decides the design. Mark anything not verified.

## 4. Write the brief
- New app or feature: `references/prd-template.md`.
- Update, DevOps, release: `references/change-brief-template.md`.
- Name the domains it touches so the router loads only those role skills.
- New app with a builder: include `.claude/ownership.md` in the file list.

## 5. Approval gate
Show the brief, ask for one yes. The yes covers building and checking in the working folder only; publishing, pushing or signing with real keys needs its own yes.

Finish with a scratchpad: detected facts, answers, decisions, open items.
