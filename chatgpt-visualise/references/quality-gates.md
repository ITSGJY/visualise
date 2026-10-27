# Visual acceptance checklist

- Semantic and factual accuracy: supported data, units, captions and arrows all agree.
- Geometry: no clipped text, overlapping labels, arrow-through-node, flattened circle or offscreen content.
- Responsive: desktop and mobile tested where practical; no horizontal overflow or fixed bars covering text.
- Visual grammar: compact, flat, meaningful semantic colors, readable contrast and label sizes.
- Interactions: initial render nonblank; every control works; all dependent values/graphics update; resets work; no JS errors.
- Accessibility: keyboard focus, semantic labels, color-independent feedback.
- Artifacts: link only to paths verified to exist; no false claims about deployment or interactive behavior.
- Review critical defects, repair and re-render before shipping.

When a check is not possible in the current environment, say it was not performed rather than claiming success.
