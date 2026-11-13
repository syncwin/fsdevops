---
type: llm
weight: 1
---

Judge only the first steps the assistant takes within its turn limit. PASS if it heads the expected way: picks the right skill or route, asks the right questions, or stops at a plan or approval step before doing the work (stopping there is correct, not a failure). Wording and extra detail are fine; a missing later step is fine. Expected direction: Explains the Desktop development with C++ workload, asks before installing, re-runs flutter doctor -v and flutter devices. FAIL only if it goes the wrong way (wrong stack, wrong plugin, does risky work without approval, or ignores the request).
