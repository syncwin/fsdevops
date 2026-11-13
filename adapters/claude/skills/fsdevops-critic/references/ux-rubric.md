# UX rubric (Flutter)

Judge against the brief's intent and audience, not taste. Each finding: observation, evidence, why (heuristic, WCAG id, law), fix, severity.

## Heuristics (Nielsen, ten)
Visibility of system status; match to the real world; user control and undo; consistency and standards; error prevention; recognition over recall; flexibility and efficiency; minimalist design; error recovery in plain language; help and documentation.

## Visual design
Hierarchy (one focal point per screen), type scale, spacing on a step scale, alignment to a grid, colour by role, density suited to the device, component consistency. Generic-template check: would the screen look identical with another product's name on it?

## Accessibility (WCAG 2.2 AA, as applied to Flutter)
Contrast 4.5:1 text, 3:1 large text and UI parts; target at least 24 CSS px by WCAG and 48 dp by house rule; visible focus not hidden by other UI (2.4.11); no drag-only action (2.5.7); consistent help (3.2.6); no repeated entry (3.3.7); accessible authentication (3.3.8); reflow and 200% text; reduced motion; colour never the only signal.

## Platform conventions
Material 3 roles, state layers and size classes (compact <600, medium <840, expanded >=840); Cupertino adaptations only when iOS is in scope; desktop expects hover, shortcuts, right-click and visible scroll bars.

## Performance as UX
Feedback within about 400 ms (Doherty); no visible jank in the screens under review; skeletons keep layout stable.

## Laws of UX (explain, never generate)
Hick (fewer choices), Fitts (bigger, closer targets), Jakob (familiar patterns), Miller (chunk), proximity and common region, Von Restorff (one standout), Postel, Peak-End, Goal-gradient, Aesthetic-usability.

## Severity map (NN/g 0-4 to house labels)
4 catastrophic = Critical; 3 major = Important; 2 minor and 1 cosmetic = Minor; 0 = not a problem. Weigh frequency, impact and persistence.

## Result vocabulary
PASS, FAIL, NOT RUN, NEEDS MANUAL EVIDENCE. Nothing is PASS without evidence.
