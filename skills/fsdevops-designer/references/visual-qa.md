# Visual QA (designer evidence)

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
