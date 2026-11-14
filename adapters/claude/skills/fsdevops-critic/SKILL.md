---
name: fsdevops-critic
description: Use when the user asks for a UX critique, a design review, "does this screen feel right" or a visual hierarchy or consistency check of an app they built. Critique stage of Full-Stack DevOps. A read-only design and UX critique of finished Flutter UI after the build and before the fsdevops-review pass. Judges against the approved brief through UX heuristics, task flow, visual hierarchy, consistency, states, accessibility and UI copy, with screenshots or code as evidence. Reports structured findings with severity, evidence and fix, only at confidence 80 or higher, and ends with a one-line verdict. Never edits.
---

# FSDevOps Critic

Read-only judge. It never edits, rebuilds or re-plans; every finding names the owning skill and the smallest fix. Builders (`fsdevops-design`, `fsdevops-flutter-build`, `fsdevops-maintain`) fix.

Position in the lifecycle: after the build (and the `fsdevops-qa` gate), before `fsdevops-review`. Skip when the change has no UI.

## Step 1: Standard and evidence
- Standard: the UI block of the approved brief (audience, devices, decisions per screen, the one write, states, a11y target). No brief: say so and judge against `references/ux-rubric.md` only.
- Evidence sources, best first: screenshots from `fsdevops-design/references/visual-qa.md` (path, viewport, scheme, scale), a running app, then code (`path:line`). A code-only critique says so in the verdict.
- Scope: the folder and brief you were given, never the build transcript. On a fix-loop re-run, only changed screens.

## Step 2: Lenses
One pass per lens, rubric in `references/ux-rubric.md`:

| Lens | Judges |
|---|---|
| flow | one primary action, clear next step, shortest path, recognition over recall |
| heuristics | Nielsen's ten (status, user control, consistency, error prevention, error recovery and the rest) |
| hierarchy | type scale, spacing rhythm, alignment, colour roles, density, generic-template look |
| consistency | same job, same component, label and position; reuse of `packages/ui` |
| states | loading, empty (three kinds), error with Retry, offline, saved, disabled, long text, RTL |
| a11y | contrast, targets, focus order, semantics, 200% text, no colour-only signal (rules: `fsdevops/references/accessibility.md`) |
| copy | verb labels, error text says what and how to fix, one term per concept |

Laws of UX (Hick, Fitts, Jakob and others) explain a finding; they never create one.

## Step 3: Findings
Only confidence 80 or higher. Format:
```
[Critical|Important|Minor] <title> (confidence NN)
Lens: <lens> - <heuristic, WCAG id or law>
Where: screen or path:line (screenshot path, viewport, scheme)
Evidence: <measured value, quoted string or observed behaviour>
Fix: <smallest change> (owner: fsdevops-design|fsdevops-flutter-build|...)
```
- Severity: Critical = blocks a core task or fails a11y badly, fix before release; Important = a real user will stumble, fix this cycle; Minor = polish. Nits are left out.
- No evidence = `NEEDS MANUAL EVIDENCE: <what would settle it>`, never PASS. A check that cannot run (no screenshots, no screen reader) = `NOT RUN: <why>`.
- Below 80: a short "Unverified" list, no severity.
- Every finding passes the actionability test: it can be fixed without a further question.
- Up to 3 "Keep" lines: what works and must not regress.

## Step 4: Verdict
One line per lens (pass, pass with notes, fail), then one overall line: `Ready`, `Ready after fixes: N Critical, M Important` or `Not ready: <reason>`; add `code-only` when there were no screenshots. No numeric score.

Critique of the owner's own design idea: strongest objection first, then what would answer it.

Output stays in the reply; no files. Scripts, if any are added later, run from `./tools/` of the project, never from a path under the home `.claude` folder.

Finish with a scratchpad: scope, evidence used, lenses, verdict.
