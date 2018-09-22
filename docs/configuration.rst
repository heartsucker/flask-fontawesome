Configuration
=============

``Flask-FontAwesome`` has a few configurations.

=================================== =============== ===
Option                              Default
=================================== =============== ===
``FONTAWESOME_USE_MINIFIED``        ``True``        Whether or not to use the minified versions of the resources.
``FONTAWESOME_SERVE_LOCAL``         ``True``        If ``True``, serve from ``/static``, else ``https://use.fontawesome.com``.
``FONTAWESOME_QUERYSTRING_REVVING`` ``True``        If ``True``, serve FontAwesome resources with an appended query string to ensure cache busting on upgrade.
``FONTAWESOME_TYPE``                ``webfont/css`` Options: ``webfont/css`` or ``svg/js``.
``FONTAWESOME_STYLES``              ``solid``       Type: ``list``, options: ``all`` , ``solid``, ``brand``, ``regular``, ``solid``. Which FontAwesome resources to load.
=================================== =============== ===
