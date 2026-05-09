# LLM Wiki

A local-first knowledge base that grows smarter every time you add sources.

Imagine you clip web articles about pasta cooking, Svelte web development, and pasta restaurant businesses. Instead of a pile of PDFs, an AI agent reads each one and builds a structured wiki where ideas are linked together. When you ask "How do I build a pasta restaurant website in Svelte?", the AI synthesizes knowledge from all three sources into a new page.

**That's the LLM Wiki pattern.** The wiki is persistent, compounding knowledge — not one-time RAG retrieval.

## Features

✅ **Clip anything** — Use any web clipper to save articles as markdown  
✅ **AI maintains your wiki** — Claude Code, Cursor, OpenAI Code, or any agent updates pages  
✅ **Structured knowledge** — Interlinked concepts, entity pages, synthesis  
✅ **Visual exploration** — Open in Obsidian to see the graph and connections  
✅ **Local-first** — Plain markdown files, version controlled with git  
✅ **Works with any LLM** — Claude, GPT-4, Ollama, etc.

## Quick Start (5 minutes)

### 1. Copy the template

```bash
cp -r template my-wiki
cd my-wiki
```

### 2. Open in an AI agent

```bash
# Using Claude Code
claude code .

# Or open in your editor + AI agent of choice
# The AGENTS.md file tells the AI how to operate
```

### 3. Clip your first article

Use [Obsidian Web Clipper](https://obsidian.md/plugins?id=obsidian-web-clipper) or any tool to save a markdown article to `sources/`.

### 4. Ask the AI to ingest it

In Claude Code, ask:
> "I clipped an article about pasta cooking. Please read `sources/article.md` and update the wiki."

### 5. Explore in Obsidian

```bash
# Install Obsidian from obsidian.md
# Open my-wiki/ as a vault
# Click Graph View to see connections form
```

Done. Your wiki is now growing.

## How It Works

```
Web Clipper → sources/ (raw) → AI reads AGENTS.md → wiki/ (structured) → Obsidian (visual)
                                    ↓
                              Ask questions
                                    ↓
                          Synthesize new pages
```

**Three layers:**

1. **Sources** — Web clipped articles (immutable, your source of truth)
2. **Wiki** — AI-generated pages (interlinked, organized, maintained)
3. **AGENTS.md** — The rules file (in `template/`) that tells the AI how to operate

## Real-World Uses

- **Personal learning** — Build a wiki as you read papers on a topic
- **Trip planning** — Clip travel articles, ask "Where should I stay?" — AI synthesizes recommendations
- **Business** — Feed in meeting notes, market research, customer feedback; build shared team knowledge
- **Research** — Track findings, flag contradictions, see emerging patterns
- **Book notes** — Clip summaries and reviews; build a structured reading journal

## Documentation

- **[GETTING_STARTED.md](GETTING_STARTED.md)** — Setup and first steps (5 min)
- **[TUTORIAL.md](TUTORIAL.md)** — Full walkthrough with complete example
- **[CLAUDE.md](CLAUDE.md)** — For developers and contributors

## Tips

- Open the folder in **Claude Code**, **Cursor**, **VS Code + CodeCompanion**, or any AI agent
- The agent reads `template/AGENTS.md` to understand how to operate
- Use **Obsidian Web Clipper** to quickly save articles
- **Lint regularly** — ask the AI to check for contradictions and orphan pages
- **Commit after each ingest** — your wiki is version controlled

## Limitations

- Works best at personal scale (~100 sources, ~hundreds of pages)
- The AI is the engine — you need access to Claude, GPT-4, Ollama, or similar
- Quality depends on what you feed in (garbage in, garbage out)
- The AI can make mistakes (lint catches most of them)

## License

MIT — See [LICENSE](LICENSE)

## Contributing

We welcome contributions! Check [CLAUDE.md](CLAUDE.md) for development info.

---

**Ready to start?** Copy the `template/` folder and open it in Claude Code. See [GETTING_STARTED.md](GETTING_STARTED.md) for the full setup.

Built on the [LLM Wiki pattern](https://github.com/karpathy/LLM-wiki) by Andrej Karpathy.
