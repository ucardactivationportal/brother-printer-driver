# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Brother Printer Driver Setup'
copyright = '2025, Brother'
author = 'Brother Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "Brother Printer Driver – Install via setup.brother.com"

# Short title used in navigation or tab headings
html_short_title = "Brother Printer Driver"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Theme (you can change or uncomment)
html_theme = 'sphinx_rtd_theme'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Static and template file paths
html_static_path = ['_static']  # Only if you're using static files
