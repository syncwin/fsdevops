# Changelog

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
