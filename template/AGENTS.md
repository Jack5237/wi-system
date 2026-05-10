# LLM Wiki Schema

This document tells AI agents how to operate this wiki. Follow these rules strictly.

## Purpose

Build a structured, interlinked knowledge base from clipped web content. The AI maintains this wiki; you curate sources and ask questions.

## Folder Structure

**Raw Data Layer** (immutable)
- `sources/` — Clipped web articles (read-only, never edit)

**Structured Data Layer** (AI-maintained)
- `wiki/` — Knowledge pages, synthesized from sources

**System Files** (at vault root)
- `index.md` — Navigation and TOC
- `log.md` — Operation history (append-only)

## Core Workflow: Ingest

When you say "I clipped a new article, please ingest it":

1. **Read** the source file from `sources/`
2. **Extract** key concepts, entities, facts, relationships
3. **Create or update** wiki pages in `wiki/`:
   - Create a summary page for the source (if substantive)
   - Create/update concept pages (e.g., "Pasta", "Svelte")
   - Create/update entity pages (e.g., "Rome", "React Framework")
   - Create/update relationship pages if meaningful
4. **Quality Gate: No Stubs** — Only create a page if it has ≥3 substantive key points OR a meaningful relationship to existing pages. Single mentions don't warrant pages.
5. **Quality Gate: No Slop** — Summaries extract *insights*, not transcribe sources. Max 150 words per summary section. Every claim must reference the source.
6. **Add cross-references** — Link only when conceptually relevant. Not every mention needs a link. Ask: "Would this link help someone understand?"
7. **Update `index.md`** — add new pages to the index with one-line summaries
8. **Append to `log.md`** — record what was ingested and what changed

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

- **Sources are immutable** — Never edit files in `raw-data/sources/`. Read-only. Period.
- **Wiki is AI-owned** — You curate sources, I maintain wiki structure and quality
- **Log is append-only** — Every operation gets a record
- **All markdown** — No binary formats
- **Git-friendly** — Commit after each ingest/lint pass

## DO NOT

- **Do not edit source files** — `sources/` is read-only. Extract and synthesize, never modify.
- **Do not create stub pages** — Pages need substance (≥3 key points) or meaningful relationships.
- **Do not over-link** — Link only when it helps understanding. Not every mention is a link.
- **Do not transcribe sources** — Extract insights, synthesize knowledge. Paraphrase, don't copy.
- **Do not mix raw and structured** — Keep sources (raw data) separate from wiki (structured knowledge).
- **Do not cite without sourcing** — Every claim in wiki pages must trace back to a source.

---

## Examples

### Good Summary (Concise, Insightful)
```
## Summary
React Flow is a node-based editor library for React with built-in dragging, zooming, and multi-selection. MIT-licensed, 7.4M weekly installs, used by Stripe and Typeform for workflow builders and data visualization.
```

### Bad Summary (Rambling, Transcribes)
```
## Summary
This article is all about React Flow, which is a library for React. It talks about how you can use it to build things. It has features for dragging nodes around on a canvas. You can also zoom in and out. It supports selecting multiple nodes at once...
```

### Good Linking (Selective)
```
Related Pages:
- [[Node-Based UI]] (React Flow is an implementation of this pattern)
- [[xyflow]] (the company behind React Flow)
```

### Bad Linking (Over-linked)
```
Related Pages:
- [[React]] (mentioned in title)
- [[JavaScript]] (implied by React)
- [[Canvas]] (used by node editors)
- [[MIT License]] (the license)
- [[npm]] (how you install it)
```

### Good Page Decision
- ✅ Create a page for "React Flow" — has 5+ distinct concepts (library, use cases, features, ecosystem)
- ❌ Do NOT create a page for "MIT License" — single mention, not substantive enough

---

This is the contract between you and the AI. Modify it to fit your needs.
