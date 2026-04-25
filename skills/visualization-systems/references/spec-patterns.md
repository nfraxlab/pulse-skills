# Visualization Spec Patterns

These schemas are generic starting points. Pulse should version, validate, and
repair them before rendering.

## Shared Config

All structured specs may include `config` or `rendererConfig`.

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

Use `auto` or omit fields unless the user intent or data shape requires a
specific setting.

Visual defaults:
- `theme` defaults to `pulse`.
- `interactive` defaults to `true`.
- `accentMode` defaults to `auto`.
- Renderers should preserve hover states, tooltips, legends, accent colors, and
  dark-mode compatibility unless the user explicitly asks for static output.

## VisualizationPlan

```json
{
  "schemaVersion": "1.0",
  "renderer": "sequence",
  "schema": "SequenceSpec",
  "reason": "ordered handoffs between named actors",
  "config": {
    "orientation": "auto",
    "density": "comfortable",
    "maxItems": 18,
    "theme": "pulse",
    "interactive": true
  }
}
```

## ChartSpec

```json
{
  "schemaVersion": "1.0",
  "kind": "chart",
  "chartType": "auto",
  "title": "Metric by Category",
  "config": {
    "orientation": "auto",
    "sort": "value_desc",
    "height": 320,
    "showLegend": true,
    "showLabels": true,
    "theme": "pulse",
    "interactive": true,
    "accentMode": "categorical"
  },
  "data": [
    {"label": "Category A", "value": 42},
    {"label": "Category B", "value": 18}
  ],
  "encoding": {
    "x": "value",
    "y": "label",
    "color": "series"
  }
}
```

Limits:
- Pie/donut: max 6 visible slices.
- Bar: max 12 visible categories before grouping.
- Line: max 6 visible series.
- Prefer table/matrix when values are mostly text.

## SequenceSpec

```json
{
  "schemaVersion": "1.0",
  "kind": "sequence",
  "title": "System Handoff Flow",
  "config": {
    "density": "comfortable",
    "maxItems": 18,
    "showLegend": true,
    "theme": "pulse",
    "interactive": true,
    "accentMode": "categorical"
  },
  "actors": [
    {"id": "client", "label": "Client"},
    {"id": "app", "label": "Application"},
    {"id": "service", "label": "Service"},
    {"id": "external", "label": "External"}
  ],
  "messages": [
    {
      "from": "client",
      "to": "app",
      "label": "Start request",
      "phase": "Initiation"
    },
    {
      "from": "app",
      "to": "service",
      "label": "Submit payload",
      "phase": "Processing"
    }
  ],
  "branches": [
    {
      "after": "Submit payload",
      "condition": "Requires review",
      "to": "Review path"
    }
  ]
}
```

Limits:
- Max 7 actors.
- Max 18 visible messages by default.
- Group low-level calls into meaningful handoffs.

## SwimlaneSpec

```json
{
  "schemaVersion": "1.0",
  "kind": "swimlane",
  "title": "Ownership By Stage",
  "config": {
    "orientation": "auto",
    "density": "comfortable",
    "groupMode": "auto",
    "maxItems": 20,
    "theme": "pulse",
    "interactive": true,
    "accentMode": "categorical"
  },
  "lanes": [
    {"id": "requester", "label": "Requester"},
    {"id": "reviewer", "label": "Reviewer"},
    {"id": "system", "label": "System"}
  ],
  "phases": [
    {"id": "submit", "label": "Submit"},
    {"id": "review", "label": "Review"},
    {"id": "complete", "label": "Complete"}
  ],
  "nodes": [
    {
      "id": "submit-request",
      "lane": "requester",
      "phase": "submit",
      "label": "Submit request",
      "type": "ui"
    }
  ],
  "edges": [
    {"from": "submit-request", "to": "review-request", "type": "primary"}
  ]
}
```

Limits:
- Max 5 lanes by default.
- Max 6 phases by default.
- Max 20 visible nodes by default.
- Use `groupMode: "auto"` for dense cells.
- Use explicit `orientation` only when the user requests it.

## GraphSpec

```json
{
  "schemaVersion": "1.0",
  "kind": "graph",
  "title": "Relationship Graph",
  "layout": "auto",
  "config": {
    "orientation": "auto",
    "groupMode": "cluster",
    "maxItems": 35,
    "showLabels": true,
    "theme": "pulse",
    "interactive": true,
    "accentMode": "categorical"
  },
  "nodes": [
    {"id": "a", "label": "Node A", "group": "Group 1"},
    {"id": "b", "label": "Node B", "group": "Group 2"}
  ],
  "edges": [
    {"from": "a", "to": "b", "label": "depends on"}
  ]
}
```

Limits:
- Max 35 visible nodes before clustering.
- Layout and routing are renderer-owned.
- No model-authored coordinates.

## TimelineSpec

```json
{
  "schemaVersion": "1.0",
  "kind": "timeline",
  "title": "Project Timeline",
  "config": {
    "orientation": "vertical",
    "density": "comfortable",
    "maxItems": 16,
    "theme": "pulse",
    "interactive": true,
    "accentMode": "sequential"
  },
  "events": [
    {
      "time": "Q1",
      "label": "Discovery",
      "detail": "Collect requirements and constraints"
    }
  ]
}
```

## MatrixSpec

```json
{
  "schemaVersion": "1.0",
  "kind": "matrix",
  "title": "Option Comparison",
  "config": {
    "density": "compact",
    "columns": 4,
    "maxItems": 12,
    "theme": "pulse",
    "interactive": true
  },
  "columns": [
    {"id": "option", "label": "Option"},
    {"id": "fit", "label": "Fit"},
    {"id": "risk", "label": "Risk"}
  ],
  "rows": [
    {"Option": "A", "Fit": "High", "Risk": "Low"}
  ]
}
```

## DashboardSpec

```json
{
  "schemaVersion": "1.0",
  "kind": "dashboard",
  "title": "Operational Summary",
  "config": {
    "density": "comfortable",
    "columns": 0,
    "maxItems": 8,
    "theme": "pulse",
    "interactive": true,
    "accentMode": "status"
  },
  "cards": [
    {"label": "Availability", "value": "99.95%", "trend": "up"},
    {"label": "Latency p95", "value": "180 ms", "trend": "down"}
  ],
  "sections": [
    {
      "title": "Top Items",
      "type": "table",
      "rows": []
    }
  ]
}
```

Limits:
- Max 8 KPI cards by default.
- Max 3 mixed sections by default.
- Compose dashboards from structured sub-renderers where possible.
