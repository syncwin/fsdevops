# Changelog

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
