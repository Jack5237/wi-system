# Advanced: Schema Customization & Power Features

Once you've done the basic setup, here's how to extend your wiki.

## Customizing Your Schema

Your `.schema.md` is the contract between you and the AI. You can modify it.

### Example: Add a "Source Review" section

Edit `.schema.md` and add:

```markdown
## Page Format

All wiki pages use this structure:

```markdown
---
source: source-file.md
date: 2026-05-09
tags: [tag1, tag2]
review_status: [unreviewed | reviewed | verified]
---

# Page Title
...
```

Then tell the AI:

> "Going forward, add a review_status field to all pages you create. Set it to 'unreviewed' until I manually review it."

### Example: Require citations for every claim

Edit `.schema.md`:

```markdown
## Linking Rules

- Every factual claim must cite its source
- Format: "Claim here[^1]" with footnotes linking to sources
```

### Example: Add page templates for specific types

Create `template/page-templates.md`:

```markdown
# Page Templates

## Entity Template
Use for people, places, organizations:
- Overview
- Key facts
- Related entities
- Sources

## Concept Template
Use for ideas, techniques, frameworks:
- Definition
- Key points
- Real-world examples
- Related concepts

## Synthesis Template
Use for analysis you've created:
- Question asked
- Relevant sources
- Analysis
- Conclusions
```

Tell the AI: > "When creating new pages of type X, use the template from template/page-templates.md."

## Linting Your Wiki

Ask the AI to periodically review everything:

```
Please lint the wiki deeply.

For each issue, tell me:
1. What you found
2. Why it matters
3. How I should fix it

Issues to check:
- Contradictions between pages
- Claims without sources
- Pages with no backlinks (orphans)
- Concepts mentioned but not paged
- Links to non-existent pages
- Outdated information
```

The AI will give you a report, optionally with fixes.

## Adding Search

For larger wikis, full-text search is helpful. Two options:

### Option 1: Simple Grep (free, built-in)

In Claude Code, ask:

```
Search the wiki for pages about [topic].
Grep through wiki/*.md for keywords.
Show me the top 5 matches.
```

### Option 2: Full-Text Search Tool

We provide `tools/search.py` (optional):

```bash
python tools/search.py "pasta recipe" wiki/
```

This indexes all pages for faster searching.

## Templating with Dataview

If you use Obsidian's Dataview plugin, you can query your wiki:

```
table date, tags
from "wiki"
where tags contains "pasta"
sort date descending
```

Tell the AI to add Dataview-compatible YAML frontmatter:

```
---
date: 2026-05-09
tags: [pasta, italian, cooking]
sources: [pasta-types.md, cookingBook.md]
---
```

## Version Control

Your wiki is a git repo. Commit after each major operation:

```bash
# After an ingest
git add -A
git commit -m "ingest: added article about pasta preservation"

# After a synthesis
git commit -m "synthesis: created page combining pasta + web dev"

# After linting
git commit -m "lint: fixed broken links and resolved contradictions"
```

Over time, you have a full history of your wiki's evolution.

## Sharing Your Wiki

Your wiki is just markdown + yaml. Easy to share:

### Share the whole vault

```bash
git push origin main
# Others can clone and open in Obsidian
```

### Share specific pages

Export pages to PDF or HTML:
- Obsidian → Export as PDF
- Or use a markdown-to-HTML tool

### Embed in a website

Host your wiki on GitHub Pages, Obsidian Publish, or any static site host.

## Scaling Beyond Personal

If your wiki grows beyond ~100 sources and you want more advanced features, consider:

- **Full-text search** — Use `tools/search.py` or build a search API
- **Semantic search** — Embed pages, search by meaning not just keywords
- **Change tracking** — Git history gives you version control
- **Collaborative editing** — Use a shared git repo or Obsidian Sync
- **Web interface** — Expose your wiki as a searchable website

But at personal scale, plain markdown + git + Obsidian is ideal.

## Troubleshooting

### "The AI didn't link related concepts"

Tell the AI: > "I notice you didn't link X to Y. They're related. Please add that link."

The AI will update the pages immediately.

### "I have conflicting information in two pages"

Ask: > "Please find all contradictions in the wiki and tell me about them."

The AI will scan and report.

### "My wiki is getting messy"

Run a lint pass: > "Please lint the wiki and suggest a cleanup plan."

### "I want to change how pages are formatted"

Edit `.schema.md` to reflect the new format, then ask: > "I updated the schema. Please reformat existing pages to match the new style."

---

For more, see [SCHEMA.md](../SCHEMA.md) or reach out.
