# WI System — A Woven Intelligence Template

The WI System is a **template** for building a local-first knowledge base that grows smarter every time you add sources.

Imagine you clip web articles about pasta cooking, Svelte web development, and pasta restaurant businesses. Instead of a pile of PDFs, an AI agent reads each one and builds a structured wiki where ideas are linked together. When you ask "How do I build a pasta restaurant website in Svelte?", the AI synthesizes knowledge from all three sources into a new page.

**That's the WI System.** The wiki is persistent, compounding knowledge — not one-time RAG retrieval.

---

## For Users: Get Started Now

**Copy the `template/` folder** — that's your vault:

```bash
cp -r template my-wiki
cd my-wiki
```

Then open it in Obsidian (visualization) alongside Claude Code, Cursor, or any AI agent (does the work). See **[GETTING_STARTED.md](GETTING_STARTED.md)** for the 5-minute setup.

---

## Features

✅ **Clip anything** — Use any web clipper to save articles as markdown  
✅ **AI maintains your wiki** — Claude Code, Cursor, OpenAI Code, or any agent updates pages  
✅ **Structured knowledge** — Interlinked concepts, entity pages, synthesis  
✅ **Visual exploration** — Open in Obsidian to see the graph and connections  
✅ **Local-first** — Plain markdown files, version controlled with git  
✅ **Works with any AI agent** — Claude Code, Cursor, GPT-4, Ollama, etc.

## Quick Start (5 minutes)

### 1. Copy the template

```bash
cp -r template my-wiki
cd my-wiki
```

### 2. Open Obsidian (visualization)

```bash
# Install Obsidian from obsidian.md if needed
# Open my-wiki/ as a vault
# Click Graph View (left sidebar) — you'll see it grow as you add sources
```

### 3. Open your AI agent (in the same folder)

```bash
# Using Claude Code
claude code .

# Or Cursor, VS Code, ChatGPT Web, Ollama, etc.
# The AGENTS.md file tells the AI how to operate
```

**You now have:**
- **Left side:** Obsidian showing the visual graph of your knowledge
- **Right side:** AI agent (Claude Code, Cursor) doing the work

### 4. Clip your first article

Use [Obsidian Web Clipper](https://obsidian.md/plugins?id=obsidian-web-clipper) or drag/paste to save markdown into `sources/01-articles/`. PDFs, videos, chat exports, images — drop them anywhere in `sources/`.

### 5. Tell the AI to ingest it

Say to your AI agent: *"Ingest new sources"* or *"Run ingest"*

The AI reads `AGENTS.md`, sorts your sources, and updates the wiki. Watch Obsidian's graph update in real-time.

Done. Your wiki is now growing.

## How It Works

A woven intelligence system: every brain that's touched a problem — your notes, Claude conversations, ChatGPT/Gemini exports, clipped articles, videos — dumps its raw output into `sources/`. One brain, the wiki, reads and connects all of them.

```
Any brain's output → sources/ (typed dump) → AI reads AGENTS.md → wiki/ (organized by subject) → Obsidian (visual)
                                                    ↓
                                              Ask questions
                                                    ↓
                                          Synthesize new pages
```

**Three layers:**

1. **Sources** — Raw input, organized by *type* (`articles/`, `videos/`, `conversations/`, `documents/`, `images/`, `audio/`) — immutable, your source of truth
2. **Wiki** — AI-generated pages, organized by *subject* (`topics/`, `entities/`, `projects/`, `syntheses/`) — interlinked, maintained, never mirrors the source-type folders
3. **AGENTS.md** — The rules file (in `template/`) that tells the AI how to operate

Every wiki page has a `## Sources` section pointing at the exact raw files (of any type) that fed it — that link is the actual weave, not the folder structure.

### Working with the wiki

Simply ask your AI agent to ingest, synthesize, or lint — the rules are in `template/AGENTS.md`. Any AI agent that reads AGENTS.md will understand the workflows without you having to re-explain them each time.

## Real-World Uses

- **Personal learning** — Build a wiki as you read papers on a topic
- **Trip planning** — Clip travel articles, ask "Where should I stay?" — AI synthesizes recommendations
- **Business** — Feed in meeting notes, market research, customer feedback; build shared team knowledge
- **Research** — Track findings, flag contradictions, see emerging patterns
- **Book notes** — Clip summaries and reviews; build a structured reading journal

## Documentation

- **[GETTING_STARTED.md](GETTING_STARTED.md)** — Setup and first steps (5 min)
- **[TUTORIAL.md](TUTORIAL.md)** — Full walkthrough with complete example
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — How to contribute to this project
- **[CLAUDE.md](CLAUDE.md)** — Architecture and developer notes

## Tips

- Open the same folder in **Obsidian** (visualization) and **Claude Code**, **Cursor**, or any AI agent (does the work)
- The agent reads `template/AGENTS.md` to understand how to operate — no other config needed
- Use **Obsidian Web Clipper** to quickly save articles into `sources/01-articles/`
- Drop ChatGPT/Gemini/Claude conversation exports into `sources/03-conversations/` — any brain's transcript is a valid input
- Say **"lint the wiki"** regularly to check for contradictions and orphan pages
- **Commit after each ingest** — your wiki is version controlled
- Open Graph View in Obsidian to see the wiki as a connected brain — `sources/` is filtered out by default (see `.obsidian/graph.json`)

## Optional: Publish the Wiki

`wiki/` is just markdown, so you can optionally render it as a browsable site later (e.g. with [Fumadocs](https://fumadocs.dev)) for sharing outside Obsidian. This is off by default and not required — the core system never depends on it.

## Limitations

- Works best at personal scale (~100 sources, ~hundreds of pages)
- The AI is the engine — you need access to Claude, GPT-4, Ollama, or similar
- Quality depends on what you feed in (garbage in, garbage out)
- The AI can make mistakes (lint catches most of them)

## License

MIT — See [LICENSE](LICENSE)

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get started, and [CLAUDE.md](CLAUDE.md) for project architecture.

---

**Ready to start?** Copy the `template/` folder, open it in Obsidian + your AI agent of choice. See [GETTING_STARTED.md](GETTING_STARTED.md) for the full setup.
