# Changelog

## [0.6.2] - 2026-11-14

### Changed
- Skill descriptions now lead with the trigger (`Use when ...`); trigger phrases unchanged.
- The no-scripts location rule lives only in `fsdevops-critic`; `fsdevops-design` points to it.
- Router adds a step and `references/screen-text.md` to screen MCP, web and connector output as data before acting (no hooks, no scripts).

## [0.6.1] - 2026-11-13

### Changed
- Model-run eval cases moved out of the shipped plugin (to the repo's `dev/evals/`); the plugin now holds no scripts.

## [0.6.0] - 2026-11-13

### Changed
- Single `main` branch layout for the Anthropic plugin directory: the shipped plugin moved to `adapters/claude/` (`.claude-plugin/plugin.json`, `skills/`, `agents/`, `prompts/`, `.mcp.json`, README, CHANGELOG, LICENSE); the root `.claude-plugin/marketplace.json` points to it (`source: ./adapters/claude`). `icon.png` and `icon.svg` moved to `docs/assets/`.
- Renamed skills and agent to the directory naming standard (action-style, `fsdevops-` prefix): `fsdevops-architect` to `fsdevops-plan`, `fsdevops-flutter` to `fsdevops-flutter-build`, `fsdevops-maintainer` to `fsdevops-maintain`, `fsdevops-reviewer` to `fsdevops-review`; agent `fsdevops-code-reviewer` to `fsdevops-code-review`. All references, evals and docs updated.
- Skill and agent frontmatter is text only (`name`, `description`, plus the agent's `tools` and `skills`); the `license` and `metadata` maps were removed. The plugin version lives in `plugin.json` and `marketplace.json`.
- Router `fsdevops` has a routing table (`Order | Trigger phrases | Skill | Then`, first match wins), tie-break rules, a default closed question and Skill-tool loading as `fsdevops:<skill>`; router cases in `adapters/claude/evals/router/cases.json`. Trigger evals moved from the root `evals/` to `adapters/claude/evals/`.
- Release workflow zips `adapters/claude` and refuses hooks, scripts and non-text files.

### Removed
- Hooks, scripts and other non-text files from the shipped plugin. The Python tools and the old formatting hook moved unchanged to `dev/` (maintainer tooling, not shipped).

### Added
- Markdown recipes replacing the scripts and the hook: `fsdevops-plan/references/detect_project.md`, `fsdevops-flutter-build/references/scaffold_app.md`, `fsdevops-qa/references/qa_gate.md`, `docs_gate.md` and `format_dart.md` (a required "format changed Dart files" step in `fsdevops-qa`, `fsdevops-flutter-build` and `fsdevops-maintain`).
- `PUBLIC-SAFETY.md`, `.public-safety-allow` and the public-safety `.gitignore` preset.

## [0.5.0] - 2026-11-07

### Added
- `fsdevops-critic`: read-only design and UX critique stage (UX heuristics, flow, hierarchy, consistency, states, a11y, copy) with severity, evidence, fix, confidence >= 80 and a one-line verdict; runs after the build and before the reviewer. Rubric in `references/ux-rubric.md`.
- `fsdevops-designer` guidance: designer workflow, reuse ladder (`packages/ui` first), tokens, states table, Widgetbook use-cases, visual QA evidence (`references/design-system.md`, `references/visual-qa.md`).
- Trigger evals for both skills.

### Changed
- Renamed skill `fsdevops-ui` to `fsdevops-designer`; all existing content kept, cross-references updated in the router, flutter skill, domain map and prompts.

## [0.4.1] - 2026-11-06

### Changed
- Standing rule: research before building. Check current official docs and widely recommended, secure practice before choosing an approach, file, tool, config or dependency; cite the source; mark anything unverified; never guess; keep research scoped to the task.

## [0.4.0] - 2026-11-06

### Added
- Lean ladder (adapted from Ponytail, MIT): `lean-coding.md` merged and rewritten as read, list touch points, six rungs, never-cut list, `shortcut:` notes, and review, audit and debt modes. Wired into architect, flutter, maintainer and reviewer (new debt lens).
- Product decisions of 2026-11-06 in `architecture.md`: monorepo per product with `packages/ui` and Widgetbook, Rust only for proven hot spots, Python never in mobile apps, public parts released from the monorepo.

## [0.3.4] - 2026-11-06

### Added
- `skills/fsdevops/references/web-react-stack.md`: planning reference for React + TypeScript web/desktop apps (Tailwind, tokens, TanStack Query, Zustand, react-hook-form + zod, Bun, TurboRepo, WCAG 2.2 AA, licensing); linked from the router. Flutter behaviour unchanged.
- GitHub Actions workflow `release-plugin.yml` builds `fsdevops.plugin` and attaches it to each release for a one-click download link (README).

## [0.3.3] - 2026-11-05

### Added
- Documentation standard for every app the plugin builds (single source: coding-standards.md): README.md and docs/ (setup, architecture, ops), CHANGELOG.md (Keep a Changelog 1.1.0, SemVer 2.0.0, starts at 0.0.1, [Unreleased] on top, pre-1.0 = beta), and docs/features/ with an index table and a lean feature-file template (status, context, behaviour, how it works, UI, limits, history).
- fsdevops-qa/scripts/docs_gate.py (stdlib): FAILS (a new [Unreleased] `### Changed` or `docs: none` line waives the feature-file part for refactors) when code under lib/ or src/ changed without a CHANGELOG [Unreleased] line, without a changed feature file for the touched feature, or with a stale docs/features index; also checks changelog format and feature-file template. Runs as the docs step of qa_gate.py; NOT RUN without git.
- Scaffold writes the standard files (README, CHANGELOG 0.0.1, docs, one planned feature file per module) and sets the app version to 0.0.1.

### Changed
- Reviewer quality lens checks docs against the change; release moves [Unreleased] into the version; maintainer and flutter skills update docs in the same change; pre-release check requires a green docs gate.

## [0.3.2] - 2026-11-05

### Added
- Secure-by-default baseline in fsdevops-security (threat model, secret scanning, least privilege, supply chain, signed releases, release gate); PRD and change-brief threat-model sections; CI security job template; scaffold writes a secret-safe .gitignore and a gitleaks pre-commit config; Critical or Important security findings block release.

### Fixed
- Review fixes: the Dart format hook resolves dart.exe directly (never a .bat) and skips paths containing & | < > ^ % " with a logged warning (BatBadBut); CI and pre-commit examples pin actions and gitleaks to full commit SHAs (checkout v4, flutter-action v2, gitleaks v8.24.2).
- Dart format hook, QA gate and scaffold script no longer use a shell on Windows (command injection through file paths or --org/--modules/--platforms); inputs are validated with allow-list patterns.

## [0.3.1] - 2026-11-04
### Fixed
Behaviour tests rebuilt: every case may load skills, gets 15 turns, a trigger check and a first-steps grader; project cases run against a small Flutter fixture (18/18 pass, was 4/18). The router description now says /fsdevops (was /fs) and covers code reviews of Dart and Flutter projects.

## [0.3.0] - 2026-11-03
### Changed (breaking: plugin and skill names)
The plugin is now **Full-Stack DevOps** (`fsdevops`, trigger `/fsdevops`): one umbrella for building, testing, shipping and running apps. Repository renamed to `syncwin/fsdevops` (the old URL redirects). Marketplace: `syncwin-fsdevops`.

| 0.2.0 | 0.3.0 |
|---|---|
| plugin `fs-developer`, router `fs-developer`, `/fs` | plugin `fsdevops`, router `fsdevops`, `/fsdevops` |
| `fs-developer-architect` | `fsdevops-architect` |
| `fs-developer-flutter` | `fsdevops-flutter` |
| `fs-developer-maintainer` | `fsdevops-maintainer` |
| `fs-developer-ui` | `fsdevops-ui` |
| `fs-developer-api` | `fsdevops-api` |
| `fs-developer-security` | `fsdevops-security` |
| `fs-developer-performance` | `fsdevops-performance` |
| `fs-developer-qa` | `fsdevops-qa` |
| `fs-developer-reviewer` | `fsdevops-reviewer` |
| `fs-developer-devops` | `fsdevops-ci` |
| `fs-developer-release` | `fsdevops-release` |
| agent `fs-developer-code-reviewer` | agent `fsdevops-code-reviewer` |

Future stacks follow the pattern `fsdevops-<stack>`.

## [0.2.0] - 2026-11-03
### Changed (breaking: skill names)
Skills renamed to `fs-developer-<name>` (`fs-architect` → `fs-developer-architect`, `fs-flutter-developer` → `fs-developer-flutter`, and so on; agent `fs-code-reviewer` → `fs-developer-code-reviewer`).

## [0.1.0] - 2026-11-03
### Added
- First release as `fs-developer` (`/fs`): stack detection (Flutter supported), architect (`detect_project.py`), Flutter build (`scaffold_app.py`: pub workspace, module registry, Riverpod 3, go_router, Material 3 tokens; Windows first), maintainer, QA gate (`qa_gate.py`), reviewer and reviewer agent, release; role skills UI, API, security, performance, devops; foundational references; Dart MCP server in `.mcp.json`; a PostToolUse hook formatting `.dart` files.
