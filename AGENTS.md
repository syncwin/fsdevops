# fsdevops agent guide

Full-Stack DevOps Claude plugin: app lifecycle (plan, build, update, verify, review, release), Flutter first.

**Structure:** `adapters/claude/` is the shipped plugin (text only: `.claude-plugin/plugin.json`, `.mcp.json`, `skills/fsdevops*` router + 12 skills with recipes in `references/`, `agents/fsdevops-code-review.md`, `evals/` (trigger evals and `router/cases.json`), `prompts/`, README, CHANGELOG, LICENSE); `dev/` holds maintainer-only Python and the old hook (never shipped); `docs/`, `.claude-plugin/marketplace.json` (source `./adapters/claude`). `main` is the only branch.

## Commands
- Strict validation (must pass): `python <aiaddon>/dev/aiaddon-review/scripts/validate_extension.py adapters/claude --strict --target directory --require-meta author,company`
- Router check: `python <aiaddon>/dev/aiaddon-review/scripts/route_check.py adapters/claude`
- Secret and private-data scan: `python <aiaddon>/dev/aiaddon-review/scripts/scan_secrets.py . --history`; false positives only in `.public-safety-allow`
- Recipes (what the old scripts did) live in `adapters/claude/skills/*/references/`: `detect_project.md`, `scaffold_app.md`, `qa_gate.md`, `docs_gate.md`, `format_dart.md`. The Python originals stay in `dev/` as maintainer tooling: `python dev/fsdevops-plan/scripts/detect_project.py <app>`, `python dev/fsdevops-qa/scripts/qa_gate.py <app> [--target ...] [--fix]`, `python dev/fsdevops-qa/scripts/docs_gate.py <app>`, `python dev/fsdevops-flutter-build/scripts/scaffold_app.py` (throwaway run). Keep recipe and script behaviour in step.
- Add a stack: follow `adapters/claude/skills/fsdevops/references/stacks.md`
- Validate: `claude plugin validate . --strict`
- Evals (real model calls): the cases live in `dev/evals/` (kept out of the shipped plugin because they hold `scaffold.sh` scripts); copy `adapters/claude` to a scratch folder, copy `dev/evals/*` into its `evals/`, then run `claude plugin eval <scratch copy> --trust-plugin --ablation none --scaffold --allow-tools Read Glob Grep Skill -j 4 --no-publish`. Rebuild cases with `python <owner-tools>/plugin-evals/regen_evals.py <plugin> <router> <fixture ids>`. Write results outside the repo (`<owner-outputs>/<plugin>/eval-results`, a local folder outside the repo); the packager includes repo files.

## Workflow
1. Read the skill or script you change, plus its neighbours.
2. Make the smallest change; run the closest check, then the full gate.
3. Update `CHANGELOG.md` for behavior changes; log ideas in `IMPROVEMENTS.md`.

## Rules
- **Directory compliance:** the shipped plugin (`adapters/claude`) has no hooks, no scripts or other non-text files, and text-only frontmatter (`name`, `description`). Features that were scripts or hooks are recipes in `skills/*/references/`; Python in `dev/` is maintainer tooling only.
- **Never publish secrets or private data** (keys, tokens, passwords, personal contact data, client names, internal URLs, local paths); the secret scan blocks every commit and release.
- Naming standard (validator `P019` to `P023`): router skill name == plugin name; every other skill, agent and command is prefixed `fsdevops-`; action-style slugs (`-review`, not `-reviewer`). Router standard (`P024` to `P028`): routing table, tie-breaks, default question, Skill-tool loading, router evals.
- Run the closest check and the full gate before committing. Never delete or weaken tests or evals. Report failed, skipped or timed-out runs honestly; NOT RUN is never a pass.
- Follow neighbouring files. Keep each `SKILL.md` under 500 lines; move detail into `references/`.
- On release, bump `version` in `adapters/claude/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` together (skills carry no `metadata` block: directory policy wants text-only frontmatter); add a `CHANGELOG.md` entry per behavior change and copy it to `adapters/claude/CHANGELOG.md`.
- No commits, pushes or PRs unless asked. Work on a branch and open a PR; never push to main.
- No new dependencies without asking (scripts stay on the Python standard library).
- Never commit secrets. Never pick names or slugs without user confirmation.
- Skill and plugin names start with `fsdevops`. Lean and coding rules live once in `adapters/claude/skills/fsdevops/references/` (`lean-coding.md`, `coding-standards.md`).

## Model routing
Opus plans, decides, writes self-contained briefs with a report word limit, and reviews every result. Haiku for search, reading and mechanical edits. Sonnet for coding, tests and multi-step work. Do 1-2 tool calls inline.

## Docs
README.md, CONTRIBUTING.md, CHANGELOG.md, docs/trademarks.md; ideas and feedback in `IMPROVEMENTS.md`.
