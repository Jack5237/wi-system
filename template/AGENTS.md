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
sources/                    ← Raw Data Layer (immutable), organized by TYPE only
├── sources.md              ← hub — links down to each type folder's hub
├── Media/               ← images, videos, audio files (native media)
│   └── Media.md         ← hub — every media file in this folder links up here
├── Articles/            ← web clips, PDFs, text notes, personal writings
│   └── Articles.md
└── Transcripts/         ← conversations, chat logs, meeting notes, dialogue transcripts
    └── Transcripts.md

wiki/                       ← Structured Data Layer (AI-maintained), organized by SUBJECT only
├── wiki.md                 ← curated top-level navigation hub
├── Records/             ← consolidated topics, pages, permanent knowledge base
│   └── Records.md       ← hub — every record page links up here
├── Individuals/         ← people, companies, organizations, entities
│   └── Individuals.md
└── Execution/           ← active projects, tasks, roadmaps, execution
    └── Execution.md

AGENTS.md                   ← this file
log.md                      ← append-only operation history — also a graph node, linked to every file it records
```

**MAT** = **M**edia · **A**rticles · **T**ranscripts (raw input)
**RIX** = **R**ecords · **I**ndividuals · e**X**ecution (consolidated knowledge)

Three source folders, three wiki folders — that's the whole shape. Never mix the two organizing principles: `sources/` sorts by *what kind of raw file this is*. `wiki/` sorts by *what the page is about*. Don't create `wiki/conversations/` or `wiki/media/` — that's a source-type concern, not a subject concern. The two layers connect through the `## Sources` section on each wiki page, not through mirrored folders. `log.md` is a third connective layer, cutting across both: every operation recorded there links to the exact files — sources and wiki pages alike — it touched.

## Hub Pages and the Graph Hierarchy

Every subfolder — every `sources/` type and every `wiki/` subject — has a hub note named after the folder itself (`Media/Media.md`, `wiki/Records/Records.md`, etc.), not `index.md`. This matters for the graph: Obsidian labels every node with its filename, so if every hub were called `index.md`, the graph would show identical "index" labels with no way to tell them apart. Naming each hub after its folder means the graph node for the media hub actually says "Media."

Because every hub name is now unique across the whole vault, **all links use the same bare `[[filename]]` style** — hub links and per-source citations alike, no special-casing:
- A media file links up to its folder hub: `Part of [[Media|Media]]`
- A folder hub links up to its root: `Part of [[sources|Sources]]` or `Part of [[wiki|Wiki]]`
- A wiki page cites the sources that fed it: `[[2026-06-28-react-flow-review]]` in its `## Sources` section

This gives a visible hierarchy in Graph View: individual source → type hub → sources root, and individual wiki page → subject hub → wiki root, with the `## Sources` citations cutting laterally across the two trees connecting a specific source to the specific page it fed.

**The hub link is non-optional, on both sides.** When ingesting a new source, link it up to its folder's hub. When creating a new wiki page, link it up to its subject hub — `Part of [[Records|Records]]` on a new record page, same as a source gets `Part of [[Articles|Articles]]`. This is the single line that draws the wiki → record edge in the graph. Skip it and the page still connects *down* to the sources it cites (via `## Sources`) but floats free of the wiki tree — a node hanging off two sources with no path back to records. That disconnected-looking node is the #1 graph defect, and it's always a missing hub link. Treat this line with exactly the same weight as the `## Sources` weave: a page isn't finished until both exist. Neither hub file itself needs editing when a child links up to it — Obsidian's backlinks make the connection visible from both directions automatically.

Three source folders, three wiki folders — that's the cap. Anything that doesn't fit a source type goes in `Media/` (if it's a file) or `Articles/` (if it's text). Don't invent new type folders per edge case. Wiki subject folders (`Records/`, `Individuals/`, `Execution/`) are fixed too — don't add new top-level wiki folders until at least 10+ pages genuinely demand a new category.

**Dumping is allowed anywhere in `sources/`.** A file landing in the wrong subfolder, or in the root of `sources/`, is fine — part of ingest is the AI moving it to the right place. Classification is the AI's job, not the user's. This only covers `sources/` itself — a file sitting at the vault root won't be picked up by "ingest new sources," since that scans inside `sources/` only. Move it in first.

## Source Files

Once ingested, every source file is normalized:

**Name:** `YYYY-MM-DD-short-slug.md`

**Frontmatter:**
```yaml
---
type: article        # article | transcript | video | audio | image | document
resource: https://example.com/react-flow-review
captured: 2026-06-28
ingested: true
---

Part of [[Articles|Articles]].
```

The `Part of [[...]]` line goes right after the frontmatter, before the original article content — that's the hub link that puts this source in the graph hierarchy.

For files in `Transcripts/`, add which brain produced it:
```yaml
---
type: transcript
brain: claude         # claude | gpt | gemini | human
captured: 2026-06-28
ingested: true
---
```
This makes provenance visible — if two brains disagree on a topic, the wiki page's `## Open Questions` can attribute each claim to its source rather than silently picking one.

`ingested: false` (or missing frontmatter entirely) marks a raw file as queued for processing. This one flag is the entire queue system — no inbox folder needed.

After ingest, source files are **immutable**. Never edit them. They're the ground truth the wiki compresses from.

## Frontmatter Reference

**Source files** (`sources/`):

| Field | Required | Values / notes |
|---|---|---|
| `type` | yes | `article` · `transcript` · `video` · `audio` · `image` · `document` |
| `captured` | yes | `YYYY-MM-DD` the source was created/clipped |
| `ingested` | yes | `true` once processed; `false` (or absent) = queued |
| `resource` | when web-origin | source URL |
| `brain` | `transcript` only | `claude` · `gpt` · `gemini` · `human` |

**Type → folder:** `article`/`transcript` → `Articles` or `Transcripts` (transcript is dialogue, article is text); `video`/`audio` (transcript only; raw files → `Media`) → `Transcripts`; `image`/`document` (can be native files) → `Media`.

**Wiki pages** (`wiki/`):

| Field | Required | Values / notes |
|---|---|---|
| `type` | yes | `record` · `individual` · `project` |
| `updated` | yes | `YYYY-MM-DD` last edited |

**Type → folder:** `record` → `Records`; `individual` → `Individuals`; `project` → `Execution`.

**Hub notes** carry only `type: hub`.

## Core Workflow: Ingest

When told to ingest (or when you find unprocessed sources), for each unprocessed file:

1. **Read** the file.
2. **Classify** — determine type, rename to convention, move to the correct `sources/` subfolder, add frontmatter (including `brain:` if it's a transcript).
3. **Link the source to its folder hub** — add `Part of [[Articles|Articles]]` (or whichever subfolder it landed in) right after the frontmatter. This is what puts the source into the graph hierarchy under its type.
4. **Extract** — main topics, entities, projects, ideas.
5. **Search the wiki first.** Never assume a page doesn't exist — check `wiki/Records/`, `wiki/Individuals/`, `wiki/Execution/` before creating anything.
6. **Update existing pages before creating new ones.** Creating a new page is the fallback, not the default.
7. **Quality Gate: No Stubs** — Only create a new page if it has ≥3 substantive key points OR a meaningful relationship to existing pages.
8. **Quality Gate: No Slop** — Extract *insights*, don't transcribe. Max 150 words per summary section. Every claim traces to a source.
9. **Weave** — add the source as a `[[wikilink]]` (filename, no extension) to every touched page's `## Sources` section — not a backtick-quoted path, which renders as inert code and creates no graph edge. This is the mapping mechanism between raw data and structured knowledge.
10. **Link every new wiki page to its subject hub — mandatory, same weight as step 9.** A new `wiki/Records/react-flow.md` page gets `Part of [[Records|Records]]` under its frontmatter, same pattern a source gets `Part of [[Articles|Articles]]`. This one line draws the wiki → record edge; omit it and the page floats free of the wiki tree. A new page isn't done until this line exists. Pages that already exist and are just being updated don't need this re-added.
11. **Flag contradictions** in the page's `## Open Questions` section instead of silently overwriting a claim.
12. **Add cross-references** — link only when conceptually relevant (`[[Other Page]]`). Not every mention needs a link.
13. **Update `wiki/RIX_WIKI.md`** — curated, not auto-appended. Add genuinely new record/individual/project pages.
14. **Mark** the source `ingested: true`.
15. **Append to `log.md` — with real wikilinks, not prose.** Every source ingested and every wiki page touched gets `[[linked]]` in the entry (see the "Log Format" section below). This is the same weight as steps 9 and 10: the entry isn't done until it links out to every file the operation touched, source and wiki page alike.
16. **Commit.**

Per-source summary pages are **not created by default** — only for long, dense, or heavily-referenced sources where a standalone summary adds value beyond what the record pages already capture.

## Core Workflow: Synthesis

When you ask a question:

1. **Search `wiki/` first** — records, individuals, projects.
2. **Follow `## Sources` links** down into the raw files when you need detail the wiki compressed away.
3. **Answer in this priority order: wiki knowledge first, raw sources second, general model knowledge last and clearly labelled as such.**
4. **Cite** — link to the wiki pages and source files you used.
5. If the answer is valuable for future reference, **save it** as a new page in `wiki/Records/` marked `type: record`.
6. **Log it** — append to `log.md` with a `[[wikilink]]` to the new record page and to every page/source it drew from.

Because records are saved as pages, questions compound too — they become nodes in the graph, not lost chat messages.

## Core Workflow: Lint

When you say "please lint the wiki":

1. **Un-ingested files** — anything in `sources/` with `ingested: false` or missing frontmatter → ingest it.
2. **Contradictions** — do any pages claim conflicting facts? (Check `## Open Questions` first.)
3. **Orphans** — pages with no inbound links → link or merge. A page linked only to its folder hub and nothing else still counts as an orphan in spirit — it's in the hierarchy but disconnected from the actual weave.
4. **Duplicates** — two pages about the same thing → merge.
5. **Dead source links** — `## Sources` entries pointing at renamed/moved files, or `Part of [[...]]` hub links pointing at the wrong folder → fix.
6. **Unlinked concepts** — mentioned but lacking their own page.
7. **Missing hub links** — any source or wiki page missing its `Part of [[...]]` line → add it. Pay special attention to wiki pages that have a `## Sources` section but no `Part of [[...]]` line: those are the nodes that show in the graph connected to their sources but disconnected from their subject hub. Every wiki page must link up to `Records`, `Individuals`, or `Execution`.
8. **Unlinked log entries** — scan `log.md` for entries that describe a file in prose instead of `[[linking]]` it (e.g. "ingested a conversation about X" with no wikilink). Rewrite the entry to link the actual file. This is the same defect class as a missing hub link, just on the fourth tree.
9. **`wiki/RIX_WIKI.md` out of date** → refresh (curated, never auto-append everything).
10. **Report findings** and offer fixes.

Commit after every ingest and lint pass. Git history is the wiki's memory.

## Wiki Page Format

```markdown
---
type: record           # record | individual | project
updated: 2026-07-02
---

Part of [[Records|Records]].   ← mandatory: this is the page's edge to its subject hub

# Page Title

## Summary
One-paragraph overview.

## Key Points
- Bullet point 1
- Bullet point 2

## Notes
Refined synthesis and context beyond the bullet points.

## Open Questions
- Unresolved gaps or contradictions across sources.

## Related
- [[Other Page]]
- [[Concept]]

## Sources
- [[2026-06-28-react-flow-review]]
- [[2026-06-30-claude-session]]
```

**Sources entries must be `[[wikilinks]]` to the filename (no extension, no path), not backtick-quoted plain text.** Obsidian only draws a graph edge for an actual link — a backtick-quoted path renders as inline code and creates no connection. Filenames are unique (`YYYY-MM-DD-slug.md`), so a bare `[[filename]]` wikilink resolves correctly regardless of which `sources/` subfolder it's actually in — no relative path math required.

Manual pages (pure thinking, no ingest event) are allowed — they just skip `## Sources`. Still add the `Part of [[...]]` hub link so the page shows up in the graph hierarchy like everything else.

## Log Format

`log.md` is append-only, but every entry must be built the same way: header line, then a bullet per file touched, each one a real `[[wikilink]]` — never a plain-text description of what happened.

```markdown
## [2026-07-03] ingest | Ingested 2 sources

- [[2026-07-03-react-flow-review]] → new page [[react-flow]]
- [[2026-07-03-claude-auth-session]] → updated [[better-auth]]

## [2026-07-03] synthesis | Saved answer

- [[pasta-ecommerce-with-svelte]] ← drew from [[pasta]], [[svelte]], [[2026-06-28-svelte-docs]]
```

Every entry names, as a wikilink: the source file(s) it processed, and the wiki page(s) it created or updated. This applies uniformly across source types — a transcript, an article, a note, a doc, a video file, an image — none get a free pass into prose-only logging. This is what makes `log.md` a real graph node connected to everything the vault has ever touched, instead of a text file the graph can't see into.

**Bad (no edges drawn):**
```markdown
## [2026-07-03] ingest | Ingested a video about React Flow and updated the topic page
```
This describes the operation but links nothing — Obsidian draws zero edges from this entry.

## Linking Rules

- Link to related concepts: `[[Concept Name]]`
- Link to sources by `[[filename]]` wikilink, never a backtick-quoted path — backticks render as inert code and create no graph edge
- Link to folder hubs the same way: `[[Media|Media]]`, `[[Records|Records]]`, `[[sources|Sources]]`, `[[wiki|Wiki]]` — every hub is named after its folder, so hub names are unique across the vault and resolve with a plain bare wikilink like everything else
- Create a page for any concept you mention more than once
- Update backlinks when creating new pages
- **Log every operation with real links, not descriptions** — see "Log Format" above

## Rules for This Vault

- **Sources are immutable** — Never edit files in `sources/`. Read-only after ingest. Period.
- **Wiki is AI-owned** — You curate sources, I maintain wiki structure and quality.
- **Log is append-only, and every entry is linked** — Every operation gets a record, and that record `[[wikilinks]]` every file it touched. Prose-only entries are incomplete.
- **`wiki/` is always markdown** — no binary formats there, ever. `sources/` can hold a source's native format *if the AI agent can actually process it*. Native files all live in `Media/`:
  - **Native format is fine:** PDFs and image files in `Media/` — a capable agent can read PDF text or view an image directly during ingest, straight from the media folder.
  - **Text only:** video and audio can't be processed directly. Put the **transcript in `Transcripts/`** with `type: video` or `type: audio`; the raw media file, if you keep it, goes in `Media/`. The transcript is the real source; the raw file is just a backing attachment.
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

### Good Weaving (multiple brains, one page)
```
## Sources
- [[2026-06-28-react-flow-review]]
- [[2026-06-29-chatgpt-flow-comparison]]
- [[2026-06-30-xyflow-talk]]
```
Three different brains and formats, one record page — this is the weave, not three separate pages.

---

## Automation (optional, layered)

You don't need any of this to start — Level 1 alone is a complete workflow.

1. **Manual (default)** — drop files in `sources/`, say "ingest" (or "synthesize: <question>", "lint the wiki"). Works with any AI agent, zero setup.
2. **Shortcuts (agent-specific, optional)** — if your AI agent supports custom commands or hooks (e.g. Claude Code's slash commands and hooks), you can wire "ingest" / "synthesize" / "lint" to a shortcut so you don't retype the phrasing. This is a convenience layer on top of the rules in this file, not a requirement.
3. **Scheduled agent (later)** — if your AI tooling supports scheduled/cron runs, ingest can run on a cadence. Don't turn this on until the manual loop is proven — automating an unproven workflow just automates mess.

**Optional future layer (off by default):** publishing `wiki/` as a browsable site via a tool like Fumadocs. Not part of the core system — a toggleable extra for sharing the wiki outside Obsidian.

---

This is the contract between you and the AI. Modify it to fit your needs.
