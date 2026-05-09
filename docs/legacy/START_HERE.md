# Start Here

Welcome! This guide gets you from zero to a working WI-system setup in 5 minutes.

## Important Distinction

**This repo** is the WI-system Python engine (`wi_system/` package).

**Your project** will have its own `wi-system/` workspace folder where the wiki actually lives.

Think of it this way:
- **wi_system/** (this repo) = the engine/tool
- **wi-system/** (your project) = the workspace/data

## What Gets Created

When you run `wi init --root <folder>`, WI-system creates:

```
your-workspace/
├── sources/     ← Raw input documents (immutable)
├── wiki/        ← Maintained wiki pages
├── index.md     ← Navigation and table of contents
└── log.md       ← Operation history (append-only)
```

These are **runtime artifacts**, not part of the engine code.

## Quickest Setup (2 minutes)

```bash
# 1. Install WI-system
pip install -e .

# 2. Create a workspace
mkdir my-wiki
cd my-wiki

# 3. Initialize it
wi init --root .

# 4. You're done!
ls -la
```

You now have a working wiki. Copy a `.md` file into `sources/` and you're ready to ingest.

## In Your Own Project

```bash
# Inside your project repo:
mkdir wi-system
cd wi-system
wi init --root .

# Add sources
cp ../docs/architecture.md sources/

# Start using it
wi ingest --root . sources/architecture.md
wi query --root . "What's our architecture?"
wi lint --root . --fix
```

Your wiki stays with your code in git.

## Using the Template

Copy `examples/wi-workspace/` as a starting point:

```bash
cp -r examples/wi-workspace my-project-wiki
cd my-project-wiki
pip install -e /path/to/wi-system
wi ingest --root . sources/example.md
```

## Next Steps

- Read [README.md](README.md) for full feature overview
- Check [ADOPTION_GUIDE.md](docs/ADOPTION_GUIDE.md) for integration patterns
- See [USE_CASES.md](docs/USE_CASES.md) for real-world examples
- Browse [AGENTS.md](AGENTS.md) if integrating with AI agents

---

**Questions?** Open an issue or check the full documentation.
