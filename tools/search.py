#!/usr/bin/env python3
"""Full-text search over the wiki directory."""

import argparse
import os
import re
import sys

WIKI_DIR = os.path.join(os.path.dirname(__file__), "..", "wiki")


def search(query: str, case_sensitive: bool = False, max_results: int = 20) -> list[dict]:
    """Search wiki files for a query string. Returns list of {file, line_num, line, context}."""
    flags = 0 if case_sensitive else re.IGNORECASE
    pattern = re.compile(re.escape(query), flags)
    results = []

    for root, _, files in os.walk(WIKI_DIR):
        for fname in sorted(files):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            rel = os.path.relpath(fpath, os.path.join(WIKI_DIR, ".."))
            try:
                with open(fpath, encoding="utf-8") as f:
                    lines = f.readlines()
            except Exception:
                continue

            for i, line in enumerate(lines, 1):
                if pattern.search(line):
                    # grab surrounding context (1 line before/after)
                    ctx_start = max(0, i - 2)
                    ctx_end = min(len(lines), i + 1)
                    context = "".join(lines[ctx_start:ctx_end]).strip()
                    results.append({
                        "file": rel,
                        "line_num": i,
                        "line": line.strip(),
                        "context": context,
                    })
                    if len(results) >= max_results:
                        return results
    return results


def main():
    parser = argparse.ArgumentParser(description="Search the wiki")
    parser.add_argument("query", help="Search query")
    parser.add_argument("-n", "--max-results", type=int, default=20, help="Max results (default: 20)")
    parser.add_argument("-c", "--case-sensitive", action="store_true", help="Case-sensitive search")
    args = parser.parse_args()

    results = search(args.query, args.case_sensitive, args.max_results)
    if not results:
        print(f"No results for '{args.query}'")
        sys.exit(0)

    print(f"Found {len(results)} result(s) for '{args.query}':\n")
    for r in results:
        print(f"  {r['file']}:{r['line_num']}")
        print(f"    {r['line']}")
        print()


if __name__ == "__main__":
    main()
