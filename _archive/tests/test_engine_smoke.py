from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from wi_system.engine import ensure_workspace, ingest_source, lint_wiki, query_wiki


class TestEngineSmoke(unittest.TestCase):
    def test_init_ingest_query_lint(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = ensure_workspace(root)

            source_file = paths.sources / "example.md"
            source_file.write_text(
                """WI-system compiles knowledge into a persistent wiki.
Traditional RAG often re-derives context for each question.
Persistent synthesis accumulates over time.
""",
                encoding="utf-8",
            )

            ingest_result = ingest_source(root, source_file)
            self.assertGreaterEqual(ingest_result["pages_touched"], 1)

            query_result = query_wiki(
                root, "How is WI-system different from RAG?", store_page=True
            )
            self.assertIn("answer", query_result)
            self.assertTrue(query_result["answer"].strip())

            lint_result = lint_wiki(root, fix=True)
            self.assertIn("missing_links", lint_result)
            self.assertIn("orphan_pages", lint_result)

            self.assertTrue((root / "index.md").exists())
            self.assertTrue((root / "log.md").exists())
            wiki_pages = list((root / "wiki").glob("*.md"))
            self.assertTrue(wiki_pages)

            first_page = wiki_pages[0].read_text(encoding="utf-8")
            self.assertTrue(first_page.startswith("---\n"))
            self.assertIn("title:", first_page)
            self.assertIn("category:", first_page)
            self.assertIn("last_updated:", first_page)


if __name__ == "__main__":
    unittest.main()
