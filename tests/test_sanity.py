# -*- coding: utf-8 -*-

from flask import Flask, render_template

from flask_fontawesome import FontAwesome


def test_basics():
    app = Flask(__name__)
    FontAwesome(app)

    @app.route('/')
    def index():
        return render_template('simple.html')

    client = app.test_client()

    app.config['FONTAWESOME_TYPE'] = 'webfont/css'
    app.config['FONTAWESOME_USE_MINIFIED'] = True
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'css/fontawesome.min.css' in text
    assert 'css/solid.min.css' in text

    app.config['FONTAWESOME_TYPE'] = 'svg/js'
    app.config['FONTAWESOME_USE_MINIFIED'] = True
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'js/fontawesome.min.js' in text
    assert 'js/solid.min.js' in text

    app.config['FONTAWESOME_TYPE'] = 'webfont/css'
    app.config['FONTAWESOME_USE_MINIFIED'] = False
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'css/fontawesome.css' in text
    assert 'css/solid.css' in text

    app.config['FONTAWESOME_TYPE'] = 'svg/js'
    app.config['FONTAWESOME_USE_MINIFIED'] = False
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'js/fontawesome.js' in text
    assert 'js/solid.js' in text

    app.config['FONTAWESOME_SERVE_LOCAL'] = False
    app.config['FONTAWESOME_TYPE'] = 'webfont/css'
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'css/fontawesome.css' in text
    assert 'css/solid.css' in text

    app.config['FONTAWESOME_TYPE'] = 'svg/js'
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'js/fontawesome.js' in text
    assert 'js/solid.js' in text
