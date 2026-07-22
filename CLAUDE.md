# WI System — Project Development

## What This Is

**WI System** is a schema-driven knowledge-base template. Users copy `template/`, open it in Obsidian alongside Claude Code or any AI agent, clip content into `sources/`, and the AI maintains a structured, interlinked wiki in `wiki/` following rules in `template/AGENTS.md`.

Three-layer architecture: immutable sources (organized by *type*), AI-maintained wiki (organized by *subject*), and an append-only log connecting both. Persistent, compounding RAG — each source makes the wiki smarter.

## Project Structure

- **Docs** (`README.md`, `GETTING_STARTED.md`, `TUTORIAL.md`, `CONTRIBUTING.md`) — User-facing
- **`template/`** — What users copy; only essential files, no bloat
  - `template/AGENTS.md` — Rules end-users' AI agents follow to operate their wiki
  - `template/sources/`, `template/wiki/`, `template/log.md`, `.obsidian/graph.json`
- **`AGENTS.md`** (root) — Rules for contributors modifying the WI System itself
- **`CLAUDE.md`** (this file) — Dev workflow and architecture

## Development Workflow

**To modify core system rules:** Edit `template/AGENTS.md`.

**To change project docs:** Edit `.md` files in root.

**To modify `template/` structure:** Update folder hierarchy or `.obsidian/graph.json` — then test end-to-end by copying `template/` to a scratch dir, opening in Claude Code + Obsidian, running a full ingest → synthesize → lint cycle.

**Testing:** No unit tests needed. Verify changes by copying the modified `template/`, seeding it with sample sources, and running actual workflows. The system's contract lives in `template/AGENTS.md` — breaking changes there break every user's wiki.

## Rules for Changes

1. Keep `template/` minimal — only files end-users absolutely need
2. Maintain the three-layer architecture (sources/wiki/log)
3. Never change file naming conventions or frontmatter schema without updating `template/AGENTS.md` *and* all examples
4. Hub-link pattern is mandatory — every source and wiki page must link to its folder hub
5. Log entries must use real wikilinks, never prose descriptions
6. All changes require `template/AGENTS.md` review — if the rule changed or an AI agent's job changed, update that doc

See `AGENTS.md` (root) for contributor workflow details.

## Git Conventions

- `refactor:` — Structural changes to template or docs
- `docs:` — Documentation updates, no code
- `fix:` — Bug fixes, schema corrections
- `feat:` — New capabilities or optional layers (rare)

Keep messages focused. Example: `docs: clarify hub-link pattern in AGENTS.md`
