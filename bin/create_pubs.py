#!/usr/bin/env python3
"""Generate content/pages/pubs.md from the group bibliography.

Replaces bin/create_pubs.sh — no system pandoc or gawk required.
Run from anywhere: uv run python bin/create_pubs.py
"""

import re
from pathlib import Path

import pypandoc

REPO = Path(__file__).parent.parent
INFILE = REPO / "templates" / "pubs-template.md"
BIBFILE = REPO / "content" / "assets" / "bib" / "group_publications.bib"
CSLFILE = REPO / "templates" / "apa.csl"
OUTFILE = REPO / "content" / "pages" / "pubs.md"


def extract_year(paragraph: str) -> str:
    m = re.search(r"\(([12][0-9]{3})[a-z]?\)", paragraph) or re.search(
        r"\. ([12][0-9]{3})[a-z]?\.", paragraph
    )
    return m.group(1) if m else "Unknown"


def main() -> None:
    raw = pypandoc.convert_file(
        str(INFILE),
        "markdown_strict",
        extra_args=[
            "--citeproc",
            f"--bibliography={BIBFILE}",
            f"--csl={CSLFILE}",
        ],
    )

    paragraphs = [p.strip() for p in re.split(r"\n\n+", raw) if p.strip()]

    year_refs: dict[str, list[str]] = {}
    for para in paragraphs:
        year_refs.setdefault(extract_year(para), []).append(para)

    lines = ["Title: CERL Publications", "Slug: pubs", ""]
    for year in sorted((y for y in year_refs if y != "Unknown"), reverse=True):
        lines += [f"## {year}", ""]
        for ref in year_refs[year]:
            lines += [ref, ""]

    if "Unknown" in year_refs:
        lines += ["## Unknown", ""]
        for ref in year_refs["Unknown"]:
            lines += [ref, ""]

    OUTFILE.write_text("\n".join(lines))
    print(f"Wrote {len(paragraphs)} references to {OUTFILE}")


if __name__ == "__main__":
    main()
