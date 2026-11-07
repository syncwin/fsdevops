# Design system rules (designer)

Flutter theming mechanics live in `fsdevops-flutter/references/theming.md`; accessibility in `fsdevops/references/accessibility.md`. This file adds the designer's decisions only.

## Reuse before building
| Step | Do | Evidence |
|---|---|---|
| 1 | Search `packages/ui` and its Widgetbook catalog for the job (not the look) | search terms and hits |
| 2 | Reuse as is | import path |
| 3 | Adapt: add a parameter or token, never fork a copy | diff in `packages/ui` |
| 4 | Build new only when 1-3 fail; name the gap | one line in the brief or scratchpad |
Paths owned by a visual builder follow `fsdevops/references/ownership.md`.

## Tokens
- One source for colour roles, type scale, spacing, radii, elevation, motion durations. No literal colours, sizes or durations in screens.
- Spacing on a fixed step scale (for example 4, 8, 12, 16, 24, 32); repeated one-off values mean a missing token.
- Colour by role (surface, on-surface, primary, error), not by hue name. Prove contrast for both schemes on the actual pairs (text 4.5:1, large text and UI parts 3:1).
- Density follows the platform: tighter on desktop, 48 dp targets on touch.

## Components
- Small widget classes with plain values and callbacks; state is wired by the caller.
- Every interactive component covers: default, hover, focus, pressed, disabled, loading, error.
- Consistent patterns: same action, same label, same position across screens.

## States table (fill per screen)
| State | Shows | Action |
|---|---|---|
| Loading | skeleton or progress that keeps layout stable | none or cancel |
| Empty, first run | what this is and the first step | one primary action |
| Empty, filtered | which filter hid items | clear filters |
| Error | what failed in plain words | Retry |
| Offline | cached data marked as such | queue or retry later |
| Saved | quiet confirmation | undo when reversible |

## Adaptive layout decisions
Pick per screen: single column, list-detail, or multi-pane at each size class; navigation per `SKILL.md`; text width capped; input modes (touch, mouse, keyboard) all work; safe areas respected.

## Widgetbook
- One component per use-case group; a use-case per state and per size class; light and dark both viewable.
- Catalog use-cases double as screenshot sources for visual QA.

## Copy
Labels are verbs; error text says what happened and how to fix it; one term per concept; sentence case unless the product says otherwise; strings through `i18n.md`, with room for longer translations.
