#!/usr/bin/env python3
"""Validate wiki link integrity and frontmatter completeness."""

import os
import re
import sys
import yaml

WIKI_DIR = os.path.join(os.path.dirname(__file__), "..", "wiki")
RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "raw")

REQUIRED_FRONTMATTER = ["title", "created", "tags"]


def parse_frontmatter(filepath: str) -> dict | None:
    """Extract YAML frontmatter from a markdown file."""
    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return None

    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except Exception:
        return None


def collect_wiki_files() -> dict[str, str]:
    """Return {relative_name_without_ext: full_path} for all wiki .md files."""
    files = {}
    for root, _, fnames in os.walk(WIKI_DIR):
        for fname in fnames:
            if not fname.endswith(".md"):
                continue
            full = os.path.join(root, fname)
            rel = os.path.relpath(full, WIKI_DIR)
            name_no_ext = rel.replace(".md", "")
            basename_no_ext = fname.replace(".md", "")
            files[name_no_ext] = full
            files[basename_no_ext] = full
    return files


def find_wikilinks(content: str) -> list[str]:
    return re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)


def validate():
    errors = []
    warnings = []
    suggestions = []

    wiki_files = collect_wiki_files()

    for root, _, fnames in os.walk(WIKI_DIR):
        for fname in fnames:
            if not fname.endswith(".md") or fname.startswith("_"):
                continue
            fpath = os.path.join(root, fname)
            rel = os.path.relpath(fpath, WIKI_DIR)

            try:
                with open(fpath, encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                errors.append(f"Cannot read: {rel}")
                continue

            # Check frontmatter
            fm = parse_frontmatter(fpath)
            if fm is None:
                warnings.append(f"Missing frontmatter: {rel}")
            else:
                for field in REQUIRED_FRONTMATTER:
                    if field not in fm:
                        warnings.append(f"Missing '{field}' in frontmatter: {rel}")

                # Check sources exist
                sources = fm.get("sources", [])
                if not sources:
                    suggestions.append(f"No sources listed: {rel}")
                else:
                    for src in sources:
                        src_path = os.path.join(os.path.dirname(WIKI_DIR), src)
                        if not os.path.exists(src_path):
                            errors.append(f"Source not found: {src} (referenced in {rel})")

            # Check wikilinks
            links = find_wikilinks(content)
            for link in links:
                # Normalize: strip wiki/ prefix if present
                clean = link.replace("wiki/", "").replace("raw/", "")
                if clean not in wiki_files and link not in wiki_files:
                    # Check if it's a raw/ reference
                    raw_path = os.path.join(os.path.dirname(WIKI_DIR), link)
                    if not os.path.exists(raw_path) and not os.path.exists(raw_path + ".md"):
                        errors.append(f"Broken link: [[{link}]] in {rel}")

    # Check for orphan entries (no incoming links)
    all_content = ""
    for root, _, fnames in os.walk(WIKI_DIR):
        for fname in fnames:
            if fname.endswith(".md"):
                try:
                    with open(os.path.join(root, fname), encoding="utf-8") as f:
                        all_content += f.read()
                except Exception:
                    pass

    for name, fpath in wiki_files.items():
        rel = os.path.relpath(fpath, WIKI_DIR)
        if rel.startswith("_") or os.path.basename(rel).startswith("_"):
            continue
        if f"[[{name}" not in all_content and f"[[{os.path.basename(rel).replace('.md', '')}" not in all_content:
            if "/" in name:  # only check full-path names to avoid dupes
                suggestions.append(f"Orphan entry (no incoming links): {rel}")

    # Print report
    print("=== Wiki Validation Report ===\n")

    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  [!] {e}")
        print()

    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  [?] {w}")
        print()

    if suggestions:
        print(f"SUGGESTIONS ({len(suggestions)}):")
        for s in suggestions:
            print(f"  [~] {s}")
        print()

    if not errors and not warnings and not suggestions:
        print("All checks passed!")

    return len(errors)


if __name__ == "__main__":
    exit_code = validate()
    sys.exit(1 if exit_code > 0 else 0)
