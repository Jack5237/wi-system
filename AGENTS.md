# WI System — Contributor Guide

**WI System** is a schema-driven knowledge-base template. Users copy `template/`, open it in Obsidian alongside Claude Code or any AI agent, clip content into `sources/`, and the AI maintains a structured, interlinked wiki in `wiki/` following rules in `template/AGENTS.md`.

Three-layer architecture: immutable sources (organized by *type*), AI-maintained wiki (organized by *subject*), and an append-only log connecting both. Persistent, compounding RAG — each source makes the wiki smarter.

This document tells contributors how to modify and extend the system itself. End-users who copy `template/` follow rules in `template/AGENTS.md`. **That file is the contract** — changes there ripple to every user's workflow. Treat it like a published API.

## Project Structure

- **Docs** (`README.md`, `GETTING_STARTED.md`, `TUTORIAL.md`) — User-facing
- **`template/`** — What users copy; only essential files, no bloat
  - `template/AGENTS.md` — Rules end-users' AI agents follow to operate their wiki
  - `template/sources/`, `template/wiki/`, `template/log.md`, `.obsidian/graph.json`
- **`AGENTS.md`** (this file) — Contributor workflow; `CLAUDE.md` and `CONTRIBUTING.md` point here

## Principles

1. **Minimal template** — Users copy `template/`. Everything in there must earn its place. No speculative features, no "nice to have" scaffolding.
2. **Schema is stable** — Frontmatter fields (`type`, `captured`, `ingested`, `updated`, etc.) and folder structure (MAT/RIX hierarchy) rarely change. If you change them, you break every existing user vault. Update `template/AGENTS.md` to match, and add migration guidance if non-trivial.
3. **Rules ≠ tools** — The system works with Claude Code, Cursor, ChatGPT, Ollama — any AI agent. Rules must be tool-agnostic. No slash commands, no agent-specific config, no hooks. Just markdown and wikilinks.
4. **Test with real wikis** — Copy `template/`, seed it with sample sources, and run the full workflow (ingest → synthesize → lint). If it breaks in practice, the change isn't done.

## Before You Change

1. **Is this change needed?** Users haven't asked for it? YAGNI — don't add it.
2. **Does `template/AGENTS.md` need updating?** If the rule changed or an AI's job changed, update that doc first. That's where the actual contract lives.
3. **Will existing vaults break?** If schema or folder structure changes, what migrates? Document it.
4. **Can the change live in docs instead?** A clarification to `TUTORIAL.md` or `AGENTS.md` beats a code/structure change every time.

## When Making Changes

1. **Edit `template/AGENTS.md`** — Propose what the rule is now. Make it clear, precise, example-rich.
2. **Update examples** in that file (Summary format, Log format, Wiki page template, etc.) to match.
3. **Update folder structure in `template/`** only if the rules demand it.
4. **Test by copying `template/`** to a scratch directory, creating sample sources, ingesting, synthesizing, linting. Confirm the workflow works end-to-end:
   ```bash
   cp -r template my-test-vault
   # open my-test-vault/ in Claude Code, Cursor, or another agent and run the workflows
   ```
5. **Update `template/.obsidian/graph.json`** if folder names or colors changed.
6. **Update root docs** (`README.md`, `TUTORIAL.md`, etc.) if the mental model changed.
7. **Commit** with a clear message explaining what changed in the contract and why.

## Commit Conventions

- `docs:` — Documentation updates, no structure change
- `refactor:` — Structural changes to template or docs
- `fix:` — Bug fixes, schema corrections
- `feat:` — New capabilities or optional layers (rare)
- `chore:` — Maintenance (CI, config, etc.)

Keep messages focused. Example: `docs: clarify hub-link pattern in AGENTS.md`

## Quality Gates

**Before merging:**

- ✓ `template/AGENTS.md` is clear and example-rich
- ✓ Examples match the described rules
- ✓ Folder structure in `template/` matches the rules
- ✓ `.obsidian/graph.json` reflects the current folders
- ✓ Tested end-to-end with a real ingest cycle
- ✓ No speculative features (only changes users asked for)
- ✓ Migration path clear (if schema changed)

**What NOT to add:**

- Automation daemons or external tools (stays agent-agnostic)
- Per-user config files (rules are universal)
- Optional "advanced" layers that fragment the system
- Stub files or example stubs (users create their own content)
- Anything that assumes a specific AI agent

## Proposing and Reviewing Changes

**Propose:** fork, branch (`feature/your-feature`), make the change in `template/AGENTS.md` language, test it end-to-end, then open a PR with the updated contract, examples, docs, and any structure changes. One focused change per PR.

**Review:** does it solve a real problem (not speculative)? Is `template/AGENTS.md` updated and do its examples match? Was it tested end-to-end? Will existing vaults still work (migration clear if not)? All yes → merge; otherwise ask for revision.

---

Remember: every change to `template/AGENTS.md` or folder structure is a breaking change for users. Small, clear, tested beats big or speculative.
