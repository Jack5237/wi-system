# WI-System Development

## Project

A schema-driven **LLM Wiki template** — a local-first knowledge base system that works with any AI agent (Claude Code, Cursor, etc.).

Users copy the `template/` folder, open in Claude Code, clip web content to `sources/`, and the AI reads `AGENTS.md` to understand how to build and maintain a structured, interlinked wiki in `wiki/`.

## Architecture Overview

**Three layers:**
1. **Sources** — Immutable clipped web content (markdown files)
2. **Wiki** — AI-maintained structured markdown pages (created/updated by AI)
3. **AGENTS.md** — Rules telling the AI how to operate

**Key insight:** The wiki is persistent and compounding (not one-time RAG). Each new source makes it smarter.

## For Contributors

This is **a minimal template and documentation project**.

### Main Files

- `README.md` — What this is, features, quick start (end-user focused)
- `GETTING_STARTED.md` — 5-minute setup guide
- `TUTORIAL.md` — Full walkthrough with pasta + Svelte example
- `CLAUDE.md` — This file, for developers
- `template/` — Starter vault (users copy this)
  - `template/AGENTS.md` — Rules for how the AI operates
  - `template/index.md` — Wiki navigation
  - `template/log.md` — Operation log
  - `template/sources/` — Where users clip content
  - `template/wiki/` — Where AI maintains pages

### Key Points

1. **Minimal and focused** — Only essential files, no bloat
2. **End-user first** — Everything designed for users copying the template
3. **AI reads AGENTS.md** — That's the contract between the system and AI
4. **Test with real wikis** — Copy `template/`, verify in Claude Code + Obsidian
5. **Keep it simple** — Lightweight, understandable, maintainable

### Workflow for Changes

1. Edit `template/AGENTS.md` if you're changing how the AI operates
2. Update docs if you're explaining something better
3. Update `template/` structure if needed
4. Test by copying `template/` and using it end-to-end
5. Commit with clear messages

### Git Conventions

- `refactor:` — Major structural changes
- `docs:` — Documentation updates
- `fix:` — Bug fixes
- Keep messages clear and focused
