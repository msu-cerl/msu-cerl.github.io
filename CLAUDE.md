# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Pelican static site for the MSU Computing Education Research Lab, hosted on GitHub Pages at `msucerl.org`. The Python environment is managed with `uv`. Pushing to `main` triggers automatic GitHub Pages build and deploy.

## Local Development

```bash
uv sync                                  # install / sync dependencies
uv run pelican content -s pelicanconf.py # one-shot build → output/
uv run pelican --listen --autoreload     # build + live-reload dev server
```

For a production build (sets `SITEURL`, deletes `output/` first):

```bash
uv run pelican content -s publishconf.py
```

## Site Architecture

Static pages live under `content/pages/` and news posts under `content/posts/`, all as Markdown files with Pelican metadata headers (plain `Key: Value` lines, no YAML fences). The custom theme is in `themes/`.

**Content pages:**

- `content/pages/home.md` — homepage (uses `index.html` template with aside sidebar)
- `content/pages/people.md` — group roster (most commonly edited)
- `content/pages/projects.md` — active research projects
- `content/pages/pubs.md` — publications (**auto-generated; do not hand-edit**)
- `content/pages/curriculumdev.md` — curriculum development efforts
- `content/pages/outreach.md` — outreach activities

**News & Perspectives posts:**

- `content/posts/` — one Markdown file per post; served at `/news/{year}/{slug}/`

**Theme (`themes/`):**

- `templates/base.html` — shared header/footer, nav, canonical link
- `templates/index.html` — extends base; adds aside sidebar
- `templates/page.html` — extends base; standard content page
- `templates/news.html` — news index listing all posts
- `templates/article.html` — individual post page
- `static/css/style.css` — layout/typography; no hardcoded colors
- `static/css/theme-msu.css` / `static/css/theme-cerl.css` — color tokens per scheme

**Config:**

- `pelicanconf.py` — development config (no absolute URLs)
- `publishconf.py` — production config (sets `SITEURL`, deletes output)
- `MENUITEMS`, `SITE_DESCRIPTION`, and `COLOR_SCHEME` are all set in `pelicanconf.py`

## Switching the Color Theme

Set `COLOR_SCHEME` in `pelicanconf.py` before building (no need to touch `publishconf.py` — it inherits the value via `from pelicanconf import *`):

```python
COLOR_SCHEME = "msu"   # MSU brand colors (Spartan Green)
COLOR_SCHEME = "cerl"  # CERL logo colors (teal, grey, black)
```

The value is baked into the theme CSS filename at build time — no JavaScript involved.

## Pelican Page Metadata Format

Each page starts with plain key-value metadata followed by a blank line:

```
Title: Page Title
Slug: url-slug

Content here...
```

The homepage uses two extra keys:

```
Save_as: index.html
Template: index
```

## Adding or Updating People

Edit `content/pages/people.md`. Sections are: Group Leaders → Group Members → External Collaborators → CERL Squirrel Alumni. Each entry follows this pattern:

```markdown
#### Firstname Lastname (pronouns)
<img src="/assets/img/FILENAME.jpg" style="float:left;margin:0 1.25rem 1rem 0" width="120" alt="Firstname Lastname">
Bio text here.
```

Place headshot images in `content/assets/img/`. The `<img>` tag is optional — some members have no photo.

## Writing News & Perspectives Posts

Create a new Markdown file in `content/posts/`. The filename becomes the source file only — the URL is controlled by the `Slug` metadata field.

```
Title: Post Title Here
Date: 2026-01-15
Author: Firstname Lastname
Slug: short-url-slug
Summary: One or two sentences shown on the news index page.

Full post content starts here...
```

- **Title** — displayed as the page heading and linked from the news index
- **Date** — controls sort order and URL path (`/news/{year}/{slug}/`)
- **Author** — optional; shown in the byline on the index and post page
- **Slug** — required; determines the URL (use lowercase-with-hyphens)
- **Summary** — optional but recommended; shown as the excerpt on `/news/`

Posts are automatically listed at `/news/` in reverse chronological order. No other configuration is needed.

## Publications Workflow

Publications are generated from a BibTeX file — do not manually edit `content/pages/pubs.md`.

1. Add new entries to `content/assets/bib/group_publications.bib`
2. Run from anywhere in the repo:

```bash
uv run python bin/create_pubs.py
```

The script uses `pypandoc` (bundled binary, no system install needed) with `--citeproc` to render APA citations, groups them by year descending, and writes `content/pages/pubs.md` with Pelican metadata. `bin/create_pubs.sh` is kept as a reference for the old shell-based workflow.
