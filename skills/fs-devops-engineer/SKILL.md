---
name: fs-devops-engineer
description: DevOps role skill of Full-Stack Developer. Sets up and checks the toolchain (Flutter SDK, Visual Studio C++ workload for Windows desktop, Android SDK and a physical device, Dart MCP server), flavors and per-environment config, and GitHub Actions CI that runs the same gate as fs-qa-engineer. Use when the user asks about setup, "flutter doctor" problems, flavors or CI.
license: MIT
metadata:
  displayName: "FS DevOps Engineer"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# FS DevOps Engineer

## Toolchain (Windows first)
1. Flutter SDK on PATH: `flutter --version`; `flutter doctor -v`. Install location is the user's choice; ask before installing anything.
2. Windows desktop: Visual Studio (not VS Code) with "Desktop development with C++" (`Microsoft.VisualStudio.Workload.NativeDesktop`); then `flutter devices` lists `windows`. A Build Tools-only install with that workload also works for CLI builds.
3. Android: Android SDK + platform-tools; on low-end PCs use a physical phone (USB or wireless debugging) instead of the emulator. `flutter doctor --android-licenses`.
4. Dart MCP server: `claude mcp add --transport stdio dart -- dart mcp-server` (the plugin's `.mcp.json` declares it). Needs Dart 3.9+.
5. Report each item PASS / FAIL / NOT RUN.

## Config and flavors
- Per-environment values: `--dart-define-from-file=config/<env>.json` (git-ignored real files, committed `*.example.json`).
- Flavors only when builds really differ (for example a store build with proprietary push and a FOSS build without): Android product flavors + a Dart entry point per flavor (official flavors page).

## CI (`references/ci.md`)
GitHub Actions running the same gate.

Finish with a scratchpad: toolchain table, config, CI status.
