# Adoption Guide: Embedding WI-system in Your Project

This guide helps you integrate WI-system into any product repository for durable, searchable project memory.

## Quick Answer: Where Does It Go?

```
your-project/
├── src/
├── docs/
├── README.md
└── wi-system/           ← The workspace folder
    ├── sources/         ← Raw inputs (read-only)
    ├── wiki/            ← Maintained pages (auto-generated)
    ├── index.md         ← Navigation/TOC (auto-generated)
    ├── log.md           ← Operation history (append-only)
    └── AGENTS.md        ← Customization rules (you create)
```

**Key principle**: The **engine** (`wi_system/` package) is installed once globally. The **workspace** (`wi-system/` folder) lives in your project and holds your actual wiki.

## Phase 1: Initial Setup (15 minutes)

### 1.1 Install WI-system

```bash
# In your project root
pip install -e /path/to/wi-system
# or: pip install wi-system  (when published to PyPI)
```

Verify:
```bash
wi --help
```

### 1.2 Create workspace

```bash
mkdir wi-system
cd wi-system
wi init --root .
```

This creates the structure above.

### 1.3 Configure AGENTS.md

Create `wi-system/AGENTS.md` to define how the LLM should work in your domain:

```markdown
# WI-system Agent Contract

## Domain
- Product: [Your product name]
- Team: [Team name]
- Scope: [What knowledge goes in this wiki]

## Page Taxonomy
- `architecture-*`: System design and components
- `api-*`: API documentation
- `decision-*`: Architectural decisions (ADRs)
- `runbook-*`: Operational procedures
- `incident-*`: Postmortem reports

## Conventions
- Pages use header hierarchy (# > ## > ###)
- Links use [[wikilinks]] format
- YAML frontmatter for metadata
- Sources are immutable; wiki pages evolve

## Review Policy
- Synthesis pages: Human review before committing
- Ingest results: Check for contradictions
- Broken links: Monthly lint + fix

## LLM Instructions
- Be precise and cite sources
- Flag uncertainty clearly
- Link related pages liberally
- Prefer clarity over brevity
```

### 1.4 Commit baseline

```bash
git add wi-system/
git commit -m "Add WI-system workspace

- Initialize wiki structure
- Define domain and conventions in AGENTS.md
"
```

## Phase 2: Kickoff (30 minutes)

### 2.1 Start with high-value sources

Identify 5-10 critical docs to ingest first:
- Existing architecture docs
- API documentation
- Key decision records
- Runbooks or playbooks
- Onboarding guides

Save them to `wi-system/sources/`.

### 2.2 Ingest one at a time

```bash
cd wi-system

# Test with one source first
wi ingest --root . sources/architecture.md

# Check the result
cat wiki/index.md      # See generated pages
cat log.md             # See what happened
```

Review the generated wiki pages. Fix any issues before ingesting more.

### 2.3 Ingest the rest

```bash
wi ingest --root . sources/api-docs.md
wi ingest --root . sources/decisions.md
wi ingest --root . sources/runbooks.md
```

### 2.4 Query to verify

Ask questions about the wiki:

```bash
wi query --root . "What are our core components?"
wi query --root . "How do we deploy to production?"
```

Good output = wiki is healthy.

## Phase 3: Operationalize (ongoing)

### 3.1 Weekly ingest cycle

On Mondays or after significant changes:

```bash
# 1. Add new sources (design docs, postmortems, etc.)
cp ../docs/new-feature.md sources/

# 2. Ingest
wi ingest --root . sources/new-feature.md

# 3. Review changes
git diff wiki/

# 4. Commit
git add wiki/ log.md index.md
git commit -m "Ingest: new-feature documentation"
```

### 3.2 Monthly maintenance

On the first Friday of each month:

```bash
cd wi-system

# 1. Lint for quality
wi lint --root . --fix

# 2. Review log
tail -50 log.md

# 3. Check for contradictions
# Look in lint output for flagged issues

# 4. Synthesize quarterly learnings
wi query --root . "What did we ship this quarter?" --store

# 5. Commit
git add wiki/ log.md
git commit -m "Monthly maintenance: lint + synthesis"
```

### 3.3 Archive old sources

Keep `sources/` tidy:

```bash
# After ingest, sources are immutable—archive old ones
mkdir sources/archive/2026-Q1
mv sources/2026-01-*.md sources/archive/2026-Q1/

# Commit
git add sources/
git commit -m "Archive Q1 2026 sources"
```

## Phase 4: Team Integration

### 4.1 Obsidian for visualization

See [OBSIDIAN_GUIDE.md](OBSIDIAN_GUIDE.md) for detailed setup.

```bash
# Team members:
# 1. Clone the project
# 2. Open wi-system/ folder in Obsidian
# 3. Explore the graph
# 4. Click pages to read
```

### 4.2 CI/CD integration

Add to your CI pipeline:

```bash
# .github/workflows/wiki-lint.yml
name: Wiki Quality

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - run: pip install -e ./wi-system
      - run: cd wi-system && wi lint --root .
```

### 4.3 Scheduled synthesis

Run monthly synthesis in CI:

```bash
# .github/workflows/wiki-synthesis.yml
name: Monthly Synthesis

on:
  schedule:
    - cron: "0 9 1 * *"  # First of month at 9am

jobs:
  synthesis:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - run: pip install -e ./wi-system
      - run: |
          cd wi-system
          wi query --root . "Summary of changes this month" --store
      - run: |
          git config user.name "bot"
          git config user.email "bot@example.com"
          git add wiki/ log.md
          git commit -m "Monthly synthesis" || true
          git push
```

## Phase 5: Scale & Maintain

### 5.1 Growing the wiki

As your wiki grows:

1. **Monthly reviews** — Spot-check new pages for accuracy
2. **Quarterly summaries** — Synthesize learning and decisions
3. **Yearly pruning** — Archive outdated or superseded pages
4. **Cross-project linking** — Link to other team wikis for network effect

### 5.2 Metrics to watch

Track in `log.md`:

```bash
# Count pages by type
grep -c "^# architecture-" wiki/

# Measure growth
wc -l log.md  # More operations = more activity

# Check update frequency
git log --oneline wi-system/ | wc -l  # Commits to wiki
```

### 5.3 Team culture

- **Weekly demos**: "What did the wiki teach us?"
- **Quarterly syncs**: Review decisions made via the wiki
- **Onboarding**: New hires explore the graph first
- **Decision making**: Cite the wiki as source of truth

## Real-world Example: Platform Team

```bash
# Initial setup
mkdir platform-wiki
cd platform-wiki
wi init --root .

# Create AGENTS.md
cat > AGENTS.md <<EOF
# Platform Wiki Contract

## Domain
Product: Platform services
Team: Infrastructure
Scope: Architecture, APIs, operations, incidents

## Taxonomy
- arch-*: Architecture decisions
- api-*: API specs and changes
- runbook-*: Operational playbooks
- incident-*: Postmortems
EOF

# Ingest existing docs
wi ingest --root . sources/service-architecture.md
wi ingest --root . sources/incident-2026-04-database-outage.md
wi ingest --root . sources/deployment-runbook.md

# Team explores in Obsidian
# → See how deployment depends on architecture
# → Understand incident root causes
# → Onboard faster

# Monthly cycle
wi lint --root . --fix
wi query --root . "What incidents did we have?" --store
git commit -m "Monthly maintenance"
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Ingest is slow | Break large sources into smaller files |
| Contradictions flagged | Review and edit pages to align |
| Broken links | Run `wi lint --root . --fix` |
| Graph is messy | Add tags in frontmatter to organize |
| Team not using it | Demo in Obsidian + ask questions |

## Next Steps

- [OBSIDIAN_GUIDE.md](OBSIDIAN_GUIDE.md) — Visualization and exploration
- [README.md](../README.md) — Full feature set
- [AGENTS.md](../AGENTS.md) — Agent integration
- [SECURITY.md](../SECURITY.md) — Keep it safe

---

**Your project now has a living, versioned knowledge base.** 🚀
