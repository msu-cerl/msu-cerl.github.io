AUTHOR = "CERL"
SITENAME = "CERL@MSU"
SITEURL = ""
SITELOGO = "/assets/img/logo.png"

SITE_DESCRIPTION = """
We're working to demystify how college students learn computing in the modern era.
<br><br>
Interested in joining us?<br>
Send an email to <a href="mailto:dsilvia@msu.edu">dsilvia@msu.edu</a>.
"""

# Theme choice: "msu" or "cerl"
COLOR_SCHEME = "cerl"

PATH = "content"
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["posts"]
ARTICLE_URL = "news/{date:%Y}/{slug}/"
ARTICLE_SAVE_AS = "news/{date:%Y}/{slug}/index.html"

DIRECT_TEMPLATES = ["news"]
NEWS_SAVE_AS = "news/index.html"

STATIC_PATHS = ["assets"]

TIMEZONE = "America/Detroit"
DEFAULT_LANG = "en"

THEME = "themes"

MENUITEMS = [
    ("Home", "/"),
    ("News & Perspectives", "/news/"),
    ("People", "/people/"),
    ("Projects", "/projects/"),
    ("Curriculum Development", "/curriculumdev/"),
    ("Outreach", "/outreach/"),
    ("Publications", "/pubs/"),
]

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Disable blog/feed features
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False

# Suppress unused output
ARCHIVES_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
INDEX_SAVE_AS = ""

PLUGINS = ["pelican.plugins.sitemap"]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.6, "indexes": 0.6, "pages": 0.8},
    "changefreqs": {"articles": "monthly", "indexes": "weekly", "pages": "monthly"},
}

TYPOGRIFY = True
