---
description: Ingest all unprocessed files in sources/ into the wiki
---

Run the **Core Workflow: Ingest** from `AGENTS.md`.

1. Scan `sources/**` for files with `ingested: false` in frontmatter, or with no frontmatter at all.
2. For each one found, follow the ingest workflow in `AGENTS.md` step by step: classify, move into the correct typed subfolder, add frontmatter, search the wiki before creating pages, weave the source path into every touched page's `## Sources` section, flag contradictions instead of overwriting, mark `ingested: true`.
3. Update `wiki/index.md` if genuinely new topic/entity/project pages were created (curated, not auto-appended).
4. Append one line per ingested file to `log.md`.
5. Report a short summary: files ingested, pages created, pages updated.
6. Commit the result.

If no unprocessed files are found, say so and stop — don't touch anything.
