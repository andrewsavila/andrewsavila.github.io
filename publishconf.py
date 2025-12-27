# publishconf.py
# Usado SOMENTE para publicação (produção)

import os
import sys

sys.path.append(os.curdir)

from pelicanconf import *

# -------------------------------------------------
# URL de produção (OBRIGATÓRIO com https)
# -------------------------------------------------
SITEURL = "https://polyglotdata.com"
RELATIVE_URLS = False

# -------------------------------------------------
# Feeds (produção)
# -------------------------------------------------
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

# -------------------------------------------------
# Limpa output antes de gerar (ok manter)
# -------------------------------------------------
DELETE_OUTPUT_DIRECTORY = True

# -------------------------------------------------
# Domínio próprio (GitHub Pages)
# -------------------------------------------------
CUSTOM_DOMAIN = "polyglotdata.com"

# -------------------------------------------------
# Arquivos estáticos extras (CNAME)
# IMPORTANTE: não sobrescrever STATIC_PATHS
# -------------------------------------------------

STATIC_PATHS = globals().get('STATIC_PATHS', ['images']) + ['extra/CNAME']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

# -------------------------------------------------
# Boas práticas recomendadas
# -------------------------------------------------
# Sitemap ajuda SEO (Elegant usa se existir)
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.8,
        "pages": 0.5,
        "indexes": 0.3,
    },
    "changefreqs": {
        "articles": "weekly",
        "pages": "monthly",
        "indexes": "daily",
    },
}

# Canonical URLs corretas
REL_CANONICAL = False
