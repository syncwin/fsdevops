# State and routing

## Riverpod 3 (default)
- `ProviderScope` at the root in `main.dart`.
- Read-only values: `Provider`; async loads: `FutureProvider` / `AsyncNotifierProvider`; mutable state: `NotifierProvider`. Codegen (`@riverpod`) only if the project already uses build_runner.
- Repositories are providers, so tests override them (`ProviderScope(overrides: [...])`).
- `ref.watch` in build, `ref.read` in callbacks, `ref.listen` for side effects (snackbars, navigation).
- After `await` in a notifier, check `ref.mounted` before touching state.
- Do not build sync or offline persistence on Riverpod's experimental features; use the data layer (`fs-developer-api`).
- Existing Bloc, Provider or other library: keep it and follow its docs; never mix.

## go_router (default)
- One `GoRouter` built in the shell from enabled modules; expose it through a provider so module changes rebuild routes.
- Main sections: `StatefulShellRoute.indexedStack` (keeps each section's state); the shell scaffold switches between `NavigationRail` (expanded and medium) and `NavigationBar` (compact).
- Typed paths as constants per module; no string paths scattered in widgets.
- Deep links: a custom scheme for desktop and mobile only when the PRD needs them; web uses the path strategy.
- Redirects for auth or disabled modules live in one `redirect` function.
