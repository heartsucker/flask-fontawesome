# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_fontawesome import FontAwesome


def create_app() -> Flask:
    app = Flask(__name__)
    FontAwesome(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
