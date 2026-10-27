# Interaction patterns

- Parameter slider: input -> calculation -> visualization and output label, using one state.
- Stepper: previous/next modifies an index, labels and drawing in lockstep.
- Comparison selector: toggles same chart scale and selected details.
- Clickable node: opens detail or sends a follow-up only through documented host actions.

Every control should do something immediately understandable. Present a meaningful initial state, reset when useful, keyboard accessibility, and text feedback in addition to color. Do not rely on a `sendPrompt()` global that only exists in upstream's custom renderer.

For a native chat widget, use official state/hooks and callbacks defined for that conversation. For an HTML artifact, use browser events and verify behavior through a browser.
