# Feed UI

- Model cards as a `sealed class FeedCard` with one subclass per type; render with an exhaustive `switch`, so a new type fails to compile until it has a widget.
- `CustomScrollView` + `SliverList.builder`; stable `ValueKey(card.id)` on each item.
- Actions per card: primary button plus a `MenuAnchor` for the rest; on touch, `Dismissible` (or a slidable package with the user's OK) for done and snooze, with Undo in a `SnackBar`.
- `RefreshIndicator` on touch; a Refresh button and F5/Ctrl+R shortcut on desktop.
- Pagination: load the next page when the last few items build; show a footer loader; stop at the end.
- Keep card widgets `const`-friendly and cheap: no heavy work in `build`, images with `cacheWidth`.
- Semantics: one merged node per card with its actions as custom semantics actions.
- Empty feed: a friendly empty state with the one next action.
