<div align="center">

# Getting Started

Set up your vault in under 5 minutes. Everything else is optional.

[TUTORIAL](https://github.com/Jack5237/wi-system/blob/main/TUTORIAL.md) • [AGENTS.md](https://github.com/Jack5237/wi-system/blob/main/template/AGENTS.md)

</div>

---

## What you need

1. **AI agent** — Claude Code, Cursor, ChatGPT, Ollama, or similar
2. **Obsidian** (optional) — [Download](https://obsidian.md) for graph visualization

## Setup (2 min)

```bash
git clone https://github.com/Jack5237/wi-system.git
cp -r wi-system/template my-wiki
cd my-wiki
```

Open in your agent:
```bash
claude code .
# or: Cursor, VS Code, ChatGPT, Ollama
```

**Optional:** Open in Obsidian — File → Open folder as vault → select `my-wiki/`. Graph View shows folder structure immediately (green for `sources/`, blue for `wiki/`).

**Templates** are pre-configured: when creating a note, `Ctrl+P` → `Templates: Insert template` → pick the one named after the note's folder. Frontmatter and the `Part of [[...]]` hub link fill in automatically.

---

## Web Clipper (3 min)

Install [Obsidian Web Clipper](https://obsidian.md/plugins?id=obsidian-web-clipper).

### 1. Set clip location

1. Open Web Clipper extension settings (browser toolbar → Obsidian Web Clipper → gear icon)
2. Go to **Templates** → click into **Default** template (open the card)
3. Under **Location**, set **Note location** to `sources/Articles`

If it keeps landing in `Clippings/` instead: doesn't matter. Clips anywhere inside `sources/` work — ingest sorts them correctly. Only avoid vault-root folders.

### 2. Schema properties (optional)

In **Default template** → **Content → Properties**, replace defaults with:

| Property | Value |
|---|---|
| `type` | `article` |
| `resource` | `{{url}}` |
| `captured` | `{{date\|date:"YYYY-MM-DD"}}` |
| `ingested` | `false` |

### 3. Note naming

In **Note name** field (top of template), use:
```
{{date|date:"YYYY-MM-DD"}}-{{title|lower}}
```

Web Clipper doesn't support character slicing — `{{title|lower}}` will lowercase it. **If titles still sprawl:** manually edit in the clipper popup before saving, or use static suffix:
```
{{date|date:"YYYY-MM-DD"}}-clip
```

Ingest renames files properly later anyway.

### 4. Hub link (optional — instant graph connection)

In **Note content**, add before `{{content}}`:
```
Part of [[Articles|Articles]].

{{content}}
```

**Critical:** Keep `{{content}}` — if Note content holds only the hub line, the article text is thrown away.

### 5. Other source types

For videos/transcripts/conversations, create additional templates with **Template triggers** (URL patterns) and **Note location**:

| Type | Trigger (example) | Location | Content prefix |
|---|---|---|---|
| Videos | `youtube.com`, `vimeo.com` | `sources/Transcripts` | `Part of [[Transcripts\|Transcripts]]` + set `type: video` property |
| AI chats | `claude.ai`, `chatgpt.com` | `sources/Transcripts` | `Part of [[Transcripts\|Transcripts]]` + set `brain: claude`/`gpt`/`gemini` property |

Clipper auto-selects the matching template per page.

---

## Done

Clips land in `sources/Articles` with schema frontmatter and hub link. Tell your agent "Ingest new sources" and it processes them. See [TUTORIAL.md](TUTORIAL.md) for prompts.
