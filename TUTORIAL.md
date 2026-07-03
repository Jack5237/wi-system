# Tutorial: Using Your Wiki

Setup done? See [GETTING_STARTED.md](GETTING_STARTED.md) if not. This is what you actually say to your agent, day to day — plain language, no slash commands.

## Prompt library

**Ingesting**
| Want | Say |
|---|---|
| Process everything new | "Ingest new sources" |
| Process one file | "Ingest sources/01-articles/that-file.md" |
| Check what's pending | "What sources are unprocessed?" |

**Asking questions**
| Want | Say |
|---|---|
| General question | "What do I know about X?" |
| Combine topics | "How would I combine X with Y?" |
| Save the answer | "Synthesize this and save it: <question>" |
| Find gaps/conflicts | "What are the open questions?" / "Where do sources disagree on X?" |

**Maintenance**
| Want | Say |
|---|---|
| Full health check | "Lint the wiki" |
| Fix a fact | "Page X says Y, but that's outdated — update it" |
| Merge duplicates | "Merge wiki/pages/a.md and b.md — same thing" |

**By source type**
| Want | Say |
|---|---|
| Only AI chat exports | "What have I learned from conversations in sources/02-conversations/?" |
| Attribute disagreement | "Claude and GPT disagree on X — check sources/02-conversations/ and flag it" |

## Try it once

1. Drop any file into `sources/` — a pasted paragraph, an article, a chat export. For a Claude or GPT conversation: copy the conversation text and paste it into a new `.md` file (e.g. `sources/02-conversations/claude-session.md`) — you don't need a formal data export, just the text.
2. Say **"Ingest new sources"**
3. Your agent reads it, files it under the right `sources/` subfolder with frontmatter, links it up to that folder's hub, creates or updates pages in `wiki/`, adds a `## Sources` link back to your file, and appends a linked entry to `log.md`
4. Check Obsidian — a new node appears in Graph View, colored by folder, connected up to its type hub, across to the wiki page it fed, and to `log.md`

Repeat that loop every time you have something new. Once you've ingested a few sources, ask a real question — the agent answers from the wiki first, and can save the answer as a new page in `wiki/pages/` marked `type: synthesis`.

## How merging actually works

Sources are raw and disposable-in-spirit; wiki pages are what tie them together — and that tying-together is **automatic**, not something you trigger separately.

Every ingest starts with "search the wiki first, update an existing page before creating a new one." So if you drop in three separate GPT conversations that all touch Svelte reactivity, the agent doesn't make three pages — it makes (or finds) one `wiki/pages/reactivity.md`, and each ingest just appends a new line to that page's `## Sources` section:

```
## Sources
- [[2026-07-01-gpt-reactivity-question]]
- [[2026-07-03-gpt-reactivity-followup]]
- [[2026-07-05-svelte-docs-clip]]
```

Three different conversations, one page, growing over time — and because these are real `[[wikilinks]]`, not plain text, Obsidian's Graph View draws an actual edge from each source to the page. That's what makes the graph show the weave instead of two unconnected piles of dots, one colored by source folder and one colored by wiki folder. No prompt needed — it's what ingest does by default.

**You can still create pages manually.** Ask your agent to write a page yourself ("create a topic page for X, here's what I know"), or write one directly in `wiki/` — manual pages just skip the `## Sources` section since there's no ingest event behind them. Automatic merging and manual authorship coexist; nothing forces you into one or the other.

## Example: two sources become one answer

Drop an article about pasta into `sources/`, ingest it — you get `wiki/pages/pasta.md` and related pages. Drop an article about Svelte, ingest it — you get `wiki/pages/svelte.md` and friends. Now ask:

> "I want to start an online pasta shop using Svelte. What should I know?"

Your agent searches both sets of wiki pages, follows their `## Sources` links for detail, and writes `wiki/pages/pasta-ecommerce-with-svelte.md` (marked `type: synthesis`) — a page that only exists because it read and combined two unrelated sources. That's the actual point of the system: not storage, synthesis.

## Less manual: automating the "say ingest" step

By default you type "ingest new sources" yourself — that's Level 1, zero setup, works with any agent. There's no reliable Obsidian-native way to auto-connect a folder-dropped file to its hub (even Templater's folder templates don't fire on files that arrive already-populated from outside Obsidian, like a dragged PDF or a pasted chat export) — the AI agent is the only part of this system that can reliably handle arbitrary file types and content, so automation belongs there, not in Obsidian.

**Full auto-ingest on session start (Claude Code):** add this as `.claude/settings.json` in your own vault (not shipped in the template — keeps the template working identically in every agent). Instead of just nudging you, it hands the agent a direct instruction the moment you open it:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "shell": "bash",
            "command": "count=$(grep -rL 'ingested: true' \"$CLAUDE_PROJECT_DIR/sources\" --include='*.md' 2>/dev/null | wc -l); if [ \"$count\" -gt 0 ]; then echo \"$count unprocessed source(s) in sources/. Ingest them now: read each, classify, link to its folder hub, extract concepts, weave into wiki/, mark ingested: true, and commit.\"; fi",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

Every time you open Claude Code on this vault, it checks for anything sitting in `sources/` without `ingested: true` — clipper output, manually dropped files, anything — and processes it before you type a word. Verify it actually triggers the agent to act rather than just print a message (hook behavior can vary by Claude Code version); if it only nudges, just confirm with "yes" and it runs.

**Scheduled ingest:** if your tooling supports cron-style scheduled agent runs, ingest can run on a timer even when you haven't opened the agent at all. Don't turn this on until the manual loop feels solid — automating an unproven workflow just automates the mess.

Both are optional add-ons layered on top of `AGENTS.md`, not requirements. See the "Automation" section at the bottom of `template/AGENTS.md` for the full breakdown.

## Common workflows

- **Ongoing learning** — drop sources as you find them, ingest each time, lint occasionally, ask questions to synthesize
- **Trip planning** — clip travel articles, ask "where should I stay?", save the answer as a synthesis page
- **Research** — clip papers, ask "where do sources disagree?", build a running summary page

---

Next: [CONTRIBUTING.md](CONTRIBUTING.md) if you want to help improve the template.
