# Accessibility

- Every interactive element has a semantic label (`Semantics`, `tooltip`, `semanticLabel`) and a 48x48 minimum hit target (44 on iOS-only screens), with at least 8 dp between adjacent targets. Icon-only buttons carry a tooltip or label; purely decorative images use `excludeFromSemantics` or `ExcludeSemantics`.
- Contrast at least 4.5:1 for text, 3:1 for large text and icons; check theme colours, not just one screen.
- Layouts work at 200% text scale without clipping.
- Full keyboard use on desktop and web: focus order, visible focus, `Shortcuts`/`Actions`, Esc closes dialogs.
- Screen readers: test with Narrator (Windows), TalkBack (Android), VoiceOver (iOS/macOS) when the target is in scope; otherwise NOT RUN.
- Motion: respect `MediaQuery.disableAnimationsOf`.
- Focus stays visible: never set focus or highlight colours to transparent; custom tappables use `InkWell`/`FocusableActionDetector` so the theme focus ring shows, and focus is not hidden under sticky bars or sheets (WCAG 2.4.11).
- Roles: use `Checkbox`, `Switch`, `Radio` and `ListTile` variants for toggles; a custom toggle sets `Semantics(checked:)` or `Semantics(toggled:)` plus `button: true` and a label, so screen readers announce role and state. Headings set `Semantics(header: true)`.
- Form fields have a visible label (`InputDecoration.labelText`), not only a hint; errors are announced (`errorText`).
- Key screens run `meetsGuideline(androidTapTargetGuideline)`, `iOSTapTargetGuideline`, `labeledTapTargetGuideline` and `textContrastGuideline` in widget tests.
- Custom cards and list items merge semantics (`MergeSemantics`) so a card reads as one item with its actions.
