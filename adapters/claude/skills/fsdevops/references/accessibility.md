# Accessibility

- Every interactive element has a semantic label (`Semantics`, `tooltip`, `semanticLabel`) and a 48x48 minimum hit target (44 on iOS-only screens).
- Contrast at least 4.5:1 for text, 3:1 for large text and icons; check theme colours, not just one screen.
- Layouts work at 200% text scale without clipping.
- Full keyboard use on desktop and web: focus order, visible focus, `Shortcuts`/`Actions`, Esc closes dialogs.
- Screen readers: test with Narrator (Windows), TalkBack (Android), VoiceOver (iOS/macOS) when the target is in scope; otherwise NOT RUN.
- Motion: respect `MediaQuery.disableAnimationsOf`.
- Custom cards and list items merge semantics (`MergeSemantics`) so a card reads as one item with its actions.
