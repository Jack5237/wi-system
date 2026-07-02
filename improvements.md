# WI System — Final Architecture

**The pitch: a woven intelligence system.** Your notes, Claude's conversations, ChatGPT exports, Gemini exports, articles, videos — every brain that's touched the problem — dump into one place and get woven into a single compounding graph. `sources/` is where every brain's raw output lands. `wiki/` is the one brain that reads all of them.

**One machine:** raw data lands in `sources/`, Claude classifies and refines it, knowledge compounds in `wiki/`. When a topic comes up — whether from a new source or a question you ask — the wiki page for that topic ties back to every raw dataset that informs it, regardless of which brain produced it.

```txt
raw data → sources/ (dump) → Claude classifies & ingests → wiki/ (compounds) → questions become pages
```

No inbox. No middle layer. `sources/` **is** the dump zone — Claude sorts it in place.

---

## Folder Structure

```txt
vault/
├── sources/
│   ├── 01-articles/         ← web clips, blog posts, docs
│   ├── 02-videos/           ← transcripts, talk notes
│   ├── 03-conversations/    ← Claude/GPT/Gemini exports, meeting notes — any brain's transcript
│   ├── 04-documents/        ← PDFs, specs, papers, books
│   ├── 05-images/           ← screenshots, diagrams
│   └── 06-audio/            ← podcast notes, voice memos
├── wiki/
│   ├── topics/              ← concepts, ideas, workflows
│   ├── entities/            ← people, tools, companies, products
│   ├── projects/            ← things you're building
│   ├── syntheses/           ← saved answers to your questions
│   └── index.md             ← curated entry point
├── AGENTS.md                ← the rules engine
└── .gitignore
```

Numbered folders give stable sort order everywhere (Obsidian, Finder, terminal, AI file listings). Six max — anything that doesn't fit goes in `04-documents/`. Never invent new type folders per edge case.

**Dumping is allowed anywhere in `sources/`.** Drop a file in the root of `sources/` or the wrong subfolder — doesn't matter. Part of ingest is Claude moving it to the right place. Classification is the AI's job, not yours.

---

## How Raw Data Gets In

No external infra (no cron, no bash daemons) — Claude Code already has the primitives for every level. Three levels, you only need Level 1 to start:

### Level 1 — Manual drop (works today, zero setup)

- **Web clipper:** set Obsidian Web Clipper's save folder to `sources/01-articles/`. Every clip lands as markdown automatically.
- **Chat exports, PDFs, transcripts:** drag them anywhere into `sources/`.
- Then say: **"ingest"**. Claude finds everything unprocessed and runs the pipeline.

### Level 2 — `.claude/` slash commands (recommended)

Ship the template with real Claude Code commands instead of a prose instruction buried in `AGENTS.md`:

```txt
template/
├── .claude/
│   ├── commands/
│   │   ├── ingest.md       ← runs the full ingest workflow below
│   │   ├── synthesize.md   ← runs the synthesis workflow, saves to wiki/syntheses/
│   │   └── lint.md         ← runs the maintenance checklist
│   └── settings.json       ← SessionStart hook (see below)
```

`/ingest`, `/synthesize`, `/lint` become first-class commands the moment someone copies the template — no setup, no memorizing phrasing.

**SessionStart hook** — every time the vault is opened in Claude Code, a hook silently checks `sources/` for anything with `ingested: false` and surfaces a one-line nudge: *"3 unprocessed sources — run /ingest?"* This replaces a file-watcher with something that fires exactly when a human is actually there to act on it.

### Level 3 — Scheduled agent (later, optional)

Claude Code supports scheduled cloud routines natively (the `/schedule` skill / cron-based agents) — no bash, no external server. A routine can run `/ingest` on a cadence (e.g. nightly) against the vault repo and commit the result.

Don't turn this on until the manual `/ingest` loop is proven. Automation of an unproven workflow just automates mess.

---

## Source Files

Once ingested, every source file is normalised:

**Name:** `YYYY-MM-DD-short-slug.md`

**Frontmatter:**

```md
---
type: article
url: https://example.com/react-flow-review
captured: 2026-06-28
ingested: true
---
```

`ingested: false` (or no frontmatter at all) = raw dump waiting for processing. This one flag is the entire queue system — no inbox folder needed.

After ingest, source files are **immutable**. They're the ground truth the wiki compresses from.

---

## The Ingest Workflow (what Claude does)

When told to ingest, for each unprocessed source:

1. **Read** the file.
2. **Classify** — determine type, rename to convention, move to the correct `sources/` subfolder, add frontmatter.
3. **Extract** — main topics, entities, projects, ideas.
4. **Search the wiki** for existing relevant pages. Never assume; always search.
5. **Update existing pages first.** Creating a new page is the fallback, not the default.
6. **Weave** — add the source's path to every touched page's `## Sources` section.
7. **Flag contradictions** in the page's `## Open Questions` instead of silently overwriting.
8. **Mark** `ingested: true`.
9. **Commit.**

---

## The Synthesis Workflow (the payoff)

You ask a question:

> "Claude, how do I create a website about pasta?"

Claude:

1. Searches `wiki/` for relevant pages (pasta, restaurants, web dev, Svelte, SEO — whatever exists).
2. Follows each page's `## Sources` links down into the raw files when it needs detail the wiki compressed away.
3. Writes the answer — **wiki knowledge first, raw sources second, general model knowledge last and clearly labelled.**
4. Saves it as `wiki/syntheses/pasta-website.md`, linked to every topic, entity, and source it drew from.

This is the tie-back you described: **whenever a topic arises, the page for it is wired to the exact datasets that inform it.** And because syntheses are saved as pages, your questions compound too — they become nodes in the graph, not lost chat messages.

---

## Wiki Page Format

```md
---
type: topic          # topic | entity | project | synthesis
updated: 2026-07-02
---

# React Flow

## Summary

One-paragraph explanation.

## Key Points

- 

## Notes

Refined synthesis and context.

## Open Questions

- Unresolved gaps or contradictions across sources.

## Related

- [[Another Topic]]

## Sources

- `sources/01-articles/2026-06-28-react-flow-review.md`
```

Manual pages (pure thinking, no ingest event) are allowed — they just skip `## Sources`.

---

## Obsidian Graph — Keep the Brain Viewer Clean

The graph should read as *the brain*, not a pile of raw dumps. Ship the template with an `.obsidian/graph.json`:

- **Filter `sources/` out of the default graph view.** Raw data isn't knowledge yet — it's ingredients. The graph should default to showing `wiki/` only, toggleable if someone wants to see the raw layer.
- **Color groups by folder**, so the shape of the brain is visible at a glance:
  - `wiki/topics/` → one color (the bulk of the graph — concepts and ideas)
  - `wiki/entities/` → a second color (people, tools, projects — the "who/what")
  - `wiki/syntheses/` → a third color (your compounding questions — these should visibly cluster as hubs pulling from multiple topics)
- **No orphan sprawl.** Because the lint pass merges/links orphan pages, the graph stays a connected web instead of a scatter of isolated dots.

This turns "open Graph View" from a novelty into an actual way to see what you know and how it connects — the point of calling this a woven intelligence system instead of a folder of markdown.

---

## Maintenance: Lint

Run periodically ("Claude, lint the wiki"):

- Files in `sources/` with `ingested: false` or missing frontmatter → ingest them.
- Wiki pages with no inbound links → link or merge.
- Two pages about the same thing → merge.
- `## Sources` entries pointing at renamed/moved files → fix.
- `index.md` out of date → refresh (curated, never auto-append everything).

Commit after every ingest and lint. Git history is the wiki's memory.

---

## What Stays Out (on purpose)

- ❌ No `_inbox/` — `sources/` is the dump zone; the `ingested` flag is the queue.
- ❌ No mirroring source-type folders inside `wiki/` — knowledge organises by subject.
- ❌ No per-source summary pages by default — only for long/dense/heavily-referenced sources.
- ❌ No folder bloat — new wiki folders only when 10+ pages demand it.
- ❌ No automation before the manual loop works.
- ❌ No external cron/bash daemons — automation stays inside Claude Code (hooks, slash commands, scheduled agents).
- ❌ No cluttered graph view — `sources/` stays out of the default Obsidian graph.

---

## Final Rules for `AGENTS.md`

**Structure**
- `sources/` is the raw dump zone; users may drop files anywhere in it.
- Claude classifies: rename to `YYYY-MM-DD-slug.md`, move to the correct numbered subfolder, add frontmatter.
- Source files are immutable after ingest.
- `wiki/` organises by subject only: `topics/`, `entities/`, `projects/`, `syntheses/`.

**Ingest**
- Anything with `ingested: false` or no frontmatter is queued for processing.
- Search for existing wiki pages before creating new ones; updating beats creating.
- Every touched page gets the source path in `## Sources`.
- Contradictions go in `## Open Questions`, never silently resolved.
- Mark `ingested: true` and commit when done.

**Synthesis**
- Answer questions from wiki first, raw sources second, general knowledge last (labelled).
- Save substantial answers to `wiki/syntheses/` with full linking.

**Maintenance**
- Lint regularly: un-ingested files, orphan pages, duplicates, dead source links, stale index.
- Keep `index.md` curated.
- Commit after each ingest and lint.

**Tooling (ships with the template)**
- `.claude/commands/ingest.md`, `synthesize.md`, `lint.md` — the three workflows as real slash commands, not prose someone has to remember.
- `.claude/settings.json` — SessionStart hook nudges when unprocessed sources exist.
- `.obsidian/graph.json` — `sources/` excluded from default graph view; `wiki/` subfolders color-grouped so the graph reads as a brain, not a dump.