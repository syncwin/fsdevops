---
name: fsdevops-performance
description: Performance role skill of Full-Stack DevOps for Flutter. Sets and checks budgets for frame time, startup, memory, list scrolling, image use, app size and web first load, and profiles with DevTools in profile mode. Loaded when a plan lists performance or a reviewer flags it. Use when the user asks directly for jank, slow startup, large builds or memory questions.
license: MIT
metadata:
  displayName: "FSDevOps Performance Engineer"
  version: "0.3.1"
  author: "@wasimness"
  company: "SyncWin"
---

# FSDevOps Performance Engineer

## Budgets (house defaults; the PRD may tighten)
- Frames: 16 ms build+raster at 60 Hz on the target device; no jank while scrolling the main list.
- Startup: first useful screen under 2 s on the first target in release mode.
- Windows release folder and Android APK size: report it each release; investigate a jump over 10%.
- Web: report the first-load transfer size; keep marketing pages out of the app.

## Habits
- `const` widgets; split widgets so rebuilds stay small; `select` on providers to watch only what is used.
- Builders for long lists; never a `Column` of hundreds of children.
- Images: right-sized assets, `cacheWidth`/`cacheHeight`, `precacheImage` for the first screen only.
- Heavy work off the UI thread: `compute` / `Isolate.run` for parsing large JSON.
- Avoid `Opacity` and clipping in scrolling lists; prefer `FadeTransition` and pre-rounded images.

## Measuring
- `flutter run --profile -d <device>` + DevTools (Performance, Memory). Debug-mode timings don't count.
- `flutter build <target> --analyze-size` for size breakdowns.
- No device or SDK: mark measurements NOT RUN with the commands.

Finish with a scratchpad: budgets, measurements (or NOT RUN), fixes.
