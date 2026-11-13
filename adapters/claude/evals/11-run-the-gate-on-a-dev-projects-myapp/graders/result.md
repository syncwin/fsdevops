---
type: llm
weight: 1
---

Judge only the first steps the assistant takes within its turn limit. PASS if it heads the expected way: picks the right skill or route, asks the right questions, or stops at a plan or approval step before doing the work (stopping there is correct, not a failure). Wording and extra detail are fine; a missing later step is fine. Expected direction: Follows the qa_gate recipe and reports each step as PASS, FAIL or NOT RUN with tool versions; never calls a skipped step clean. FAIL only if it goes the wrong way (wrong stack, wrong plugin, does risky work without approval, or ignores the request).
