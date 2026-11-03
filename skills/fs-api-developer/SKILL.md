---
name: fs-api-developer
description: Data role skill of Full-Stack Developer for Flutter. Builds the API client (typed from an OpenAPI spec or hand-written), models, repositories, auth token handling, error mapping, retries, offline cache with an outbox write queue, and sync conflict rules. Loaded by the build skills when a plan touches data or a backend. Use when the user asks directly for API, models, offline or sync questions.
license: MIT
metadata:
  displayName: "FS API Developer"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# FS API Developer

## Client
- One HTTP client per app (existing one wins; default `dio`). Base URL and flags from config per flavor, never hard-coded secrets (`fs-security-engineer`).
- OpenAPI spec available: generate the client and models in CI-reproducible steps; commit the spec, not hand edits to generated files.
- No spec: small hand-written client per resource; models with freezed + json_serializable once there are three or more, otherwise plain classes with `fromJson`/`toJson`.
- Interceptors: auth header, retry with backoff for idempotent requests (GET, PUT with ids) on timeouts and 5xx, one log line per failure.
- Map transport errors to typed app errors at the repository boundary.

## Repositories
Interfaces only when a fake is needed in tests or two sources exist; otherwise a concrete class behind a provider (tests override the provider).

## Offline (only when the PRD asks) — `references/offline.md`
Local cache, outbox, sync and conflicts.

## Auth
Tokens in secure storage (`fs-security-engineer`); refresh once on 401, then sign out cleanly; never log tokens.

Finish with a scratchpad: endpoints, models, error mapping, offline decisions.
