# Data visualization

Prefer a native chart component with the current schema. Pick type based on the question:
- Magnitude across categories -> bar
- Value over time -> line
- Quantities summing to a whole -> carefully labeled share chart
- Two numeric variables -> scatter
- Comparison across the same scale -> aligned dots/bars

Always label unit, source and time range. Use correct axes (zero baseline for bar). Avoid distortion, fabricated datasets, misleading interpolation or false precision. Keep numerical and visual values consistent. Data with missing values must visibly stay missing.

For interactive quantitative charts use one state source and derive every plot mark and number from that state. For downloadable HTML, ordinary JavaScript and charting libraries may be used if the browser can load them; avoid runtime dependencies where offline portability matters.
