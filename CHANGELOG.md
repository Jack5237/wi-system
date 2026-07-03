# Changelog

All notable changes to the WI System template are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Professional project structure: CONTRIBUTING.md, SECURITY.md
- Configuration files: .editorconfig, .gitattributes
- GitHub issue templates (bug report, feature request)
- Pull request template for contributions
- Enhanced README with side-by-side Obsidian + AI workflow
- `.wi/schema.yaml` — a normative, machine-readable folder/type/frontmatter/log contract, making the "schema-driven" description literal. AGENTS.md references it and carries a human-readable Frontmatter Reference table
- Pre-configured Obsidian graph colors via path-based groups (`path:sources` green, `path:wiki` blue, `AGENTS.md`/`log.md` grey) — 3 groups, zero setup, and survives folder renames because it keys off the top-level path rather than each subfolder
- **`log.md` is now a real graph node** — AGENTS.md defines a mandatory "Log Format": every entry must `[[wikilink]]` the exact source and wiki files it touched, instead of describing them in prose. Lint now checks for un-linked log entries the same way it checks for missing hub links

### Changed
- **Restructured `sources/` from 6 folders to 3:** `01-articles` (authored text), `02-conversations` (dialogue & talk transcripts, incl. video/audio transcripts), `03-attachments` (raw native files — PDFs, images, audio, video). `type:` frontmatter stays granular
- **Restructured `wiki/` from 4 folders to 3:** `pages`, `entities`, `projects`. Syntheses now live in `pages/` marked `type: synthesis` — no separate folder
- **Renamed `wiki/topics/` to `wiki/pages/`** (hub note, folder, and every cross-reference in AGENTS.md/docs/schema updated to match)
- Elevated the wiki-page → subject-hub link to mandatory (same weight as `## Sources` weaving), fixing the graph defect where a new page connected to its sources but floated free of the wiki tree
- Cleaned template structure: removed AI-specific config from template/
- AGENTS.md is now the single source of truth for all AI agents
- Documentation reorganized for clarity

### Removed
- Removed template/.claude/ configuration (replaced by universal AGENTS.md)
- Removed improvements.md (consolidated into AGENTS.md)
- Removed root .claude/ local project config

## [1.0.0] - 2026-07-02

### Added
- Initial WI System template release
- AGENTS.md ruleset for AI agent workflows
- Structured sources/ folder (typed by source)
- Organized wiki/ folder (by subject)
- .obsidian/graph.json for visualization
- README, GETTING_STARTED, TUTORIAL documentation
- Example initialization and ingest workflows

### Features
- Works with any AI agent (Claude, Cursor, GPT, Ollama, etc.)
- Local-first markdown storage with git version control
- Compounding knowledge base that grows with each source
- Source linking and wiki synthesis workflows
