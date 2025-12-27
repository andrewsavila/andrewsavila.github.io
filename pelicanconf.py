AUTHOR = 'André Wanderley de Souza'
SITENAME = 'PolyglotData'

SITEURL = ""
RELATIVE_URLS = True

PATH = "content"

PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt_br'

THEME = 'themes/elegant'

PYGMENTS_STYLE = 'monokai'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10





# Opcional: configurações úteis
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("Theme - Elegant", "https://https://elegant.oncrashreboot.com/"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)