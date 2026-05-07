# Computing Education Research Lab at MSU

This is the website for the Computing Education Research Lab at Michigan State University. It is built with [Pelican](https://getpelican.com) (a Python static site generator) and hosted on GitHub Pages. The Python environment is managed with [uv](https://docs.astral.sh/uv/).

## Prerequisites

Install `uv` if you don’t have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Alternatively, `uv` can be installed via a package manager (e.g. `brew install uv` on macOS). See the [official installation docs](https://docs.astral.sh/uv/getting-started/installation/) for all options.

## Building the website locally

Clone the repo and install dependencies:

```bash
git clone https://github.com/msu-cerl/msu-cerl.github.io
cd msu-cerl.github.io
uv sync
```

Then start a live-reloading local server:

```bash
uv run pelican --listen --autoreload
```

The site will be available at `http://localhost:8000`. Changes to content files are picked up automatically.

To do a one-shot build without serving:

```bash
uv run pelican content -s pelicanconf.py
```

Pushing to `main` triggers an automatic GitHub Pages build and deploy (takes a few minutes).

## Adding a news post

Create a new Markdown file in `content/posts/` with the following metadata at the top:

```
Title: Post Title Here
Date: 2026-01-15
Author: Firstname Lastname
Slug: short-url-slug
Summary: One or two sentences shown on the news index page.

Full post content starts here...
```

The post will appear automatically at `/news/` in reverse chronological order. The URL will be `/news/{year}/{slug}/`.

## Updating publications

Publications are generated from `content/assets/bib/group_publications.bib`. After adding new BibTeX entries, regenerate the publications page with:

```bash
uv run python bin/create_pubs.py
```

Then commit the updated `content/pages/pubs.md` along with your bib changes.

## GitHub Pages setup

The site deploys automatically via GitHub Actions on every push to `main`. One-time setup required in the repository settings:

1. Go to **Settings → Pages**
2. Under **Source**, select **GitHub Actions** (not "Deploy from a branch")

After that, pushing to `main` triggers the workflow, which builds the Pelican site and deploys the output. You can also trigger a deploy manually from the **Actions** tab using the "Run workflow" button.

## Questions or contributions

Let me know if you run into issues when working with the website. If you have content you’d like to have featured on the website, but would rather not go down the path of updating the repo yourself, just send that along and I’ll get it up there.
