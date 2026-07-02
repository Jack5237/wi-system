---
type: topic
updated: 2026-07-02
---

Part of [[topics|Topics]].

# React Flow

## Summary

React Flow is a node-based editor library for React with built-in dragging, zooming, and multi-selection. MIT-licensed, widely used for workflow builders and data visualization. Maintained by xyflow, which also ships a Svelte port.

## Key Points

- Minimal setup for a working node canvas; controlled/uncontrolled state modes
- Layout is not built in — pairs with `dagre` or `elkjs` for auto-layout
- Custom node types registered via the `nodeTypes` prop
- Positioned as a canvas primitive, not a full app builder — you bring your own UI chrome
- Recommended over Rete.js/jsPlumb unless the app needs to *execute* the node graph, not just edit it

## Notes

The "controlled vs uncontrolled" state pattern trips up most new users — most real apps end up controlled (state lives outside the component) once they need persistence or multi-user collaboration.

## Open Questions

- How does layout performance hold up past a few hundred nodes? Not covered in any source yet.

## Related

- [[xyflow]]
- [[dashboard-builder]]
- [[should-i-use-react-flow]]

## Sources

- [[2026-06-28-react-flow-review]]
- [[2026-06-30-xyflow-talk]]
- [[2026-06-29-chatgpt-flow-comparison]]
- [[2026-07-01-react-flow-api-spec]]
