---
description: Answer a question by synthesizing across the wiki, saving the result as a new page
argument-hint: <question>
---

Run the **Core Workflow: Synthesis** from `AGENTS.md` for this question: $ARGUMENTS

1. Search `wiki/topics/`, `wiki/entities/`, `wiki/projects/`, and `wiki/syntheses/` for anything relevant. Don't assume — search first.
2. Follow each relevant page's `## Sources` links into the raw files under `sources/` when you need detail the wiki compressed away.
3. Answer in this priority order: wiki knowledge first, raw sources second, general model knowledge last and clearly labelled as such.
4. Cite every wiki page and source file you drew from.
5. If the answer is substantial enough to be worth keeping, save it as a new page in `wiki/syntheses/` using the standard wiki page format, linked to every topic, entity, and source it drew from. Update `wiki/index.md`.
6. Commit if a new page was saved.
