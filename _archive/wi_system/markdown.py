from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
import re
from typing import Iterable


SECTION_HEADERS = [
    "Summary",
    "Key claims",
    "Entities",
    "Sources",
    "Open questions",
    "Related pages",
]


@dataclass
class WikiPage:
    slug: str
    title: str
    category: str
    summary: str = ""
    key_claims: list[str] = field(default_factory=list)
    entities: list[str] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)
    open_questions: list[str] = field(default_factory=list)
    related_pages: list[str] = field(default_factory=list)
    last_updated: str = field(default_factory=lambda: utc_now())


@dataclass
class ParseResult:
    title: str
    category: str
    last_updated: str
    sections: dict[str, str]


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slugify(text: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9\s-]", "", text).strip().lower()
    value = re.sub(r"[\s_]+", "-", value)
    return value or "untitled"


def parse_markdown_page(content: str) -> ParseResult:
    frontmatter, body = _parse_frontmatter(content)

    title_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Untitled"
    title = frontmatter.get("title", title).strip() or "Untitled"

    category_match = re.search(r"^Category:\s*(.+)$", body, re.MULTILINE)
    category = category_match.group(1).strip() if category_match else "uncategorized"
    category = frontmatter.get("category", category).strip() or "uncategorized"

    updated_match = re.search(r"^Last updated:\s*(.+)$", body, re.MULTILINE)
    last_updated = updated_match.group(1).strip() if updated_match else ""
    last_updated = frontmatter.get("last_updated", last_updated).strip()

    sections: dict[str, str] = {}
    pattern = re.compile(r"^##\s+(.+)$", re.MULTILINE)
    matches = list(pattern.finditer(body))
    for idx, match in enumerate(matches):
        section_name = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        sections[section_name] = body[start:end].strip()

    return ParseResult(title=title, category=category, last_updated=last_updated, sections=sections)


def _to_bullets(items: Iterable[str]) -> str:
    clean = [i.strip() for i in items if i and i.strip()]
    if not clean:
        return "- None"
    return "\n".join(f"- {item}" for item in clean)


def page_to_markdown(page: WikiPage, page_titles: dict[str, str] | None = None) -> str:
    page_titles = page_titles or {}

    def link_slug(slug: str) -> str:
        text = page_titles.get(slug, slug.replace("-", " ").title())
        return f"[[{slug}|{text}]]"

    entities_lines = []
    for item in page.entities:
        slug = slugify(item)
        entities_lines.append(f"{item} ({link_slug(slug)})")

    related_lines = [link_slug(slugify(item)) if "/" not in item else item for item in page.related_pages]

    category_slug = slugify(page.category)
    frontmatter = (
        "---\n"
        f'title: {_yaml_quote(page.title)}\n'
        f'slug: {_yaml_quote(page.slug)}\n'
        f'category: {_yaml_quote(page.category)}\n'
        f'last_updated: {_yaml_quote(page.last_updated)}\n'
        f"tags: [wi-system, {category_slug}]\n"
        "---\n\n"
    )

    return (
        f"{frontmatter}"
        f"# {page.title}\n\n"
        "## Summary\n"
        f"{page.summary.strip() or 'TBD'}\n\n"
        "## Key claims\n"
        f"{_to_bullets(page.key_claims)}\n\n"
        "## Entities\n"
        f"{_to_bullets(entities_lines)}\n\n"
        "## Sources\n"
        f"{_to_bullets(page.sources)}\n\n"
        "## Open questions\n"
        f"{_to_bullets(page.open_questions)}\n\n"
        "## Related pages\n"
        f"{_to_bullets(related_lines)}\n"
    )


def parse_bulleted_section(text: str) -> list[str]:
    items = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("- "):
            value = line[2:].strip()
            value = re.sub(r"\s*\(\[[^\]]+\]\([^\)]+\)\)$", "", value).strip()
            value = re.sub(r"\s*\(\[\[[^\]]+\]\]\)$", "", value).strip()

            # Handle raw wikilink bullets like [[slug|Title]] or [[slug]].
            wikilink = re.fullmatch(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", value)
            if wikilink:
                alias = wikilink.group(2)
                value = (alias or wikilink.group(1)).strip()

            if value and value.lower() != "none":
                items.append(value)
    return items


def _yaml_quote(value: str) -> str:
    return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'


def _parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    if not content.startswith("---\n"):
        return {}, content

    end = content.find("\n---\n", 4)
    if end == -1:
        return {}, content

    raw = content[4:end]
    body = content[end + 5 :]

    meta: dict[str, str] = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip().lower()
        value = value.strip()
        if value.startswith('"') and value.endswith('"') and len(value) >= 2:
            value = value[1:-1].replace('\\"', '"').replace('\\\\', '\\')
        meta[key] = value

    return meta, body
