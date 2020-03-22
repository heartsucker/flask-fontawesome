# -*- coding: utf-8 -*-
'''
flask_fontawesome
-----------------

This moudle provides helpers to quickly add FontAwesome resources to your Flask app.

:license: MIT / Apache 2.0 (seen LICENSE-MIT and LICENSE-APACHE for details)
'''

from flask import Flask, Blueprint, url_for, Markup, current_app

FONTAWESOME_VERSION = '5.3.1'
__version__ = '0.1.4'


def fontawesome_html() -> Markup:
    '''
    Returns :class:`~flask.Markup` of all the requested FontAwesome resources. This can be embedded
    in your Jinja templates to add FontAwesome to your site.
    '''
    if current_app.config['FONTAWESOME_SERVE_LOCAL']:
        return current_app.extensions['fontawesome']._static.resources_html()
    else:
        return current_app.extensions['fontawesome']._use_fa.resources_html()


def fontawesome_js() -> Markup:
    '''
    Returns :class:`~flask.Markup` of the JS FontAwesome resources.
    '''
    if current_app.config['FONTAWESOME_SERVE_LOCAL']:
        return current_app.extensions['fontawesome']._static.js_html()
    else:
        return current_app.extensions['fontawesome']._use_fa.js_html()


def fontawesome_css() -> Markup:
    '''
    Returns :class`~flask.Markup` of the CSS FontAwesome resources.
    '''
    if current_app.config['FONTAWESOME_SERVE_LOCAL']:
        return current_app.extensions['fontawesome']._static.css_html()
    else:
        return current_app.extensions['fontawesome']._use_fa.css_html()


class Cdn(object):

    def resources_html(self) -> Markup:
        return self.css_html() + self.js_html()

    def css_html(self) -> Markup:
        raise NotImplementedError()

    def js_html(self) -> Markup:
        raise NotImplementedError()

    def _check_type(self) -> None:
        typ = current_app.config['FONTAWESOME_TYPE']
        if typ not in ['webfont/css', 'svg/js']:
            raise ValueError('Illegal parameter for FONTAWESOME_TYPE: {}'.format(typ))


class StaticCdn(Cdn):

    def css_html(self) -> Markup:
        self._check_type()
        if current_app.config['FONTAWESOME_TYPE'] == 'webfont/css':
            return self.__gen_html(self.__css)
        else:
            return Markup()

    def js_html(self) -> Markup:
        self._check_type()
        if current_app.config['FONTAWESOME_TYPE'] == 'svg/js':
            return self.__gen_html(self.__js)
        else:
            return Markup()

    def __gen_html(self, func) -> Markup:
        use_min = current_app.config['FONTAWESOME_USE_MINIFIED']
        html = []

        styles = current_app.config['FONTAWESOME_STYLES']
        if 'all' in styles:
            html.append(func('all', use_min))
        else:
            html.append(func('fontawesome', use_min))
            for style in styles:
                html.append(func(style, use_min))

        if current_app.config['FONTAWESOME_INCLUDE_V4_SHIMS']:
            html.append(func('v4-shims', use_min))

        return Markup('\n'.join(html))

    def __url(self, resource: str) -> str:
        params = {'filename': resource}
        if current_app.config['FONTAWESOME_QUERYSTRING_REVVING']:
            params['version'] = FONTAWESOME_VERSION
        return url_for('fontawesome.static', **params)

    def __css(self, style: str, use_min: bool) -> str:
        min_str = '.min' if use_min else ''
        resource = 'css/{}{}.css'.format(style, min_str)
        return '<link href="{}" rel="stylesheet">'.format(self.__url(resource))

    def __js(self, style: str, use_min: bool) -> str:
        min_str = '.min' if use_min else ''
        resource = 'js/{}{}.js'.format(style, min_str)
        return '<script defer src="{}" rel="stylesheet"></script>'.format(self.__url(resource))


class UseFontAwesomeComCdn(Cdn):

    __URL_BASE = 'https://use.fontawesome.com/releases/v{}'.format(FONTAWESOME_VERSION)

    __INTEGRITY_MAP = {
        'webfont/css': {
            'all': 'sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU',
            'brands': 'sha384-rf1bqOAj3+pw6NqYrtaE1/4Se2NBwkIfeYbsFdtiR6TQz0acWiwJbv1IM/Nt/ite',
            'fontawesome': (
                'sha384-1rquJLNOM3ijoueaaeS5m+McXPJCGdr5HcA03/VHXxcp2kX2sUrQDmFc3jR5i/C7'),
            'solid': 'sha384-VGP9aw4WtGH/uPAOseYxZ+Vz/vaTb1ehm1bwx92Fm8dTrE+3boLfF1SpAtB1z7HW',
            'v4-shims': 'sha384-lmquXrF9qn7mMo6iRQ662vN44vTTVUBpcdtDFWPxD9uFPqC/aMn6pcQrTTupiv1A',
        },
        'svg/js': {
            'all': 'sha384-kW+oWsYx3YpxvjtZjFXqazFpA7UP/MbiY4jvs+RWZo2+N94PFZ36T6TFkc9O3qoB',
            'brands': 'sha384-2vdvXGQdnt+ze3ylY5ESeZ9TOxwxlOsldUzQBwtjvRpen1FwDT767SqyVbYrltjb',
            'fontawesome': (
                'sha384-2OfHGv4zQZxcNK+oL8TR9pA+ADXtUODqGpIRy1zOgioC4X3+2vbOAp5Qv7uHM4Z8'),
            'solid': 'sha384-GJiigN/ef2B3HMj0haY+eMmG4EIIrhWgGJ2Rv0IaWnNdWdbWPr1sRLkGz7xfjOFw',
            'v4-shims': 'sha384-DtdEw3/pBQuSag11V3is/UZMjGkGMLDRBgk1UVAOvH6cYoqKjBmCEhePm13skjRV',
        },
    }

    def css_html(self) -> Markup:
        self._check_type()
        if current_app.config['FONTAWESOME_TYPE'] == 'webfont/css':
            return self.__gen_html(self.__css, 'webfont/css')
        else:
            return Markup()

    def js_html(self) -> Markup:
        self._check_type()
        if current_app.config['FONTAWESOME_TYPE'] == 'svg/js':
            return self.__gen_html(self.__js, 'svg/js')
        else:
            return Markup()

    def __gen_html(self, func, typ) -> Markup:
        typ = self.__INTEGRITY_MAP[typ]
        html = []

        styles = current_app.config['FONTAWESOME_STYLES']
        if 'all' in styles:
            integrity = typ['all']
            html.append(func('all', integrity))
        else:
            html.append(func('fontawesome', typ['fontawesome']))
            for style in styles:
                integrity = typ.get(style, None)
                if integrity is None:
                    raise ValueError('Unknown style: {}'.format(style))
                html.append(func(style, integrity))

        if current_app.config['FONTAWESOME_INCLUDE_V4_SHIMS']:
            integrity = typ['v4-shims']
            html.append(func('v4-shims', integrity))

        return Markup('\n'.join(html))

    def __css(self, style: str, integrity: str) -> str:
        url = '{}/css/{}.css'.format(self.__URL_BASE, style)
        return ('<link rel="stylesheet" href="{}" integrity="{}" crossorigin="anonymous">'
                .format(url, integrity))

    def __js(self, style: str, integrity: str) -> str:
        url = '{}/js/{}.js'.format(self.__URL_BASE, style)
        return ('<script defer src="{}" integrity="{}" crossorigin="anonymous"></script>'
                .format(url, integrity))


class FontAwesome(object):

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

        self._static = StaticCdn()
        self._use_fa = UseFontAwesomeComCdn()

    def init_app(self, app: Flask) -> None:
        if not hasattr(app, 'extensions'):
            app.extensions = {}

        app.extensions['fontawesome'] = self

        app.config.setdefault('FONTAWESOME_INCLUDE_V4_SHIMS', False)
        app.config.setdefault('FONTAWESOME_QUERYSTRING_REVVING', True)
        app.config.setdefault('FONTAWESOME_SERVE_LOCAL', True)
        app.config.setdefault('FONTAWESOME_STYLES', ['solid'])
        app.config.setdefault('FONTAWESOME_TYPE', 'webfont/css')
        app.config.setdefault('FONTAWESOME_USE_MINIFIED', True)

        blueprint = Blueprint(
            'fontawesome',
            __name__,
            static_folder='static',
            static_url_path=app.static_url_path + '/fontawesome')

        app.jinja_env.globals['fontawesome_html'] = fontawesome_html
        app.jinja_env.globals['fontawesome_css'] = fontawesome_css
        app.jinja_env.globals['fontawesome_js'] = fontawesome_js
        app.register_blueprint(blueprint)
