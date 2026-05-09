# Archive

This folder contains the original Python implementation of WI-system (CLI tool).

It's preserved here for reference, but the **primary way to use LLM Wiki is now via AI agents** (Claude Code, Cursor, etc.) with the `.schema.md` schema file.

The pattern:
- Old way: Use the `wi` CLI tool
- New way: Open `template/` in Claude Code, and the AI handles everything via `.schema.md`

If you want to use the Python tools for something specific (search, lint), they'll be extracted into `tools/` as utilities. But for day-to-day wiki management, the schema-driven approach is simpler.

See `../SCHEMA.md` for how the new system works.
