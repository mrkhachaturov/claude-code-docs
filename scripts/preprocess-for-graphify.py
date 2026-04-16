#!/usr/bin/env python3
"""Preprocess Claude Code docs for graphify knowledge graph extraction.

Strips presentation noise (JSX, React, CDN URLs, identical headers) while
preserving semantic content and converting cross-references to clean
markdown links that graphify subagents can parse as EXTRACTED edges.

Usage:
    python scripts/preprocess-for-graphify.py [--src docs/] [--dst graphify-out/.preprocessed/]
"""
import argparse
import re
from pathlib import Path

SKIP_FILES = {"changelog.md", "docs_manifest.json"}

# JSX tags whose content is meaningful (strip tag, keep content)
CONTENT_TAGS = ["Tip", "Warning", "Note", "Info", "Danger", "Callout", "Experiment"]

# JSX tags that are purely structural (strip tag and attributes)
STRUCTURAL_TAGS = [
    "Steps", "Step", "Tabs", "Tab", "CodeGroup", "Frame",
    "CardGroup", "Card", "AccordionGroup", "Accordion",
    "Update", "Schema",
]


def convert_cross_reference(match: re.Match) -> str:
    """Convert /en/topic#section links to topic.md#section format."""
    link_text = match.group(1)
    path = match.group(2)
    # /en/agent-sdk/foo -> agent-sdk__foo
    path = re.sub(r"^/en/", "", path)
    path = path.replace("/", "__")
    if "#" in path:
        base, anchor = path.split("#", 1)
        return f"[{link_text}]({base}.md#{anchor})"
    return f"[{link_text}]({path}.md)"


def preprocess(text: str) -> str:
    """Clean a single doc file for graphify extraction."""

    # 1. Strip the identical 3-line index blockquote header (same in every file)
    text = re.sub(
        r"^> ## Documentation Index\n> Fetch the complete.*?\n> Use this file.*?\n\n",
        "",
        text,
        count=1,
    )

    # 2. Convert /en/ cross-references to clean markdown links
    text = re.sub(r"\[([^\]]+)\]\(/en/([^)]+)\)", convert_cross_reference, text)

    # 3. Strip content JSX tags but keep their inner text
    for tag in CONTENT_TAGS:
        text = re.sub(rf"<{tag}>\s*\n?", "", text)
        text = re.sub(rf"</{tag}>\s*\n?", "", text)

    # 4. Strip structural JSX tags (with possible attributes)
    for tag in STRUCTURAL_TAGS:
        text = re.sub(rf"<{tag}[^>]*>\s*\n?", "", text)
        text = re.sub(rf"</{tag}>\s*\n?", "", text)

    # 5. Replace <img> tags with alt text (drop CDN URLs)
    text = re.sub(r'<img[^>]*alt="([^"]*)"[^>]*/?>', r"[Image: \1]", text)

    # 6. Strip <video> tags
    text = re.sub(r"<video[^>]*>[^<]*</video>", "[Video]", text)
    text = re.sub(r"<video[^>]*/>", "[Video]", text)

    # 7. Strip embedded React component definitions (export const ...)
    text = re.sub(
        r"^export const \w+.*?(?=\n#|\n\n##|\Z)",
        "",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )

    # 8. Strip <div> wrappers (presentation only)
    text = re.sub(r"<div[^>]*>\s*\n?", "", text)
    text = re.sub(r"</div>\s*\n?", "", text)

    # 9. Clean up excessive blank lines
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--src",
        type=Path,
        default=Path("docs"),
        help="Source docs directory (default: docs/)",
    )
    parser.add_argument(
        "--dst",
        type=Path,
        default=Path("graphify-out/.preprocessed"),
        help="Output directory (default: graphify-out/.preprocessed/)",
    )
    args = parser.parse_args()

    args.dst.mkdir(parents=True, exist_ok=True)

    files_processed = 0
    headers_stripped = 0
    links_converted = 0

    for f in sorted(args.src.glob("*.md")):
        if f.name in SKIP_FILES:
            continue

        original = f.read_text()

        # Count links before conversion for stats
        link_count = len(re.findall(r"\[([^\]]+)\]\(/en/([^)]+)\)", original))
        links_converted += link_count

        if original.startswith("> ## Documentation Index"):
            headers_stripped += 1

        cleaned = preprocess(original)
        (args.dst / f.name).write_text(cleaned)
        files_processed += 1

    print(f"Preprocessed {files_processed} files -> {args.dst}/")
    print(f"  Headers stripped: {headers_stripped}")
    print(f"  Cross-references converted: {links_converted}")
    print(f"  Skipped: {', '.join(SKIP_FILES)}")


if __name__ == "__main__":
    main()
