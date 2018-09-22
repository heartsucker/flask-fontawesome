``Flask-FontAwesome``
=====================

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
        {{ fontawesome_html() }}
        <title>FontAwesome Example</title>
      </head>
      <body>
        <h1>FontAwesome Example</h1>
        <p>This is an example of a <span class="fas fa-link"></span> link.</p>
      </body>
    </html>

Configuration
-------------

See `Configuration </api/modules>` for more details.

Full API Docs
-------------

Full :doc:`API Docs </api/modules>` cover basic usage of this package.

.. toctree::
    :maxdepth: 2
    :caption: API Docs:

    api/modules
