#!/usr/bin/env python3
"""Export the wiki knowledge graph as JSON for visualization."""

import json
import os
import re
import argparse

WIKI_DIR = os.path.join(os.path.dirname(__file__), "..", "wiki")


def extract_graph() -> dict:
    """Build a graph of nodes and edges from wiki wikilinks."""
    link_pattern = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
    nodes = {}
    edges = []

    for root, _, files in os.walk(WIKI_DIR):
        for fname in files:
            if not fname.endswith(".md") or fname.startswith("_"):
                continue
            fpath = os.path.join(root, fname)
            rel = os.path.relpath(fpath, WIKI_DIR)
            name = rel.replace(".md", "")
            category = rel.split(os.sep)[0] if os.sep in rel else "root"

            # Extract title from first heading
            title = name
            try:
                with open(fpath, encoding="utf-8") as f:
                    content = f.read()
                heading = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                if heading:
                    title = heading.group(1).strip()
            except Exception:
                content = ""

            nodes[name] = {"id": name, "label": title, "category": category}

            # Extract links
            for link in link_pattern.findall(content):
                clean = link.replace("wiki/", "")
                if clean != name:
                    edges.append({"source": name, "target": clean})

    return {"nodes": list(nodes.values()), "edges": edges}


def main():
    parser = argparse.ArgumentParser(description="Export wiki knowledge graph")
    parser.add_argument("-o", "--output", default=None, help="Output file (default: stdout)")
    parser.add_argument("--format", choices=["json", "dot"], default="json", help="Output format")
    args = parser.parse_args()

    graph = extract_graph()

    if args.format == "dot":
        lines = ["digraph KnowledgeBase {", '  rankdir=LR;', '  node [shape=box];']
        for node in graph["nodes"]:
            lines.append(f'  "{node["id"]}" [label="{node["label"]}"];')
        for edge in graph["edges"]:
            lines.append(f'  "{edge["source"]}" -> "{edge["target"]}";')
        lines.append("}")
        output = "\n".join(lines)
    else:
        output = json.dumps(graph, ensure_ascii=False, indent=2)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Graph exported to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
