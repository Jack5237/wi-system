# Getting Started

Get your woven intelligence vault up and running in 5 minutes.

## What You Need

1. **An AI agent** — Claude Code, Cursor, VS Code + extension, ChatGPT, Ollama, or similar. This is the engine — it does the reading, classifying, and writing.
2. **Obsidian** (free) — [Download](https://obsidian.md). This is the windshield — it visualizes the graph the agent builds.
3. **A web clipper** (optional but recommended) — [Obsidian Web Clipper](https://obsidian.md/plugins?id=obsidian-web-clipper)

## Setup (3 steps)

### Step 1: Clone and copy the template

```bash
git clone https://github.com/Jack5237/wi-system.git
cp -r wi-system/template my-wiki
cd my-wiki
ls -la
```

You should see:
- `AGENTS.md` — The entire contract. Every agent reads this and knows what to do — no other config needed.
- `log.md` — Operation log
- `sources/` — Raw data dump, organized by type (`01-articles/`, `02-videos/`, `03-conversations/`, `04-documents/`, `05-images/`, `06-audio/`)
- `wiki/` — Where the agent creates pages, organized by subject (`topics/`, `entities/`, `projects/`, `syntheses/`), with `index.md` as the navigation hub
- `.obsidian/graph.json` — pre-configured graph view, every `sources/` and `wiki/` subfolder already color-grouped — nothing to set up

### Step 2: Open your AI agent — this is the main interface

```bash
claude code .

# Or open my-wiki/ in Cursor, VS Code + an agent, ChatGPT, Ollama — any agentic interface
```

The agent reads `AGENTS.md` on its own and understands how to operate. No slash commands to memorize, no plugin to install — you just talk to it.

### Step 3: Open Obsidian — this is the visualization

1. Launch Obsidian
2. Click "Open folder as vault"
3. Select `my-wiki/`
4. Click Graph View (left sidebar) — empty for now, it fills in as the agent works

**You now have:** your AI agent doing the work, and Obsidian showing you the graph it's building — both pointed at the same `my-wiki/` folder.

## First Ingestion

### Clip an article

Use the Obsidian Web Clipper browser extension to save an article. It will be saved as markdown. (Chat exports, PDFs, and transcripts work too — drop them anywhere in `sources/`.)

### Save it to sources/

Either:
- Drag the file directly into Obsidian → `sources/` folder (any subfolder, or the root — the AI sorts it)
- Or manually copy it: `cp ~/Downloads/article.md my-wiki/sources/01-articles/`

### Tell the AI to ingest it

Say to your AI agent:

> "Ingest new sources"

The AI will:
1. Read each unprocessed file in `sources/`
2. Classify it, rename it, move it to the right typed subfolder, and add frontmatter
3. Extract key concepts and search the wiki before creating anything
4. Create or update pages in `wiki/topics/`, `wiki/entities/`, or `wiki/projects/`
5. Weave the source's file path into every touched page's `## Sources` section
6. Update `wiki/index.md`
7. Log the changes and commit

### See the results

In Obsidian:
1. Open `wiki/topics/` or `wiki/entities/` to see new pages
2. Click on one → see the backlinks and its `## Sources` section
3. View → Graph View to see connections forming — raw sources and wiki pages are already color-coded by folder, so you can see at a glance what's raw input versus structured knowledge (see `.obsidian/graph.json`)

## Querying Your Wiki

Once you have a few sources, just ask questions directly:

> "What are the main topics in my wiki?"

> "How would I combine topic A with topic B?"

> "Are there any contradictions in my wiki?"

The AI searches your wiki (not raw sources) first, then falls back to raw sources and general knowledge (clearly labelled), and can save a new page in `wiki/syntheses/` with the result.

## Linting

Periodically say:

> "Lint the wiki"

This checks for un-ingested files, contradictions, orphan pages, duplicates, dead source links, and a stale index — then offers fixes.

## Next Steps

- Read [TUTORIAL.md](TUTORIAL.md) for a complete example walkthrough
- Check [CLAUDE.md](CLAUDE.md) for developer information

---

**Questions?** Check the README or TUTORIAL, or open an issue.
