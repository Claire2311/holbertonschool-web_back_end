#!/usr/bin/env python3
""" App module
"""
import pytz
from pytz.exceptions import UnknownTimeZoneError
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


class Config:
    """configuration of languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """determine the locale to use"""
    locale = request.args.get('locale')
    if locale is not None and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        if (g.user.get("locale") is not None and
                g.user.get("locale") in app.config['LANGUAGES']):
            return g.user.get("locale")

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """get the timezone of the user"""
    timezone = request.args.get('timezone')
    if timezone is not None:
        try:
            tz = pytz.timezone(timezone)
            return tz
        except pytz.UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']

    if g.user:
        if g.user.get("timezone") is not None:
            try:
                tz = pytz.timezone(timezone)
                return tz
            except pytz.UnknownTimeZoneError:
                return app.config['BABEL_DEFAULT_TIMEZONE']


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """Get the user"""
    try:
        user_id = int(user_id)
        return users.get(user_id)
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """check if there is an user"""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route("/")
def hello() -> str:
    """ return index template
    """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")
