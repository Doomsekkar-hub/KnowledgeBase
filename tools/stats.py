#!/usr/bin/env python3
"""Statistics for the knowledge base wiki."""

import os
import re
import sys

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
WIKI_DIR = os.path.join(BASE_DIR, "wiki")
RAW_DIR = os.path.join(BASE_DIR, "raw")


def count_md_files(directory: str) -> int:
    count = 0
    for root, _, files in os.walk(directory):
        for f in files:
            if f.endswith(".md"):
                count += 1
    return count


def count_words(directory: str) -> int:
    total = 0
    for root, _, files in os.walk(directory):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            try:
                with open(os.path.join(root, fname), encoding="utf-8") as f:
                    text = f.read()
                # count CJK chars + English words
                cjk = len(re.findall(r'[\u4e00-\u9fff]', text))
                eng = len(re.findall(r'[a-zA-Z]+', text))
                total += cjk + eng
            except Exception:
                continue
    return total


def count_wikilinks(directory: str) -> dict:
    """Count wikilinks and find broken ones."""
    link_pattern = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
    all_links = []
    existing_files = set()

    for root, _, files in os.walk(directory):
        for fname in files:
            if fname.endswith(".md"):
                rel = os.path.relpath(os.path.join(root, fname), directory)
                existing_files.add(rel.replace(".md", ""))
                existing_files.add(os.path.basename(rel).replace(".md", ""))

    for root, _, files in os.walk(directory):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            try:
                with open(os.path.join(root, fname), encoding="utf-8") as f:
                    content = f.read()
                links = link_pattern.findall(content)
                all_links.extend(links)
            except Exception:
                continue

    broken = [l for l in set(all_links) if l not in existing_files]
    return {"total": len(all_links), "unique": len(set(all_links)), "broken": broken}


def main():
    print("=== Knowledge Base Statistics ===\n")

    # Raw stats
    raw_count = count_md_files(RAW_DIR)
    raw_words = count_words(RAW_DIR)
    print(f"Raw materials:  {raw_count} files, ~{raw_words:,} words")

    # Wiki stats
    wiki_count = count_md_files(WIKI_DIR)
    wiki_words = count_words(WIKI_DIR)
    print(f"Wiki entries:   {wiki_count} files, ~{wiki_words:,} words")

    # Per-category
    categories = ["concepts", "topics", "guides", "comparisons", "timelines", "glossary"]
    print("\nWiki breakdown:")
    for cat in categories:
        cat_dir = os.path.join(WIKI_DIR, cat)
        if os.path.isdir(cat_dir):
            n = count_md_files(cat_dir)
            print(f"  {cat}: {n} files")

    # Links
    links = count_wikilinks(WIKI_DIR)
    print(f"\nWikilinks:      {links['total']} total, {links['unique']} unique")
    if links["broken"]:
        print(f"Broken links:   {len(links['broken'])}")
        for bl in links["broken"][:10]:
            print(f"  - [[{bl}]]")

    # Registry status
    registry_path = os.path.join(RAW_DIR, "_registry.md")
    if os.path.exists(registry_path):
        with open(registry_path, encoding="utf-8") as f:
            content = f.read()
        pending = content.count("pending")
        compiled = content.count("compiled")
        print(f"\nRegistry:       {compiled} compiled, {pending} pending")


if __name__ == "__main__":
    main()
