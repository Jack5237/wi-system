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
| Merge duplicates | "Merge wiki/topics/a.md and b.md — same thing" |

**By source type**
| Want | Say |
|---|---|
| Only AI chat exports | "What have I learned from conversations in sources/03-conversations/?" |
| Attribute disagreement | "Claude and GPT disagree on X — check sources/03-conversations/ and flag it" |

## Try it once

1. Drop any file into `sources/` — a pasted paragraph, an article, a chat export
2. Say **"Ingest new sources"**
3. Your agent reads it, files it under the right `sources/` subfolder with frontmatter, creates or updates pages in `wiki/`, and adds a `## Sources` link back to your file
4. Check Obsidian — a new node appears in Graph View, colored by folder

Repeat that loop every time you have something new. Once you've ingested a few sources, ask a real question — the agent answers from the wiki first, and can save the answer as a new page in `wiki/syntheses/`.

## Example: two sources become one answer

Drop an article about pasta into `sources/`, ingest it — you get `wiki/topics/pasta.md` and related pages. Drop an article about Svelte, ingest it — you get `wiki/topics/svelte.md` and friends. Now ask:

> "I want to start an online pasta shop using Svelte. What should I know?"

Your agent searches both sets of wiki pages, follows their `## Sources` links for detail, and writes `wiki/syntheses/pasta-ecommerce-with-svelte.md` — a page that only exists because it read and combined two unrelated sources. That's the actual point of the system: not storage, synthesis.

## Common workflows

- **Ongoing learning** — drop sources as you find them, ingest each time, lint occasionally, ask questions to synthesize
- **Trip planning** — clip travel articles, ask "where should I stay?", save the answer as a synthesis page
- **Research** — clip papers, ask "where do sources disagree?", build a running summary page

---

Next: [CONTRIBUTING.md](CONTRIBUTING.md) if you want to help improve the template.
