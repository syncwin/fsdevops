# Recipe: scaffold a Flutter workspace app, part 3 (documentation files and report)

Contents: 9 documentation files, 10 report. Placeholders as in `scaffold_app.md`. Never overwrite existing files.

## 9. Documentation standard (`fsdevops/references/coding-standards.md`)
Use today's date (YYYY-MM-DD) for `{today}` and the module names for `{module list}`.

`<root>/README.md` (the inner fence is part of the file):
````
# {Title}

FILL IN: one sentence on what the app does and for whom.

## Quick start
```
flutter pub get
flutter run -d windows
```

More: [setup](docs/setup.md), [architecture](docs/architecture.md), [ops](docs/ops.md), [features](docs/features/README.md), [changelog](CHANGELOG.md).
````
`<root>/CHANGELOG.md`:
```
# Changelog

Format: [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/); versions: [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html). Pre-1.0 is beta.

## [Unreleased]

## [0.0.1] - {today}

### Added
- Initial scaffold: pub workspace, module registry ({module list}), theme, router.
```
`<root>/docs/setup.md`:
```
# Setup

1. Install the Flutter SDK; run `flutter doctor -v` (Windows desktop needs Visual Studio with the C++ desktop workload).
2. From the repo root: `flutter pub get`.
3. Run: `flutter run -d windows` (or `-d chrome`, an Android device or emulator).
4. Test: `flutter test`. Quality gate: the QA and docs gate recipes of the fsdevops-qa skill.
```
`<root>/docs/architecture.md` (`{pkgs}` = the module package names):
```
# Architecture

- Pub workspace: `apps/{name}` (shell), `packages/{p}_core` (module contract, enabled-module ids), `packages/{p}_ui` (theme tokens), one package per module: {pkgs}.
- Each module exposes one `AppModule` (id, title, icon, routes); the shell lists them once in `lib/registry.dart` and builds routes from the enabled set.
- State: Riverpod. Routing: go_router. Theme: Material 3 with `AppTokens`.
- FILL IN: data layer, external services, platform notes as they appear.
```
`<root>/docs/ops.md`:
```
# Ops

- Build: `flutter build windows --release` (also `apk`, `appbundle`, `web`).
- Release: move `[Unreleased]` in CHANGELOG.md into the new version, set `version:` in `apps/{name}/pubspec.yaml`, tag, build from a clean checkout.
- Config and secrets: never committed; see `.gitignore` and `.pre-commit-config.yaml` (gitleaks).
- Troubleshooting: FILL IN as issues are found.
```
`<root>/docs/features/{m-slug}.md` per module (`{Mt}` = module name as Title Case words, `{pkg}` as above):
```
# {Mt}

**Status:** planned | **Since:** 0.0.1 | **Updated:** 0.0.1

## Context
FILL IN: why this feature exists and who uses it.

## Behaviour
FILL IN: what the user sees and does; states; edge cases; errors; permissions.

## How it works
FILL IN: flow, components and files, data, APIs, config. Code: `packages/{pkg}/`.

## UI
FILL IN: text description of layout, controls and states (no screenshots needed).

## Limits & known issues
None yet.

## History
- 0.0.1: planned (module scaffolded)
```
`<root>/docs/features/README.md`:
```
# Features

One file per feature. Keep this table current (status, since version).

| Feature | Status | Since | File |
|---|---|---|---|
| {Mt} | planned | 0.0.1 | [{m-slug}.md]({m-slug}.md) |
```
(one table row per module)

## 10. Report
List the files written and the files skipped (already existed). If the shell was not created by this run, print the manual steps: in `<app_dir>/pubspec.yaml` add `resolution: workspace` and the dependencies `flutter_riverpod`, `go_router`, `{p}_core`, `{p}_ui` and each module package (workspace packages as `any`); in `lib/main.dart` call `runApp(ProviderScope(overrides: appOverrides, child: const App()));`.

Next steps to print: `cd <root>`, `flutter pub get`, `flutter test apps/{name}`, then `flutter run -d windows` from `apps/{name}`. Run the format step (`fsdevops-qa/references/format_dart.md`) on the generated Dart files.
