---
name: fs-security-engineer
description: Security role skill of Full-Stack Developer, always applied to builds and loaded by review. Covers secrets (never in the app bundle or repo), secure token storage, personal-data privacy and local encryption, input validation, platform permissions, network security, deep-link safety, logging hygiene, and dependency health and licence checks. Use when the user asks any security, privacy or dependency-licence question about an app.
license: MIT
metadata:
  displayName: "FS Security Engineer"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# FS Security Engineer

## Rules (every build)
1. **No secrets in the client or the repo.** Anything shipped in an app can be extracted. API keys that must stay secret live on the server; public config uses `--dart-define-from-file` with a git-ignored file and a committed `*.example`.
2. **Tokens** in `flutter_secure_storage` (Windows Credential Manager, Android Keystore, iOS Keychain). Web has no true secure storage: short-lived tokens, refresh via HTTP-only cookies when the backend allows.
3. **Personal data:** collect the minimum; encrypt local databases holding personal data (SQLCipher for drift) when the PRD says so; clear on sign-out.
4. **Input:** validate at the UI for UX and again at the boundary; never build SQL by string concatenation (drift queries are parameterised).
5. **Network:** HTTPS only; certificate pinning only for your own API and only with a rotation plan.
6. **Deep links:** validate parameters; never act (delete, pay, send) from a link without a confirm screen.
7. **Logs:** no tokens, passwords or personal data; release builds log errors only.
8. **Permissions:** request at the moment of use with a reason; declare only what is used.

## Dependencies (`references/dependencies.md`)
Health and licence check before adding any package.

## Review lens
When `fs-reviewer` runs the security lens, report findings with a weakness name (for example CWE-798 hard-coded credentials) and confidence.

Finish with a scratchpad: secrets found or ruled out, storage, dependency checks.
