---
name: visualization-systems
description: >-
  Guides production-ready visualization generation in Pulse using product-owned
  renderer selection, structured specs, validation, shared renderer
  configuration, and deterministic renderers instead of prompt-authored
  HTML/SVG geometry. Use when planning, generating, debugging, or improving
  charts, diagrams, swimlanes, sequences, timelines, matrices, dashboards,
  graph layouts, Mermaid-style visuals, or visualization tooling.
metadata:
  author: nfraxlab
  version: "1.1"
---

# Visualization Systems

Pulse visualizations are product artifacts. The model may interpret the user's
goal and fill structured data, but Pulse owns renderer selection, validation,
layout, routing, theming, accessibility, export behavior, and repair.

The strength of Pulse visualizations is the consistent, polished, interactive
UI. Repairs, fallbacks, and simplified renderers must preserve that product
feel. Never downgrade a visualization into a plain checklist, unstyled table,
or monochrome technical dump just because the data is difficult.

## Core Contract

Do not make production geometry prompt-driven.

Use this pipeline:

```
user intent
  -> VisualizationPlan
  -> renderer-specific structured spec
  -> shared renderer config
  -> validation and repair
  -> deterministic Pulse renderer
```

The model can fill labels, values, actors, events, nodes, and relationships. It
must not compute coordinates, SVG paths, connector routes, chart geometry, font
sizes, colors, spacing, or layout dimensions for production renderers.

## First-Shot Reliability

Before creating a visualization, decide the renderer from the shape of the
content and the user's stated goal. Do not expose every chart type as an open
choice to the model.

Create a compact plan:

```json
{
  "renderer": "sequence",
  "schema": "SequenceSpec",
  "reason": "ordered handoffs between named actors",
  "config": {
    "orientation": "auto",
    "density": "comfortable",
    "maxItems": 18,
    "groupMode": "auto"
  }
}
```

Then fill only the selected schema. If a user asks for a specific format that
would be misleading or broken, preserve the user's analytical goal and let the
tool repair to the clearest truthful renderer.

## Shared Renderer Config

Every structured spec may include `config` or `rendererConfig`. Keep it generic
and let each renderer apply only the options that make sense.

```json
{
  "config": {
    "orientation": "auto",
    "density": "comfortable",
    "maxItems": 24,
    "showLegend": true,
    "showLabels": true,
    "interactive": true,
    "groupMode": "auto",
    "sort": "input",
    "height": 320,
    "columns": 0,
    "theme": "pulse",
    "accentMode": "auto"
  }
}
```

Supported values:

- `orientation`: `auto`, `horizontal`, `vertical`
- `density`: `compact`, `comfortable`, `spacious`
- `groupMode`: `auto`, `none`, `cluster`, `summarize`
- `sort`: `input`, `value_asc`, `value_desc`, `label_asc`, `label_desc`
- `theme`: `pulse`, `neutral`
- `accentMode`: `auto`, `categorical`, `sequential`, `status`

Use explicit config only when it reflects user intent or content shape. Prefer
`auto` for layout choices the renderer can decide better than the model.

## Visual System Requirements

Every renderer must use the Pulse visual language:

- Pulse design tokens for text, surface, borders, shadows, and accents.
- The shared six-accent palette for categories, phases, actors, and status.
- Dark-mode compatible colors.
- Rounded 8px-or-less cards, compact pills, subtle borders, and restrained
  shadows.
- Hover states, tooltips, legends, filtering, zoom, expand/collapse, or other
  meaningful interaction when the renderer supports it.
- Consistent typography and spacing across charts, diagrams, timelines,
  matrices, and dashboards.

Fallbacks must be beautiful too. A repaired sequence, summarized graph, or
clustered swimlane should still look like a first-class Pulse visualization.

## Renderer Selection

Use product-owned rules:

| Input shape | Renderer |
|-------------|----------|
| Numeric categories, time series, distributions | `ChartSpec` |
| Request/response, protocols, ordered handoffs | `SequenceSpec` |
| Ownership by stage with compact lanes/phases | `SwimlaneSpec` |
| Dependencies, topology, architecture networks | `GraphSpec` |
| Chronological events or milestones | `TimelineSpec` |
| Comparisons, tradeoffs, feature matrices | `MatrixSpec` or `TableSpec` |
| KPIs plus mixed cards/tables/charts | `DashboardSpec` |
| Low-risk explanatory composition | `FreeformHTML` only when deliberate |

## Renderer Rules

### Charts

Use `ChartSpec`; never hand-author chart SVG.

Renderer repairs:
- Pie/donut: at most 6 meaningful slices; otherwise bar or grouped Other.
- Many categories: horizontal bar by default.
- Time series: line or area.
- Part-to-whole with many categories: stacked bar or treemap.
- Correlation: scatter.
- Text-heavy data: matrix/table.

### Sequences

Use for messages, ordered handoffs, request/response flows, lifecycle traces,
and multi-system protocols. Group tiny implementation details into meaningful
messages. Keep actor count and message count bounded.

### Swimlanes

Use only when the purpose is ownership by stage and both lanes and stages are
explicit. Horizontal and vertical swimlanes are both valid:

- Horizontal: phases across columns, lanes down rows.
- Vertical: lanes across columns, phases down rows.
- `orientation: "auto"` lets Pulse choose based on density and aspect ratio.

If most cells would be empty, many placements are guessed, or connectors would
travel long distances, use sequence or graph instead.

### Graphs

Use for topology, dependency, architecture, and relationship networks. The model
provides nodes/edges/groups only. Pulse or a layout engine owns coordinates,
routing, clustering, and edge bundling.

### Timelines

Use for chronological events, releases, incidents, histories, and roadmaps.
Prefer concise event labels with optional details.

### Matrices

Use when comparison is the task. Keep columns scan-friendly and move long prose
into details/tooltips when possible.

### Dashboards

Use for KPI cards and mixed operational summaries. Dashboards should be dense,
scannable, and composed from smaller structured specs rather than freeform HTML.

## Validation And Repair

Every structured visualization must pass validation:

- Required fields present.
- IDs unique.
- References resolve.
- Labels fit renderer limits.
- Counts stay within renderer limits.
- Chart type matches data shape.
- Important nodes/events are not orphaned.
- Diagram density is appropriate for the chosen renderer.
- Config values are known and bounded.

Repair internally when possible:

```
bad pie -> bar
sparse swimlane -> sequence
dense swimlane cell -> clustered milestone
large graph -> clustered graph
too many messages -> summarized sequence
too many categories -> group as Other
wide table -> matrix/table with fewer columns
```

Do not expose retry loops to the user unless no truthful repair is possible.

## Production Quality Bar

A visualization is not production-ready if it has:

- clipped or overflowing text
- tiny or inconsistent type
- excessive empty space
- a plain checklist/list treatment for complex relationships
- missing actor/category/phase color or tags when those dimensions matter
- missing hover/tooltips/interactivity where details are available
- hardcoded visual styling outside Pulse tokens
- connector crossings in empty space
- diagonal spaghetti routes
- ambiguous reading order
- too many visible marks to scan
- hidden exception paths in decision flows
- chart type that misrepresents the data

Prefer fewer, clearer marks over exhaustive dumps.

## Implementation Guidance

Prefer renderer-specific schemas behind one configurable tool:

```
ChartSpec + config
SequenceSpec + config
SwimlaneSpec + config
GraphSpec + config
TimelineSpec + config
MatrixSpec + config
DashboardSpec + config
FreeformHTML only when deliberate
```

Raw HTML is acceptable for low-risk visual cards, but graph-like visuals,
charts, and production diagrams should use structured specs.

## References

For suggested schema shapes and limits, see:

`references/spec-patterns.md`
