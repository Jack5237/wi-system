# Complete Tutorial: From Zero to Living Wiki

This tutorial walks through a complete example: building a team wiki from scratch in 30 minutes.

## Scenario

You're starting a new project team. You have:
- Existing design documents
- API specifications  
- Deployment runbooks
- Incident reports

You want a searchable, interconnected wiki that your team can explore.

## Step 0: Prerequisites (5 minutes)

### Install Python and create project

```bash
# Verify Python 3.10+
python --version

# Create a project folder
mkdir my-team-project
cd my-team-project

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### Install WI-system

```bash
# From GitHub (latest)
pip install git+https://github.com/Jack5237/wi-system.git

# Or from local repo
pip install -e /path/to/wi-system

# Verify
wi --help
```

## Step 1: Initialize Wiki (2 minutes)

Create the workspace folder:

```bash
mkdir wi-system
cd wi-system
wi init --root .
```

Check what was created:

```bash
ls -la
# Output:
# sources/     ← You'll add documents here
# wiki/        ← Auto-generated pages (empty now)
# index.md     ← Navigation (empty now)
# log.md       ← Operation log (empty now)
```

## Step 2: Gather Documents (5 minutes)

Create sample source documents in `sources/`:

### sources/architecture.md
```markdown
# Architecture Overview

We run a microservices platform with these core services:

1. **Auth Service** — Handles user authentication and tokens
2. **API Gateway** — Routes requests to services
3. **Data Service** — Manages persistent data
4. **Cache Service** — Caches hot data for performance

## Key Design Decisions

- Services communicate via gRPC
- All data is eventually consistent
- Authentication is stateless (JWT-based)
- Each service manages its own database

## Deployment

All services run in Kubernetes on AWS. See deployment runbook for details.
```

### sources/api-spec.md
```markdown
# API Specification v2

## Authentication Endpoint

```
POST /auth/token
Request: {username, password}
Response: {token, expires_in}
```

## Data Endpoints

```
GET /data/{id}        — Fetch a record
POST /data            — Create a record
PUT /data/{id}        — Update a record
DELETE /data/{id}     — Delete a record
```

## Rate Limits

- 1000 requests/minute per token
- Cache responses when possible
```

### sources/deployment-runbook.md
```markdown
# Deployment Runbook

## Prerequisites

- kubectl configured
- AWS credentials set
- Docker images built

## Deployment Process

1. **Build** — Build Docker images for all services
2. **Test** — Run integration tests
3. **Tag** — Tag images with version
4. **Push** — Push to registry
5. **Deploy** — Update Kubernetes manifests
6. **Verify** — Check service health

## Rollback Procedure

If deployment fails:
1. Get previous revision: `kubectl rollout history deployment/auth-service`
2. Rollback: `kubectl rollout undo deployment/auth-service`
3. Verify: `kubectl get pods`

See incident reports for past issues.
```

### sources/incident-2026-04.md
```markdown
# Incident Report: Data Service Outage 2026-04-15

## Timeline

- 14:32 UTC — Data Service returns 500 errors
- 14:45 UTC — Team alerted, investigation begins
- 15:10 UTC — Root cause identified: database connection pool exhausted
- 15:30 UTC — Deployed fix
- 15:45 UTC — All services recovered

## Root Cause

A bug in Auth Service caused connection pool leaks. Each failed authentication consumed a connection.

## Fix

Updated connection pool cleanup in Auth Service. See commit abc123.

## Lessons

- Monitor connection pool usage
- Add circuit breaker to Auth Service
- Improve alerting for connection exhaustion

## Follow-up

- [ ] Add connection pool monitoring
- [ ] Implement circuit breaker
- [ ] Update runbook with warning signs
```

Verify the files are there:

```bash
ls -la sources/
# Should see: architecture.md, api-spec.md, deployment-runbook.md, incident-2026-04.md
```

## Step 3: Ingest Documents (5 minutes)

Now ingest the documents into the wiki:

```bash
# Ingest one at a time and watch the magic happen
wi ingest --root . sources/architecture.md

# Check the result
cat wiki/index.md       # See generated pages
cat log.md              # See operation history

# Ingest the rest
wi ingest --root . sources/api-spec.md
wi ingest --root . sources/deployment-runbook.md
wi ingest --root . sources/incident-2026-04.md
```

Watch `index.md` and `wiki/` folder fill with auto-generated content:

```bash
# See all generated pages
ls -la wiki/

# Peek at generated content
head -20 wiki/index.md
```

Check the log:

```bash
tail -30 log.md
# Shows: pages ingested, links created, contradictions (if any)
```

## Step 4: Query the Wiki (5 minutes)

Now ask questions about what you just ingested:

```bash
# Question 1: Architecture understanding
wi query --root . "What are the main services and how do they communicate?"

# Output should mention:
# - Auth Service, API Gateway, Data Service, Cache Service
# - gRPC communication
# - Eventually consistent architecture
```

```bash
# Question 2: Operational knowledge
wi query --root . "How do we deploy and what should we watch for?"

# Output should mention:
# - Kubernetes deployment process
# - Connection pool exhaustion issue (from incident)
# - Monitoring recommendations
```

```bash
# Question 3: Store an answer
wi query --root . "What happened on April 15?" --store

# This creates a new synthesis page in wiki/
# that you can commit and share with the team
```

Check the new synthesis page:

```bash
ls -la wiki/
# Should see a new synthesis-*.md page

cat wiki/synthesis-*.md
```

## Step 5: Explore in Obsidian (5 minutes)

### Open in Obsidian

1. Open Obsidian desktop app
2. Click "Open folder as vault"
3. Select your `wi-system` folder
4. Wait for Obsidian to index (a few seconds)

### Explore the Graph

1. Click the **Graph View** icon (top-right sidebar)
2. You see nodes connected by lines:
   - `index.md` in the center
   - Your generated pages branching out
   - Lines showing cross-references

3. **Click on any node**:
   - See the page content
   - View backlinks (what links to this page)
   - Click to navigate

### Navigate with Backlinks

1. Click on a page (e.g., "Architecture")
2. In the right sidebar, see "Backlinks" section
3. Shows all pages that mention this page
4. Click to jump between related topics

### Organize with Tags

Add tags to pages in Obsidian for better filtering. In the page frontmatter:

```markdown
---
tags:
  - architecture
  - design
  - core-service
---
```

Then in Graph View, filter by tag to see only architecture pages.

## Step 6: Maintain Weekly (2 minutes)

Run weekly maintenance:

```bash
# Check for issues
wi lint --root .

# Output shows:
# - Broken links (if any)
# - Orphan pages (unlinked pages)
# - Contradictions (conflicting info)

# Fix automatically where possible
wi lint --root . --fix

# View changes
git diff wiki/
```

## Step 7: Commit to Git (2 minutes)

Save your wiki to git:

```bash
# Go back to project root
cd ..

# Stage the wiki
git add wi-system/

# Commit
git commit -m "Initial wiki: architecture, API, operations, incidents

- Ingested 4 source documents
- Generated 8 wiki pages
- Established cross-references
- Ready for team exploration
"

# View the log
git log --oneline wi-system/
```

## What You've Built

```
wi-system/
├── sources/              ← Your raw documents (4 files)
│   ├── architecture.md
│   ├── api-spec.md
│   ├── deployment-runbook.md
│   └── incident-2026-04.md
├── wiki/                 ← Auto-generated pages (8 files)
│   ├── index.md          ← Navigation
│   ├── architecture-overview.md
│   ├── auth-service.md
│   ├── api-specification.md
│   ├── deployment-process.md
│   ├── incident-postmortem.md
│   ├── synthesis-*.md    ← Your stored query
│   └── ...
├── index.md              ← Table of contents
├── log.md                ← Full operation history
└── .git/                 ← Version controlled
```

## Next Steps

### Share with Team

```bash
# Team members can explore:
1. Clone the repo
2. Open wi-system/ in Obsidian
3. Click nodes in the graph
4. Ask questions about the wiki

# Command line for any team member:
cd wi-system
wi query --root . "How do we handle authentication?"
```

### Grow the Wiki

Each week:

```bash
# Add new documents
cp ../docs/new-design.md sources/

# Ingest
wi ingest --root . sources/new-design.md

# Query for new insights
wi query --root . "How does this fit with our architecture?" --store

# Maintain
wi lint --root . --fix

# Commit
git add wiki/ log.md
git commit -m "Ingest: new design document + synthesis"
```

### Scheduled Operations

```bash
# Weekly sync: Tuesday at 10am
# wi ingest --root . sources/weekly-update.md

# Monthly analysis: First Friday
# wi query --root . "What changed this month?" --store
# wi lint --root . --fix

# Quarterly summary: First day of quarter
# wi query --root . "Achievements and decisions this quarter?" --store
```

## Common Questions

**Q: Can I edit pages in Obsidian?**
A: Yes! Edit, add links, create tags. Commit changes to git. Keep `sources/` immutable.

**Q: What if documents contradict each other?**
A: WI-system flags contradictions. Review and edit pages to align. Document the resolution.

**Q: How many documents can I ingest?**
A: 100+ is fine. Break very large documents into chapters for better organization.

**Q: Can multiple people ingest at once?**
A: Yes, but coordinate via git. Merge conflicts in wiki/ are rare (mostly non-overlapping pages).

**Q: How do I back up the wiki?**
A: Git handles it! Push to GitHub/GitLab/etc. The wiki is just markdown—easy to migrate.

## Success Criteria

Your wiki is working well when:

- ✅ Team members explore the graph regularly
- ✅ New documents are ingested weekly
- ✅ Synthesis queries reveal unexpected insights
- ✅ Lint finds and fixes issues proactively
- ✅ Pages stay current with few contradictions
- ✅ Onboarding happens via the wiki

## See Also

- [OBSIDIAN_GUIDE.md](OBSIDIAN_GUIDE.md) — Advanced Obsidian usage
- [ADOPTION_GUIDE.md](ADOPTION_GUIDE.md) — Team rollout playbook
- [README.md](../README.md) — Full reference
- [AGENTS.md](../AGENTS.md) — Customize for your domain

---

**Congratulations! You've built a living knowledge base.** 🎉
