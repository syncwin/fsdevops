# Domain map (one owner per domain)

| Domain | Owner |
|---|---|
| Stack and work-type routing | `fsdevops` |
| Write-less discipline, coding standards, i18n, accessibility rules | `fsdevops/references/*` |
| PRD, change brief, approval, project detection | `fsdevops-architect` |
| App structure, workspace, module registry, state, routing, theming, platforms | `fsdevops-flutter` |
| Safe changes to existing code, migrations, parity | `fsdevops-maintainer` |
| Widgets, adaptive layout, design tokens in code, feed/list UI | `fsdevops-ui` |
| API client, models, auth tokens, offline cache and outbox, sync | `fsdevops-api` |
| Secrets, secure storage, privacy, permissions, dependency licences | `fsdevops-security` |
| Frame budget, startup, memory, web bundle | `fsdevops-performance` |
| Mechanical gate, tests, scenarios, scope check | `fsdevops-qa` |
| Independent review | `fsdevops-reviewer` + agent `fsdevops-code-reviewer` |
| SDK setup, CI, flavors, signing setup | `fsdevops-ci` |
| Versioning, changelog, packaging, store and site delivery | `fsdevops-release` |

A skill that needs another domain's rule loads that owner; it never restates the rule.
