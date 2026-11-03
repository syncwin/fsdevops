# Domain map (one owner per domain)

| Domain | Owner |
|---|---|
| Stack and work-type routing | `fs-developer` |
| Write-less discipline, coding standards, i18n, accessibility rules | `fs-developer/references/*` |
| PRD, change brief, approval, project detection | `fs-architect` |
| App structure, workspace, module registry, state, routing, theming, platforms | `fs-flutter-developer` |
| Safe changes to existing code, migrations, parity | `fs-maintainer` |
| Widgets, adaptive layout, design tokens in code, feed/list UI | `fs-ui-developer` |
| API client, models, auth tokens, offline cache and outbox, sync | `fs-api-developer` |
| Secrets, secure storage, privacy, permissions, dependency licences | `fs-security-engineer` |
| Frame budget, startup, memory, web bundle | `fs-performance-engineer` |
| Mechanical gate, tests, scenarios, scope check | `fs-qa-engineer` |
| Independent review | `fs-reviewer` + agent `fs-code-reviewer` |
| SDK setup, CI, flavors, signing setup | `fs-devops-engineer` |
| Versioning, changelog, packaging, store and site delivery | `fs-release-manager` |

A skill that needs another domain's rule loads that owner; it never restates the rule.
