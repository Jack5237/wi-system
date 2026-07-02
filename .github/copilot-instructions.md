# GitHub Copilot Instructions

GitHub Copilot should read and follow the rules in `template/AGENTS.md` when working with WI System vaults.

## Primary Reference

- **`template/AGENTS.md`** — The canonical rules for how the AI should operate on WI System vaults

## Key Rules

When users copy the `template/` folder and use it as a WI System vault:

1. Read `AGENTS.md` in the vault root first
2. Follow the ingest, synthesis, and lint workflows exactly as specified
3. Maintain source immutability and wiki organization
4. Update existing wiki pages before creating new ones
5. Always link sources back to wiki pages via `## Sources` sections
6. Commit after each ingest and lint operation

## Context

The WI System is a woven intelligence architecture where:
- `sources/` → raw data dump (articles, videos, conversations, documents, images, audio)
- `wiki/` → AI-maintained knowledge organized by subject (topics, entities, projects, syntheses)
- Slash commands (`/ingest`, `/synthesize`, `/lint`) drive the workflows

See `template/AGENTS.md` for complete operational rules.
