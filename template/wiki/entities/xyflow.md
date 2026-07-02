---
type: entity
updated: 2026-07-02
---

Part of [[entities|Entities]].

# xyflow

## Summary

xyflow is the small team that builds and maintains React Flow and its Svelte port, Svelte Flow. Positions its libraries as canvas primitives rather than full drag-and-drop app builders.

## Key Points

- Maintains both React Flow and Svelte Flow as separate packages rather than one framework-agnostic core
- Design philosophy: "the canvas primitive, not the product" — minimal opinions on styling and UI chrome
- Known large-scale deployment: Stripe uses it internally for workflow builders

## Notes

Deliberately kept React Flow and Svelte Flow as separate codebases instead of abstracting a shared core — a tradeoff for framework-idiomatic APIs over shared maintenance burden.

## Related

- [[react-flow]]

## Sources

- [[2026-06-28-react-flow-review]]
- [[2026-06-30-xyflow-talk]]
- [[2026-07-01-react-flow-podcast-notes]]
