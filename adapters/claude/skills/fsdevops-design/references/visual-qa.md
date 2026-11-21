# Visual QA (designer evidence)

## Shoot, fix, re-shoot
1. Shoot each key screen at phone size (390x844 logical) and desktop size (1440x900), plus the size-class checks below. Sources: golden or widget tests setting `tester.view.physicalSize` and `devicePixelRatio`, `integration_test` `takeScreenshot`, the Dart MCP widget inspector, a resized Windows window, or Playwright only for the Flutter web target.
2. Look at every image (do not only save it): overflow stripes, clipped text, cramped targets, broken alignment, wrong navigation for the size.
3. Fix the smallest cause, then re-shoot the same screen and size; keep before and after paths. Stop after two rounds on one screen and report what is left.
4. Record path, size, scheme and text scale per image. No image = NOT RUN with the command that would make it.

Measure, then look. One pass at the end of the build, not per widget.

| Check | How | Pass when |
|---|---|---|
| Size classes | Run on Windows desktop (first target) at compact, medium, expanded; capture screenshots | no clipping, overflow or empty gaps; navigation matches the class |
| Themes | Light and dark | contrast pairs hold; no hard-coded colours leak |
| Text scale | 200% | nothing clipped; actions still reachable |
| Long and RTL text | longest label and an RTL locale | wraps or truncates by design |
| Targets and semantics | flutter_test guidelines (tap target, labelled target, contrast) on key screens | guideline tests pass |
| Keyboard | Tab through each screen | logical order, visible focus, Esc closes dialogs |
| Goldens | golden tests for key screens when the project uses them | match, or the change is intended and reviewed |

- Capture sources: Dart MCP widget inspector, integration tests, or Widgetbook use-cases. Record each screenshot path with viewport, scheme and scale.
- A step the environment cannot run (no device, no screen reader) is NOT RUN with the command to run it.
- Hand the evidence list to `fsdevops-critic`; the critic judges, this file only gathers.
