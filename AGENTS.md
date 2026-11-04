# fsdevops agent guide

Full-Stack DevOps Claude plugin: app lifecycle (plan, build, update, verify, review, release), Flutter first.

**Structure:** `skills/fsdevops*` (router + 11 role skills), `agents/fsdevops-code-reviewer.md`, `hooks/hooks.json`, `scripts/format_dart.py`, `evals/`, `docs/`, `prompts/`.

## Commands
- Detect stack: `python skills/fsdevops-architect/scripts/detect_project.py <app>`
- QA gate on an app: `python skills/fsdevops-qa/scripts/qa_gate.py <app> [--target windows|apk|appbundle|web|ios|none] [--fix]`
- Scaffold test: a throwaway `python skills/fsdevops-flutter/scripts/scaffold_app.py` run
- Add a stack: follow `skills/fsdevops/references/stacks.md`
- Validate: `claude plugin validate . --strict`
- Evals (real model calls): `claude plugin eval . --trust-plugin --ablation none --scaffold --allow-tools Read Glob Grep Skill -j 4 --no-publish`. Rebuild cases with `python A:\Automation\plugin-evals\regen_evals.py <plugin> <router> <fixture ids>`. Write results outside the repo (`D:\SyncWin\AI Outputs\<plugin>\eval-results`); the packager includes repo files.

## Workflow
1. Read the skill or script you change, plus its neighbours.
2. Make the smallest change; run the closest check, then the full gate.
3. Update `CHANGELOG.md` for behavior changes; log ideas in `IMPROVEMENTS.md`.
4. Branch, commit, open a PR; never push to main.

## Rules
- Run the closest check and the full gate before committing. Never delete or weaken tests or evals. Report failed, skipped or timed-out runs honestly; NOT RUN is never a pass.
- Follow neighbouring files. Keep each `SKILL.md` under 500 lines; move detail into `references/`.
- On release, bump `version` in `.claude-plugin/plugin.json` and every skill's `metadata.version` together; add a `CHANGELOG.md` entry per behavior change.
- No commits, pushes or PRs unless asked. Work on a branch and open a PR; never push to main.
- No new dependencies without asking (scripts stay on the Python standard library).
- Never commit secrets. Never pick names or slugs without user confirmation.
- Skill and plugin names start with `fsdevops`. Lean and coding rules live once in `skills/fsdevops/references/` (`lean-coding.md`, `coding-standards.md`).

## Model routing
Opus plans, decides, writes self-contained briefs with a report word limit, and reviews every result. Haiku for search, reading and mechanical edits. Sonnet for coding, tests and multi-step work. Do 1-2 tool calls inline.

## Docs
README.md, CONTRIBUTING.md, CHANGELOG.md, docs/trademarks.md; ideas and feedback in `IMPROVEMENTS.md`.
