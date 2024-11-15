#!/usr/bin/env python3
""" App module
"""
from flask import Flask, render_template, request
from flask_babel import Babel


def get_locale():
    """get the default language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)


@app.route("/")
def hello() -> str:
    """ return index template
    """
    return render_template("0-index.html")


class Config:
    """configuration of languages"""
    LANGUAGES = ["en", "fr"]


babel = Babel(app, locale_selector="en",  timezone_selector="UTC")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")
