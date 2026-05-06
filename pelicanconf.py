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
ARTICLE_PATHS = []
STATIC_PATHS = ["assets/img"]

TIMEZONE = "America/Detroit"
DEFAULT_LANG = "en"

THEME = "themes"

MENUITEMS = [
    ("Home", "/"),
    ("People", "/people/"),
    ("Projects", "/projects/"),
    ("Curriculum Development", "/curriculumdev/"),
    ("Publications", "/pubs/"),
    ("Outreach", "/outreach/"),
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
CATEGORIES_SAVE_AS = ""
TAGS_SAVE_AS = ""
INDEX_SAVE_AS = ""

PLUGINS = ["pelican.plugins.sitemap"]

SITEMAP = {
    "format": "xml",
    "priorities": {"pages": 0.8},
    "changefreqs": {"pages": "monthly"},
}

TYPOGRIFY = True
