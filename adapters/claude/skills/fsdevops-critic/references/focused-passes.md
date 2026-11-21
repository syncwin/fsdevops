# Focused passes

A pass is a narrow edit with one goal. The critic recommends at most two passes per screen in its verdict; `fsdevops-design` runs them (the critic never edits). Each pass keeps behaviour, copy meaning, tokens and accessibility intact, then re-shoots the screen (`fsdevops-design/references/visual-qa.md`).

| Pass | Fits a critique that finds | Typical changes | Out of scope |
|---|---|---|---|
| bolder | flat, generic, no focal point | strengthen one focal element (size, weight, colour role), increase contrast between levels, use the signature detail from `DESIGN.md` | add new colours, gradients or decoration |
| quieter | busy, loud, everything competes | remove borders and shadows that carry no meaning, merge duplicate labels, lower secondary weight, add space | hide actions the task needs |
| typeset | weak hierarchy in text, uneven rhythm | map each text to a `TextTheme` role, fix line height and width, tabular figures for numbers | introduce a third family |
| layout | misalignment, cramped or empty areas, breaks at a size class | align to the grid, fix spacing to the step scale, re-check compact and expanded | change navigation without the brief |
| polish | ready but rough | states (hover, focus, pressed, disabled), motion tokens, truncation, empty and error copy, last pixel alignment | start before Critical and Important findings are fixed |

Order when several apply: layout, typeset, quieter or bolder (never both on one screen), polish last.
