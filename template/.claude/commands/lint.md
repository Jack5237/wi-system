---
description: Run the wiki maintenance/lint checklist
---

Run the **Core Workflow: Lint** from `AGENTS.md`.

Check for and report:
1. Un-ingested files in `sources/` (`ingested: false` or missing frontmatter).
2. Contradictions between pages (cross-check `## Open Questions` sections first).
3. Orphan pages — no inbound links.
4. Duplicate pages covering the same subject.
5. Dead `## Sources` entries pointing at renamed/moved files.
6. Concepts mentioned repeatedly but lacking their own page.
7. A stale `wiki/index.md`.

Report findings as a list, then offer to fix them. Only make changes the user confirms, except for ingesting already-flagged unprocessed sources (run `/ingest` for those instead of duplicating the workflow here). Commit after any fixes are applied.
