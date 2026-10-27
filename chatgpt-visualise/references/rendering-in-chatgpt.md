# Rendering in ChatGPT

The current client contract is authoritative. Do not assume undocumented capabilities.

## Decision tree

1. User wants a narrative visual in the chat:
   - Use a supported diagram format (e.g., Mermaid for flowcharts, an SVG component if supported, or chart widget for quantitative data).
   - Use DIL inputs/state/callbacks if available for live interaction. Keep hooks at the top level.
   - Do not emit an unsupported `visualizer` code fence.
2. User wants a shareable interactive standalone:
   - Create a real self-contained .html with inline CSS/JS, verify path, screenshot desktop/mobile if browser tools exist.
3. User wants a static image:
   - Produce an image only when requested; do not confuse screenshots with working interactions.
4. Client renderer limited:
   - Deliver the simplest supported native diagram or an HTML file. Explain what couldn't run inline.

## Original bridge vs ChatGPT

Upstream: model emits raw fragments in a `visualizer` code fence; a custom client intercepts it, injects CSS, runs JS inside a sandboxed iframe and defines `sendPrompt()`.

ChatGPT: native chart, diagram and stateful component contracts vary by chat surface; action callbacks are explicitly declared. There is no automatic assumption that arbitrary HTML executes.

## Rules

- All visible controls must be wired to actual state.
- No fabricated control callbacks or host actions.
- Renderer-specific colors/styles should be translated to the supported theme mechanism.
- Scripts in a standalone HTML artifact are distinct from in-chat code blocks.
- Use native platform maps for geospatial pins/routes, and preserve exact source facts and citations.
