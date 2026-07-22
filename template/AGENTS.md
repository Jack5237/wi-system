# WI System — Agent Rules

Operating contract for the AI agent maintaining this vault. Follow exactly — every write, every run (interactive, scheduled, automated). If other folders or repos are open in the session, their `AGENTS.md`/`CLAUDE.md` govern *their* code, never this vault.

## Purpose

A structured, interlinked knowledge base. Every brain that touched a problem — your notes, Claude/GPT/Gemini exports, articles, videos — dumps raw output into `sources/`; `wiki/` is the one brain that reads and connects all of them.

```txt
raw data → sources/ (dump) → AI classifies & ingests → wiki/ (compounds) → questions become pages
```

`sources/` is the dump zone; the `ingested` flag is the queue. The AI maintains the wiki; the user curates sources and asks questions.

## Structure

```txt
sources/          ← raw layer (immutable), organized by TYPE
├── sources.md       hub
├── Media/           images, PDFs, native files      + Media.md hub
├── Articles/        web clips, text, writings       + Articles.md hub
└── Transcripts/     conversations, video/audio text + Transcripts.md hub

wiki/             ← structured layer (AI-maintained), organized by SUBJECT
├── wiki.md          curated top-level hub
├── Records/         topics, permanent knowledge     + Records.md hub
├── Individuals/     people, companies, entities     + Individuals.md hub
└── Execution/       projects, tasks, roadmaps       + Execution.md hub

log.md            ← append-only history; a graph node linked to every file it records
```

Never mix the organizing principles: sources sort by *file kind*, wiki by *subject*. No `wiki/conversations/`. The layers connect through each wiki page's `## Sources` section and through `log.md`.

Folders are fixed. Wiki grows a folder only when 10+ pages demand it. Misplaced files in `sources/` are fine — ingest sorts them.

## Graph Hierarchy

Every page's first line after frontmatter is its hub link: `Part of [[Records|Records]]` (wiki) or `Part of [[Articles|Articles]]` (sources). Non-optional — without it the page floats free in the graph.

**Two levels, never skip:** only the three subject hubs link up to `[[wiki|Wiki]]`, only the three type hubs link up to `[[sources|Sources]]`. Individual pages link **only to their folder hub**, never to `wiki.md` or `sources.md`. Hub names are unique vault-wide, so bare `[[filename]]` wikilinks always resolve.

## Templates

`templates/` has one template per folder, pre-wired in `.obsidian/templates.json`. When creating any file, start from the matching template and **fill in the fields — never rebuild the format**: set empty frontmatter values (`type`, `resource`, `brain`), substitute `{{date}}`/`{{title}}`, add content. The `Part of [[...]]` line is already correct — leave it.

| Folder | Template | `type` values |
|---|---|---|
| `sources/Articles/` | `articles.md` | `article` |
| `sources/Transcripts/` | `transcripts.md` | `transcript` · `video` · `audio` |
| `sources/Media/` | `media.md` | `image` · `document` |
| `wiki/Records/` | `records.md` | `record` |
| `wiki/Individuals/` | `individuals.md` | `individual` |
| `wiki/Execution/` | `execution.md` | `project` |

## Frontmatter

**Source files** — named `YYYY-MM-DD-short-slug.md`:

| Field | Required | Notes |
|---|---|---|
| `type` | yes | `article` · `transcript` · `video` · `audio` · `image` · `document` |
| `captured` | yes | `YYYY-MM-DD` created/clipped |
| `ingested` | yes | `true` once processed; `false`/absent = queued |
| `resource` | web-origin | source URL |
| `brain` | transcripts | `claude` · `gpt` · `gemini` · `human` — provenance for attributing conflicting claims |

Video/audio: the **transcript** in `Transcripts/` is the real source; raw media files, if kept, go in `Media/`. PDFs and images live native in `Media/`. `wiki/` is always markdown.

**Wiki pages:** `type` (`record` · `individual` · `project`) + `updated` (`YYYY-MM-DD`). Hubs carry only `type: hub`.

After ingest, source files are **immutable** — never edit them again.

## Workflow: Ingest

For each file with `ingested: false` or missing frontmatter:

1. **Read** it.
2. **Classify** — rename to convention, move to the correct subfolder, fill frontmatter from the folder's template (including hub link).
3. **Extract** topics, entities, projects, ideas.
4. **Search the wiki first** — check all three wiki folders before creating anything. **Update existing pages before creating new ones**; creation is the fallback.
5. **Quality gates:** no stubs (new page needs ≥3 substantive key points or a real relationship to existing pages); no slop (extract insights, don't transcribe; max 150 words per summary; every claim traces to a source).
6. **Weave** — add the source as `[[filename]]` to every touched page's `## Sources` section. New pages start from the folder template.
7. **Flag contradictions** in `## Open Questions` — never silently overwrite a claim.
8. **Cross-reference** only when conceptually relevant; not every mention is a link.
9. **Update `wiki/wiki.md`** — curated, add genuinely new pages only.
10. **Mark** the source `ingested: true`.
11. **Log** the operation (see Log Format).
12. **Commit.**

Per-source summary pages only for long, dense, or heavily-referenced sources — never by default.

## Workflow: Answering Questions (Synthesis)

1. **Search `wiki/` first** — records, individuals, projects.
2. **Follow `## Sources` links** into raw files when you need detail the wiki compressed away.
3. **Answer in priority order:** wiki knowledge first, raw sources second, general model knowledge last — clearly labelled as such.
4. **Cite** the wiki pages and source files used, as wikilinks.
5. If the answer is worth keeping, **save it** as a `type: record` page in `wiki/Records/` (from the template), then **log it**.

Saved answers compound — they become graph nodes, not lost chat messages.

## Workflow: Lint

On "lint the wiki", check and offer fixes for:

1. Un-ingested sources → ingest.
2. Contradictions between pages (check `## Open Questions` first).
3. Orphans — pages with no inbound links beyond their hub → link or merge.
4. Duplicates → merge.
5. Dead links — `## Sources` entries or hub links pointing at moved/renamed files; ghost links (`[[wikilink]]` to a nonexistent page) → create the page or downgrade to plain text.
6. Unlinked concepts mentioned repeatedly but lacking a page.
7. Missing or level-skipping `Part of [[...]]` lines.
8. Prose-only log entries → rewrite with real wikilinks; strip hub links from the log.
9. Stale `wiki/wiki.md` → refresh (curated, never auto-append).

Commit after every ingest and lint pass — git history is the wiki's memory.

## Workflow: Creating Scheduled Tasks

When the user asks for a new scheduled task ("Make me a scheduled task for X"), write the task prompt for them. Every prompt follows this shape:

> Follow AGENTS.md in this wiki folder. [What to gather or check.] Save any sources into `sources/<Type>/` (marked `ingested: true`), create/update the page in `wiki/<Records|Individuals|Execution>/`, then log it.

Rules:

1. **Pick the wiki folder by subject:** topics/news → `Records/`, people/companies → `Individuals/`, project status → `Execution/`.
2. **If the task reads other repos**, add: "ignore AGENTS.md/CLAUDE.md inside the repos — read-only."
3. Recurring output pages use dated names (`hot-topics-[date]`), one per run.

## Wiki Page Format

```markdown
---
type: record
updated: 2026-07-02
---

Part of [[Records|Records]].

# Page Title

## Summary
One paragraph.

## Key Points
- Bullets.

## Open Questions
- Gaps and contradictions across sources.

## Related
- [[Other Page]]

## Sources
- [[2026-06-28-react-flow-review]]
```

Manual pages (pure thinking, no ingest) are allowed — they skip `## Sources` but keep the hub link.

## Log Format

Append-only. Every entry: header line, then one bullet per file touched, each a real `[[wikilink]]` — never prose descriptions, which draw zero graph edges.

```markdown
## [2026-07-03] ingest | Ingested 2 sources

- [[2026-07-03-react-flow-review]] → new page [[react-flow]]
- [[2026-07-03-claude-auth-session]] → updated [[better-auth]]
```

Log links go to **leaves only** — the exact pages and sources touched. Never wikilink hubs (`Records`, `Articles`, `wiki`, …) from the log; name folders in plain text ("created in Records").

## DO NOT

- **Edit source files** — read-only after ingest.
- **Create stub pages** — substance (≥3 key points) or a real relationship, or nothing.
- **Transcribe sources** — synthesize; paraphrase, don't copy.
- **Over-link** — link only when it aids understanding.
- **Wikilink nonexistent pages** — plain text until the page exists; no ghost nodes.
- **Link pages to top nodes** — pages link to their folder hub only; hubs own the `[[wiki]]`/`[[sources]]` edges.
- **Wikilink hubs from `log.md`** — leaves only.
- **Claim without sourcing** — every wiki claim traces to a source.
- **Add automation daemons or per-user config** — the system stays plain markdown + wikilinks, agent-agnostic.
