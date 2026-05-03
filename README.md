# WI-system

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status: Beta](https://img.shields.io/badge/status-beta-orange.svg)]()

**WI-system** is a local, LLM-maintained living wiki engine. It transforms raw sources into an evolving knowledge base that improves over time, perfect for agentic projects and teams that need durable project memory.

## Features

- **Local-first**: Run entirely on your machine or local LLM
- **LLM-powered**: Uses OpenAI-compatible APIs (local models supported)
- **Git-friendly**: Wiki integrates with your project repo
- **Schema-less**: Markdown-based with YAML frontmatter for queries
- **Append-only logs**: Full audit trail of all operations
- **Link maintenance**: Automatic contradiction detection and link cleanup
- **Agent-ready**: Easy CLI interface for agentic workflows

## Quick Start (3 steps, 10 minutes)

### 1. Install
```bash
pip install git+https://github.com/Jack5237/wi-system.git
wi --help
```

### 2. Create your wiki
```bash
mkdir my-wiki && cd my-wiki
wi init --root .
```

### 3. Ingest and explore
```bash
# Add a document
echo "# My Project" > sources/doc.md

# Ingest
wi ingest --root . sources/doc.md

# Open in Obsidian and view the graph!
# (File → Open as vault → select my-wiki)
```

**→ [GETTING_STARTED.md](GETTING_STARTED.md) — 10-minute guide**

**→ [docs/TUTORIAL.md](docs/TUTORIAL.md) — Complete walkthrough**

## Architecture

### Key Concept

Two distinct things:

1. **`wi_system/`** (underscore) — Python engine package (this repo)
2. **`wi-system/`** (hyphen) — Runtime workspace folder in your project

The engine is installed once; the workspace is created once per project.

### What lives where

```
your-project/
├── src/
├── docs/
└── wi-system/           ← Workspace folder
    ├── sources/         ← Raw inputs (immutable)
    ├── wiki/            ← Maintained pages
    ├── index.md         ← Navigation/TOC
    └── log.md           ← Operation history (append-only)
```

This keeps project memory with project code, tracked in git.

## Configuration

### Environment Variables

```bash
# Use local LLM (OpenAI-compatible API)
export WI_LLM_MODE=openai
export WI_LLM_BASE_URL=http://localhost:11434/v1
export WI_LLM_MODEL=mistral:latest
export WI_LLM_API_KEY=your-api-key

# Or use OpenAI
export WI_LLM_MODE=openai
export WI_LLM_BASE_URL=https://api.openai.com/v1
export WI_LLM_MODEL=gpt-4
export WI_LLM_API_KEY=sk-...
```

## Project Structure

- **`wi_system/`** — Core engine modules
  - `cli.py` — Command-line interface
  - `engine.py` — Main orchestration
  - `llm.py` — LLM integration
  - `markdown.py` — Markdown parsing and writing
- **`examples/`** — Starter workspace template (copy to use)
- **`tests/`** — Smoke tests for reliability
- **`.github/`** — CI workflows and templates
- **`docs/`** — Guides and use cases

## How it works

1. **Ingest**: Read raw source documents into the wiki
2. **Index**: Build searchable index of pages and links
3. **Query**: Find relevant pages, synthesize answers with LLM
4. **Lint**: Detect contradictions, orphan pages, outdated claims
5. **Fix**: Clean up links and flag inconsistencies

## Conventions

- **Sources are immutable** after ingest (audit trail)
- **Log is append-only** (complete operation history)
- **Pages are interlinked** (knowledge graph structure)
- **Frontmatter drives queries** (YAML metadata for filtering)

## Real-world workflow

1. Capture web content with Obsidian Web Clipper → `sources/`
2. Ingest: `wi ingest --root . sources/captured.md`
3. Query: `wi query --root . "What did we learn?"`
4. Store answers back as synthesis pages
5. Weekly lint: `wi lint --root . --fix` to catch stale info

## How It Works (Visual Flow)

```
Raw Documents → Ingest → Wiki Pages → Query → Synthesis
      ↓                      ↓
   sources/              wiki/
                          ↓
                    View in Obsidian
                    (graph + backlinks)
```

1. **Ingest** raw docs from `sources/` 
2. **Generate** wiki pages, index, and links
3. **Explore** the graph in Obsidian (or browse HTML)
4. **Query** the wiki for insights
5. **Synthesize** answers and store as new pages
6. **Lint** weekly to maintain quality

## Documentation

**Getting Started**
- **[GETTING_STARTED.md](GETTING_STARTED.md)** — 10-minute quick start
- **[START_HERE.md](START_HERE.md)** — Minimal reference
- **[docs/TUTORIAL.md](docs/TUTORIAL.md)** — Complete walkthrough with examples

**Usage Guides**
- **[docs/OBSIDIAN_GUIDE.md](docs/OBSIDIAN_GUIDE.md)** — Visualization in Obsidian
- **[docs/ADOPTION_GUIDE.md](docs/ADOPTION_GUIDE.md)** — Team rollout and workflows
- **[docs/USE_CASES.md](docs/USE_CASES.md)** — Real-world examples

**Reference**
- **[AGENTS.md](AGENTS.md)** — Agent integration contracts
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — Contributing guidelines
- **[SECURITY.md](SECURITY.md)** — Security policy

## License

MIT — See [LICENSE](LICENSE) for details.

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

Built for teams that need durable, versioned, searchable project memory.
