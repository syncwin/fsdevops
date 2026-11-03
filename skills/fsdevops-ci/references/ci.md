# CI (GitHub Actions)

Template `.github/workflows/ci.yml` (adjust the Flutter version to the project's):

```yaml
name: ci
on: [push, pull_request]
jobs:
  gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
        with:
          channel: stable
          cache: true
      - run: flutter pub get
      - run: dart format --output=none --set-exit-if-changed .
      - run: flutter analyze --fatal-infos
      - run: flutter test
  windows:
    needs: gate
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
        with:
          channel: stable
          cache: true
      - run: flutter pub get
      - run: flutter build windows --release
        working-directory: apps/<app>
```

- Public repos: Actions minutes are free; private repos use the plan's monthly minutes (Windows runners cost more per minute, so run the Windows job on main and PRs only).
- Never put secrets in the workflow file; use repository secrets and `${{ secrets.NAME }}`.
- Signing in CI only after the user sets the secrets (`fsdevops-release`).
