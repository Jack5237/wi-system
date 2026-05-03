# Contributing

Thanks for contributing to WI-system.

## Development setup

1. Create a virtual environment.
2. Install editable package.
3. Run tests before submitting changes.

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -e .
python -m unittest discover -s tests -p "test_*.py"
```

## Contribution expectations

- Keep `sources/` immutable by design.
- Preserve markdown page structure and interlinking behavior.
- Keep `index.md` content-oriented and `log.md` append-only chronological.
- Add tests for behavior changes in ingest/query/lint flows.
- Avoid unrelated refactors in the same change.

## Pull request checklist

- Code builds and tests pass.
- README/docs updated when behavior changes.
- Backward compatibility considered for page format and log format.
