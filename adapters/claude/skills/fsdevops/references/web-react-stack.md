# Web / desktop React + TypeScript stack (planning reference)

Used for plans and architecture briefs only. React work is not a supported build stack yet (`stacks.md`); Flutter behaviour is unchanged. Same choices as the WordPress admin app stack, minus WordPress specifics.

- **UI:** React + TypeScript, one SPA, internal routing inside it. Talk to the backend only through a versioned JSON API (`/api/v1/...`); never bump a version in place once anything depends on it.
- **Styling:** Tailwind utility classes in the markup. No BEM or custom class-naming system. Repeated utility groups become a component, not a CSS class.
- **Tokens:** one token file (JSON/JS) is the source of truth, compiled to CSS custom properties (light/dark, brand swaps) and the Tailwind config. No value defined twice.
- **Data and state:** TanStack Query for fetching and caching, Zustand for client state, `react-hook-form` + `zod` for forms and validation.
- **Tooling:** Bun for packages, bundling and dev server (frontend only).
- **Monorepo:** TurboRepo (or similar) only when several related products share packages (API client, UI, tokens). Development-level sharing: each product keeps its own backend, database and deployment.
- **Accessibility:** WCAG 2.2 AA, `axe-core` in CI on every build, plus a manual pass (keyboard, screen reader, contrast) before release; non-drag alternative for drag-and-drop. See `accessibility.md`.
- **Security:** least privilege, no secrets in code or logs, encryption at rest for stored credentials, dependency audit (`npm audit`) every build, a published disclosure channel (`security.txt`).
- **Licensing:** prefer MIT, Apache-2.0, BSD. Never AGPL. Avoid other GPL libraries unless the project itself is GPL.
- **Tests:** for logic where a silent bug is damaging (data, payments, destructive actions), write numbered test scenarios before building and treat them as a release gate.
