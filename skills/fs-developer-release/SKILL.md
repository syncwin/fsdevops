---
name: fs-developer-release
description: Release stage of Full-Stack Developer. Versions, changelogs, builds and packages apps for each target - Windows (release folder, MSIX, installer, Microsoft Store), Android (APK, App Bundle, Play internal testing, F-Droid), iOS (TestFlight via a Mac or cloud build) and web (static hosting) - with signing handled only through the user's own keys. Invoked by fs-developer at the ship step. Use when the user asks directly for packaging or publishing questions.
license: MIT
metadata:
  displayName: "FS Release Manager"
  version: "0.2.0"
  author: "@wasimness"
  company: "SyncWin"
---

# FS Release Manager

## Every release
1. Pre-release check (`fs-developer-qa` §4) green on the release target.
2. Version: `version: X.Y.Z+N` in the app's `pubspec.yaml` (semver for X.Y.Z, build number N always increases).
3. `CHANGELOG.md`: Added / Changed / Fixed / Removed for X.Y.Z.
4. Build, package, record artifact paths and sizes.
5. Publishing, uploading, tagging or pushing needs the user's explicit yes for that action.

## Targets (`references/targets.md`)
Windows, Android, iOS, web: commands, packaging and signing.

## Signing
Keys and certificates belong to the user. Never create, store or commit them in the repo; reference them via environment variables or CI secrets and give the user the steps.

Finish with a scratchpad: version, artifacts, what was published (or waiting for a yes).
