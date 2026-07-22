# Your Wiki — Quick Start

You copied the WI System template. This folder is your local-first knowledge base.

## Three layers:

1. **`sources/`** — Clip web content, paste notes, drop files here. Organize by *type* (Media, Articles, Transcripts).
2. **`wiki/`** — AI-maintained structured pages. Organized by *subject* (Records, Individuals, Execution).
3. **`log.md`** — Append-only operation history. Every ingest gets logged with wikilinks to every file touched.

## Your first steps:

1. Open this folder in Obsidian (for visualization) and Claude Code (for AI operations) side-by-side.
2. Read `AGENTS.md` — that's the rules your AI agent follows to operate this wiki.
3. Clip your first web article or paste a note into `sources/Articles/`.
4. Tell your AI: "ingest" or "please ingest new sources."

The AI will classify it, add frontmatter, move it to the right folder, weave it into the wiki, and log the operation.

That's it. Repeat: clip → ingest → ask questions → wiki grows.

## Key files:

- **`AGENTS.md`** — Rules and workflows. Read this. Modify only if you want to change how the AI operates.
- **`log.md`** — Operation history. Append-only, wikilinked to every file it touched.
- **`.obsidian/graph.json`** — Pre-configured graph view (green = sources, blue = wiki, grey = meta).

## Clip workflows:

- **Web:** Browser extension (Web Clipper, Evernote, similar) → `sources/Articles/`
- **Note:** Paste into a new `.md` file → `sources/Articles/`
- **File:** PDF, image, video → `sources/Media/`, or transcript + raw file if applicable
- **Conversation:** Copy from Claude, ChatGPT, etc. → `sources/Transcripts/`

Never edit `sources/` files after ingest — they're immutable. The AI reads them and synthesizes into wiki pages.

---

Questions? See `AGENTS.md` workflow sections (Ingest, Synthesis, Lint).
