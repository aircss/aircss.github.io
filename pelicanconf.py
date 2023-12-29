AUTHOR = 'Morgan Delahaye'
SITEURL = ""
SITENAME = 'Air CSS'
VERSION = '2.2.0'

PATH = "content"
THEME = 'theme'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

ADD_CSS_CLASSES = {}
ADD_CSS_CLASSES_TO_ARTICLE = {
    "p": ["llm", "lh-body", "fw3", "tj"],
    "pre": ["f8"],
    "h2": ["f-subtitle", "fw3", "i"],
    "h3": ["f1", "fw3", "i"],
    "tt": ["red"],
}

PLUGIN_PATHS = ["plugins",]
PLUGINS = [
    "mnemonics",
    "add_css_classes",
]

ARTICLE_SAVE_AS = 'docs/{category}/{slug}.html'


TEMPLATE_PAGES = {
    'CNAME': 'CNAME',
    'air.css': 'air.css',
    'air.min.css': 'air.min.css',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
