# PRD: <app or feature>

## Goal
One paragraph: who uses it, what job it does, what "done" looks like.

## Scope
| In | Out (and when it may come) |
|---|---|

## Targets and order
1. Windows desktop  2. Android  3. iOS  4. Web (edit as agreed)

## Architecture
- Repo: pub workspace (`apps/<app>`, `packages/<prefix>_core`, `packages/<prefix>_ui`, `packages/<prefix>_<module>`), or single package for small apps.
- State: Riverpod 3. Routing: go_router. Models: freezed + json_serializable (or plain classes if under three models). Local data: drift (only if offline is in scope).
- Module registry: yes/no; modules and their on/off source.
- Ownership: builder-owned paths, generated paths.

## Screens and flows
| Screen | Purpose | Data | Actions |
|---|---|---|---|

## Data and API
Endpoints or mock repositories, auth, offline behaviour.

## Non-functional
Accessibility (`accessibility.md`), i18n locales, performance budget, security notes.

## Threat model
Assets (data, keys, accounts) · entry points (inputs, deep links, network, files) · top 3 abuse cases with the control for each. Rules: `fsdevops-security`.

## Domains touched
UI / API / security / performance / devops / release.

## Done when
- [ ] Gate green on the first target (format, analyze, test, build)
- [ ] Scenarios pass: ...
- [ ] Reviewer: no Critical or Important findings

## Open questions
