# Dependencies: health and licence

Before adding a package (and only after the lean ladder says a package is needed):
- **Ask the user** for a new dependency, naming it, its licence and why.
- **Health:** pub.dev score and "verified publisher" when present, last release within about 12 months, supports the target platforms (check the platform badges), null-safe, Dart 3.
- **Licence:** permissive (MIT, BSD, Apache-2.0) fits any project. GPL/AGPL in a client app distributed under MIT is a red flag; tell the user. Record the licence in the PR.
- **Audit command:** `flutter pub deps --style=compact` for the tree; list licences with a licence-checker tool if the project has one, otherwise check each direct dependency's pub.dev page (mark transitive licences NOT RUN).
- **Pinning:** caret constraints in packages; commit `pubspec.lock` for apps and install from it (`flutter pub get --enforce-lockfile` in CI). Pin GitHub Actions to a full commit SHA, and pre-commit hooks to a released tag.
- **Vulnerability audit:** run `osv-scanner --lockfile=pubspec.lock` (or `dart pub outdated` plus the pub.dev advisories) on every release and in CI; a known High/Critical advisory without a fix or mitigation blocks release. Mark the audit NOT RUN when the tool is missing; never call it clean.
- **Typosquatting:** check the exact name, publisher and repo link before adding; prefer verified publishers.
- **FOSS store builds (F-Droid):** no proprietary SDKs (Firebase, Play Services) in that flavor.
