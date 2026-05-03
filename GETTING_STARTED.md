# Getting Started with WI-system

The fastest way to go from zero to a working wiki with Obsidian visualization.

## 3-Step Quick Start (10 minutes)

### 1️⃣ Install
```bash
pip install git+https://github.com/Jack5237/wi-system.git
wi --help
```

### 2️⃣ Create your wiki
```bash
mkdir my-wiki && cd my-wiki
wi init --root .
```

### 3️⃣ Add documents and ingest
```bash
# Save a document to sources/
echo "# My Knowledge" > sources/doc.md

# Ingest it
wi ingest --root . sources/doc.md

# Explore in Obsidian
# (Open this folder in Obsidian → Graph View)
```

**Done!** Your wiki is live.

---

## Next: Visualize in Obsidian

### Install Obsidian
1. Download from [obsidian.md](https://obsidian.md)
2. Open the app
3. Click "Open folder as vault"
4. Select your `my-wiki` folder

### Explore Your Wiki

1. **Graph View** (left sidebar icon) — See nodes and connections
2. **Backlinks** (right sidebar) — Find related pages
3. **Search** (Ctrl/Cmd+P) — Jump to pages
4. **Click nodes** — Read content

---

## Full Guides

- **[TUTORIAL.md](docs/TUTORIAL.md)** ← Complete walkthrough with examples (READ THIS FIRST!)
- [ADOPTION_GUIDE.md](docs/ADOPTION_GUIDE.md) — How to roll out in a team
- [OBSIDIAN_GUIDE.md](docs/OBSIDIAN_GUIDE.md) — Advanced visualization tips
- [START_HERE.md](START_HERE.md) — Minimal reference
- [README.md](README.md) — Full feature reference

---

## Common Workflows

### Ingest a document
```bash
wi ingest --root . sources/new-doc.md
```

### Ask the wiki a question
```bash
wi query --root . "What's the architecture?"
```

### Store an answer as a new page
```bash
wi query --root . "What's the architecture?" --store
```

### Maintain the wiki
```bash
wi lint --root . --fix
```

### See operation history
```bash
cat log.md
```

---

## Your First Wiki (5 minutes)

### 1. Create source documents
```bash
mkdir -p my-wiki/sources
cd my-wiki

cat > sources/hello.md << 'EOF'
# Project Overview

This is our main project. It has:
- A backend API
- A web frontend
- Mobile apps

## Key Technologies
- Python for backend
- React for frontend
- TypeScript everywhere
EOF

cat > sources/architecture.md << 'EOF'
# System Architecture

## Backend
- REST API in Python/FastAPI
- PostgreSQL for data
- Redis for caching

## Frontend
- React web app
- React Native mobile
- Shared TypeScript types

## Deployment
- Docker containers
- Kubernetes orchestration
- GitHub Actions CI/CD
EOF
```

### 2. Initialize and ingest
```bash
wi init --root .
wi ingest --root . sources/hello.md
wi ingest --root . sources/architecture.md
```

### 3. Open in Obsidian
1. Open Obsidian → "Open folder as vault"
2. Select the `my-wiki` folder
3. Click Graph View (left sidebar)
4. Explore the connections!

### 4. Query
```bash
wi query --root . "What technologies do we use?"
wi query --root . "How is the system deployed?" --store
```

### 5. Explore the results
In Obsidian, you'll see new pages with:
- Auto-generated connections
- Backlinks showing relationships
- Synthesized answers

**Your wiki is live!** 🎉

---

## Obsidian Tips

**Graph View**
- Zoom: Scroll wheel
- Pan: Drag background
- Click nodes: Read page
- Filter by tag: Use tag search

**Backlinks Panel** (right sidebar)
- See what links to this page
- Jump to references
- Understand relationships

**Search** (Cmd/Ctrl + P)
- Find pages by name
- Jump instantly
- Filter by tag

**Tags**
- Add to frontmatter: `tags: [topic, design]`
- Use to organize pages
- Filter graph by tag

---

## What's Next?

### Read the Tutorial
Work through [docs/TUTORIAL.md](docs/TUTORIAL.md) for a complete example with real documents.

### Explore the Guides
- **Team rollout?** → [ADOPTION_GUIDE.md](docs/ADOPTION_GUIDE.md)
- **Obsidian deep dive?** → [OBSIDIAN_GUIDE.md](docs/OBSIDIAN_GUIDE.md)
- **All features?** → [README.md](README.md)

### Get Productive
1. Add your real documents to `sources/`
2. Ingest them
3. Ask questions
4. Share the graph with your team

---

## Troubleshooting

### Graph is empty
- Check `wi init --root .` was run
- Run `wi ingest --root . sources/doc.md`
- Reload Obsidian (Cmd/Ctrl + R)

### Broken links in Obsidian
- Run `wi lint --root . --fix`
- Check page names match exactly

### LLM not responding
- Check `WI_LLM_API_KEY` is set
- Check `WI_LLM_BASE_URL` is correct
- Run `wi query` with short, simple question first

### Need help?
- Check [README.md](README.md)
- See [TUTORIAL.md](docs/TUTORIAL.md) examples
- Open an issue on GitHub

---

**You now have everything to build a living knowledge base!** 🚀

Next: [docs/TUTORIAL.md](docs/TUTORIAL.md) for a complete walkthrough.
