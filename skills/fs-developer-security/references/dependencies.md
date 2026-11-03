# Dependencies: health and licence

Before adding a package (and only after the lean ladder says a package is needed):
- **Ask the user** for a new dependency, naming it, its licence and why.
- **Health:** pub.dev score and "verified publisher" when present, last release within about 12 months, supports the target platforms (check the platform badges), null-safe, Dart 3.
- **Licence:** permissive (MIT, BSD, Apache-2.0) fits any project. GPL/AGPL in a client app distributed under MIT is a red flag; tell the user. Record the licence in the PR.
- **Audit command:** `flutter pub deps --style=compact` for the tree; list licences with a licence-checker tool if the project has one, otherwise check each direct dependency's pub.dev page (mark transitive licences NOT RUN).
- **Pinning:** caret constraints in packages; commit `pubspec.lock` for apps.
- **FOSS store builds (F-Droid):** no proprietary SDKs (Firebase, Play Services) in that flavor.
