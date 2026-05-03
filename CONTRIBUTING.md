# Contributing to WI-system

Thank you for considering contributing to WI-system! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful, inclusive, and constructive in all interactions.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- Basic familiarity with markdown and CLI tools

### Development Setup

```bash
# Clone the repository
git clone https://github.com/Jack5237/wi-system.git
cd wi-system

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Run tests
python -m pytest tests/ -v

# Run linting
ruff check wi_system/ tests/
mypy wi_system/
```

## Contribution Areas

We welcome contributions in:

- **Bug fixes** — Please include a test case
- **Documentation** — Guides, examples, and clarifications
- **Tests** — Improve coverage for existing functionality
- **Features** — Discuss in an issue first before implementing

## Making Changes

### Code Style

- Follow [PEP 8](https://pep8.org/)
- Use type hints for all function signatures
- Keep functions focused and testable
- Write descriptive commit messages

### Key Design Principles

- **`sources/` are immutable** — Data integrity by design
- **`log.md` is append-only** — Complete audit trail
- **Wiki pages interlink** — Maintain knowledge graph structure
- **YAML frontmatter** — Enable semantic queries and filtering
- **Local-first** — No external dependencies for core functionality

### Testing

- Add tests for any new behavior
- Keep tests in `tests/` with `test_*.py` naming
- Run full test suite before submitting: `python -m pytest tests/`

### Documentation

- Update README.md if behavior changes
- Document new CLI options in help text
- Add examples in docstrings for complex functions

## Submission Process

1. **Fork and branch** — Create a feature branch from `main`
2. **Implement** — Keep commits focused and atomic
3. **Test** — Ensure tests pass and linting is clean
4. **Document** — Update docs/README as needed
5. **Submit PR** — Include description of changes and why

### Pull Request Checklist

- [ ] Tests pass: `python -m pytest tests/`
- [ ] Linting passes: `ruff check` and `mypy`
- [ ] Code follows PEP 8 style
- [ ] Commits have clear messages
- [ ] README/docs updated (if behavior changes)
- [ ] Backward compatibility maintained for page/log formats
- [ ] No API keys or secrets in code

## Questions?

Open an issue or discussion in the GitHub repository.

---

**Thank you for making WI-system better!** 🙏
