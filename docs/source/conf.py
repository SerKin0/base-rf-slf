# docs/source/conf.py
import os
import sys
from datetime import datetime

# ---------------------------- Основные настройки ---------------------------- #
author = "SerKin0"
project = "InfoBase"
release = "0.0.1"
version = "0.1.22"
base_year = 2026
actual_year = datetime.now().year


html_title = "БАЗА - РФ СЛФ"


if base_year == actual_year:
    copyright = f"{base_year}, {author}"
else:
    copyright = f"{base_year}-{actual_year}, {author}"



# --- MyST (Markdown) ---
myst_enable_extensions = [
    "dollarmath",    # $x$ и $$x$$
    "amsmath",       # \begin{equation}
    "colon_fence",   # ::: блоки
]

exclude_patterns = ['build', 'draft.md']

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_nb',
    'sphinx.ext.mathjax',
]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}


# --- Тема ---
html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'
language = "ru"

html_theme_options = {
    'navigation_with_keys': True,
    'globaltoc_collapse': False,
    'globaltoc_includehidden': False,
    'show_prev_next': True,
    'main_nav_links': {},
}

pygments_style = 'monokai'
pygments_style_dark = 'monokai'


# Для подключения CSS (стили иконок)
html_css_files = [
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css',
]

# --- HTML ---
html_static_path = ["_static"]