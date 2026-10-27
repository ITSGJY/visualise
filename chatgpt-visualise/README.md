# Visualise for ChatGPT

An independent [Visualise](https://github.com/bentossell/visualise) derivative tailored for ChatGPT's native visual and interaction components.

Use this skill for diagrams, network topologies, workflows, comparative charts, illustrated mechanisms, interactive sliders, and data-driven explainers in ChatGPT conversations.

## Install

Package this directory alone as a ChatGPT Skill ZIP and upload it through Skills settings. Skill name: `chatgpt-visualise` (separate from `visualise`).

## Differences from upstream

The upstream relies on a special ```visualizer``` fence, injected theme CSS, a sandboxed iframe and an optional `sendPrompt` bridge. ChatGPT does not promise that custom protocol, so this adaptation routes to actually available UI/rendering tools first and emits verified HTML/SVG artifacts where appropriate.

## Examples

- "@Visualise for ChatGPT Map client -> CDN -> API -> database and distinguish trust boundaries."
- "@Visualise for ChatGPT Show JVM garbage collection visually."
- "@Visualise for ChatGPT Create an interactive cache hit-rate explanation with sliders."
- "@Visualise for ChatGPT Plot these quarterly values on a consistent scale."

## Project contents

`SKILL.md`: runtime policy and workflow.
`references/`: visual standards, diagram/chart/interaction rules, quality gates, and exact upstream documents.
`scripts/`: static visual lint.
`assets/`: small HTML and SVG sample assets.

## Origin and license

Based on bentossell/visualise (MIT). Unmodified upstream source documents remain in `references/upstream-*.md`. This fork's ChatGPT extension is unofficial.
