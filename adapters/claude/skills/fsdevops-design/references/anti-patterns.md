# Anti-patterns by product type

Pick the row for the product (the brief names it), copy the chosen lines into `DESIGN.md` under "Avoid", and add project-specific ones there. The critic checks screens against that list.

| Product type | Avoid |
|---|---|
| All | literal colours or sizes in screens; colour as the only signal; spinner where a skeleton keeps layout; hidden destructive actions with no confirm or undo; text in images |
| Productivity, personal tools, dashboards | dense walls of equal-weight cards; metrics with no comparison or unit; changing figure widths (use tabular figures); modal for every small edit; notifications for things the user did |
| Finance and money | rounding that hides cents; red and green as the only up and down signal; confirm text that does not repeat the amount; playful motion on balances |
| Health and wellbeing | alarming colour for neutral data; streak guilt; medical-sounding claims in copy; tiny targets for tired or older users |
| Content, feed, reading | line length past about 70 characters; infinite scroll with no position or end; autoplay motion; unlabelled icon-only actions on cards |
| Settings, admin, developer tools | toggles that apply nothing until a hidden Save; jargon labels; destructive and safe actions side by side in the same style |
| Onboarding and forms | more than one question per step on phone; errors shown only on submit; placeholder used as the label; blocking paste into fields |

Lines here are short on purpose: they are prompts for judgement, not a style database.
