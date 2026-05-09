# Obsidian Integration Guide

This guide shows how to use WI-system with Obsidian for a seamless wiki visualization and editing experience.

## Why Obsidian + WI-system?

- **Visual graph**: See knowledge connections and relationships
- **Backlink navigation**: Jump between related pages instantly
- **Local-first**: All data stays on your machine
- **Beautiful UI**: Obsidian's interface makes wiki browsing delightful
- **Bi-directional syncing**: Edit pages and push changes back to the wiki

## Setup (5 minutes)

### 1. Create WI-system workspace

```bash
mkdir my-project-wiki
cd my-project-wiki
wi init --root .
```

You now have:
```
my-project-wiki/
├── sources/     ← Raw docs go here
├── wiki/        ← Generated pages
├── index.md     ← Navigation
└── log.md       ← Operation history
```

### 2. Open in Obsidian

1. Open Obsidian
2. Click "Open folder as vault"
3. Select your `my-project-wiki` folder
4. Obsidian creates `.obsidian/` folder for settings

### 3. Configure Obsidian for WI-system

In Obsidian settings:

**File & Links:**
- Set "New note location" → `wiki/`
- Enable "Use [[wikilinks]]"

**Display:**
- Show "Graph view" in sidebar
- Enable "Show outline"

**Excluded files:**
```
sources/
log.md
.obsidian/
```

## Workflow

### Phase 1: Capture
1. Use **Obsidian Web Clipper** or **Save to Sources** to capture content
2. Save articles/docs to `sources/` folder as markdown

```
sources/
├── 2026-05-03-architecture-notes.md
├── 2026-05-03-api-design.md
└── 2026-05-04-incident-postmortem.md
```

### Phase 2: Ingest

Run ingest to merge sources into the wiki:

```bash
wi ingest --root . sources/architecture-notes.md
```

WI-system automatically:
- Extracts key topics
- Creates/updates wiki pages
- Builds links between pages
- Flags contradictions
- Updates `index.md`

### Phase 3: Explore (in Obsidian)

Now in Obsidian, you see:

1. **Graph View** — Visual map of connections
   - Nodes = wiki pages
   - Lines = cross-references
   - Colors = page types/tags

2. **Backlinks** — See what links to this page
   - Know impact of changes
   - Discover related concepts

3. **Outline** — Navigate page structure
   - Jump to sections
   - See page hierarchy

### Phase 4: Query & Synthesize

Ask WI-system questions about the wiki:

```bash
wi query --root . "What are our architectural principles?"
wi query --root . "What changed in Q2?" --store
```

The `--store` flag saves answers as new synthesis pages in `wiki/`.

These appear in Obsidian as new nodes in the graph.

### Phase 5: Maintain

Weekly maintenance:

```bash
wi lint --root . --fix
```

This:
- Detects broken links
- Finds orphan pages (unlinked)
- Flags contradictions
- Suggests fixes

Check `log.md` for all operations.

## Practical Example

### Step-by-step: Team Architecture Wiki

**1. Setup**
```bash
mkdir tech-wiki
cd tech-wiki
wi init --root .
```

**2. Capture knowledge**
Save to `sources/`:
- `api-design-v2.md` — New API design document
- `microservices-architecture.md` — System architecture
- `deployment-checklist.md` — Deployment procedures

**3. Ingest into wiki**
```bash
wi ingest --root . sources/api-design-v2.md
wi ingest --root . sources/microservices-architecture.md
wi ingest --root . sources/deployment-checklist.md
```

**4. Open in Obsidian**
```bash
# In Obsidian: File → Open folder → select tech-wiki
```

**5. Explore the graph**
- Click on "API Design" node
- See how it connects to "Deployment" and "Architecture"
- Click backlinks to see what depends on this design

**6. Query for insights**
```bash
wi query --root . "What are our service boundaries?"
wi query --root . "What's the deployment process?" --store
```

**7. Maintain weekly**
```bash
wi lint --root . --fix
```

## Graph View Tips

### Understanding the Graph

- **Large nodes** = highly connected pages (important concepts)
- **Isolated clusters** = separate knowledge domains
- **Hub nodes** = central concepts linking domains
- **Long chains** = sequence of related ideas

### Customizing Display

In Obsidian Graph Settings:
- **Node size**: Larger for more connections
- **Link distance**: Closer nodes are more related
- **Colors**: By tag, type, or link direction
- **Filter**: Hide certain node types

### Using Tags

Add to wiki pages for better organization:

```markdown
---
tags:
  - architecture
  - design
  - api-v2
---

# API Design v2
...
```

Then filter graph by tag to see only architecture pages.

## Real-world Uses

### Product Team
- Quarterly planning: Query past decisions and learnings
- Onboarding: New members explore the graph
- Architecture review: See how components connect

### Research Team
- Literature synthesis: Ingest papers, see connections
- Methodology tracking: Document experiments and results
- Finding gaps: Identify unlinked concepts

### Operations Team
- Runbook management: Searchable incident playbooks
- Change tracking: Query "What changed in deployment?"
- Auditing: Check log.md for all modifications

## Advanced: Templating

Create templates in `wiki/` for consistency:

**template-page.md**
```markdown
---
tags: [topic]
created: <% tp.date.now() %>
---

# Title

## Overview
[Summary]

## Key Points
- Point 1
- Point 2

## Related
[Links to related pages]
```

**template-decision.md**
```markdown
---
tags: [decision, status-active]
decided-date: 
decision-maker:
---

# Decision: [Title]

## Context
[Why this decision?]

## Options Considered
1. Option A
2. Option B

## Decision
[What we chose and why]

## Impact
[Results and consequences]

## Related Decisions
[Links to related decisions]
```

## Troubleshooting

### Graph not updating?
- Run `wi ingest` to regenerate links
- Check `index.md` for broken references
- Reload Obsidian (Cmd+R / Ctrl+R)

### Broken links in Obsidian?
- Run `wi lint --root . --fix` to repair
- Check that page names match exactly
- Remove broken references from contradictions

### Too many orphan pages?
- Run `wi query --root . "topic"` to find context
- Link them to relevant pages manually in Obsidian
- Or delete if truly unused

## Tips for Success

1. **Regular cadence** — Ingest weekly, lint monthly
2. **Clear naming** — Use descriptive page titles
3. **Tag everything** — Makes graph traversal easier
4. **Archive old sources** — Keep `sources/` tidy
5. **Review synthesis** — Verify LLM-generated answers
6. **Backup wiki** — Git commit regularly
7. **Share the graph** — Export for team viewing

## Next Steps

- [README.md](../README.md) — Full feature overview
- [START_HERE.md](../START_HERE.md) — Quick start
- [USE_CASES.md](USE_CASES.md) — Real examples
- [SECURITY.md](../SECURITY.md) — Keep it safe

---

**Your wiki is now visual, interconnected, and beautiful!** 📚✨
