---
name: fsdevops-reviewer
description: Independent review stage of Full-Stack DevOps. Reviews finished app code read-only through one lens per pass - security, quality, lean (over-engineering), accessibility or performance - reporting only findings with confidence 80 or higher in a fixed format with severity, location, evidence and fix, and ends with a one-line verdict. Run after the fsdevops-qa gate is green, preferably through the fsdevops-code-reviewer agent. Use when the user asks directly to review any Flutter code.
license: MIT
metadata:
  displayName: "FSDevOps Reviewer"
  version: "0.3.4"
  author: "@wasimness"
  company: "SyncWin"
---

# FSDevOps Reviewer

Read-only. Scope: the folder and the approved brief; never the build transcript. On a fix-loop re-run, only changed files.

## Lenses (one per pass)
| Lens | Look for |
|---|---|
| security | `fsdevops-security` rules: secrets in code or config, tokens in plain storage or logs, unvalidated deep links, risky permissions, unsafe dependencies |
| quality | docs out of step with the change (`coding-standards.md` Documentation standard: changelog line, feature file, index), bugs, unhandled errors and states, `BuildContext` across async gaps, state leaks, wrong provider scope, missing tests for changed behaviour, broken ownership rules |
| lean | code the plan didn't need, duplicate utilities, abstractions with one use, a second state or routing library (`fsdevops/references/lean-coding.md`) |
| a11y | missing semantics, small targets, contrast, keyboard paths on desktop |
| performance | rebuild storms, unbounded lists, heavy `build`, oversized images |

## Finding format
```
[Critical|Important|Minor] <title> (confidence NN)
Where: path:line
Evidence: <quoted code or behaviour>
Fix: <smallest change>
```
Only confidence >= 80. Security lens adds an "Unverified suspicions" list below 80.

## Verdict
One line: `PASS` (no Critical or Important), or `FAIL: N Critical, M Important`. A security-lens FAIL blocks release (`fsdevops-release`).

Finish with a scratchpad: lens, scope, verdict.
