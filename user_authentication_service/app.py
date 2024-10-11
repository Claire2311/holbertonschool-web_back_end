#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort, make_response
from flask_cors import (CORS, cross_origin)
from auth import Auth

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

AUTH = Auth()


@app.route('/')
def welcome():
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
    print(AUTH.valid_login(email, password))
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    print(session_id)
    res = make_response(
        jsonify({"message": "Login in", "email": email})
    )
    print(res)
    res.set_cookie("session_id", session_id)
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")
