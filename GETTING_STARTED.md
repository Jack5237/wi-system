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

## You're set up. Now what?

Setup is done — `my-wiki/` exists, your agent reads `AGENTS.md`, Obsidian is watching. That's it for installation.

Everything about actually *using* the system — the prompts you type, ingesting your first source, asking questions, linting — lives in **[TUTORIAL.md](TUTORIAL.md)**. It has a full prompt reference plus a worked example so you're not guessing what to say.

## Next Steps

1. Drop one real file into `sources/` (an article, a chat export, anything)
2. Open **[TUTORIAL.md](TUTORIAL.md)** and follow "Your First Ingest"
3. Keep the prompt library there open as a reference while you work

---

**Questions?** Check the [README](README.md) or [TUTORIAL.md](TUTORIAL.md), or open an issue.
