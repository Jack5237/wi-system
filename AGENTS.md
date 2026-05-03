# WI-system Agent Contract

Use this repo as a living wiki maintenance engine.

Obsidian is the visual IDE for this wiki: the agent writes and maintains markdown, humans browse and inspect in Obsidian.

This system is intended as the contextual memory layer for agentic projects.

Raw internet material can be collected into sources/ (for example with Obsidian Web Clipper), then transformed into structured wiki context by the agent.

## Rules

- Never modify files inside `sources/`.
- Always update `index.md` after wiki page changes.
- Always append operation events to `log.md`.
- Keep wiki pages interlinked and structured.
- Prefer Obsidian wikilinks (`[[slug|Title]]`) when linking pages.
- Keep `index.md` content-oriented and grouped by category.
- Keep `log.md` chronological and append-only with parseable headings.
- Prefer markdown output that is easy for humans to read and edit.
- Preserve local-first operation: no cloud dependency is required.

## Required page sections

Every file in `wiki/` must include:

- YAML frontmatter with `title`, `slug`, `category`, `last_updated`, `tags`

- Summary
- Key claims
- Entities
- Sources
- Open questions

## Core operations

- Ingest: extract entities/claims/concepts, merge into existing pages, flag contradictions.
- Query: search wiki first, synthesize across pages, optionally persist synthesis page.
- Lint: detect contradictions, missing links, orphan pages, outdated claims; apply safe fixes when possible.

## Model routing

- Hosted model and local model backends are both valid.
- OpenAI-compatible local endpoints (for example Ollama/LM Studio style APIs) are supported through environment configuration.

## Logging format

Use:

- `## [ISO_UTC_TIMESTAMP] ingest | ...`
- `## [ISO_UTC_TIMESTAMP] query | ...`
- `## [ISO_UTC_TIMESTAMP] lint | ...`
