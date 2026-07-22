# Tutorial: Using Your Wiki

Setup done? See [GETTING_STARTED.md](GETTING_STARTED.md) if not. Day-to-day: drop files in `sources/`, tell your agent what you want, it maintains `wiki/` and `log.md`.

## Prompt library

| Task | Say |
|------|-----|
| Process new files | "Ingest new sources" |
| Process one file | "Ingest sources/Articles/that-file.md" |
| Check pending | "What sources are unprocessed?" |
| Query | "What do I know about X?" |
| Combine topics | "How would I combine X with Y?" |
| Save answer | "Synthesize this and save it: <question>" |
| Find conflicts | "Where do sources disagree on X?" |
| Health check | "Lint the wiki" |
| Fix outdated fact | "Page X says Y, but that's outdated — update it" |
| Merge duplicates | "Merge wiki/Records/a.md and b.md — same thing" |
| Learn from transcripts | "What have I learned from conversations in sources/Transcripts/?" |

## The loop

1. Drop file(s) into `sources/` (article, pasted text, chat export)
2. Say "Ingest new sources"
3. Agent reads it, classifies, links to hubs, weaves into `wiki/`, updates `log.md`
4. Check Obsidian graph — new nodes appear, connected

Repeat. Once you have sources, ask questions — agent answers from wiki, can save synthesis as new page.

---

**More:**
- [Set Up Your Wiki on Cowork](COWORK_SETUP.md) — create a personal productivity assistant project
