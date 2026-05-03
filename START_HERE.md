# Start Here

This repo is the WI-system engine, not a pre-filled wiki workspace.

Important:

- `wi_system/` is engine code.
- `sources/` and `wiki/` are runtime data in each project workspace.

## What happens when you run it

`wi init --root <folder>` creates runtime files in that folder:

- `sources/` for raw inputs
- `wiki/` for maintained pages
- `index.md` for navigation
- `log.md` for history

## Fastest way to use it in any repo

1. Create a `wi-system/` folder inside your project repo.
2. Optionally copy the template from `examples/wi-workspace/`.
3. Install WI-system there.
4. Run `wi init --root .` from inside that folder.
5. Ingest sources and query/lint regularly.

## Minimal commands

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
wi init --root .
wi ingest --root . sources/your-file.md
wi query --root . "What changed?" --store
wi lint --root . --fix
```
