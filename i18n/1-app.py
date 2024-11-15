#!/usr/bin/env python3
""" App module
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app, locale_selector="en")


@app.route("/")
def hello() -> str:
    """ return index template
    """
    return render_template("0-index.html")


class Config:
    """configuration of languages"""
    LANGUAGES = ["en", "fr"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")
