# Getting Started

Set up your vault in under 5 minutes.

## What you need

1. **An AI agent** — Claude Code, Cursor, ChatGPT, Ollama, or similar. Does the actual work.
2. **Obsidian** (free) — [Download](https://obsidian.md). Visualizes the graph. Optional but recommended.

## Setup

```bash
git clone https://github.com/Jack5237/wi-system.git
cp -r wi-system/template my-wiki
cd my-wiki
```

`my-wiki/` contains:
- `AGENTS.md` — the entire contract, every agent reads it, nothing else to configure
- `sources/` — drop raw files here (articles, PDFs, chat exports, anything)
- `wiki/` — where your agent writes structured pages
- `.obsidian/graph.json` — pre-colored: green for `sources/`, blue for `wiki/`, grey for `AGENTS.md`/`log.md` — zero setup

**Open your agent:**

```bash
claude code .
# or open my-wiki/ in Cursor, VS Code + an agent, ChatGPT, Ollama — any agentic tool
```

**Open Obsidian:** launch it, "Open folder as vault," select `my-wiki/`.

Graph View shows the skeleton immediately — two small trees (`sources/` in green, `wiki/` in blue) hanging off their folder hubs, plus `AGENTS.md` and `log.md` linked in grey. No content nodes yet — that's correct. It fills in and starts connecting laterally (a source to the wiki page it fed, and both to `log.md`) once you ingest something.

## Optional: set up the web clipper

Install [Obsidian Web Clipper](https://obsidian.md/plugins?id=obsidian-web-clipper), then open its extension settings (puzzle-piece icon in your browser toolbar → Obsidian Web Clipper → the gear/settings icon).

The save folder isn't a general setting — it's set per **Template**. Go to **Templates** in the left sidebar, click into the **Default** template itself (not just the list — open the card), and under the **Location** section, set **Note location** to `sources/01-articles`. That's different from picking a vault in the clip popup, which doesn't persist the folder on its own.

If it still won't stick and keeps landing in a `Clippings/` folder or asking every time — don't fight it. The one thing that actually matters is that clips end up **somewhere inside `sources/`**, not at the vault root. Any subfolder, or even the root of `sources/` itself, works — ingest sorts it correctly regardless (`AGENTS.md`: dumping anywhere inside `sources/` is fine). A vault-root `Clippings/` folder is the one place to avoid, since ingest only scans inside `sources/`.

### Make clips connect to the hub instantly (optional)

By default, a fresh clip is just raw content — it won't show connected to `01-articles.md` on the graph until your agent ingests it (that's what actually writes the hub link into the file). If you want clips to show connected the moment they land, without waiting for ingest:

In the same **Default template** editor, scroll to the **Content** section and open **Note content** (not **Properties** — wikilinks in the frontmatter properties aren't reliably resolved into graph edges across Obsidian versions, but wikilinks in the note body always are). Add this line before whatever variable currently pulls in the page text (usually something like `{{content}}`):

```
Part of [[01-articles|Articles]].

```

Leave the existing variable content below it untouched. Every future clip using that template will include the hub link automatically, so it connects on the graph immediately. Ingest still matters for everything else — normalizing the frontmatter, extracting concepts into wiki pages, weaving it into `## Sources` sections — this only fixes the graph connection specifically.

This only covers clips made through the Web Clipper. Files added any other way (pasted manually, dragged in as PDFs, chat export text files) won't get the hub link until your agent ingests them, unless you also set up **Templater folder templates** (below) — the one Obsidian-native way to auto-insert a link based on folder alone for notes you create yourself. See TUTORIAL.md's "Less manual" section for a way to make ingest itself automatic, by having your agent process new sources on every session start instead of waiting to be told.

### Doing this for other source types

Web Clipper is fundamentally "save the page I'm browsing" — so everything it produces is web *text*, which lands in one of the two text folders. For the types that fit, create **additional templates** (not just Default), each with its own **Template triggers** (URL pattern), **Note location**, and hub line:

| Source type | Trigger URL pattern (example) | Note location | Note content prefix |
|---|---|---|---|
| AI conversations | `chatgpt.com`, `claude.ai`, `gemini.google.com` | `sources/02-conversations` | `Part of [[02-conversations\|Conversations]]` — also set the `brain` property (claude/gpt/gemini) per template |
| Video / talk pages | `youtube.com`, `vimeo.com` | `sources/02-conversations` | `Part of [[02-conversations\|Conversations]]` — clip the transcript/description; set `type: video` |
| Docs & articles | blog / doc-site domains you use often | `sources/01-articles` | `Part of [[01-articles\|Articles]]` |

Web Clipper auto-selects whichever template's trigger matches the page you're on, so clipping a YouTube page and clipping a blog post can land in the right folder with the right hub link automatically, with no manual folder-picking either way.

**Attachments don't fit the clipper pattern** — a PDF, image, audio, or video is a file you already have, not a webpage you're browsing, so there's nothing for Web Clipper to clip. Drag them into `sources/03-attachments/`. They then behave differently at ingest:

- **PDFs & images:** an actual `.pdf`/`.png`/`.jpg` is fine to drag straight into `sources/03-attachments/`. A capable AI agent reads the PDF text or views the image directly during ingest — you don't need to transcribe or caption it yourself first.
- **Audio & video:** the raw `.mp3`/`.mp4` can sit in `sources/03-attachments/` as a backing file, but most agents can't listen or watch during ingest, so it won't get processed on its own. Generate a **transcript** (a transcription tool, or an agent that supports audio/video input) and drop that text into `sources/02-conversations/` with `type: audio`/`type: video` — the transcript is the real source.

Either way, drag the file/text in and let ingest add the hub link — or just type the matching `Part of [[...]]` line yourself when you create the note, which takes two seconds and needs no template at all.

## Optional: auto-link notes you write yourself (Templater)

Everything above covers clips and AI ingest. But you'll also write notes by hand — a manual source, a wiki page you drafted yourself — and typing `Part of [[01-articles|Articles]]` every time gets old. Obsidian's own **Templates** core plugin can't help here: it only inserts on a manual command, never automatically based on which folder you're in. The **[Templater](https://obsidian.md/plugins?id=templater-obsidian)** community plugin can, via its **Folder Templates** feature — a new note created *inside Obsidian*, in a mapped folder, gets that folder's template content inserted automatically, no command, no typing.

The template folder `.templates/` already ships with the vault, pre-written for every folder where manually authoring markdown makes sense:

| Folder | Template |
|---|---|
| `sources/01-articles` | `.templates/01-articles.md` |
| `sources/02-conversations` | `.templates/02-conversations.md` |
| `wiki/pages` | `.templates/pages.md` |
| `wiki/entities` | `.templates/entities.md` |
| `wiki/projects` | `.templates/projects.md` |

(`sources/03-attachments` has no template — it holds native files like PDFs and images, not authored markdown. A manual note belongs in `01-articles` or `wiki/` instead.)

**Setup:**
1. Install Templater (Settings → Community plugins → Browse → search "Templater").
2. In Templater's settings, set **Template folder location** to `.templates`.
3. Turn on **Trigger Templater on new file creation**.
4. Under **Folder Templates**, add the five folder→template mappings from the table above.

Now right-click any of those five folders → **New note** (or use the folder's "new note" hotkey), and the note opens pre-filled with correct frontmatter and its `Part of [[...]]` hub link already in place — connected on the graph the instant it's created, no AI involved. `.templates/` itself is excluded from Graph View (pre-configured in `graph.json`), so the template files never show up as stray nodes.

This only fires for notes created *inside* Obsidian. A file dragged in from your file manager, or pasted from outside, still needs either a manual `Part of [[...]]` line or an AI ingest pass to get connected — Templater can't run against files that arrive already-populated from outside Obsidian.

You're set up. For how to actually use it — the prompts you'll type day to day — see **[TUTORIAL.md](TUTORIAL.md)**.
