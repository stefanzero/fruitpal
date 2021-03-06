# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import sys
project_path = os.path.abspath('..')
fruit_app_path = os.path.join(project_path, 'fruit_app')
print('project_path', project_path)
print('fruit_app_path', fruit_app_path)
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(1, fruit_app_path)

from django.conf import settings
settings.configure()

os.environ['DJANGO_SETTINGS_MODULE'] = 'projectname.settings'
import django
django.setup()

# -- Project information -----------------------------------------------------

project = 'fruitpal'
copyright = '2020, Stefan Musarra'
author = 'Stefan Musarra'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.napoleon']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'classic'

html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_sidebars = {
    '**': [
        # 'about.html',
        # 'navigation.html',
        'localtoc.html',
        'relations.html',
        # 'sourcelink.html',
        'searchbox.html'
    ]
}

html_theme_options = {
    # 'canonical_url': '',
    # Toc options
    # 'collapse_navigation': False,
}

autodoc_member_order = 'bysource'

autodoc_default_flags = ['members', 'private-members']
