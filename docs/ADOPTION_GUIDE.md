# Adoption Guide: WI-system In Any Repository

Use this guide to embed WI-system into each product repository.

## Separation of concerns

- `wi_system/` (underscore) is engine code.
- `wi-system/` (hyphen) is the workspace folder you place in each project.
- `sources/` and `wiki/` belong to the workspace, not to the engine package.

## Recommended layout

```text
<repo-root>/
  src/
  docs/
  wi-system/
    sources/
    wiki/
    index.md
    log.md
    AGENTS.md
```

## Rollout steps

1. Copy or install WI-system in `wi-system/`.
2. Tailor `AGENTS.md` to your domain (taxonomy, page conventions, review policy).
3. Start with a curated set of 5-20 high-value sources.
4. Run ingest one source at a time and validate wiki quality.
5. Add a weekly lint routine.
6. Add a monthly synthesis review session.

## Team operating model

- Humans curate sources and steer priorities.
- LLM handles synthesis, linking, indexing, and bookkeeping.
- Maintainers review high-impact page changes.

## Governance recommendations

- Keep `sources/` immutable.
- Keep log append-only for auditability.
- Commit wiki updates with descriptive commit messages.
- Tag milestones (for example, quarter summaries).

## CI suggestion

Run this in CI for smoke validation:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

Optionally schedule lint in automation:

```bash
python -m wi_system.cli --root . lint
```
