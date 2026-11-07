---
name: fsdevops-designer
description: UI role skill of Full-Stack DevOps for Flutter. Builds widgets and screens, adaptive layouts across desktop, tablet, phone and web (window size classes, NavigationRail and NavigationBar, keyboard and mouse on desktop), feed and list UIs with mixed card types and swipe actions, loading, empty and error states, and design tokens in code. Loaded by the build skills when a plan touches UI. Use when the user asks directly for layout, widget or feed-UI questions. Also acts as the UI/UX designer of a change: reuses packages/ui and the Widgetbook catalog first, keeps design tokens in one place, designs every state, applies accessibility rules, and gathers visual evidence (screenshots per size class, light and dark, 200% text).
license: MIT
metadata:
  displayName: "FSDevOps UI Developer"
  version: "0.5.0"
  author: "@wasimness"
  company: "SyncWin"
---

# FSDevOps UI Developer

Applies `fsdevops/references/accessibility.md`, `i18n.md` and `fsdevops-flutter/references/theming.md`.

## Adaptive layout
- Size classes from `MediaQuery.sizeOf(context).width`: compact <600, medium <840, expanded >=840.
- Navigation: expanded → `NavigationRail` (extended) or a side panel; medium → `NavigationRail`; compact → `NavigationBar`.
- List-detail on expanded widths: two panes; compact: push the detail route.
- Desktop first: hover states, tooltips, right-click (`MenuAnchor`), keyboard shortcuts for main actions, visible scroll bars, `SelectableText` where people copy text, a minimum window width the layout survives.

## Screens
- Every async screen renders loading, error (with Retry) and empty states from `AsyncValue`.
- Screens compose small widget classes; no `_buildX()` helpers.
- Constrain readable text width (about 700 logical pixels) on wide screens.

## Designer workflow (brief to code)
Work like the designer on the team: the brief decides, taste does not.
1. Read the UI block of the brief (audience, devices and input, decisions per screen, data read, the one write, states list, theme source, a11y target). A line that cannot be filled: ask, do not guess.
2. Reuse ladder: check `packages/ui` and its Widgetbook catalog; reuse as is, then adapt (a parameter, a token), then build new. A new widget names the gap it fills.
3. One primary action per screen; the next step is obvious; recognition over recall.
4. Tokens before widgets, states before polish, a11y while building, visual evidence at the end (`references/design-system.md`, `references/visual-qa.md`).

## States (design all, not just the happy path)
Loading, empty (first run, filtered to nothing, load error), error with Retry, offline, saved or done, disabled, long text, short text, RTL. Read-only views say so in words. Table and copy rules: `references/design-system.md`.

## Accessibility while building
Rules live in `fsdevops/references/accessibility.md`; do not restate them. Designer additions: check both light and dark schemes, a logical focus order on desktop, no colour-only signals, one `Semantics` label per merged card, and run the flutter_test accessibility guidelines (tap target, labelled target, contrast) on key screens.

## Widgetbook
Every new reusable widget gets use-cases for its states and size classes in the catalog. Details: `references/design-system.md`.

## Visual QA
Render key screens at compact, medium and expanded widths, light and dark, 200% text scale; look at the screenshots, then record the paths. A check that cannot run is NOT RUN, never PASS. Details: `references/visual-qa.md`. The independent judgement pass is `fsdevops-critic`.

## Feed and lists (`references/feed-ui.md`)
Mixed card types, actions, refresh, pagination.

## Builder-owned UI
When a visual builder owns the UI package, widgets there take plain values and callbacks; wire state in the module package (`fsdevops/references/ownership.md`).

Finish with a scratchpad: widgets added, layouts checked per size class, open items.

Scripts, if any are added later, run from `./tools/` of the project, never from a path under the home `.claude` folder.
