# Flutter shortcuts (use these before custom code)

| Need | Use |
|---|---|
| Responsive layout | `LayoutBuilder`, `MediaQuery.sizeOf`, `NavigationBar` / `NavigationRail` / `NavigationDrawer` by width |
| Consistent styling | `ThemeData` + component themes + `ThemeExtension` tokens, not per-widget styles |
| Colours | `ColorScheme.fromSeed` |
| Lists | `ListView.builder` / `SliverList.builder`, `RefreshIndicator`, `Dismissible` |
| Forms | `Form` + `TextFormField` validators |
| Dialogs and sheets | `showDialog`, `showModalBottomSheet`, `showMenu`, `MenuAnchor` |
| Keyboard shortcuts (desktop) | `Shortcuts` + `Actions` + `Intent`, `CallbackShortcuts` |
| Hover, cursor, right-click (desktop) | `MouseRegion`, `ContextMenuController` / `MenuAnchor` |
| Window size and title (desktop) | Defaults in `windows/runner/main.cpp`; a package only if runtime control is required |
| Dates and numbers | `intl` (`DateFormat`, `NumberFormat`) |
| Localization | `flutter_localizations` + ARB + `l10n.yaml` |
| JSON | `dart:convert` for a few models; json_serializable after that |
| Debounce, async work | `Timer`, `Future.wait`, `Stream` transforms |
| Images and icons | `Image.asset`, `Icons`, `Icon` with `semanticLabel` |
| Animations | Implicit animations (`AnimatedContainer`, `AnimatedSwitcher`) before controllers |
