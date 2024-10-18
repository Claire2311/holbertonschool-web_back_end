#!/usr/bin/env python3
"""
Main file
"""


import requests


BASE_URL = 'http://127.0.0.1:8000'


def register_user(email: str, password: str) -> None:
    """test the registration of an user"""
    r = requests.post(
        f'{BASE_URL}/users',
        data={"email": email, "password": password}
    )
    assert r.json()["email"] == email
    assert r.json()["message"] == "user created"


def log_in_wrong_password(email: str, password: str) -> None:
    """test the registration with a wrong password"""
    r = requests.post(
        f'{BASE_URL}/sessions',
        data={"email": email, "password": password}
    )
    assert r.status_code == 401


def log_in(email: str, password: str) -> str:
    """log in the session"""
    r = requests.post(
        f'{BASE_URL}/sessions',
        data={"email": email, "password": password}
    )
    assert r.json()["email"] == email
    assert r.json()["message"] == "logged in"
    assert r.cookies["session_id"]
    return r.cookies["session_id"]


def profile_unlogged() -> None:
    """profile unlogged"""
    r = requests.get(
        f'{BASE_URL}/profile')
    assert r.status_code == 403


def profile_logged(session_id: str) -> None:
    """ profile logged"""
    r = requests.get(
        f'{BASE_URL}/profile', cookies=dict(session_id=session_id)
    )
    assert r.status_code == 200


def log_out(session_id: str) -> None:
    """log out of the session"""
    r = requests.delete(
        f'{BASE_URL}/sessions', cookies=dict(session_id=session_id)
    )
    assert r.json()["message"] == "Bienvenue"


def reset_password_token(email: str) -> str:
    """resest password token"""
    r = requests.post(
        f'{BASE_URL}/reset_password',
        data={"email": email}
    )
    assert r.json()["email"] == email
    assert r.status_code == 200
    return r.json()["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """update password"""
    r = requests.put(
        f'{BASE_URL}/reset_password',
        data={
            "email": email,
            "reset_token": reset_token,
            "new_password": new_password
        }
    )
    assert r.json()["email"] == email
    assert r.json()["message"] == "Password updated"
    assert r.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
