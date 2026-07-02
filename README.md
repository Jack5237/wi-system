# WI System

**One woven intelligence. Every brain that's touched your problem, feeding one compounding graph.**

Your notes. Claude's conversations. GPT's exports. Gemini's answers. Articles you clipped at 2am. A video transcript from six months ago. Every brain that's ever thought about your problem — human or AI — has produced fragments of an answer, scattered across a dozen tools you'll never reopen.

The WI System is a template for pulling all of it into one place and letting an AI agent weave it into a living wiki. Not a chat log. Not a pile of PDFs. A structured, interlinked knowledge base that gets smarter with every source you feed it — and remembers, so you never have to ask the same question twice.

---

## The flow

```
1. Clone this repo
2. Open template/ in Claude Code      → the agent does the work
   (or Cursor, or any AI agent — the interface is agentic, not a plugin)
3. Open template/ in Obsidian         → watch the graph
4. Drop sources in, tell the agent to ingest
5. Ask it anything — it answers from the wiki first, raw sources second
```

The AI agent is the engine. Obsidian is the windshield. You drive by talking, not clicking.

```bash
git clone https://github.com/Jack5237/wi-system.git
cp -r wi-system/template my-wiki
cd my-wiki
```

Open `my-wiki/` in Claude Code (or Cursor, or any agent) — that's the actual interface, and it reads `AGENTS.md` and knows exactly what to do. Open the same folder in Obsidian for the visual graph. Full walkthrough in **[GETTING_STARTED.md](GETTING_STARTED.md)** (5 minutes).

---

## Why this exists

Every AI conversation you have is a dead end. You ask Claude something brilliant, close the tab, and it's gone. You ask GPT the same question three months later because you forgot the answer existed. Your knowledge doesn't compound — it evaporates.

The WI System fixes that by treating every brain's output as raw material for one persistent structure:

- ✅ **Any source, any brain** — clip articles, drop chat exports from Claude/GPT/Gemini, paste transcripts, drag PDFs
- ✅ **Agent-native** — no plugin, no dashboard. You talk to your AI agent; it reads, classifies, and writes
- ✅ **Structured, not stacked** — pages organize by *subject* (topics, entities, projects, syntheses), never by which tool produced the source
- ✅ **Traceable** — every wiki page links back to the exact raw files that built it
- ✅ **Compounding** — each new source makes every future answer better, because the wiki remembers
- ✅ **Visual** — open the same folder in Obsidian and watch the graph grow as the AI works
- ✅ **Yours** — plain markdown, local-first, version-controlled with git. No lock-in, no server

---

## Quick start (5 minutes)

### 1. Copy the template

```bash
cp -r template my-wiki
cd my-wiki
```

### 2. Open your AI agent — the engine

```bash
claude code .
# or open my-wiki/ in Cursor, VS Code + an agent, ChatGPT, Ollama — anything agentic
```

The agent reads `AGENTS.md` on its own. No config, no setup, no plugin to install.

### 3. Open Obsidian — the graph

Open `my-wiki/` as a vault, click **Graph View**. Empty for now. It fills in as you feed it.

### 4. Feed it a source

Clip an article with [Obsidian Web Clipper](https://obsidian.md/plugins?id=obsidian-web-clipper), or just drag a file into `sources/`. Chat exports, PDFs, transcripts, screenshots — all valid, all fine wherever they land.

### 5. Tell the agent to ingest

> "Ingest new sources"

Watch the graph in Obsidian fill in as the agent classifies the source, writes wiki pages, and links everything together.

**That's the loop.** Feed sources, ask questions, watch it compound.

---

## How it's woven together

```
Every brain's output → sources/ (typed dump) → agent reads AGENTS.md → wiki/ (organized by subject) → graph (visual)
                                                        ↓
                                                  ask a question
                                                        ↓
                                              synthesis becomes a page
```

**Three layers, one contract:**

| Layer | Organized by | Role |
|---|---|---|
| `sources/` | *type* — articles, videos, conversations, documents, images, audio | Immutable raw input, any brain, any format |
| `wiki/` | *subject* — topics, entities, projects, syntheses | AI-maintained, interlinked, compounding knowledge |
| `AGENTS.md` | — | The one file every agent reads to know the rules |

Every wiki page carries a `## Sources` section pointing straight at the raw files that built it — human notes, a Claude session, a GPT export, an article, whatever. That link is the actual weave. Not the folders — the citations.

Talk to your agent in plain language. No slash commands, no memorized syntax:

> "Ingest new sources" · "Lint the wiki" · "What do I know about X?" · "Where do my sources disagree?"

The rules live in `template/AGENTS.md`. Any agent that reads it understands the whole system.

---

## What people build with it

- **Personal learning** — a compounding wiki as you read into a topic
- **Trip planning** — clip everything, ask "where should I stay?", get an answer synthesized from all of it
- **Team knowledge** — feed in meeting notes, research, customer feedback; one shared brain
- **Research** — track findings, surface contradictions between sources automatically
- **Reading journal** — clip reviews and summaries, build a structured library of what you've read

---

## Documentation

- **[GETTING_STARTED.md](GETTING_STARTED.md)** — Setup and first steps (5 min)
- **[TUTORIAL.md](TUTORIAL.md)** — Full walkthrough with a real example
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — How to contribute to this project
- **[CLAUDE.md](CLAUDE.md)** — Architecture and developer notes

## Tips

- Keep Obsidian and your AI agent open on the same folder at the same time — visualize while it works
- Drop ChatGPT/Gemini/Claude exports into `sources/03-conversations/` — any brain's transcript is valid input
- Say **"lint the wiki"** regularly to catch contradictions and orphan pages
- Commit after every ingest — your wiki's history is its memory
- Every folder is pre-colored in the graph — `sources/` subfolders and `wiki/` subfolders all get distinct colors out of the box, zero setup (see `.obsidian/graph.json`)

## Optional: publish the wiki

`wiki/` is just markdown — render it as a browsable site later (e.g. [Fumadocs](https://fumadocs.dev)) if you want to share it outside Obsidian. Off by default, never required.

## Limitations

- Built for personal/team scale (~100 sources, hundreds of pages) — not enterprise RAG
- The agent is the engine — you need access to Claude, GPT, Ollama, or similar
- Garbage in, garbage out — quality depends on what you feed it
- Agents make mistakes; that's what linting is for

## License

MIT — see [LICENSE](LICENSE)

## Contributing

Contributions welcome. See **[CONTRIBUTING.md](CONTRIBUTING.md)** to get started and **[CLAUDE.md](CLAUDE.md)** for how the project is organized.

---

**Ready?** Copy `template/`, open it in your AI agent of choice, add Obsidian for the visuals, and start weaving. Full setup in **[GETTING_STARTED.md](GETTING_STARTED.md)**.
