# WI-system

WI-system is a drop-in knowledge memory engine for agentic projects.

It converts raw sources into a maintained markdown wiki that improves over time.
 
## Architecture (most important)

There are two different things:

1. `wi_system/` (underscore) is the Python engine package.
2. `wi-system/` (hyphen, in your product repo) is the runtime workspace folder.

Direct answer to your question:

- `sources/` and `wiki/` should NOT live inside the Python package folder `wi_system/`.
- `sources/` and `wiki/` are runtime project data and should live inside each project's `wi-system/` workspace.

## What you were seeing

- index.md: the wiki table of contents and navigation map.
- log.md: append-only operation history (ingest, query, lint).

Those files are runtime artifacts for a WI-system workspace, not the core engine code.

## What this repo contains

- engine code: [wi_system](wi_system)
- CLI entrypoint: [wi_system/cli.py](wi_system/cli.py)
- maintainer contract: [AGENTS.md](AGENTS.md)
- example workspace template: [examples/wi-workspace](examples/wi-workspace)

## Repo map (why these folders exist)

- `wi_system/`: core engine package
- `examples/`: copyable starter workspace for real projects
- `tests/`: smoke tests so changes do not break user workflows
- `.github/`: CI and contribution templates
- `docs/`: adoption/use-case references

`tests/` and `examples/` are intentionally included to make the project reliable and easy to adopt.

## What goes in each target repo

Inside any product repo, add a wi-system folder (or similar name) and run WI-system there.

Recommended shape:

```text
my-product-repo/
  src/
  docs/
  wi-system/
    sources/
    wiki/
    index.md
    log.md
```

This keeps project memory with project code.

Why teams need this:

- knowledge stops getting lost in chats/docs
- agent outputs become durable project memory
- onboarding and handoffs become faster
- decisions stay tied to code history in git

## 5-minute usage

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -e .
wi init --root .
```

Then:

```bash
wi ingest --root . sources/your-file.md
wi query --root . "What changed in our architecture?" --store
wi lint --root . --fix
```

## Real-world flow

1. Capture web content with Obsidian Web Clipper into sources.
2. Ask agent to ingest and merge into wiki pages.
3. Browse the graph/pages in Obsidian.
4. Store high-value query outputs back into wiki.
5. Run lint weekly to keep the wiki healthy.

## Local model support

WI-system uses OpenAI-compatible APIs, so local servers are supported.

```bash
set WI_LLM_MODE=openai
set WI_LLM_API_KEY=your_token_or_local_value
set WI_LLM_MODEL=gemma3:4b
set WI_LLM_BASE_URL=http://localhost:11434/v1
```

## Why Python

Python keeps this portable, easy to edit, and simple to automate from agents.

## Conventions

- sources are immutable after ingest
- log is append-only
- wiki pages are interlinked
- wiki pages include YAML frontmatter for filtering/querying

## Additional docs

- [START_HERE.md](START_HERE.md)
- [docs/ADOPTION_GUIDE.md](docs/ADOPTION_GUIDE.md)
- [docs/USE_CASES.md](docs/USE_CASES.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [SECURITY.md](SECURITY.md)
