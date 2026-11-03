# Changelog

## [0.2.0] - 2026-11-03
### Changed (breaking: skill names)
Every skill and the agent now start with the router name, so typing `fs-developer` lists them all.

| 0.1.0 | 0.2.0 |
|---|---|
| `fs-architect` | `fs-developer-architect` |
| `fs-flutter-developer` | `fs-developer-flutter` |
| `fs-maintainer` | `fs-developer-maintainer` |
| `fs-ui-developer` | `fs-developer-ui` |
| `fs-api-developer` | `fs-developer-api` |
| `fs-security-engineer` | `fs-developer-security` |
| `fs-performance-engineer` | `fs-developer-performance` |
| `fs-qa-engineer` | `fs-developer-qa` |
| `fs-reviewer` | `fs-developer-reviewer` |
| `fs-devops-engineer` | `fs-developer-devops` |
| `fs-release-manager` | `fs-developer-release` |
| agent `fs-code-reviewer` | agent `fs-developer-code-reviewer` |

Future stacks follow the same pattern: `fs-developer-<stack>`.

## [0.1.0] - 2026-11-03
### Added
- First release. Router `fs-developer` (`/fs`), stack detection (Flutter supported; others report "not supported yet").
- Lifecycle skills: architect (with `detect_project.py`), Flutter build (with `scaffold_app.py`: pub workspace, module registry, Riverpod 3, go_router, Material 3 tokens; Windows first), maintainer, QA gate (with `qa_gate.py`), reviewer and reviewer agent, release.
- Role skills: UI, API, security, performance, devops.
- Foundational references: lean coding, Flutter shortcuts, coding standards, i18n, accessibility, precedence, ownership (builder-safe rules), official docs.
- `.mcp.json` declaring the Dart and Flutter MCP server; PostToolUse hook formatting edited `.dart` files.
