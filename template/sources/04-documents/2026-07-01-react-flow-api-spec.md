---
type: document
resource: https://example.com/react-flow-api-docs
captured: 2026-07-01
ingested: true
---

Part of [[04-documents|Documents]].

# React Flow API Reference (excerpt)

Core props: `nodes`, `edges`, `onNodesChange`, `onEdgesChange`, `onConnect`. Node objects require `id`, `position: {x, y}`, and `data`; custom node types are registered via the `nodeTypes` prop as a map of type-name to component.

Layout is not built in — pairs well with `dagre` or `elkjs` for auto-layout on load. Background component supports `dots`, `lines`, and `cross` variants.
