#!/usr/bin/env python3
"""hash password"""


import bcrypt


def hash_password(password: str) -> bytes:
    """hash a password"""
    return bcrypt.hashpw(password, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """check if the hashed password matches the password"""
    matched_password = bcrypt.checkpw(password, hashed_password)
    return matched_password
