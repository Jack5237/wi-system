# Full Tutorial: Building Your First Wiki

This guide walks you through a complete example: building a wiki about pasta cooking + web development.

## Scenario

You want to track what you learn about:
1. Italian pasta cooking
2. Building web apps with Svelte
3. How to combine them: selling pasta products online

You'll clip 3 articles and watch the AI build connections.

## Part 1: Setup

### Copy the template

```bash
cp -r template pasta-wiki
cd pasta-wiki
```

### Open in Obsidian

Drag `pasta-wiki/` into Obsidian or use "Open folder as vault".

You should see `sources/` (typed subfolders: `01-articles/`, `02-videos/`, `03-conversations/`, `04-documents/`, `05-images/`, `06-audio/`) and `wiki/` (subject subfolders: `topics/`, `entities/`, `projects/`, `syntheses/`, plus `index.md`), all empty to start.

### Open your AI agent

```bash
claude code .
```

Or open the same `pasta-wiki/` folder in Cursor, VS Code, or your AI agent of choice. Read the `AGENTS.md` file — this is your contract with the AI.

## Part 2: Your First Source

### Find an article

Go to a blog or website about pasta. For this example, let's say:
- https://example.com/italian-pasta-types (fictional)

### Clip it

Click the Obsidian Web Clipper extension → save as markdown.

Or manually create a file: `sources/01-articles/pasta-types.md`

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

### Ask the AI to ingest it

Say to your AI agent:

> "Ingest new sources"

### Watch the AI work

The AI will:
1. Read the article, rename it (`sources/01-articles/2026-07-02-pasta-types.md`), and add frontmatter
2. Create pages:
   - `wiki/topics/spaghetti.md` — long noodles, light sauces
   - `wiki/topics/penne.md` — tubes, chunky sauces
   - `wiki/topics/ravioli.md` — pockets, fillings
   - `wiki/topics/pasta.md` — overview, linking to the three above
3. Add each page's `## Sources` entry pointing at the article
4. Update `wiki/index.md`
5. Append to `log.md`

### Check in Obsidian

Refresh Obsidian. You should see new files in `wiki/topics/`.

Click on `pasta.md` → see backlinks to spaghetti, penne, ravioli, and its `## Sources` section pointing at the article.

View → Graph View — you should see a small network forming (`sources/` stays out of the default view).

## Part 3: Your Second Source

### Clip an article about Svelte

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

### Ingest it

Say to your AI agent:

> "Ingest new sources"

The AI will create:
- `wiki/topics/svelte.md`
- `wiki/topics/reactivity.md`
- `wiki/topics/components.md`
- `wiki/topics/javascript.md`

And update the index again.

### Graph View is getting interesting

You now have two islands: Pasta pages and Web Development pages.

## Part 4: Synthesis

### Ask a synthesizing question

Now the interesting part. Ask your AI agent:

> "I want to start an online pasta shop using Svelte. What should I know?"

The AI will:
1. Search `wiki/topics/` for pasta, svelte, components, reactivity
2. Follow their `## Sources` links back to the raw articles for any detail it needs
3. Create `wiki/syntheses/pasta-ecommerce-with-svelte.md`, synthesizing advice like:
   - "Show pasta types (link to `wiki/topics/pasta.md`)"
   - "Use Svelte components for product listings"
   - "Reactive pricing based on selected items"
4. Link the new page to every topic and source it drew from, and update `wiki/index.md`

### Check the graph

Your graph now has a new hub connecting Pasta and Web Development. This is the real power: synthesis that required reading and understanding multiple sources.

## Part 5: Linting

Over time, you add more sources. Say:

> "Lint the wiki"

The AI checks for contradictions, orphan pages, duplicates, dead source links, unlinked concepts, and a stale index — then reports what it finds and offers fixes.

## Part 6: Queries

Once your wiki has some depth, you can ask sophisticated questions:

```
What are the top 3 pasta types for beginners, and how would I build a Svelte component to showcase them?
```

The AI searches the wiki (not the raw articles), synthesizes an answer, and optionally creates a new page.

## Key Takeaways

1. **Clipping is easy** — Any web clipper works
2. **Ingestion is guided** — The `AGENTS.md` tells the AI how to build pages
3. **Connections form automatically** — The AI links related concepts
4. **Synthesis compounds** — Each new source makes the wiki smarter
5. **The graph is visual** — Obsidian shows you what's connected

## Common Workflows

### "I want to keep learning on a topic"

1. Clip articles over weeks/months
2. Ask the AI to ingest each one
3. Periodically lint
4. Ask questions to synthesize
5. By the end: a rich, structured knowledge base

### "I'm planning a trip"

1. Clip travel blogs, restaurant reviews, hotel pages
2. Ask "Where should I stay?" — AI synthesizes from your clipped sources
3. Ask "Best restaurants near my hotel?" — AI connects ideas
4. Create a synthesis page: "My Ideal Trip Itinerary"

### "I'm doing research"

1. Clip papers, articles, reports
2. Ask "What are the open questions?" — AI finds gaps
3. Ask "Where do sources disagree?" — AI flags contradictions
4. Create a synthesis page: "State of the Field" or "What We Know and Don't Know"

---

Next: See [CONTRIBUTING.md](CONTRIBUTING.md) if you want to help improve the template, or dive back into your own vault and keep feeding it sources.
