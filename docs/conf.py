# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import flask_fontawesome  # noqa

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

project = 'flask-fontawesome'
copyright = '2018, heartsucker'
author = 'heartsucker'
version = flask_fontawesome.__version__
release = version

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
]

if not on_rtd:
    extensions.append('pallets_sphinx_themes')

source_suffix = '.rst'
master_doc = 'index'
language = None
todo_include_todos = True
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'

if on_rtd:
    html_theme = 'default'
else:
    html_theme = 'flask'

htmlhelp_basename = 'flask-fontawesomedoc'

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']
