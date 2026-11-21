# Design direction (plan before code)

Write the direction before the first widget. The brief and the project's `DESIGN.md` win; this plan fills only what they leave open. Brand colours or fonts given by the owner are never replaced.

## The plan (one short block in the scratchpad or `DESIGN.md`)
| Item | Decide | Flutter home |
|---|---|---|
| Purpose and tone | who uses it, in what mood, one adjective pair (for example calm and exact) | brief |
| Colours | 4 to 6 roles: one primary, one accent at most, neutrals for surface and text, error; each with a reason | `ColorScheme` (seed or explicit roles), both schemes |
| Typefaces | at most two families, each with a role (display or headings, body and UI); a mono only for code or figures | `TextTheme` roles, bundled font assets |
| Layout idea | one sentence: the grid, density and the one focal point per main screen | size classes in `SKILL.md` |
| Signature detail | one memorable choice (shape, rhythm, motion or illustration), used with restraint | tokens, never one-off values |

## Pick the mode first
Most app screens are tools people operate daily: consistency and clarity beat expression there, so the signature stays small. Onboarding, empty states and marketing screens may carry more of it.

## Reject the defaults (check each, say why kept if kept)
- The template seed colour and an untouched `ColorScheme.fromSeed` with no reason.
- Gradient or glow accents added only to look modern; the common generated-app palettes (purple on white, warm cream with one rust accent, near-black with one neon accent).
- Decorative tells with no meaning: numbered markers where nothing is a sequence, one highlighted word per headline, all-caps labels above every title, arrows on every link.
- Ask of each choice: would it fit any other brief unchanged? If yes, revise it.
- One weight everywhere; headings that differ from body only by size.
- Every surface a card with the same radius and shadow; centred everything.
- Icons with no label for main actions; decoration that carries no meaning.

Keep a default when it is the right call (platform familiarity, accessibility); note the reason in one line.

## Limits
- Taste never beats the brief, contrast, or the 48 dp target rule (`fsdevops/references/accessibility.md`).
- One direction per product, recorded in `DESIGN.md`; new screens follow it instead of re-planning.
- No new font or package without the owner's yes (licence, size).
