---
name: fsdevops-release
description: Release stage of Full-Stack DevOps. Versions, changelogs, builds and packages apps for each target - Windows (release folder, MSIX, installer, Microsoft Store), Android (APK, App Bundle, Play internal testing, F-Droid), iOS (TestFlight via a Mac or cloud build) and web (static hosting) - with signing handled only through the user's own keys. Invoked by fsdevops at the ship step. Use when the user asks directly for packaging or publishing questions.
license: MIT
metadata:
  displayName: "FSDevOps Release Manager"
  version: "0.4.1"
  author: "@wasimness"
  company: "SyncWin"
---

# FSDevOps Release Manager

## Every release
1. Pre-release check (`fsdevops-qa` §4) green on the release target, **security gate** passed: reviewer security lens has no Critical or Important findings, secret scan and dependency audit run (or NOT RUN, named), `fsdevops-security` §Secure by default satisfied.
2. Version: `version: X.Y.Z+N` in the app's `pubspec.yaml` (semver for X.Y.Z, build number N always increases).
3. `CHANGELOG.md`: move `[Unreleased]` into `## [X.Y.Z] - date` (keep a fresh empty `[Unreleased]` on top); categories Added / Changed / Deprecated / Removed / Fixed / Security. Feature files and index: Status, Since, Updated and History match X.Y.Z. Pre-1.0 = beta; `1.0.0` only when the owner says. Standard: `fsdevops/references/coding-standards.md`.
4. Build, package, record artifact paths and sizes.
5. Publishing, uploading, tagging or pushing needs the user's explicit yes for that action.

## Targets (`references/targets.md`)
Windows, Android, iOS, web: commands, packaging and signing.

## Signing
Keys and certificates belong to the user. Never create, store or commit them in the repo; reference them via environment variables or CI secrets and give the user the steps. Release artifacts are signed with those keys and shipped with a SHA-256 checksum file; build from a clean checkout of the tagged commit.

Finish with a scratchpad: version, artifacts, what was published (or waiting for a yes).
