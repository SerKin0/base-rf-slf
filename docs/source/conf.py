# docs/source/conf.py
import os
import sys
from datetime import datetime

# ---------------------------- Основные настройки ---------------------------- #
author = "SerKin0"
project = "InfoBase"
release = "0.0.1"
version = "0.0.1"
base_year = 2026
actual_year = datetime.now().year




# --- Путь к коду FABPY (важно!) ---
sys.path.insert(0, os.path.abspath("../.."))  # от docs/source/ → корень проекта


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

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    "myst_parser",               # Markdown вместо .rst
]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}


# --- Тема ---
html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'

# --- Язык ---
language = "ru"  # или "en"

html_theme_options = {
    'navigation_with_keys': True,
    'sidebar_hide_name': False,
    # Furo автоматически показывает полное оглавление
}

# --- HTML ---
html_static_path = ["_static"]