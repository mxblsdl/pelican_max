import bulrush

THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS

AUTHOR = "max blasdel"
SITENAME = "maxblasdel"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "en"
DEFAULT_DATE = "fs"
# DEFAULT_CATEGORY = None


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Github", "https://github.com/mxblsdl"),
    ("Linkedin", "https://www.linkedin.com/in/max-blasdel/"),
    ("Resume", "extra/blasdel_max.pdf"),
    ("Email", "mailto:maxblasdel@gmail.com?subject='website query'"),
)

DEFAULT_PAGINATION = 10

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
    },
    "output_format": "html5",
}

STATIC_PATHS = [
    "images",
    "extra",
]

EXTRA_PATH_METADATA = {
    # "extra/robots.txt": {"path": "robots.txt"},
    # "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/style.css": {"path": "style.css"},
}

# LOAD_CONTENT_CACHE = False
CATEGORY_SAVE_AS = ""
AUTHOR_SAVE_AS = ""

DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    # ("About", "/about/"),
    ("Past Projects", "/projects/"),
    ("Main", "../index.html"),
    ("Shiny Server", "/shiny-server/"),
)
