# Full-Stack DevOps (`fsdevops`)

A Claude plugin that takes an app from idea to release: plan, build, update, test, review and ship. **Flutter first** (Windows desktop, then Android, iOS and web). More stacks (React, Next.js and others) plug in later as their own build skills, sharing the same lifecycle.

## What it does
`/fsdevops` (or just ask to build, fix, test, review or release app code) runs:

1. **Architect**: detects the project, asks up to five questions, writes a PRD or change brief, gets one approval.
2. **Build**: `fsdevops-flutter` for new apps and modules (pub workspace, module registry with runtime on/off, Riverpod 3, go_router, Material 3 tokens), `fsdevops-maintainer` for changes.
3. **QA gate**: format, fix, analyze, test, codegen and a release build, reported as PASS / FAIL / NOT RUN.
4. **Independent review** by a read-only agent, one lens per pass.
5. **Release**: versions, changelog, Windows / Android / iOS / web packaging.

Role skills: UI, API and offline data, security, performance, devops, release. Always applied: write less (lean coding), coding standards, i18n, accessibility.

## Requirements
- Flutter SDK on PATH (Dart 3.9+ for the Dart MCP server). Windows desktop builds need Visual Studio with "Desktop development with C++".
- Python 3 for the bundled scripts (standard library only).
- Without the SDK the plugin still plans and writes code; gate steps report NOT RUN with the command to run.

## Install
```
/plugin marketplace add <path-or-repo>
/plugin install fsdevops@syncwin-fsdevops
```

## Works with visual builders
If a visual builder (for example Nowa) edits part of the UI, record it in `.claude/ownership.md`; the plugin follows builder-safe editing rules for those paths. It never operates other apps itself: app-operator plugins can do that and may call this plugin, never the other way around.

## Not for
WordPress (use `fswp-developer`).

## License
MIT. See `CREDITS.md` for the projects that shaped it and `SECURITY.md` for reporting issues. Contact: support@syncwin.com.
