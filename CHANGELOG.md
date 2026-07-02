# Changelog

All notable changes to the WI System template are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Professional project structure: CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md
- Configuration files: .editorconfig, .gitattributes
- GitHub issue templates (bug report, feature request)
- Pull request template for contributions
- Enhanced README with clear user/contributor distinction

### Changed
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
