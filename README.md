# Computing Education Research Lab at MSU

This is the website for the Computing Education Research Lab at Michigan State University. It is built with [Pelican](https://getpelican.com) (a Python static site generator) and hosted on GitHub Pages. The Python environment is managed with [uv](https://docs.astral.sh/uv/).

## Prerequisites

Install `uv` if you don’t have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Building the website locally

Clone the repo and install dependencies:

```bash
git clone https://github.com/msu-cerl/msu-cerl.github.io
cd msu-cerl.github.io
uv sync
```

Then start a live-reloading local server:

```bash
uv run pelican --autoreload --listen
```

The site will be available at `http://localhost:8000`. Changes to content files are picked up automatically.

To do a one-shot build without serving:

```bash
uv run pelican content -s pelicanconf.py
```

Pushing to `main` triggers an automatic GitHub Pages build and deploy (takes a few minutes).

## Updating publications

Publications are generated from `content/assets/bib/group_publications.bib`. After adding new BibTeX entries, regenerate the publications page with:

```bash
uv run python bin/create_pubs.py
```

Then commit the updated `content/pages/pubs.md` along with your bib changes.

## Questions or contributions

Let me know if you run into issues when working with the website. If you have content you’d like to have featured on the website, but would rather not go down the path of updating the repo yourself, just send that along and I’ll get it up there.
