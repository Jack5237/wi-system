# LLM Wiki Schema

This document tells AI agents how to operate this wiki. Copy this to `.schema.md` in your vault.

## Purpose

Build a structured, interlinked knowledge base from clipped web content. The AI maintains this wiki; you curate sources and ask questions.

## Folder Structure

- `sources/` — Raw clipped articles (immutable, read-only)
- `wiki/` — AI-maintained pages (created/updated by AI)
- `index.md` — Navigation and TOC (AI-maintained)
- `log.md` — Operation history, append-only (AI-maintained)

## Core Workflow: Ingest

When you say "I clipped a new article, please ingest it":

1. **Read** the source file from `sources/`
2. **Extract** key concepts, entities, facts, relationships
3. **Create or update** wiki pages in `wiki/`:
   - Create a summary page for the source
   - Create/update concept pages (e.g., "Pasta", "Svelte")
   - Create/update entity pages (e.g., "Rome", "React Framework")
   - Create/update relationship pages if needed
4. **Add cross-references** — link related pages together
5. **Update `index.md`** — add new pages to the index with one-line summaries
6. **Append to `log.md`** — record what was ingested and what changed

## Core Workflow: Query

When you ask a question:

1. **Read `index.md`** to understand what's in the wiki
2. **Search relevant pages** based on your question
3. **Synthesize** an answer using wiki content
4. **Cite sources** — link to the wiki pages you used
5. **Optionally create a new page** if the answer is valuable for future reference

## Core Workflow: Lint

When you say "please lint the wiki":

1. **Check for contradictions** — do any pages claim conflicting facts?
2. **Find orphans** — pages with no inbound links
3. **Find unlinked concepts** — mentioned but lacking their own page
4. **Check source citations** — are all claims tied to a source?
5. **Report findings** and offer fixes

## Page Format

All wiki pages use this structure:

```markdown
---
source: source-file.md
date: 2026-05-09
tags: [tag1, tag2]
---

# Page Title

## Summary
One-paragraph overview.

## Key Points
- Bullet point 1
- Bullet point 2

## Related Pages
- [[Other Page]]
- [[Concept]]

## Sources
- Source file: `sources/source-file.md`
```

## Linking Rules

- Link to related concepts: `[[Concept Name]]`
- Link to sources: reference the original filename
- Create a page for any concept you mention more than once
- Update backlinks when creating new pages

## Rules for This Vault

- **Sources are immutable** — Never edit files in `sources/`
- **Wiki is AI-owned** — You maintain it, I write it
- **Log is append-only** — Every operation gets a record
- **All markdown** — No binary formats
- **Git-friendly** — Commit after each ingest/lint pass

---

This is the contract between you and the AI. Modify it to fit your needs.
