---
type: project
updated: 2026-07-02
---

Part of [[projects|Projects]].

# Dashboard Builder

## Summary

Internal prototype: a visual data-pipeline builder using React Flow, with custom node types for data sources, transforms, and outputs, connected by labeled edges showing data type flow.

## Key Points

- Custom node types: "data source," "transform," "output" — registered via React Flow's `nodeTypes` prop
- Uses the dotted background variant with a minimap for navigation on larger graphs
- Not yet using an auto-layout library — nodes are currently positioned manually

## Notes

Next step is probably wiring in `dagre` for auto-layout once the pipeline graphs get complex enough that manual positioning becomes tedious — see the open question on [[react-flow]] about layout performance at scale.

## Open Questions

- Should transforms be executable in-browser, or just a visual spec that compiles to a backend pipeline? Unresolved.

## Related

- [[react-flow]]

## Sources

- [[2026-07-01-react-flow-dashboard-screenshot]]
- [[2026-07-01-react-flow-api-spec]]
