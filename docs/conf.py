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
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

if not on_rtd:
    extensions.append('pallets_sphinx_themes')

source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'

module_path = os.path.join(os.path.dirname(__file__), '..', 'flask_fontawesome')
module_path = os.path.abspath(module_path)

if on_rtd:
    html_theme = 'default'
else:
    html_theme = 'flask'

htmlhelp_basename = 'flask-fontawesomedoc'

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "flask": ("http://flask.pocoo.org/docs/", None),
}
