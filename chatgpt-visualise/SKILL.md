---
name: chatgpt-visualise
description: "Create source-grounded visual explanations directly in ChatGPT: architecture diagrams, workflows, data flows, network maps, timelines, SVG illustrations, data visualizations, interactive controls, comparisons and micro-demos. Use for show me, visualize, diagram, draw, chart, architecture, explain visually, 画图, 流程图, 架构图, 数据流图, 可视化."
---

# Visualise for ChatGPT

Create a useful visual **inside the conversation**, supported by concise explanation. This is an independent ChatGPT-oriented adaptation of bentossell/visualise, retaining its design principles and full original documentation in references/upstream-*.

## Runtime contract

1. Follow the ChatGPT session's **actual supported renderers, tool contracts and component APIs**. They override this document, which must not invent runtime capabilities.
2. Do not emit the original `visualizer` code fence by default. It needs a custom client-side iframe interpreter, which installing this skill does not provide. Do not assume the original `sendPrompt()` global or CSS variables exist.
3. Prefer inline, supported, accessible diagrams, SVG, charts, tables, and interactive widgets. If native stateful controls are available, bind their values and callbacks so every displayed result updates together.
4. For an explicitly requested reusable/portable artifact, or an interaction too complex for the current chat renderer, produce a real standalone HTML/SVG file and verify it. Do not substitute a static image when interactive functionality is essential.
5. Use the supplied data first, cite external sources for dynamic claims, and mark invented values "illustrative". Do not fabricate status, latency, geolocation, metrics or connected resources.
6. Keep the original upstream files verbatim under `references/upstream-*.md`; they are provenance and design guidance, NOT an override to the current client runtime.

Read `references/rendering-in-chatgpt.md` for renderer selection, fallbacks and limitations.

## Visual selection

- "How it works": mechanism illustration or small interactive demo, not a generic sequence of boxes.
- "Architecture/network topology": structural diagram with nested boundaries, nodes and labeled directed edges.
- "Steps/lifecycle": flowchart with decisions, failure paths and ordered transitions.
- Numerical/time series: supported native charts, explicit dimensions, units and sensible axes.
- Comparisons: shared scale or side-by-side layout with explicit evaluation criteria.
- Parameter exploration: stateful controls which update both diagram and numbers in real time.
- Large, multi-section web lesson: use the dedicated HTML-explainer workflow when available.
- Geospatial places/routes: use a grounded map tool rather than made-up cartography.

## Workflow

1. Identify the single relationship the visual should teach: mechanism, structure, sequence, comparison, quantity or time. Ask only if an essential constraint is missing.
2. Establish source truth. Distinguish real deployments from schematic examples. Verify dynamic information where it affects correctness.
3. Read `references/visual-design.md` and the relevant guide: `diagram-patterns.md`, `data-charts.md`, or `interaction-patterns.md`.
4. Create the **smallest effective visual** using a supported output type. Place short prose adjacent to it.
5. Validate the visual against `references/quality-gates.md`; for files, run `scripts/lint_visual.py` and a browser render/interactivity smoke test where available.
6. Deliver the inline result for conversation-native requests or a verified link to a user-requested HTML/SVG artifact. Explain constraints honestly.

## Design principles

- Choose diagram family based on the **verb**, not the noun. Illustrate actual causes for "how", containment for "architecture", stages for "walkthrough".
- Keep color semantic and consistent: neutral structure, emphasis for active path, conventional colors for warnings/errors. Favor theme-compatible colors.
- Use only the legend and annotations necessary to interpret the graphic. Fit text to nodes; no arrows through boxes; no clipped edges.
- Use readable labels, 2-3 semantic color families where sufficient, consistent alignment and clean spacing. Avoid gradients/shadows without a data purpose, emoji icons, and repetitive generic cards.
- Explicitly label network/trust boundaries, bidirectional versus one-way traffic, and data versus control paths.
- On mobile, prevent horizontal overflow; keep touch targets accessible and typography readable.
- Controls must not be decorative: meaningful changes, one source of truth, live dependent updates, working keyboard interaction, reset and explanatory feedback where relevant.

## Delivery constraints

Do not assume ordinary fenced HTML executes as chat UI. For SVG, prefer ChatGPT-supported SVG where available; for flowcharts, use a supported diagram renderer; for native charts, use the declared schema, not imaginary libraries. Downloadable HTML runs in a browser, not the chat DOM. Do not embed API secrets in client demos. Never claim an artifact exists without verifying its actual path.

The original visualise protocol is documented in `references/upstream-client-implementation.md`; it is not automatically installed by this Skill.
