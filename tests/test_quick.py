# -*- coding: utf-8 -*-


def test_webfont_css_minified(app):
    client = app.test_client()

    app.config['FONTAWESOME_TYPE'] = 'webfont/css'
    app.config['FONTAWESOME_USE_MINIFIED'] = True
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'css/fontawesome.min.css' in text
    assert 'css/solid.min.css' in text


def test_svg_js_minified(app):
    client = app.test_client()

    app.config['FONTAWESOME_TYPE'] = 'svg/js'
    app.config['FONTAWESOME_USE_MINIFIED'] = True
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'js/fontawesome.min.js' in text
    assert 'js/solid.min.js' in text


def test_webfont_css_v4_shims(app):
    client = app.test_client()

    app.config['FONTAWESOME_TYPE'] = 'webfont/css'
    app.config['FONTAWESOME_USE_MINIFIED'] = True
    app.config['FONTAWESOME_INCLUDE_V4_SHIMS'] = True
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'css/v4-shims.min.css' in text


def test_svg_js_v4_shims(app):
    client = app.test_client()

    app.config['FONTAWESOME_TYPE'] = 'svg/js'
    app.config['FONTAWESOME_USE_MINIFIED'] = True
    app.config['FONTAWESOME_INCLUDE_V4_SHIMS'] = True
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'js/v4-shims.min.js' in text


def test_webfont_css_all(app):
    client = app.test_client()

    app.config['FONTAWESOME_TYPE'] = 'webfont/css'
    app.config['FONTAWESOME_STYLES'] = 'all'
    app.config['FONTAWESOME_USE_MINIFIED'] = True
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'css/all.min.css' in text


def test_svg_js_all(app):
    client = app.test_client()

    app.config['FONTAWESOME_TYPE'] = 'svg/js'
    app.config['FONTAWESOME_STYLES'] = 'all'
    app.config['FONTAWESOME_USE_MINIFIED'] = True
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'js/all.min.js' in text


def test_webfont_css_non_minified(app):
    client = app.test_client()

    app.config['FONTAWESOME_TYPE'] = 'webfont/css'
    app.config['FONTAWESOME_USE_MINIFIED'] = False
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'css/fontawesome.css' in text
    assert 'css/solid.css' in text


def test_svg_js_non_minified(app):
    client = app.test_client()

    app.config['FONTAWESOME_TYPE'] = 'svg/js'
    app.config['FONTAWESOME_USE_MINIFIED'] = False
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'js/fontawesome.js' in text
    assert 'js/solid.js' in text


def test_webfont_css_remote(app):
    client = app.test_client()

    app.config['FONTAWESOME_SERVE_LOCAL'] = False
    app.config['FONTAWESOME_TYPE'] = 'webfont/css'
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'css/fontawesome.css' in text
    assert 'css/solid.css' in text


def test_svg_js_remote(app):
    client = app.test_client()
    app.config['FONTAWESOME_SERVE_LOCAL'] = False
    app.config['FONTAWESOME_TYPE'] = 'svg/js'
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'js/fontawesome.js' in text
    assert 'js/solid.js' in text


def test_webfont_css_v4_shims_remote(app):
    client = app.test_client()

    app.config['FONTAWESOME_TYPE'] = 'webfont/css'
    app.config['FONTAWESOME_SERVE_LOCAL'] = False
    app.config['FONTAWESOME_INCLUDE_V4_SHIMS'] = True
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'css/v4-shims.css' in text


def test_svg_js_v4_shims_remote(app):
    client = app.test_client()

    app.config['FONTAWESOME_TYPE'] = 'svg/js'
    app.config['FONTAWESOME_SERVE_LOCAL'] = False
    app.config['FONTAWESOME_INCLUDE_V4_SHIMS'] = True
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'js/v4-shims.js' in text


def test_webfont_css_all_remote(app):
    client = app.test_client()

    app.config['FONTAWESOME_TYPE'] = 'webfont/css'
    app.config['FONTAWESOME_SERVE_LOCAL'] = False
    app.config['FONTAWESOME_STYLES'] = 'all'
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'css/all.css' in text


def test_svg_js_all_remote(app):
    client = app.test_client()

    app.config['FONTAWESOME_TYPE'] = 'svg/js'
    app.config['FONTAWESOME_SERVE_LOCAL'] = False
    app.config['FONTAWESOME_STYLES'] = 'all'
    resp = client.get('/')
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    assert 'js/all.js' in text
