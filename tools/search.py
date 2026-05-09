#!/usr/bin/env python3
"""Simple full-text search over markdown wiki."""

import os
import sys
from pathlib import Path

def search(query: str, wiki_dir: str) -> list[tuple[str, int]]:
    """Search wiki for query term. Returns [(filepath, match_count)]."""
    results = []
    wiki_path = Path(wiki_dir)

    if not wiki_path.exists():
        print(f"Error: {wiki_dir} not found")
        return []

    for md_file in wiki_path.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
            count = content.lower().count(query.lower())
            if count > 0:
                results.append((str(md_file), count))

    # Sort by match count (descending)
    results.sort(key=lambda x: x[1], reverse=True)
    return results

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python search.py <query> <wiki_dir>")
        print("Example: python search.py 'pasta' wiki/")
        sys.exit(1)

    query = sys.argv[1]
    wiki_dir = sys.argv[2]

    results = search(query, wiki_dir)

    if not results:
        print(f"No matches found for '{query}'")
    else:
        print(f"Found {len(results)} files matching '{query}':\n")
        for filepath, count in results:
            print(f"{filepath}: {count} matches")
