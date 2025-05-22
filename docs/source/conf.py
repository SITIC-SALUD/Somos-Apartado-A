# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Investigadores en Apartado A'
copyright = '2025, SITIC-SALUD'
author = 'SITIC-SALUD'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_nb']

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

source_suffix = ['.rst', '.md']

html_sidebars = {
    # Todas las páginas (comodín '**') conservan la barra lateral por defecto
    '**': [
        #'about.html',
        #'searchbox.html',
    ],
}

html_theme_options = {
    'body_max_width': '100%',  # o por ejemplo '80%', '1200px'
}
