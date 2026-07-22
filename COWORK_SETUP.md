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

1. **Get the vault:** follow [GETTING_STARTED](https://github.com/Jack5237/wi-system/blob/main/GETTING_STARTED.md) — clone, copy `template/` to a folder named `YOUR_AGENT_NAME`.

2. **Open in Cowork:** New Project → browse to your folder → open

3. **Add project instructions** (replace `YOUR_AGENT_NAME`):

   ```
   You are YOUR_AGENT_NAME. Manage my wiki. Follow AGENTS.md in this folder.

   Prompts:
   - "Ingest new sources"
   - "What do I know about X?"
   - "Synthesize this and save: [question]"
   - "Lint the wiki"

   See TUTORIAL.md for all.
   ```

4. **Test:** Say "Who are you?" — agent should introduce itself. Then drop files in `sources/` and start prompting.

   *Optional: open the folder in [Obsidian](https://obsidian.md) for graph visualization.*

---

## Scheduled tasks

Cowork → **Scheduled** → **Add Scheduled Task**. Create each task below.

**Settings (all tasks):**

- **Frequency:** Default or Every Sunday 4:00 AM
- **Model:** Haiku (light) or Sonnet 4.6 (complex)
- **Auto approve:** Enable

Every prompt starts with "Follow AGENTS.md in this wiki folder" — that pins the run to the wiki contract (templates, hub links, log entries), so the prompts stay short.

### 1. project-status

- **Project folders:** Your wiki folder **and** the parent folder containing your repos
- **Prompt:**

  > Follow AGENTS.md in my wiki folder — it governs all wiki writes; ignore AGENTS.md/CLAUDE.md inside the repos. Check `[YOUR_PROJECT1]`, `[YOUR_PROJECT2]` read-only. Summarize commits, PRs, blockers into `wiki/Execution/project-status-[date].md`, then log it.

### 2. hot-topics

- **Project folders:** None
- **Prompt:**

  > Follow AGENTS.md in this wiki folder. Search for this week's trending `[YOUR_TOPIC]` news. Save top 3 with links into `wiki/Records/hot-topics-[date].md`, then log it.

### 3. people-tracking

- **Project folders:** None
- **Prompt:**

  > Follow AGENTS.md in this wiki folder. For `[PERSON1]`, `[PERSON2]`: search recent work, talks, articles. Save the top sources into `sources/Articles/` (marked `ingested: true`), create/update each person's page in `wiki/Individuals/`, then log it.

### 4. other

Want something else on a schedule? Skip the form — just send this in Cowork chat:

> Make me a new scheduled task for "[what you want to do]"

The agent builds the task for you, wired to AGENTS.md.

---

Ready. Replace placeholders, create the tasks, done.
