#!/usr/bin/env python3
""" App module
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """configuration of languages"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = "en"
app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"
babel = Babel(app)


@app.route("/")
def hello() -> str:
    """ return index template
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")
