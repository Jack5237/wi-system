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
- `.obsidian/graph.json` — pre-colored: green for `sources/`, blue for `wiki/`, grey for `AGENTS.md`/`log.md` — zero setup

**Open your agent:**

```bash
claude code .
# or open my-wiki/ in Cursor, VS Code + an agent, ChatGPT, Ollama — any agentic tool
```

**Open Obsidian:** launch it, "Open folder as vault," select `my-wiki/`.

Graph View shows the skeleton immediately — two small trees (`sources/` in green, `wiki/` in blue) hanging off their folder hubs, plus `AGENTS.md` and `log.md` linked in grey. No content nodes yet — that's correct. It fills in and starts connecting laterally (a source to the wiki page it fed) once you ingest something.

## Optional: set up the web clipper

Install [Obsidian Web Clipper](https://obsidian.md/plugins?id=obsidian-web-clipper), then open its extension settings (puzzle-piece icon in your browser toolbar → Obsidian Web Clipper → the gear/settings icon).

The save folder isn't a general setting — it's set per **Template**. Go to **Templates** in the left sidebar, click into the **Default** template itself (not just the list — open the card), and set its own **Path** field to `sources/01-articles`. That's different from picking a vault in the clip popup, which doesn't persist the folder on its own.

If it still won't stick and keeps landing in a `Clippings/` folder or asking every time — don't fight it. The one thing that actually matters is that clips end up **somewhere inside `sources/`**, not at the vault root. Any subfolder, or even the root of `sources/` itself, works — ingest sorts it correctly regardless (`AGENTS.md`: dumping anywhere inside `sources/` is fine). A vault-root `Clippings/` folder is the one place to avoid, since ingest only scans inside `sources/`.

You're set up. For how to actually use it — the prompts you'll type day to day — see **[TUTORIAL.md](TUTORIAL.md)**.
