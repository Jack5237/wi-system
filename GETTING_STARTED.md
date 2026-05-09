# Getting Started

Get your LLM Wiki up and running in 5 minutes.

## What You Need

1. **Obsidian** (free) — [Download](https://obsidian.md)
2. **An AI agent** — Claude Code, Cursor, VS Code + extension, or similar
3. **A web clipper** (optional but recommended) — [Obsidian Web Clipper](https://obsidian.md/plugins?id=obsidian-web-clipper)

## Setup (3 steps)

### Step 1: Copy the template

```bash
cp -r template my-wiki
cd my-wiki
ls -la
```

You should see:
- `AGENTS.md` — Rules for the AI
- `index.md` — Navigation
- `log.md` — Operation log
- `sources/` — Where clipped articles go
- `wiki/` — Where AI creates pages

### Step 2: Open in Claude Code (or your AI agent)

```bash
claude code .
```

The AI reads `AGENTS.md` and understands how to operate.

### Step 3: Open in Obsidian

1. Launch Obsidian
2. Click "Open folder as vault"
3. Select `my-wiki/`
4. You're done!

## First Ingestion

### Clip an article

Use the Obsidian Web Clipper browser extension to save an article. It will be saved as markdown.

### Save it to sources/

Either:
- Drag the file directly into Obsidian → `sources/` folder
- Or manually copy it: `cp ~/Downloads/article.md my-wiki/sources/`

### Tell the AI to ingest it

In Claude Code, ask:

```
I just clipped an article about [topic].
The file is in sources/article.md.
Please read it and update the wiki.
```

The AI will:
1. Read the article
2. Extract key concepts
3. Create wiki pages
4. Link related ideas
5. Update index.md
6. Log the changes

### See the results

In Obsidian:
1. Open `wiki/` to see new pages
2. Click on one → see the backlinks
3. View → Graph View to see connections forming

## Querying Your Wiki

Once you have a few sources, ask questions:

```
What are the main topics in my wiki?
```

```
How would I combine topic A with topic B?
```

```
Are there any contradictions in my wiki?
```

The AI searches your wiki (not raw sources), synthesizes an answer, and can create a new page with the result.

## Linting

Periodically ask:

```
Please lint the wiki. Check for:
- Contradictions
- Orphan pages
- Unlinked concepts
- Missing cross-references
```

The AI will review everything and suggest fixes.

## Next Steps

- Read [TUTORIAL.md](TUTORIAL.md) for a complete example walkthrough
- Check [CLAUDE.md](CLAUDE.md) for developer information

---

**Questions?** Check the README or TUTORIAL, or open an issue.
