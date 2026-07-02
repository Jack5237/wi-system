---
type: conversation
brain: gpt
captured: 2026-06-29
ingested: true
---

Part of [[03-conversations|Conversations]].

# ChatGPT: React Flow vs Alternatives

Asked GPT to compare React Flow against Rete.js and jsPlumb for a workflow-builder use case.

GPT's take: Rete.js has a steeper learning curve but more flexibility for custom execution engines; jsPlumb is framework-agnostic but feels dated and harder to style. For a React app needing a polished canvas quickly, React Flow was recommended as the default choice, with Rete.js only if the app needs to actually *execute* the node graph (not just edit it).
