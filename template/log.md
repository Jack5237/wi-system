# Operation Log

Append-only record of every ingestion and change. Every entry is linked — each source and wiki page touched gets a `[[wikilink]]` here. This makes log.md a real graph node connected to everything ever processed.

Format: `## [YYYY-MM-DD] TYPE | Description` followed by bullets with real `[[wikilinks]]` to the pages and sources touched — never to hubs, never to pages that don't exist. See AGENTS.md's "Log Format" section for examples.

## [2026-07-02] init | Vault initialized

Ready for first ingestion
