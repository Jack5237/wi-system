# WI Workspace Template

This is a clean runtime workspace template to place inside any product repository.

How to use:

1. Copy this folder into your repo as `wi-system/`.
2. Open a terminal in that folder.
3. Run `wi init --root .`.
4. Start adding raw sources to `sources/`.
5. Use `ingest`, `query`, and `lint` regularly.

After copying this folder into a project repo, run:

```bash
wi init --root .
```

That command creates/refreshes:

- `sources/`
- `wiki/`
- `index.md`
- `log.md`
