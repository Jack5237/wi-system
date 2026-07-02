# Tutorial: Using Your Wiki

Setup is done — see [GETTING_STARTED.md](GETTING_STARTED.md) if you haven't gotten `my-wiki/` running yet. This guide is about what happens *after* that: the actual day-to-day of talking to your AI agent and watching the wiki grow.

Everything here is plain language. There are no slash commands to memorize — your agent reads `AGENTS.md` and understands every phrase below.

---

## Prompt Library

Keep this section open as a reference. These are the phrases you'll use most.

### Ingesting sources

| What you want | What to say |
|---|---|
| Process everything new | `"Ingest new sources"` |
| Process one specific file | `"Ingest sources/01-articles/that-file.md"` |
| Check what's waiting first | `"What sources are unprocessed?"` |
| Prioritize recent drops | `"Ingest the sources I added today"` |

### Asking questions (synthesis)

| What you want | What to say |
|---|---|
| A general question | `"What do I know about X?"` |
| Combine two topics | `"How would I combine X with Y?"` |
| Save the answer as a page | `"Synthesize this and save it: <your question>"` |
| Find gaps | `"What are the open questions in my wiki?"` |
| Find disagreement | `"Where do my sources disagree on X?"` |

### Maintenance

| What you want | What to say |
|---|---|
| Full health check | `"Lint the wiki"` |
| Find unlinked pages | `"Are there any orphan pages?"` |
| Find duplicates | `"Are any wiki pages duplicates of each other?"` |
| Fix broken links | `"Check for dead source links"` |
| Refresh navigation | `"Update wiki/index.md"` |

### Editing and correcting

| What you want | What to say |
|---|---|
| Fix a wrong fact | `"Page X says Y, but that's outdated — update it"` |
| Merge two pages | `"Merge wiki/topics/a.md and wiki/topics/b.md — they're the same thing"` |
| Split an overloaded page | `"wiki/topics/X.md is doing too much — split out the Y section into its own page"` |
| Reduce over-linking | `"Review the links on wiki/topics/X.md — remove any that aren't meaningful"` |

### Filtering by source type

| What you want | What to say |
|---|---|
| Only what came from AI chats | `"What have I learned from conversations in sources/03-conversations/?"` |
| Only clipped articles | `"Summarize what's in sources/01-articles/"` |
| Attribute conflicting claims | `"Claude and GPT disagree on X — check sources/03-conversations/ and flag it"` |

---

## Your First Ingest

Quick, concrete version — do this once to see the loop work end to end.

**1. Drop a file into `sources/`.** Anything works: paste a paragraph into a new `.md` file, drag a PDF, or clip a real article with [Obsidian Web Clipper](https://obsidian.md/plugins?id=obsidian-web-clipper). It doesn't matter which subfolder — the agent sorts it.

**2. Say to your agent:**

> "Ingest new sources"

**3. Watch what happens.** The agent will:
1. Read the file, rename it (`YYYY-MM-DD-slug.md`), move it to the correct typed subfolder, add frontmatter
2. Extract the concepts inside it and search `wiki/` for existing related pages
3. Create or update pages in `wiki/topics/`, `wiki/entities/`, or `wiki/projects/`
4. Add the source's file path to every touched page's `## Sources` section
5. Update `wiki/index.md`
6. Log the change and commit

**4. Check Obsidian.** New nodes appear in Graph View, colored by folder. Click a new page — you'll see its `## Sources` section pointing straight back at your file.

That's the entire loop. Repeat it every time you have something new to add.

---

## Full Walkthrough: Building a Wiki From Scratch

A longer, concrete example — building a wiki about pasta cooking + web development, from an empty vault to a synthesized answer that spans both.

### Scenario

You want to track what you learn about:
1. Italian pasta cooking
2. Building web apps with Svelte
3. How to combine them — selling pasta products online

You'll add 2 sources and watch the AI build connections, then ask a question that draws on both.

### Source 1: Pasta

Create `sources/01-articles/pasta-types.md`:

```markdown
# Italian Pasta Types

From https://example.com/italian-pasta-types

Pasta comes in many shapes. Spaghetti is thin and long. Penne is tube-shaped.
Ravioli are pockets filled with cheese. Each has a traditional pairing with sauces.

## Popular Types

### Spaghetti
- Long, thin noodles
- Pairs with light sauces like aglio e olio

### Penne
- Short tubes with angled ends
- Great for chunky, meat-based sauces

### Ravioli
- Sealed pockets
- Traditionally filled with ricotta and spinach
```

Say to your agent:

> "Ingest new sources"

The agent will:
1. Rename and file the source (`sources/01-articles/2026-07-02-pasta-types.md`), add frontmatter
2. Create `wiki/topics/spaghetti.md`, `wiki/topics/penne.md`, `wiki/topics/ravioli.md`, and `wiki/topics/pasta.md` (an overview linking the three)
3. Add `## Sources` entries pointing back at the article on every page it touched
4. Update `wiki/index.md`

Check Obsidian: refresh, open `wiki/topics/pasta.md`, see the backlinks to spaghetti/penne/ravioli and the `## Sources` section. Graph View shows a small network — the source node and its wiki pages, each colored by folder.

### Source 2: Svelte

Create `sources/01-articles/svelte-basics.md`:

```markdown
# Svelte Basics

From https://example.com/svelte-tutorial

Svelte is a JavaScript framework for building web interfaces.
Unlike React, Svelte compiles components to vanilla JavaScript.
This makes apps smaller and faster.

## Key Concepts

### Reactivity
- Use the `$:` label to create reactive variables
- `$: doubled = count * 2;` automatically updates when count changes

### Components
- Svelte files are components
- Each .svelte file is one component
- Import and use them in other components
```

Say:

> "Ingest new sources"

The agent creates `wiki/topics/svelte.md`, `wiki/topics/reactivity.md`, `wiki/topics/components.md`, `wiki/topics/javascript.md`, and updates the index. In Graph View you now have two separate islands: pasta pages and web dev pages.

### Synthesis: connecting the two

This is the payoff. Ask your agent:

> "I want to start an online pasta shop using Svelte. What should I know?"

The agent:
1. Searches `wiki/topics/` for pasta, svelte, components, reactivity
2. Follows their `## Sources` links back to the raw articles for detail it needs
3. Creates `wiki/syntheses/pasta-ecommerce-with-svelte.md` with synthesized advice — e.g. "show pasta types (link to `wiki/topics/pasta.md`)", "use Svelte components for product listings", "reactive pricing based on selected items"
4. Links the new page to every topic and source it drew from, and updates the index

Check Graph View again — there's now a new hub connecting the two previously separate islands. That hub only exists because the agent read and combined multiple sources. That's the actual point of the system: not storage, synthesis.

### Maintenance

As your vault grows, periodically say:

> "Lint the wiki"

The agent checks for contradictions, orphan pages, duplicates, dead source links, unlinked concepts, and a stale index, then reports what it finds and offers fixes.

### Deeper queries

Once your wiki has some depth, ask compound questions:

> "What are the top 3 pasta types for beginners, and how would I build a Svelte component to showcase them?"

The agent answers from the wiki first (not the raw articles), and can save the answer as a new synthesis page if it's worth keeping.

---

## Common Workflows

### "I want to keep learning on a topic"

1. Drop sources in over weeks/months as you find them
2. Say "ingest new sources" each time
3. Periodically say "lint the wiki"
4. Ask questions to synthesize what you've collected
5. Over time: a rich, structured knowledge base that never forgets

### "I'm planning a trip"

1. Clip travel blogs, restaurant reviews, hotel pages
2. Ask "Where should I stay?" — the agent synthesizes from your clipped sources
3. Ask "Best restaurants near my hotel?" — it connects ideas across sources
4. Say "Save that as a synthesis page" — build "My Ideal Trip Itinerary"

### "I'm doing research"

1. Clip papers, articles, reports
2. Ask "What are the open questions?" — the agent finds gaps
3. Ask "Where do sources disagree?" — it flags contradictions with attribution
4. Say "Synthesize the state of the field" — build a running summary page

### "I dropped a bunch of AI chat exports"

1. Drop Claude/GPT/Gemini conversation exports into `sources/03-conversations/`
2. Say "ingest new sources" — the agent tags each with `brain: claude` / `brain: gpt` / etc.
3. Ask "Where do Claude and GPT disagree?" — contradictions get attributed per source, not silently merged

---

## Key Takeaways

1. **No memorized syntax** — every interaction is a plain sentence to your agent
2. **Ingestion is guided** — `AGENTS.md` tells the agent exactly how to build pages, so it's consistent every time
3. **Connections form automatically** — the agent links related concepts as it works
4. **Synthesis compounds** — each new source makes future answers better, and saved syntheses become permanent pages
5. **The graph is visual proof** — Obsidian shows you the shape of what you know, color-coded, zero setup

---

Next: See [CONTRIBUTING.md](CONTRIBUTING.md) if you want to help improve the template, or go feed your own vault more sources.
