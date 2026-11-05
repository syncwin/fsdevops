# CI (GitHub Actions)

Template `.github/workflows/ci.yml` (adjust the Flutter version to the project's):

```yaml
name: ci
on: [push, pull_request]
jobs:
  gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - uses: subosito/flutter-action@1a449444c387b1966244ae4d4f8c696479add0b2 # v2
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
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - uses: subosito/flutter-action@1a449444c387b1966244ae4d4f8c696479add0b2 # v2
        with:
          channel: stable
          cache: true
      - run: flutter pub get
      - run: flutter build windows --release
        working-directory: apps/<app>
```

Security job (add to every project; actions below are pinned to full commit SHAs, re-check and update the SHA when bumping):

```yaml
permissions:
  contents: read
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
        with:
          fetch-depth: 0
      - name: Secret scan
        run: |
          # install a pinned gitleaks release, then:
          gitleaks detect --redact --no-banner
      - name: Dependency audit
        run: |
          # install a pinned osv-scanner release, then:
          osv-scanner --lockfile=pubspec.lock
```

Make `security` a required check next to `gate`.

- Public repos: Actions minutes are free; private repos use the plan's monthly minutes (Windows runners cost more per minute, so run the Windows job on main and PRs only).
- Least privilege: workflow-level `permissions: contents: read`; use `pull_request`, not `pull_request_target`, for untrusted code; never echo secrets or pass them to forks.
- Never put secrets in the workflow file; use repository secrets and `${{ secrets.NAME }}`.
- Signing in CI only after the user sets the secrets (`fsdevops-release`).
