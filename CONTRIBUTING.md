# Contributing to WI System

Thank you for improving the WI System template! This guide explains how to contribute.

## What to contribute

We welcome improvements to:
- **`template/AGENTS.md`** — Rules for AI agents (the core)
- **`template/` structure** — Sources, wiki folders, initialization
- **Documentation** — README, GETTING_STARTED, TUTORIAL
- **Bug fixes** — Issues with the template workflow

## How to contribute

### 1. Fork and clone
```bash
git clone https://github.com/YOUR_USERNAME/wi-system.git
cd wi-system
```

### 2. Create a branch
```bash
git checkout -b feature/your-feature
```

### 3. Make changes
- Test by copying `template/` and using it end-to-end
- Verify in Claude Code, Cursor, or another AI agent
- Keep changes focused (one feature per PR)

### 4. Commit with clear messages
```bash
git commit -m "docs: clarify X" or "refactor: improve Y" or "fix: resolve Z"
```

### 5. Push and create a PR
```bash
git push origin feature/your-feature
```

## Commit conventions

- `docs:` — Documentation changes
- `refactor:` — Architecture or structure changes
- `fix:` — Bug fixes
- `chore:` — Maintenance (dependencies, CI, etc.)

## Testing changes

Before opening a PR, test the template:

```bash
cp -r template my-test-vault
cd my-test-vault
# Open in Claude Code or Cursor
# Test the workflows described in AGENTS.md
```

## Questions?

Open an issue or email the maintainers.

Thanks for contributing! 🙌
