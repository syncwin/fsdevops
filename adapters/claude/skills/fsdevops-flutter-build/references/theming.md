# Theming

- `ThemeData(useMaterial3: true, colorScheme: ColorScheme.fromSeed(seedColor: ..., brightness: ...))` for light and dark; `ThemeMode` from settings.
- Design tokens as one `ThemeExtension<AppTokens>` (spacing, radii, durations, elevations) with `copyWith` and `lerp`. Widgets read `Theme.of(context).extension<AppTokens>()!`, never hard-coded numbers.
- Component themes (`filledButtonTheme`, `cardTheme`, `inputDecorationTheme`, `navigationRailTheme`) carry styling; widgets stay plain.
- Typography: `TextTheme` from the theme; custom fonts bundled under `assets/fonts` with their licence noted.
- Builder-owned UI package: the builder may edit the theme file; keep it in the ui package and follow `ownership.md`.
- Desktop density: `VisualDensity.adaptivePlatformDensity`.
