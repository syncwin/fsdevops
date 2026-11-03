# Domain map (one owner per domain)

| Domain | Owner |
|---|---|
| Stack and work-type routing | `fs-developer` |
| Write-less discipline, coding standards, i18n, accessibility rules | `fs-developer/references/*` |
| PRD, change brief, approval, project detection | `fs-developer-architect` |
| App structure, workspace, module registry, state, routing, theming, platforms | `fs-developer-flutter` |
| Safe changes to existing code, migrations, parity | `fs-developer-maintainer` |
| Widgets, adaptive layout, design tokens in code, feed/list UI | `fs-developer-ui` |
| API client, models, auth tokens, offline cache and outbox, sync | `fs-developer-api` |
| Secrets, secure storage, privacy, permissions, dependency licences | `fs-developer-security` |
| Frame budget, startup, memory, web bundle | `fs-developer-performance` |
| Mechanical gate, tests, scenarios, scope check | `fs-developer-qa` |
| Independent review | `fs-developer-reviewer` + agent `fs-developer-code-reviewer` |
| SDK setup, CI, flavors, signing setup | `fs-developer-devops` |
| Versioning, changelog, packaging, store and site delivery | `fs-developer-release` |

A skill that needs another domain's rule loads that owner; it never restates the rule.
