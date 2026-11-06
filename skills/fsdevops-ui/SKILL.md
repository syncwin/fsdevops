---
name: fsdevops-ui
description: UI role skill of Full-Stack DevOps for Flutter. Builds widgets and screens, adaptive layouts across desktop, tablet, phone and web (window size classes, NavigationRail and NavigationBar, keyboard and mouse on desktop), feed and list UIs with mixed card types and swipe actions, loading, empty and error states, and design tokens in code. Loaded by the build skills when a plan touches UI. Use when the user asks directly for layout, widget or feed-UI questions.
license: MIT
metadata:
  displayName: "FSDevOps UI Developer"
  version: "0.4.0"
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

## Feed and lists (`references/feed-ui.md`)
Mixed card types, actions, refresh, pagination.

## Builder-owned UI
When a visual builder owns the UI package, widgets there take plain values and callbacks; wire state in the module package (`fsdevops/references/ownership.md`).

Finish with a scratchpad: widgets added, layouts checked per size class, open items.
