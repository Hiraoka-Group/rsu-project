import os
import sys

sys.path.insert(0, os.path.abspath('../'))


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RSU Analyzer'
copyright = '2024, Hiraoka Laboratory, The University of Tokyo'
author = 'Hiraoka Laboratory, The University of Tokyo'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.githubpages']


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

html_logo = '_static/logo.svg'
html_favicon = '_static/favicon.svg'

autodoc_member_order = 'bysource'

# Napoleon settings
napoleon_use_admonition_for_examples = False
