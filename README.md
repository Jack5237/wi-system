# WI System

<picture><source media="(prefers-color-scheme: dark)" srcset="https://www.shieldcn.dev/github/stars/Jack5237/wi-system.svg?variant=secondary&size=sm&mode=dark"><img alt="GitHub Stars" src="https://www.shieldcn.dev/github/stars/Jack5237/wi-system.svg?variant=secondary&size=sm&mode=light"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="https://www.shieldcn.dev/github/forks/Jack5237/wi-system.svg?variant=secondary&size=sm&mode=dark"><img alt="GitHub Forks" src="https://www.shieldcn.dev/github/forks/Jack5237/wi-system.svg?variant=secondary&size=sm&mode=light"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="https://www.shieldcn.dev/github/last-commit/Jack5237/wi-system.svg?variant=secondary&size=sm&mode=dark"><img alt="Last commit" src="https://www.shieldcn.dev/github/last-commit/Jack5237/wi-system.svg?variant=secondary&size=sm&mode=light"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="https://www.shieldcn.dev/github/license/Jack5237/wi-system.svg?variant=ghost&size=sm&mode=dark"><img alt="License" src="https://www.shieldcn.dev/github/license/Jack5237/wi-system.svg?variant=ghost&size=sm&mode=light"></picture>

**One woven intelligence. Every brain that's touched your problem, feeding one compounding graph.**

Your notes, Claude's conversations, GPT's exports, clipped articles — every brain that's thought about your problem, human or AI, produces fragments of an answer that usually just evaporate. WI System is a template for pulling all of it into one place and letting an AI agent weave it into a living, structured wiki that gets smarter with every source you feed it.

## Get started

```bash
git clone https://github.com/Jack5237/wi-system.git
cp -r wi-system/template my-wiki
cd my-wiki
```

Open `my-wiki/` in **Claude Code** (or Cursor, or any AI agent) — that's the real interface, it reads `AGENTS.md` and knows what to do. Open the same folder in **Obsidian** for the visual graph.

> "Ingest new sources"

That's the whole loop: drop files in `sources/`, tell your agent to ingest, watch the wiki grow.

**Full setup:** [GETTING_STARTED.md](GETTING_STARTED.md) · **How to use it:** [TUTORIAL.md](TUTORIAL.md)

## Why

- **Any source, any brain** — articles, Claude/GPT/Gemini exports, PDFs, transcripts, screenshots
- **Agent-native** — no plugin, no dashboard, just plain language to your AI agent
- **Structured, not stacked** — pages organize by subject, not by which tool made the source
- **Traceable** — every wiki page links back to the raw files that built it
- **Compounding** — each new source makes every future answer better
- **Visual** — Obsidian shows the graph as your agent builds it, fully color-coded, zero setup
- **Yours** — plain markdown, local-first, version-controlled, no lock-in

## How it works

| Layer | Organized by | Role |
|---|---|---|
| `sources/` | *type* — articles, videos, conversations, documents, images, audio | Immutable raw input, any brain, any format |
| `wiki/` | *subject* — topics, entities, projects, syntheses | AI-maintained, interlinked, compounding knowledge |
| `AGENTS.md` | — | The one file every agent reads to know the rules |

Every wiki page has a `## Sources` section pointing at the exact raw files that built it. That link is the actual weave.

## Documentation

- **[GETTING_STARTED.md](GETTING_STARTED.md)** — Install and set up (5 min)
- **[TUTORIAL.md](TUTORIAL.md)** — Prompt library and worked example
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — How to contribute
- **[CLAUDE.md](CLAUDE.md)** — Architecture notes

## Limitations

Built for personal/team scale, not enterprise RAG. Requires an AI agent (Claude, GPT, Ollama, etc). Quality depends on what you feed it.

## License

MIT — see [LICENSE](LICENSE)

## Contributing

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

[![Jack5237/wi-system contributors](https://shieldcn.dev/contributors/Jack5237/wi-system.svg?preset=transparent&names=true&titleAlign=center&align=left&mode=dark)](https://github.com/Jack5237/wi-system/graphs/contributors)

![Star history chart](https://shieldcn.dev/chart/github/stars/Jack5237/wi-system.svg)
