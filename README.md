# Full-Stack DevOps (`fsdevops`)

A Claude plugin that takes an app from idea to release: plan, build, update, test, review and ship. **Flutter first** (Windows desktop, then Android, iOS and web). More stacks (React, Next.js and others) plug in later as their own build skills, sharing the same lifecycle.

**Download:** [fsdevops.plugin](https://github.com/syncwin/fsdevops/releases/latest/download/fsdevops.plugin) (always the latest release)

## What it does
`/fsdevops` (or just ask to build, fix, test, review or release app code) runs:

1. **Plan** (`fsdevops-plan`): detects the project, asks up to five questions, writes a PRD or change brief, gets one approval.
2. **Build**: `fsdevops-flutter-build` for new apps and modules (pub workspace, module registry with runtime on/off, Riverpod 3, go_router, Material 3 tokens), `fsdevops-maintain` for changes.
3. **QA gate**: format, fix, analyze, test, codegen and a release build, reported as PASS / FAIL / NOT RUN.
4. **Critique** (UI work): `fsdevops-critic`, a read-only design and UX pass with severity, evidence and fix.
5. **Independent review** by a read-only agent, one lens per pass.
6. **Release**: versions, changelog, Windows / Android / iOS / web packaging.

Role skills: designer (UI/UX), API and offline data, security, performance, devops, release. Always applied: write less (lean coding), coding standards, i18n, accessibility.

## Requirements
- Flutter SDK on PATH (Dart 3.9+ for the Dart MCP server). Windows desktop builds need Visual Studio with "Desktop development with C++".
- Without the SDK the plugin still plans and writes code; gate steps report NOT RUN with the command to run.

## Layout
```
adapters/claude/      the Claude plugin, text only: .claude-plugin, skills (with recipes), agents, evals, prompts
dev/                  maintainer-only Python tools and the old hook (never shipped)
docs/                 feature docs, trademarks, icon source
.claude-plugin/marketplace.json   points to adapters/claude
```
`main` is the only branch and the source for the Anthropic plugin directory. The shipped plugin has no hooks, scripts or Python: what used to be scripts and a hook are recipes in `adapters/claude/skills/*/references/` (`detect_project`, `scaffold_app` (three files), `qa_gate`, `docs_gate`, `format_dart`) that Claude follows. The Dart MCP server stays in `adapters/claude/.mcp.json` (config only, it runs `dart mcp-server` from your own SDK).

## Install
```
/plugin marketplace add <path-or-repo>
/plugin install fsdevops@syncwin-fsdevops
```

## Works with visual builders
If a visual builder (for example Nowa) edits part of the UI, record it in `.claude/ownership.md`; the plugin follows builder-safe editing rules for those paths. It never operates other apps itself: app-operator plugins can do that and may call this plugin, never the other way around.

## Not for
WordPress (use `fswpdevops`).

## License
MIT. See `CREDITS.md` for the projects that shaped it and `SECURITY.md` for reporting issues. Contact: support@syncwin.com.
