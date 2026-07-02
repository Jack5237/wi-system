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
- `sources/` — drop raw files here (articles, PDFs, chat exports, anything)
- `wiki/` — where your agent writes structured pages
- `.obsidian/graph.json` — every folder pre-colored, zero setup

**Open your agent:**

```bash
claude code .
# or open my-wiki/ in Cursor, VS Code + an agent, ChatGPT, Ollama — any agentic tool
```

**Open Obsidian:** launch it, "Open folder as vault," select `my-wiki/`.

Graph View will look empty — that's correct. The only real notes in a fresh template are `AGENTS.md`, `log.md`, and `wiki/index.md`; everything else is a placeholder folder waiting for content. It fills in once you ingest something.

## Optional: set up the web clipper

Install [Obsidian Web Clipper](https://obsidian.md/plugins?id=obsidian-web-clipper), open its extension settings, and under **Behavior → Note location**, point it at `sources/01-articles` in your vault. Now every clip lands pre-sorted.

Don't stress about getting this exact — anything dropped anywhere in `sources/` gets sorted correctly during ingest anyway. The clipper folder setting just saves your agent a step.

You're set up. For how to actually use it — the prompts you'll type day to day — see **[TUTORIAL.md](TUTORIAL.md)**.
