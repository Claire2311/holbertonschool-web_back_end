#!/usr/bin/env python3
""" Module of session views
"""
from os import getenv
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def view_auth() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      -
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or email == '':
        return jsonify({"error": "email missing"}), 400

    if not password or password == '':
        return jsonify({"error": "password missing"}), 400

    user = User()
    # try:
    user_search = User.search({'email': email})
    # except Exception:
    if not user_search:
        return jsonify({"error": "no user found for this email"}), 404

    for user in user_search:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 404

    # if not user:
    #     return jsonify({"error": "no user found for this email"}), 404

    # if not User.is_valid_password(password):
    #     return jsonify({"error": "wrong password"}), 404

    if user_search:
        from api.v1.app import auth
        session_id = auth.create_session(user_search[0].id)
        cookie_name = getenv('SESSION_NAME')
        response_to_send = jsonify(user.to_json())
        print('response_to_send', response_to_send)
        print(type(response_to_send))
        response_to_send.set_cookie(cookie_name, session_id)
        return response_to_send
