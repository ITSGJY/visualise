# Diagrams and visual mechanisms

## Route by intent

- Flowchart: ordered states, branches, failures, retries and lifecycle.
- Structural: containment, networks, nested trust boundaries and components.
- Illustrative: depict actual mechanical or causal processes instead of abstract box sequences.
- Data flow: distinguish request paths, replies, async queues, and external services.

## Geometry

- Choose one principal direction for flows.
- Layout nodes to fit the available horizontal space, especially mobile.
- Arrows must not cross labels or boxes.
- Include arrowheads and direction for directed flows; show distinct paths for bidirectional edges when important.
- Diagram insets: maintain sufficient SVG viewBox padding.
- An architecture diagram must not invent a real deployment component.
- Break large systems into overview and focused subflows.

## Checks

Verify that every edge is justified and endpoints are correctly typed. Label illustrative topologies. Keep legend symbols consistent and captions factual.
