---
type: synthesis
updated: 2026-07-02
---

Part of [[syntheses|Syntheses]].

# Should I Use React Flow?

## Summary

Yes, if the goal is an editable node canvas (workflow builder, pipeline editor, diagramming tool) inside a React app — not if the app needs to actually *execute* the resulting graph as a runtime, where something like Rete.js fits better.

## Key Points

- React Flow is the fastest path to a polished, draggable, zoomable node canvas in React
- It's a canvas primitive: expect to bring your own styling, layout algorithm, and most UI chrome
- Stripe's internal usage (via [[xyflow]]) is the strongest evidence of production-scale viability
- If building something like [[dashboard-builder]], plan for an auto-layout library from the start rather than manual node positioning

## Notes

The comparison against Rete.js and jsPlumb (from a GPT conversation) consistently comes back to one axis: does the app need to *run* the graph, or just let a user *build* it visually. React Flow wins for the latter.

## Related

- [[react-flow]]
- [[xyflow]]
- [[dashboard-builder]]

## Sources

- [[2026-06-28-react-flow-review]]
- [[2026-06-29-chatgpt-flow-comparison]]
