from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .engine import ensure_workspace, ingest_source, lint_wiki, query_wiki


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="wi", description="WI-system living wiki engine")
    parser.add_argument("--root", default=".", help="Workspace root containing sources/, wiki/, index.md, log.md")

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init", help="Initialize WI-system folders and core markdown files")

    p_ingest = sub.add_parser("ingest", help="Ingest a source file from /sources")
    p_ingest.add_argument("source", help="Path to source file (must be under /sources)")

    p_query = sub.add_parser("query", help="Query the wiki and synthesize an answer")
    p_query.add_argument("question", help="Natural language question")
    p_query.add_argument("--store", action="store_true", help="Store answer as a synthesis page")

    p_lint = sub.add_parser("lint", help="Lint the wiki structure")
    p_lint.add_argument("--fix", action="store_true", help="Apply non-destructive fixes (link cleanup)")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()

    try:
        if args.command == "init":
            paths = ensure_workspace(root)
            print(f"Initialized WI-system at {paths.root}")
            return 0

        if args.command == "ingest":
            result = ingest_source(root, Path(args.source).resolve())
            print(f"Ingested. pages_touched={result['pages_touched']} contradictions_flagged={result['contradictions_flagged']}")
            return 0

        if args.command == "query":
            result = query_wiki(root, args.question, store_page=args.store)
            print("Matched pages:", result["matched_pages"] or "none")
            print()
            print(result["answer"])
            return 0

        if args.command == "lint":
            result = lint_wiki(root, fix=args.fix)
            print(
                "Lint:",
                f"missing_links={result['missing_links']}",
                f"orphan_pages={result['orphan_pages']}",
                f"contradictions={result['contradictions']}",
                f"outdated_claims={result['outdated_claims']}",
            )
            return 0

        parser.print_help()
        return 1
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
