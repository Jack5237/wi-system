<div align="center">

# Set Up Your Wiki on Cowork

[![Repo](https://img.shields.io/badge/repo-wi--system-blue)](https://github.com/Jack5237/wi-system)
![Setup](https://img.shields.io/badge/setup-5%20min-green)
![License](https://img.shields.io/badge/license-MIT-orange)

Personal productivity assistant. Ingest sources, agent synthesizes answers.

[GETTING_STARTED](https://github.com/Jack5237/wi-system/blob/main/GETTING_STARTED.md) • [TUTORIAL](https://github.com/Jack5237/wi-system/blob/main/TUTORIAL.md)

</div>

---

## Initial setup

1. **Clone repo:**
```bash
git clone https://github.com/Jack5237/wi-system.git
```

2. **Copy template folder:**

**Linux/Mac:**
```bash
cp -r wi-system/template ~/Desktop/YOUR_AGENT_NAME
rm -rf wi-system
```

**Windows:**
- Open File Explorer → navigate to `wi-system/template`
- Copy to Desktop → rename to `YOUR_AGENT_NAME`
- Delete `wi-system` folder

3. **Open in Cowork:**
   New Project → browse folder → open

4. **Add project instructions:**
   Paste into project instructions field (replace `YOUR_AGENT_NAME`):
   ```
   You are YOUR_AGENT_NAME. Manage my wiki. Follow AGENTS.md in this folder.

   Prompts:
   - "Ingest new sources"
   - "What do I know about X?"
   - "Synthesize this and save: [question]"
   - "Lint the wiki"

   See TUTORIAL.md for all.
   ```

5. **Test:**
   Tell agent: "Who are you?" → should introduce itself.
   Drop files in `sources/` and start prompting.
   *Optional: [Obsidian](https://obsidian.md) for graph visualization.*

---

## Scheduled tasks

### How to create

Cowork → **Scheduled** → **Add Scheduled Task** for each task.

### Default settings (all tasks)

- **Frequency:** Default or Every Sunday 4:00 AM
- **Model:** Haiku (light) or Sonnet 4.6 (complex)
- **Auto approve:** Enable

### Tasks

#### project-status
- **Description:** Weekly project status summary
- **Project folders:** Parent folder containing repos (e.g., `~/Desktop/Code/`)
- **Prompt:** Follow AGENTS.md. Check `[YOUR_PROJECT1]`, `[YOUR_PROJECT2]`, `[YOUR_PROJECT3]` repos. Summarize commits, PRs, blockers. Create `wiki/Execution/project-status-[date].md` with: `Part of [[Execution|Execution]].` at top, frontmatter (type, updated), content.

#### hot-topics
- **Description:** Weekly trending topics in your field
- **Project folders:** None
- **Prompt:** Follow AGENTS.md. Search YouTube for trending `[YOUR_TOPIC]`. List top 3 with links. Create `wiki/Records/hot-topics-[date].md` with: `Part of [[Records|Records]].` at top, frontmatter (type, updated), content.

#### people-tracking
- **Description:** Track and profile notable people
- **Project folders:** None
- **Prompt:** Follow AGENTS.md. For `[PERSON1]`, `[PERSON2]`, `[PERSON3]`: Search recent work/talks/articles. List top 3 sources. Pull into `sources/Transcripts/` with frontmatter. Create/update `wiki/Individuals/[person].md` with: `Part of [[Individuals|Individuals]].` at top, frontmatter (type, updated), bio, expertise, recent work, source links.

---

Ready. Customize placeholders and create tasks.
