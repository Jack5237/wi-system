# Getting Started

Set up your vault in under 5 minutes.

## What you need

1. **An AI agent** — Claude Code, Cursor, ChatGPT, Ollama, or similar. Does the actual work.
2. **Obsidian** (free) — [Download](https://obsidian.md). Visualizes the graph. Optional but recommended.

## Setup

```bash
git clone https://github.com/Jack5237/wi-system.git
cp -r wi-system/template my-wiki
cd my-wiki
```

`my-wiki/` contains:
- `AGENTS.md` — the entire contract, every agent reads it, nothing else to configure
- `sources/` — drop raw files here (articles, PDFs, chat exports, anything). Ships with one worked example per type (a "React Flow" research thread) so you can see the pattern before adding your own.
- `wiki/` — where your agent writes structured pages. Ships with the wiki pages that example thread produced — one topic, one entity, one project, one synthesis, fully cross-linked.
- `.obsidian/graph.json` — pre-colored: green for `sources/`, blue for `wiki/`, grey for `AGENTS.md`/`log.md` — zero setup

**Open your agent:**

```bash
claude code .
# or open my-wiki/ in Cursor, VS Code + an agent, ChatGPT, Ollama — any agentic tool
```

**Open Obsidian:** launch it, "Open folder as vault," select `my-wiki/`.

Graph View shows a real, connected graph immediately — the example thread, plus `AGENTS.md` and `log.md` linked into both trees. Sources are green, wiki pages are blue, so you can see the weave at a glance: which wiki page a source fed, and which folder hub each node belongs to. When you're ready, delete the example files (or ask your agent to) and start feeding it your own sources — the pattern stays the same.

## Optional: set up the web clipper

Install [Obsidian Web Clipper](https://obsidian.md/plugins?id=obsidian-web-clipper), open its extension settings, and under **Behavior → Note location**, point it at `sources/01-articles` in your vault. Now every clip lands pre-sorted.

Don't stress about getting this exact — anything dropped anywhere in `sources/` gets sorted correctly during ingest anyway. The clipper folder setting just saves your agent a step.

## Optional: table view with Obsidian Bases

`sources.base` and `wiki.base` (vault root) give you a spreadsheet-style table of every source or wiki page — filterable and sortable by `type`, `captured`/`updated`, `ingested`, etc. — as an alternative to the graph. Open one from the file explorer or the command palette ("Open base"). If Obsidian's Base editor flags the syntax, use its visual editor to regenerate the file — Bases is a newer feature and its schema may have moved since these were written.

You're set up. For how to actually use it — the prompts you'll type day to day — see **[TUTORIAL.md](TUTORIAL.md)**.
