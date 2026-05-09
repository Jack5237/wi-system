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

### Open in Claude Code

```bash
claude code .
```

Read the `.schema.md` file — this is your contract with the AI.

### Open in Obsidian

Drag `pasta-wiki/` into Obsidian or use "Open folder as vault".

You should see three empty folders: `wiki/`, `sources/`, and an `index.md` file.

## Part 2: Your First Source

### Find an article

Go to a blog or website about pasta. For this example, let's say:
- https://example.com/italian-pasta-types (fictional)

### Clip it

Click the Obsidian Web Clipper extension → save as markdown.

Or manually create a file: `sources/pasta-types.md`

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

In Claude Code, copy this into the prompt:

```
I clipped a new article about Italian pasta types.
It's in sources/pasta-types.md.

Please read it and update the wiki. Follow the rules in .schema.md:
- Extract key concepts (Spaghetti, Penne, Ravioli, etc.)
- Create pages for each
- Link them together
- Update index.md
- Log the ingestion
```

### Watch the AI work

The AI will:
1. Read the article
2. Create pages:
   - `wiki/Spaghetti.md` — long noodles, light sauces
   - `wiki/Penne.md` — tubes, chunky sauces
   - `wiki/Ravioli.md` — pockets, fillings
   - `wiki/Pasta.md` — overview
3. Add links between them
4. Update `wiki/index.md`
5. Append to `wiki/log.md`

### Check in Obsidian

Refresh Obsidian. You should see new files in `wiki/`.

Click on `Pasta.md` → see backlinks to Spaghetti, Penne, Ravioli.

View → Graph View — you should see a small network forming.

## Part 3: Your Second Source

### Clip an article about Svelte

Create `sources/svelte-basics.md`:

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

In Claude Code:

```
I clipped an article about Svelte.
It's in sources/svelte-basics.md.

Please ingest it and update the wiki.
```

The AI will create:
- `wiki/Svelte.md`
- `wiki/Reactivity.md`
- `wiki/Components.md`
- `wiki/JavaScript.md`

And update the index again.

### Graph View is getting interesting

You now have two islands: Pasta pages and Web Development pages.

## Part 4: Synthesis

### Ask a synthesizing question

Now the interesting part. In Claude Code, ask:

```
I want to start an online pasta shop using Svelte.
What should I know?

Please:
1. Search the wiki for relevant pages
2. Create a new page that combines the insights
3. Update index.md to link to this new page
```

The AI will:
1. Read Pasta pages, Svelte pages, and concepts like "Components" and "Reactivity"
2. Create `wiki/Building a Pasta E-Commerce Site with Svelte.md`
3. Synthesize advice like:
   - "Show pasta types (link to Pasta.md)"
   - "Use Svelte components for product listings"
   - "Reactive pricing based on selected items"

### Check the graph

Your graph now has a new hub connecting Pasta and Web Development. This is the real power: synthesis that required reading and understanding multiple sources.

## Part 5: Linting

Over time, you add more sources. Ask the AI:

```
Please lint the wiki.

Check for:
- Contradictions (does any page contradict another?)
- Orphan pages (pages with no backlinks)
- Unlinked concepts (mentioned but no own page)
- Missing citations (claims without a source)

Report what you find.
```

The AI will scan everything and suggest fixes.

## Part 6: Queries

Once your wiki has some depth, you can ask sophisticated questions:

```
What are the top 3 pasta types for beginners, and how would I build a Svelte component to showcase them?
```

The AI searches the wiki (not the raw articles), synthesizes an answer, and optionally creates a new page.

## Key Takeaways

1. **Clipping is easy** — Any web clipper works
2. **Ingestion is guided** — The `.schema.md` tells the AI how to build pages
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

Next: [docs/ADVANCED.md](ADVANCED.md) for schema customization and power features.
