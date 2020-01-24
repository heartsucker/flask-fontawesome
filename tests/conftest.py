import pytest
from flask import Flask, render_template
from flask_fontawesome import FontAwesome


@pytest.fixture(scope='function')
def app():
    app = Flask(__name__)
    FontAwesome(app)

    @app.route('/')
    def index():
        return render_template('simple.html')

    return app
