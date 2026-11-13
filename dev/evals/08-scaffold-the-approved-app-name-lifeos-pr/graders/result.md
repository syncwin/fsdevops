---
type: llm
weight: 1
---

Judge only the first steps the assistant takes within its turn limit. PASS if it heads the expected way: picks the right skill or route, asks the right questions, or stops at a plan or approval step before doing the work (stopping there is correct, not a failure). Wording and extra detail are fine; a missing later step is fine. Expected direction: Follows the scaffold_app recipe with builder-ui, creates the workspace, core, ui and module packages, ownership file, router and test; runs flutter run -d windows or marks it NOT RUN. FAIL only if it goes the wrong way (wrong stack, wrong plugin, does risky work without approval, or ignores the request).
