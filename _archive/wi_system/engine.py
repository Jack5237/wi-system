from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import re
from typing import Iterable

from .llm import LlmClient
from .markdown import WikiPage, page_to_markdown, parse_bulleted_section, parse_markdown_page, slugify, utc_now


@dataclass
class WorkspacePaths:
    root: Path

    @property
    def sources(self) -> Path:
        return self.root / "sources"

    @property
    def wiki(self) -> Path:
        return self.root / "wiki"

    @property
    def index(self) -> Path:
        return self.root / "index.md"

    @property
    def log(self) -> Path:
        return self.root / "log.md"


def ensure_workspace(root: Path) -> WorkspacePaths:
    paths = WorkspacePaths(root=root)
    paths.sources.mkdir(parents=True, exist_ok=True)
    paths.wiki.mkdir(parents=True, exist_ok=True)
    if not paths.index.exists():
        paths.index.write_text("# WI-system Index\n\n", encoding="utf-8")
    if not paths.log.exists():
        paths.log.write_text("# WI-system Log\n\n", encoding="utf-8")
    return paths


def _append_log(log_file: Path, event: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if ":" in event:
        op, detail = event.split(":", 1)
        op = op.strip()
        detail = detail.strip()
    else:
        op = "event"
        detail = event.strip()
    with log_file.open("a", encoding="utf-8") as f:
        f.write(f"## [{ts}] {op} | {detail}\n\n")


def _read_source(path: Path) -> str:
    if path.suffix.lower() in {".txt", ".md", ".csv", ".json", ".yaml", ".yml"}:
        return path.read_text(encoding="utf-8", errors="ignore")
    # For binary formats (e.g., PDF), this keeps ingestion deterministic; users can preprocess text.
    return path.read_bytes().decode("utf-8", errors="ignore")


def _unique(items: Iterable[str]) -> list[str]:
    seen = set()
    out = []
    for item in items:
        key = item.strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(item.strip())
    return out


def _load_existing_pages(wiki_dir: Path) -> dict[str, WikiPage]:
    pages: dict[str, WikiPage] = {}
    for path in sorted(wiki_dir.glob("*.md")):
        slug = path.stem
        parsed = parse_markdown_page(path.read_text(encoding="utf-8"))
        pages[slug] = WikiPage(
            slug=slug,
            title=parsed.title,
            category=parsed.category,
            summary=parsed.sections.get("Summary", "").strip(),
            key_claims=parse_bulleted_section(parsed.sections.get("Key claims", "")),
            entities=parse_bulleted_section(parsed.sections.get("Entities", "")),
            sources=parse_bulleted_section(parsed.sections.get("Sources", "")),
            open_questions=parse_bulleted_section(parsed.sections.get("Open questions", "")),
            related_pages=parse_bulleted_section(parsed.sections.get("Related pages", "")),
            last_updated=parsed.last_updated or utc_now(),
        )
    return pages


def _write_index(index_path: Path, pages: dict[str, WikiPage]) -> None:
    by_category: dict[str, list[tuple[str, WikiPage]]] = {}
    for slug, page in pages.items():
        by_category.setdefault(page.category or "uncategorized", []).append((slug, page))

    lines = [
        "# WI-system Index",
        "",
        "This is the content map for the living wiki.",
        "",
        "Read this file first for navigation, then open linked pages in wiki/.",
        "",
    ]

    for category in sorted(by_category.keys(), key=str.lower):
        lines.append(f"## {category}")
        lines.append("")
        for slug, page in sorted(by_category[category], key=lambda x: x[1].title.lower()):
            desc = (page.summary or "").replace("|", " ").strip()
            if len(desc) > 120:
                desc = desc[:117] + "..."
            lines.append(f"- [[{slug}|{page.title}]] - {desc}")
        lines.append("")

    lines.append("")
    index_path.write_text("\n".join(lines), encoding="utf-8")


def _persist_pages(wiki_dir: Path, pages: dict[str, WikiPage]) -> None:
    titles = {slug: page.title for slug, page in pages.items()}
    for slug, page in pages.items():
        page.last_updated = utc_now()
        content = page_to_markdown(page, page_titles=titles)
        (wiki_dir / f"{slug}.md").write_text(content, encoding="utf-8")


def ingest_source(root: Path, source_path: Path, llm: LlmClient | None = None) -> dict[str, int]:
    llm = llm or LlmClient()
    paths = ensure_workspace(root)

    if not source_path.exists():
        raise FileNotFoundError(f"Source not found: {source_path}")

    if source_path.parent.resolve() != paths.sources.resolve():
        raise ValueError("Ingest requires source files to live in /sources (immutable store).")

    source_text = _read_source(source_path)
    pages = _load_existing_pages(paths.wiki)
    existing_index = paths.index.read_text(encoding="utf-8") if paths.index.exists() else ""

    extraction = llm.extract_knowledge(source_name=source_path.name, source_text=source_text, existing_index=existing_index)
    raw_pages = extraction.get("pages", [])

    touched = 0
    for raw in raw_pages:
        title = str(raw.get("title", "Untitled")).strip() or "Untitled"
        slug = slugify(title)
        incoming = WikiPage(
            slug=slug,
            title=title,
            category=str(raw.get("category", "uncategorized")).strip() or "uncategorized",
            summary=str(raw.get("summary", "")).strip(),
            key_claims=[str(x).strip() for x in raw.get("key_claims", []) if str(x).strip()],
            entities=[str(x).strip() for x in raw.get("entities", []) if str(x).strip()],
            sources=[str(x).strip() for x in raw.get("sources", []) if str(x).strip()] or [f"sources/{source_path.name}"],
            open_questions=[str(x).strip() for x in raw.get("open_questions", []) if str(x).strip()],
            related_pages=[str(x).strip() for x in raw.get("related_pages", []) if str(x).strip()],
        )

        if slug in pages:
            current = pages[slug]
            current.category = incoming.category or current.category
            if incoming.summary and len(incoming.summary) >= len(current.summary):
                current.summary = incoming.summary
            current.key_claims = _unique([*current.key_claims, *incoming.key_claims])
            current.entities = _unique([*current.entities, *incoming.entities])
            current.sources = _unique([*current.sources, *incoming.sources])
            current.open_questions = _unique([*current.open_questions, *incoming.open_questions])
            current.related_pages = _unique([*current.related_pages, *incoming.related_pages])
        else:
            pages[slug] = incoming
        touched += 1

    # Ensure every page has at least one related link when possible.
    all_slugs = sorted(pages.keys())
    for slug, page in pages.items():
        if page.related_pages:
            continue
        for candidate in all_slugs:
            if candidate != slug and candidate in {slugify(e) for e in page.entities}:
                page.related_pages.append(candidate)
                break

    _persist_pages(paths.wiki, pages)
    _write_index(paths.index, pages)

    contradictions = extraction.get("contradictions", [])
    _append_log(paths.log, f"ingest: source={source_path.name} pages_touched={touched} contradictions_flagged={len(contradictions)}")

    return {
        "pages_touched": touched,
        "contradictions_flagged": len(contradictions),
    }


def query_wiki(root: Path, question: str, store_page: bool = False, llm: LlmClient | None = None) -> dict[str, str]:
    llm = llm or LlmClient()
    paths = ensure_workspace(root)
    pages = _load_existing_pages(paths.wiki)

    terms = [t.lower() for t in re.findall(r"[a-zA-Z0-9]{3,}", question)]
    scored: list[tuple[int, WikiPage]] = []

    for page in pages.values():
        hay = " ".join([
            page.title,
            page.summary,
            " ".join(page.key_claims),
            " ".join(page.entities),
            " ".join(page.open_questions),
        ]).lower()
        score = sum(hay.count(term) for term in terms)
        if score > 0:
            scored.append((score, page))

    if not scored:
        answer = "No relevant wiki pages matched this query yet. Ingest more sources first."
        _append_log(paths.log, f"query: question={question!r} matched_pages=0")
        return {"answer": answer, "matched_pages": ""}

    scored.sort(key=lambda x: x[0], reverse=True)
    top_pages = [p for _, p in scored[:5]]

    context_blocks = []
    for p in top_pages:
        context_blocks.append(
            f"# {p.title}\nSummary: {p.summary}\nClaims: {'; '.join(p.key_claims[:8])}\n"
        )
    context = "\n".join(context_blocks)

    answer = llm.synthesize_answer(question, context)
    page_titles = ", ".join(p.title for p in top_pages)

    if store_page:
        synth_title = f"Synthesis - {question[:60].strip()}"
        synth_slug = slugify(synth_title)
        pages[synth_slug] = WikiPage(
            slug=synth_slug,
            title=synth_title,
            category="synthesis",
            summary=answer[:600],
            key_claims=[answer[:240]],
            entities=[],
            sources=[f"wiki/{slugify(p.title)}.md" for p in top_pages],
            open_questions=[],
            related_pages=[slugify(p.title) for p in top_pages],
        )
        _persist_pages(paths.wiki, pages)
        _write_index(paths.index, pages)

    _append_log(paths.log, f"query: question={question!r} matched_pages={len(top_pages)} stored={store_page}")
    return {"answer": answer, "matched_pages": page_titles}


def lint_wiki(root: Path, fix: bool = False) -> dict[str, int]:
    paths = ensure_workspace(root)
    pages = _load_existing_pages(paths.wiki)

    existing = set(pages.keys())
    incoming_links = {slug: 0 for slug in existing}

    missing_links = 0
    contradictions = 0
    outdated_claims = 0

    for slug, page in pages.items():
        cleaned_links = []
        for link in page.related_pages:
            link_slug = slugify(link)
            if link_slug in existing:
                incoming_links[link_slug] += 1
                cleaned_links.append(link_slug)
            else:
                missing_links += 1
        if fix:
            page.related_pages = _unique(cleaned_links)

        # Simple contradiction heuristic: look for claim and negated version.
        claims = "\n".join(page.key_claims).lower()
        if " is " in claims and " is not " in claims:
            contradictions += 1

        source_latest = 0.0
        for src in page.sources:
            if src.startswith("sources/"):
                src_file = paths.root / src
                if src_file.exists():
                    source_latest = max(source_latest, src_file.stat().st_mtime)
        page_file = paths.wiki / f"{slug}.md"
        if source_latest > 0 and page_file.exists() and page_file.stat().st_mtime < source_latest:
            outdated_claims += 1

    orphan_pages = sum(1 for slug, page in pages.items() if incoming_links.get(slug, 0) == 0 and not page.related_pages)

    if fix:
        _persist_pages(paths.wiki, pages)
        _write_index(paths.index, pages)

    _append_log(
        paths.log,
        (
            "lint: "
            f"missing_links={missing_links} orphan_pages={orphan_pages} contradictions={contradictions} "
            f"outdated_claims={outdated_claims} fixed={fix}"
        ),
    )

    return {
        "missing_links": missing_links,
        "orphan_pages": orphan_pages,
        "contradictions": contradictions,
        "outdated_claims": outdated_claims,
    }
