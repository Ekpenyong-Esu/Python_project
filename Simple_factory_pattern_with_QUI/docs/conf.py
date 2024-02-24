# conf.py

import os
import sys

# Add the path to your documentation source directory
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'simple_factory_pattern_with_QUI'
author = 'MAhonri'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

latex_elements = {
    # Additional LaTeX packages
    'preamble': r'''
        \usepackage{hyperref}
    ''',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to the source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# Theme options are theme-specific and customize the look and feel of a theme
# further. For a list of options available for each theme, see the
# documentation.
html_theme = 'alabaster'

# -- Options for other output formats ----------------------------------------

# Add any other formats you want to generate: PDF, LaTeX, etc.

# -- Extension configuration -------------------------------------------------

# You can remove the redundant 'extensions' and 'html_theme' sections below

# -- General configuration ---------------------------------------------------

# If you have other extensions, add them here

# -- Options for HTML output -------------------------------------------------

# Change the theme here if needed

# Add any other Sphinx configuration options here
