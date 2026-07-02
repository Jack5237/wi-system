# WI System — Agent Rules

This document tells AI agents how to operate this wiki. Follow these rules strictly.

Governs [[sources]] and [[wiki]].

## Purpose

Build a structured, interlinked knowledge base — a **woven intelligence system**. Your notes, Claude's conversations, ChatGPT exports, Gemini exports, articles, videos: every brain that's touched a problem dumps its raw output into `sources/`, and `wiki/` is the one brain that reads and connects all of them.

Works for **any workflow**:
- **Broad wikis:** General knowledge bases (e.g., "Jack's Brain" with diverse topics)
- **Narrow wikis:** Project-specific docs (e.g., "Gambling Site" focused on one project)

The system is domain-agnostic. Your clips define the scope.

The AI maintains this wiki; you curate sources and ask questions.

## Three Core Stages

Every workflow follows this cycle:

1. **Ingest** — Raw data (any brain's output, any format) lands in `sources/`. Manual, user-driven.
2. **Interact** — AI classifies, reads, and weaves it into `wiki/`. Agentic processing layer.
3. **Inspect** — You view, query, and use the wiki in Obsidian. Manual discovery and exploration.

```txt
raw data → sources/ (dump) → AI classifies & ingests → wiki/ (compounds) → questions become pages
```

No inbox. No middle layer. `sources/` **is** the dump zone — the AI sorts it in place.

This is a **manual personal RAG** — sources as context, AI as synthesizer, Obsidian as interface.

## Folder Structure

```txt
vault/
├── sources/                 ← Raw Data Layer (immutable), organized by TYPE only
│   ├── sources.md            ← hub — links down to each type folder's hub
│   ├── 01-articles/         ← web clips, blog posts, docs
│   │   └── 01-articles.md    ← hub — every article in this folder links up here
│   ├── 02-videos/           ← transcripts, talk notes
│   │   └── 02-videos.md
│   ├── 03-conversations/    ← Claude/GPT/Gemini exports, meeting notes — any brain's transcript
│   │   └── 03-conversations.md
│   ├── 04-documents/        ← PDFs, specs, papers, books
│   │   └── 04-documents.md
│   ├── 05-images/           ← screenshots, diagrams
│   │   └── 05-images.md
│   └── 06-audio/            ← podcast notes, voice memos
│       └── 06-audio.md
├── wiki/                    ← Structured Data Layer (AI-maintained), organized by SUBJECT only
│   ├── wiki.md               ← curated top-level navigation hub
│   ├── topics/               ← concepts, ideas, workflows
│   │   └── topics.md         ← hub — every topic page links up here
│   ├── entities/             ← people, tools, companies, products
│   │   └── entities.md
│   ├── projects/             ← things you're building
│   │   └── projects.md
│   └── syntheses/            ← saved answers to your questions
│       └── syntheses.md
├── AGENTS.md                ← this file
└── log.md                   ← append-only operation history
```

**Never mix the two organizing principles.** `sources/` sorts by *what kind of raw file this is*. `wiki/` sorts by *what the page is about*. Don't create `wiki/conversations/` or `wiki/videos/` — that's a source-type concern, not a subject concern. The two layers connect through the `## Sources` section on each wiki page, not through mirrored folders.

## Hub Pages and the Graph Hierarchy

Every subfolder — every `sources/` type and every `wiki/` subject — has a hub note named after the folder itself (`02-videos/02-videos.md`, `wiki/topics/topics.md`, etc.), not `index.md`. This matters for the graph: Obsidian labels every node with its filename, so if every hub were called `index.md`, the graph would show a dozen identical "index" labels with no way to tell them apart. Naming each hub after its folder means the graph node for the videos hub actually says "02-videos."

Because every hub name is now unique across the whole vault, **all links use the same bare `[[filename]]` style** — hub links and per-source citations alike, no special-casing:
- An article links up to its folder hub: `Part of [[01-articles|Articles]]`
- A folder hub links up to its root: `Part of [[sources|Sources]]` or `Part of [[wiki|Wiki]]`
- A wiki page cites the sources that fed it: `[[2026-06-28-react-flow-review]]` in its `## Sources` section

This gives a visible hierarchy in Graph View: individual source → type hub → sources root, and individual wiki page → subject hub → wiki root, with the `## Sources` citations cutting laterally across the two trees connecting a specific source to the specific page it fed.

When ingesting a new source, link it up to its folder's hub. When creating a new wiki page, link it up to its subject hub. Neither hub file itself needs editing when a child links up to it — Obsidian's backlinks make the connection visible from both directions automatically.

Six source folders max. Anything that doesn't fit goes in `04-documents/`. Don't invent new type folders per edge case. Wiki subject folders (`topics/`, `entities/`, `projects/`, `syntheses/`) are fixed too — don't add new top-level wiki folders until at least 10+ pages genuinely demand a new category.

**Dumping is allowed anywhere in `sources/`.** A file landing in the wrong subfolder, or in the root of `sources/`, is fine — part of ingest is the AI moving it to the right place. Classification is the AI's job, not the user's. This only covers `sources/` itself — a file sitting at the vault root (e.g. a `Clippings/` folder some tools create by default, outside `sources/` entirely) won't be picked up by "ingest new sources," since that scans inside `sources/` only. Move it in first.

## Source Files

Once ingested, every source file is normalized:

**Name:** `YYYY-MM-DD-short-slug.md`

**Frontmatter:**
```yaml
---
type: article        # article | video | conversation | document | image | audio
resource: https://example.com/react-flow-review
captured: 2026-06-28
ingested: true
---

Part of [[01-articles|Articles]].
```

The `Part of [[...]]` line goes right after the frontmatter, before the original article content — that's the hub link that puts this source in the graph hierarchy.

For files in `03-conversations/`, add which brain produced it:
```yaml
---
type: conversation
brain: claude         # claude | gpt | gemini | human
captured: 2026-06-28
ingested: true
---
```
This makes provenance visible — if two brains disagree on a topic, the wiki page's `## Open Questions` can attribute each claim to its source rather than silently picking one.

`ingested: false` (or missing frontmatter entirely) marks a raw file as queued for processing. This one flag is the entire queue system — no inbox folder needed.

After ingest, source files are **immutable**. Never edit them. They're the ground truth the wiki compresses from.

## Core Workflow: Ingest

When told to ingest (or when you find unprocessed sources), for each unprocessed file:

1. **Read** the file.
2. **Classify** — determine type, rename to convention, move to the correct `sources/` subfolder, add frontmatter (including `brain:` if it's a conversation).
3. **Link the source to its folder hub** — add `Part of [[01-articles|Articles]]` (or whichever subfolder it landed in) right after the frontmatter. This is what puts the source into the graph hierarchy under its type.
4. **Extract** — main topics, entities, projects, ideas.
5. **Search the wiki first.** Never assume a page doesn't exist — check `wiki/topics/`, `wiki/entities/`, `wiki/projects/` before creating anything.
6. **Update existing pages before creating new ones.** Creating a new page is the fallback, not the default.
7. **Quality Gate: No Stubs** — Only create a new page if it has ≥3 substantive key points OR a meaningful relationship to existing pages.
8. **Quality Gate: No Slop** — Extract *insights*, don't transcribe. Max 150 words per summary section. Every claim traces to a source.
9. **Weave** — add the source as a `[[wikilink]]` (filename, no extension) to every touched page's `## Sources` section — not a backtick-quoted path, which renders as inert code and creates no graph edge. This is the mapping mechanism between raw data and structured knowledge, and it's what makes the Obsidian graph actually show sources connected to the wiki pages they fed — a topic page can be fed by an article, a Claude conversation, and a video at once, and each is an explicit `[[link]]` in `## Sources`.
10. **Link every new wiki page to its subject hub** — a new `wiki/topics/react-flow.md` page gets `Part of [[topics|Topics]]` under its frontmatter, same pattern as sources. Pages that already exist and are just being updated don't need this re-added.
11. **Flag contradictions** in the page's `## Open Questions` section instead of silently overwriting a claim.
12. **Add cross-references** — link only when conceptually relevant (`[[Other Page]]`). Not every mention needs a link.
13. **Update `wiki/wiki.md`** — curated, not auto-appended. Add genuinely new topic/entity/project pages.
14. **Mark** the source `ingested: true`.
15. **Append to `log.md`** — record what was ingested and what changed.
16. **Commit.**

Per-source summary pages are **not created by default** — only for long, dense, or heavily-referenced sources where a standalone summary adds value beyond what the topic pages already capture.

## Core Workflow: Synthesis

When you ask a question:

1. **Search `wiki/` first** — topics, entities, projects, existing syntheses.
2. **Follow `## Sources` links** down into the raw files when you need detail the wiki compressed away.
3. **Answer in this priority order: wiki knowledge first, raw sources second, general model knowledge last and clearly labelled as such.**
4. **Cite** — link to the wiki pages and source files you used.
5. If the answer is valuable for future reference, **save it** as a new page in `wiki/syntheses/`, linked to every topic, entity, and source it drew from.

Because syntheses are saved as pages, questions compound too — they become nodes in the graph, not lost chat messages.

## Core Workflow: Lint

When you say "please lint the wiki":

1. **Un-ingested files** — anything in `sources/` with `ingested: false` or missing frontmatter → ingest it.
2. **Contradictions** — do any pages claim conflicting facts? (Check `## Open Questions` first.)
3. **Orphans** — pages with no inbound links → link or merge. A page linked only to its folder hub and nothing else still counts as an orphan in spirit — it's in the hierarchy but disconnected from the actual weave.
4. **Duplicates** — two pages about the same thing → merge.
5. **Dead source links** — `## Sources` entries pointing at renamed/moved files, or `Part of [[...]]` hub links pointing at the wrong folder → fix.
6. **Unlinked concepts** — mentioned but lacking their own page.
7. **Missing hub links** — any source or wiki page missing its `Part of [[...]]` line → add it.
8. **`wiki/wiki.md` out of date** → refresh (curated, never auto-append everything).
9. **Report findings** and offer fixes.

Commit after every ingest and lint pass. Git history is the wiki's memory.

## Wiki Page Format

```markdown
---
type: topic           # topic | entity | project | synthesis
updated: 2026-07-02
---

Part of [[topics|Topics]].

# Page Title

## Summary
One-paragraph overview.

## Key Points
- Bullet point 1
- Bullet point 2

## Notes
Refined synthesis and context beyond the bullet points.

## Open Questions
- Unresolved gaps or contradictions across sources (attribute to `brain:` when relevant).

## Related
- [[Other Page]]
- [[Concept]]

## Sources
- [[2026-06-28-react-flow-review]]
- [[2026-06-30-claude-session]]
```

**Sources entries must be `[[wikilinks]]` to the filename (no extension, no path), not backtick-quoted plain text.** Obsidian only draws a graph edge for an actual link — a backtick-quoted path renders as inline code and creates no connection. This is the difference between the graph showing the weave and the graph showing two piles of unconnected dots. Filenames are unique (`YYYY-MM-DD-slug.md`), so a bare `[[filename]]` wikilink resolves correctly regardless of which `sources/` subfolder it's actually in — no relative path math required.

Manual pages (pure thinking, no ingest event) are allowed — they just skip `## Sources`. Still add the `Part of [[...]]` hub link so the page shows up in the graph hierarchy like everything else.

## Linking Rules

- Link to related concepts: `[[Concept Name]]`
- Link to sources by `[[filename]]` wikilink, never a backtick-quoted path — backticks render as inert code and create no graph edge
- Link to folder hubs the same way: `[[01-articles|Articles]]`, `[[topics|Topics]]`, `[[sources|Sources]]`, `[[wiki|Wiki]]` — every hub is named after its folder, so hub names are unique across the vault and resolve with a plain bare wikilink like everything else
- Create a page for any concept you mention more than once
- Update backlinks when creating new pages

## Rules for This Vault

- **Sources are immutable** — Never edit files in `sources/`. Read-only after ingest. Period.
- **Wiki is AI-owned** — You curate sources, I maintain wiki structure and quality.
- **Log is append-only** — Every operation gets a record.
- **All markdown** — No binary formats.
- **Git-friendly** — Commit after each ingest/lint pass.

## What Stays Out (on purpose)

- **No `_inbox/`** — `sources/` is the dump zone; the `ingested` flag is the queue.
- **No mirroring source-type folders inside `wiki/`** — knowledge organizes by subject, never by where it came from.
- **No per-source summary pages by default** — only for long/dense/heavily-referenced sources.
- **No folder bloat** — new wiki folders only when 10+ pages genuinely demand it.
- **No external cron/bash daemons** — automation stays inside the AI agent's own primitives (slash commands, hooks, scheduled agents), never external infrastructure.
- **No manual graph setup** — every `sources/` and `wiki/` subfolder is already color-grouped in `.obsidian/graph.json`; the user should never need to configure colors or filters themselves.

## DO NOT

- **Do not edit source files** — `sources/` is read-only. Extract and synthesize, never modify.
- **Do not create stub pages** — Pages need substance (≥3 key points) or meaningful relationships.
- **Do not over-link** — Link only when it helps understanding. Not every mention is a link.
- **Do not transcribe sources** — Extract insights, synthesize knowledge. Paraphrase, don't copy.
- **Do not mix raw and structured** — Keep `sources/` (by type) separate from `wiki/` (by subject).
- **Do not cite without sourcing** — Every claim in wiki pages must trace back to a source.

---

## Examples

### Good Summary (Concise, Insightful)
```
## Summary
React Flow is a node-based editor library for React with built-in dragging, zooming, and multi-selection. MIT-licensed, 7.4M weekly installs, used by Stripe and Typeform for workflow builders and data visualization.
```

### Bad Summary (Rambling, Transcribes)
```
## Summary
This article is all about React Flow, which is a library for React. It talks about how you can use it to build things. It has features for dragging nodes around on a canvas. You can also zoom in and out. It supports selecting multiple nodes at once...
```

### Good Linking (Selective)
```
## Related
- [[Node-Based UI]] (React Flow is an implementation of this pattern)
- [[xyflow]] (the company behind React Flow)
```

### Bad Linking (Over-linked)
```
## Related
- [[React]] (mentioned in title)
- [[JavaScript]] (implied by React)
- [[Canvas]] (used by node editors)
- [[MIT License]] (the license)
- [[npm]] (how you install it)
```

### Good Weaving (multiple brains, one page)
```
## Sources
- [[2026-06-28-react-flow-review]]
- [[2026-06-29-chatgpt-flow-comparison]]
- [[2026-06-30-xyflow-talk]]
```
Three different brains and formats, one topic page — this is the weave, not three separate pages.

### Good Page Decision
- Create a page for "React Flow" — has 5+ distinct concepts (library, use cases, features, ecosystem)
- Do NOT create a page for "MIT License" — single mention, not substantive enough

---

## Automation (optional, layered)

You don't need any of this to start — Level 1 alone is a complete workflow.

1. **Manual (default)** — drop files in `sources/`, say "ingest" (or "synthesize: <question>", "lint the wiki"). Works with any AI agent, zero setup.
2. **Shortcuts (agent-specific, optional)** — if your AI agent supports custom commands or hooks (e.g. Claude Code's slash commands and hooks), you can wire "ingest" / "synthesize" / "lint" to a shortcut so you don't retype the phrasing. This is a convenience layer on top of the rules in this file, not a requirement.
3. **Scheduled agent (later)** — if your AI tooling supports scheduled/cron runs, ingest can run on a cadence. Don't turn this on until the manual loop is proven — automating an unproven workflow just automates mess.

**Optional future layer (off by default):** publishing `wiki/` as a browsable site via a tool like Fumadocs. Not part of the core system — a toggleable extra for sharing the wiki outside Obsidian.

---

This is the contract between you and the AI. Modify it to fit your needs.
