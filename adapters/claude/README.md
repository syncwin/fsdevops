# Full-Stack DevOps (Claude plugin)

Plans, builds, updates, verifies, reviews and releases apps, Flutter first (Windows desktop, then Android, iOS and web). It works in Claude Code, Cowork and the desktop app.

## Install

```
/plugin marketplace add syncwin/fsdevops
/plugin install fsdevops@syncwin-fsdevops
```

## Use

Then type `/fsdevops` or ask to build, fix, test, review or release app code. The `fsdevops` skill is the router: it detects the stack, picks a skill from its routing table and sequences plan, build, QA gate, critique, independent review and release.

The plugin is text only: no hooks, scripts or Python. What used to be scripts and a hook are recipes Claude follows with Read, Glob, Grep and Bash:

| Recipe | Where |
|---|---|
| Detect the project | `skills/fsdevops-plan/references/detect_project.md` |
| Scaffold a Flutter workspace app | `skills/fsdevops-flutter-build/references/scaffold_app.md` |
| Format Dart files after edits | `skills/fsdevops-qa/references/format_dart.md` |
| Mechanical QA gate | `skills/fsdevops-qa/references/qa_gate.md` |
| Documentation gate | `skills/fsdevops-qa/references/docs_gate.md` |

The Dart and Flutter MCP server is declared in `.mcp.json` (`dart mcp-server`, run by your own Dart SDK; it needs Dart 3.9 or newer).

## Skills

`fsdevops` (router), `fsdevops-plan`, `fsdevops-flutter-build`, `fsdevops-maintain`, `fsdevops-qa`, `fsdevops-critic`, `fsdevops-review`, `fsdevops-design`, `fsdevops-api`, `fsdevops-security`, `fsdevops-performance`, `fsdevops-ci`, `fsdevops-release`; agent `fsdevops-code-review` (read-only reviewer).

See the root README for install and layout. Contact: see the author entry in `.claude-plugin/plugin.json`.
