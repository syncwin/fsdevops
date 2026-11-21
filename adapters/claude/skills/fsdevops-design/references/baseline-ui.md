# Baseline UI rules (Flutter)

Hard rules every screen meets before critique. Each line is checkable in code or a screenshot. Accessibility rules live in `fsdevops/references/accessibility.md`.

## Type and figures
- Numbers that change or line up (money, counts, timers, tables) use tabular figures: `fontFeatures: [FontFeature.tabularFigures()]` in the text style token.
- Leave letter spacing at the theme's `TextTheme` values unless the brief asks; never tighten headings further, no negative `letterSpacing` on body or labels.
- Loading text ends with an ellipsis character; units keep a non-breaking space to their number.
- Body line height about 1.4 to 1.6; readable width capped (about 700 logical px).
- Truncation is a choice: `maxLines` plus `TextOverflow.ellipsis` and the full text in a tooltip or detail view.

## Actions and dialogs
- Destructive or irreversible actions get a real `AlertDialog` (or `showAdaptiveDialog`) that names the object and the consequence, with the safe button as default; or an undo `SnackBar` when the action is reversible. Never a silent delete.
- Buttons show a loading state and block double submit while work runs.
- One primary (filled) button per view; the others tonal, outlined or text.

## Motion
- Durations from tokens; feedback on a tap or hover at most about 200 ms (`Durations.short4`), larger transitions up to `Durations.medium2`; Material easing curves (decelerate on entry); no literal `Duration` in screens.
- Looping or auto-playing motion stops off-screen and offers pause when it runs longer than a few seconds.
- Animate opacity and transform, not layout size, where possible; no motion that blocks input.
- Respect `MediaQuery.disableAnimationsOf(context)`: skip or shorten motion.

## Layout and states
- Spacing from the step scale only; content respects `SafeArea`.
- Layout stays stable while loading (skeleton or fixed-size placeholder); no jump when data arrives.
- Empty, error and offline states per `design-system.md`.

## Not carried over from web sources
CSS utility classes, viewport units, `cursor` rules and browser `confirm()`: Flutter has its own equivalents above.
