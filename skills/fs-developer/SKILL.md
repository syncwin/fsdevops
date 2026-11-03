---
name: fs-developer
description: Full-Stack Developer - the entry point and router for the whole app development lifecycle, Flutter first (Windows desktop, then Android, iOS and web). Use whenever the user wants to build a new app or module, add a feature, fix, refactor or upgrade existing app code, write tests, set up CI, or review, secure, optimize, package or release an app; also when they invoke /fs. Detects the stack and work type, then sequences fs-developer-architect, a build skill (fs-developer-flutter, fs-developer-maintainer), fs-developer-qa and fs-developer-reviewer, backed by role skills for UI, API, security, performance, devops and release, on top of the always-applied lean-coding and coding-standards references this skill owns. Not for WordPress (that is fswp-developer) and not for operating an app's own UI such as clicking through a visual builder (that is an app-operator plugin).
license: MIT
metadata:
  displayName: "Full-Stack Developer"
  version: "0.2.0"
  author: "@wasimness"
  company: "SyncWin"
---

# FS Developer (router)

Router only. Each rule lives in the skill or reference that owns it. Everything is self-contained in `skills/`; no external skill dependency. Official documentation is linked, not copied: `references/official-docs.md`.

## Trigger

`/fs`, or a plain-language request to build, change, test, review or ship app code. No other trigger.

## Step 0: Detect the stack

Run `fs-developer-architect/scripts/detect_project.py <dir>` once (or read the files yourself). Rules: `references/stacks.md`.

| Signal | Stack | Build skill |
|---|---|---|
| `pubspec.yaml` with `flutter:` | Flutter | `fs-developer-flutter` |
| No project yet, user names Flutter or a desktop/mobile app | Flutter (default) | `fs-developer-flutter` |
| `package.json`, `go.mod`, others | Not supported yet | Say so; offer a plan only |

## Step 1: Classify the work

| The user wants to... | Work type | Build skill |
|---|---|---|
| Make a new app | New app | `fs-developer-flutter` |
| Add a module or feature to an app they own | New feature | `fs-developer-flutter` (feature mode) |
| Fix, refactor, upgrade or migrate existing code | Update | `fs-developer-maintainer` |
| Review or audit code they already have | Review only | `fs-developer-reviewer` (skip to step 4) |
| Set up CI, toolchain, signing | DevOps | `fs-developer-devops` |
| Package or publish a build | Release | `fs-developer-release` |

Unclear or mixed? Ask one question. Details: `references/work-types.md`.

## Step 2: Sequence (never skip or reorder)

1. **`fs-developer-architect`**: triage, one question round, research, PRD or change brief, the single approval gate.
2. **Build skill** from the table. `references/lean-coding.md`, `references/coding-standards.md` and `fs-developer-security` always apply. Load other role skills only for the domains the plan lists (`references/domain-map.md`).
3. **`fs-developer-qa`**: mechanical gate (format, fix, analyze, test, build), scenarios, scope check. Every result is PASS, FAIL or NOT RUN; NOT RUN is never a pass.
4. **`fs-developer-reviewer`**: independent read-only review. In Claude Code delegate to the `fs-developer-code-reviewer` agent; without agents, run a separate pass and disclose it as a self-review.
5. **Fix loop**: fix every Critical and Important finding, re-run steps 3 and 4 on changed files only.
6. **Ship**: `fs-developer-release` when the target is a build or release; otherwise deliver the diff with a short summary.

## Platform order

Desktop (Windows) first, then Android, then iOS and web, unless the user says otherwise. Every new app is scaffolded for all targets but verified on the first target before the next (`fs-developer-flutter/references/platforms.md`).

## Selection rules

- **One owner per domain** (`references/domain-map.md`).
- **Official first.** docs.flutter.dev and dart.dev, then role skills, then house rules; house rules may be stricter, never looser (`references/precedence.md`).
- **Ownership file.** If the repo has `.claude/ownership.md`, obey it: paths owned by a visual builder or generator are edited only by its rules (`references/ownership.md`).
- **Never invent facts about the user's project.** Names, links, versions and credentials not given are left out.
- This plugin never depends on another plugin and never operates other apps' UIs. If a step needs an app action (a builder's button, a store console), print it as a manual step for the user.

## Foundational, always applied

- `references/lean-coding.md`: write less; Dart, Flutter and the project first.
- `references/coding-standards.md` (with `references/i18n.md`, `references/accessibility.md`).
- `fs-developer-security`: secrets, storage, input, dependencies.

Keep replies short: lead with the result, list decisions and open items only. Load only what the task needs.

## Degradation

- **No Flutter SDK:** plan and write code, mark every gate step NOT RUN with the command to run; `fs-developer-devops` covers installing it.
- **No Dart MCP server:** use the CLI commands in `fs-developer-qa`.
- **No agents (claude.ai):** review runs as a disclosed self-review.

## Stable contract

- Plugin slug and router skill: `fs-developer`. Trigger `/fs`.
- Skills: `fs-developer-architect`, `fs-developer-flutter`, `fs-developer-maintainer`, `fs-developer-ui`, `fs-developer-api`, `fs-developer-security`, `fs-developer-performance`, `fs-developer-qa`, `fs-developer-reviewer`, `fs-developer-devops`, `fs-developer-release`; agent `fs-developer-code-reviewer`.
- A future stack adds `fs-developer-<stack>` plus stack references; the lifecycle skills stay shared.
- Result vocabulary: PASS, FAIL, NOT RUN.

## Reference index

| File | Read it for |
|---|---|
| `references/stacks.md` | Stack detection and how a new stack is added |
| `references/work-types.md` | What each work type changes |
| `references/domain-map.md` | Which skill owns which domain |
| `references/precedence.md` | Official docs vs. role skills vs. house rules |
| `references/ownership.md` | Paths owned by builders, generators or other tools |
| `references/official-docs.md` | Canonical Flutter and Dart links |
| `references/lean-coding.md`, `references/flutter-shortcuts.md` | Writing less |
| `references/coding-standards.md`, `references/i18n.md`, `references/accessibility.md` | How code is written |

Finish with a scratchpad: request, stack, work type, decisions, gate results, open items.
