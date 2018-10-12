# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, url_for, Markup, current_app

FONTAWESOME_VERSION = '5.3.1'
__version__ = '0.1.2'


class Cdn(object):

    def _check_type(self, typ: str) -> None:
        if typ not in ['webfont/css', 'svg/js']:
            raise ValueError('Illegal parameter for FONTAWESOME_TYPE: {}'.format(typ))


class StaticCdn(Cdn):

    def resources_html(self) -> Markup:
        typ = current_app.config['FONTAWESOME_TYPE']
        self._check_type(typ)
        func = self.__css if typ == 'webfont/css' else self.__js
        use_min = current_app.config['FONTAWESOME_USE_MINIFIED']

        urls = []
        styles = current_app.config['FONTAWESOME_STYLES']
        if 'all' in styles:
            urls.append(func('all', use_min))
        else:
            urls.append(func('fontawesome', use_min))
            for style in styles:
                urls.append(func(style, use_min))

        return Markup('\n'.join(urls))

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
            'regular': 'sha384-ZlNfXjxAqKFWCwMwQFGhmMh3i89dWDnaFU2/VZg9CvsMGA7hXHQsPIqS+JIAmgEq',
            'solid': 'sha384-VGP9aw4WtGH/uPAOseYxZ+Vz/vaTb1ehm1bwx92Fm8dTrE+3boLfF1SpAtB1z7HW',
        },
        'svg/js': {
            'all': 'sha384-kW+oWsYx3YpxvjtZjFXqazFpA7UP/MbiY4jvs+RWZo2+N94PFZ36T6TFkc9O3qoB',
            'brands': 'sha384-2vdvXGQdnt+ze3ylY5ESeZ9TOxwxlOsldUzQBwtjvRpen1FwDT767SqyVbYrltjb',
            'fontawesome': (
                'sha384-2OfHGv4zQZxcNK+oL8TR9pA+ADXtUODqGpIRy1zOgioC4X3+2vbOAp5Qv7uHM4Z8'),
            'regular': 'sha384-sqmLTIuB+bQgkyOcdJ/hAvXl51Z7qqdK/lcH/rt6sdvDKFincQWI+fVgcDZM6NMz',
            'solid': 'sha384-GJiigN/ef2B3HMj0haY+eMmG4EIIrhWgGJ2Rv0IaWnNdWdbWPr1sRLkGz7xfjOFw',
        },
    }

    def resources_html(self) -> Markup:
        typ = current_app.config['FONTAWESOME_TYPE']
        self._check_type(typ)
        func = self.__css if typ == 'webfont/css' else self.__js
        typ = self.__INTEGRITY_MAP[typ]

        urls = []
        styles = current_app.config['FONTAWESOME_STYLES']
        if 'all' in styles:
            integrity = typ['all']
            urls.append(func('all', integrity))
        else:
            urls.append(func('fontawesome', typ['fontawesome']))
            for style in styles:
                integrity = typ.get(style, None)
                if integrity is None:
                    raise ValueError('Unknown style: {}'.format(style))
                urls.append(func(style, integrity))

        return Markup('\n'.join(urls))

    def __css(self, style: str, integrity: str) -> str:
        url = '{}/css/{}.css'.format(self.__URL_BASE, style)
        return ('<link rel="stylesheet" href="{}" integrity="{}" crossorigin="anonymous">'
                .format(url, integrity))

    def __js(self, style: str, integrity: str) -> str:
        url = '{}/js/{}.js'.format(self.__URL_BASE, style)
        return ('<script defer src="{}" integrity="{}" crossorigin="anonymous"></script>'
                .format(url, integrity))


class FontAwesome(object):

    def __init__(self, app: Flask=None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        app.config.setdefault('FONTAWESOME_USE_MINIFIED', True)
        app.config.setdefault('FONTAWESOME_QUERYSTRING_REVVING', True)
        app.config.setdefault('FONTAWESOME_STYLES', ['solid'])
        app.config.setdefault('FONTAWESOME_SERVE_LOCAL', True)
        app.config.setdefault('FONTAWESOME_TYPE', 'webfont/css')

        blueprint = Blueprint(
            'fontawesome',
            __name__,
            static_folder='static',
            static_url_path=app.static_url_path + '/fontawesome')

        static = StaticCdn()
        use_fa = UseFontAwesomeComCdn()

        def fontawesome_html() -> Markup:
            if app.config['FONTAWESOME_SERVE_LOCAL']:
                return static.resources_html()
            else:
                return use_fa.resources_html()

        app.jinja_env.globals['fontawesome_html'] = fontawesome_html
        app.register_blueprint(blueprint)
