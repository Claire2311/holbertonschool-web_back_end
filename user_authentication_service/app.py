#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from flask_cors import (CORS, cross_origin)
from auth import Auth

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

AUTH = Auth()


@app.route('/')
def welcome() -> str:
    """welcome message"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    """register user"""
    email = request.form['email']
    password = request.form['password']
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    if user:
        return jsonify({"email": email, "message": "user created"})


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """create a new session"""
    email = request.form['email']
    password = request.form['password']
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    res = make_response(
        jsonify({"email": email, "message": "logged in"})
    )
    res.set_cookie("session_id", session_id)
    return res


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """logout of the current session"""
    session_id = request.cookies.get("session_id")

    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """check if user exists"""
    session_id = request.cookies.get("session_id")

    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token() -> str:
    """reset password token"""
    email = request.form['email']
    try:
        new_token = AUTH.get_reset_password_token(email)
        if new_token:
            return jsonify({"email": email, "reset_token": new_token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password() -> str:
    """update password"""
    email = request.form['email']
    reset_token = request.form['reset_token']
    new_password = request.form['new_password']
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")
