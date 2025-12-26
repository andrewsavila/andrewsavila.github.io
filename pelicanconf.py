AUTHOR = 'André Wanderley de Souza'
SITENAME = 'PolyglotData'
SITEURL = ""

# ---------- Conteúdo ----------
PATH = "content"
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']


# ---------- URLs baseadas em slug ----------
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'


TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt_br'

THEME_TEMPLATES_OVERRIDES = ['templates']

THEME = 'themes/elegant'

# Opcional: configurações úteis
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}

PYGMENTS_STYLE = 'monokai'  # ou 'friendly', 'colorful', etc.
# GITHUB_URL = 'https://github.com/seuusuario/seurepositorio'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing

RELATIVE_URLS = True

# Domínio próprio (caso tenha usado quickstart e respondido "yes")
CUSTOM_DOMAIN = "polyglotdata.com"
