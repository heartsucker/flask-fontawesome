``Flask-FontAwesome``
=====================
.. currentmodule:: flask_fontawesome

``Flask-FontAwesome`` adds FontAwesome to your Flask app.

Quick Start
-----------

.. code:: python

    from flask import Flask, render_template
    from flask_fontawesome import FontAwesome

    app = Flask(__name__)
    fa = FontAwesome(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    app.run(host='127.0.0.1', port=8080)


.. code:: html

    <!DOCTYPE html>
    <html>
      <head>
        {{ fontawesome_css() }}
        <title>FontAwesome Example</title>
      </head>
      <body>
        <h1>FontAwesome Example</h1>
        <p>This is an example of a <span class="fas fa-link"></span> link.</p>
        {{ fontawesome_js() }}
      </body>
    </html>

API Docs
-------------

.. module:: flask_fontawesome
   :noindex:

.. autoclass:: FontAwesome
   :noindex:

   .. automethod:: init_app
      :noindex:

Jinja Functions
~~~~~~~~~~~~~~~

.. module:: flask_fontawesome
   :noindex:

.. autofunction:: fontawesome_html
   :noindex:

.. autofunction:: fontawesome_css
   :noindex:

.. autofunction:: fontawesome_js
   :noindex:

Configuration
~~~~~~~~~~~~~

``Flask-FontAwesome`` has a few configurations.

=================================== =============== ===
Option                              Default
=================================== =============== ===
``FONTAWESOME_INCLUDE_V4_SHIMS``    ``False``       Whether or not to include the v4 shims.
``FONTAWESOME_QUERYSTRING_REVVING`` ``True``        If ``True``, serve FontAwesome resources with an appended query string to ensure cache busting on upgrade.
``FONTAWESOME_SERVE_LOCAL``         ``True``        If ``True``, serve from ``/static``, else ``https://use.fontawesome.com``.
``FONTAWESOME_STYLES``              ``solid``       Type: ``list``, options: ``all`` , ``solid``, ``brand``, . Which FontAwesome resources to load.
``FONTAWESOME_TYPE``                ``webfont/css`` Options: ``webfont/css`` or ``svg/js``.
``FONTAWESOME_USE_MINIFIED``        ``True``        Whether or not to use the minified versions of the resources.
=================================== =============== ===

Full API
~~~~~~~~
Full :doc:`API Docs </api/modules>` cover basic usage of this package.
 
.. toctree::
    :maxdepth: 2
    :caption: API Docs:

    api/modules
