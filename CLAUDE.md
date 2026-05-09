# WI-System Development

## Project

A schema-driven **LLM Wiki template** — a local-first knowledge base system that works with any AI agent (Claude Code, Cursor, etc.).

Users copy the `template/` folder, open in Claude Code, clip web content to `sources/`, and the AI reads `.schema.md` to understand how to build and maintain a structured, interlinked wiki in `wiki/`.

## Architecture Overview

**Three layers:**
1. **Sources** — Immutable clipped web content (markdown files)
2. **Wiki** — AI-maintained structured markdown pages (created/updated by AI)
3. **Schema** — `.schema.md` rules telling the AI how to operate

**Key insight:** The wiki is persistent and compounding (not one-time RAG). Each new source makes it smarter.

## For Contributors

This is **primarily a template and documentation project**, not a CLI tool.

### Main Files

- `README.md` — What this is, features, quick start (end-user focused)
- `GETTING_STARTED.md` — 5-minute setup guide
- `SCHEMA.md` — Core rules document (users copy this to their vaults)
- `docs/TUTORIAL.md` — Full walkthrough with pasta + Svelte example
- `docs/ADVANCED.md` — Schema customization, power features, troubleshooting
- `template/` — Starter vault (users copy this)
- `tools/` — Optional Python utilities (search, etc.)
- `_archive/` — Original Python package (for reference only)

### Key Points

1. **Documentation is first** — Most changes should update docs, not code
2. **End-user focused** — Write for people copying the template, not developers
3. **Test with real wikis** — When you change something, copy `template/`, make changes, verify in Claude Code + Obsidian
4. **Keep it simple** — This works best when it's lightweight and understandable
5. **Schema is the contract** — If you change how the AI should operate, update `SCHEMA.md`

### Workflow for Changes

1. Update `SCHEMA.md` if you're changing how the AI should operate
2. Update docs if you're explaining something better
3. Update `template/` if you're changing the starter vault structure
4. Test by copying `template/` and actually using it
5. Commit with clear messages explaining what changed and why

### Making a Change (Example)

**Adding a new page template type:**

1. Edit `SCHEMA.md` to define the new template
2. Update `docs/ADVANCED.md` to explain it
3. Add an example in `docs/examples/`
4. Test by asking the AI (in Claude Code) to create a page using the new template
5. Commit with message: `docs: add [feature]`

### Running Tests (Optional)

```bash
python -m pytest tests/ 2>/dev/null || echo "Tests in archive"
```

(Tests are in `_archive/` since we moved away from the Python CLI)

### Git Conventions

- `refactor:` — Major structural changes (like Sections 1-4 of the overhaul)
- `docs:` — Documentation updates
- `feat:` — New features or templates
- `fix:` — Bug fixes
- Keep messages clear and focused
