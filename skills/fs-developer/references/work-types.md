# Work types

| Type | Starts with | Changes | Brief |
|---|---|---|---|
| New app | Empty folder | Whole repo (workspace, shell, packages, CI) | PRD (`fs-developer-architect/references/prd-template.md`) |
| New feature | Existing app | One new module package or feature folder, plus its registration | PRD (short) |
| Update | Existing code | Only the files the brief names; parity list for behaviour kept | Change brief (`fs-developer-architect/references/change-brief-template.md`) |
| Review only | Existing code | Nothing; a report | Lens and scope |
| DevOps | Repo | CI, toolchain, flavors, signing config | Change brief |
| Release | Green build | Version, changelog, artifacts | Release checklist |

Mixed request (for example "fix this bug and add dark mode"): split it into an Update and a New feature, one approval covering both.
