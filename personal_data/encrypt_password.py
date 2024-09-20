#!/usr/bin/env python3
"""hash password"""


import bcrypt


def hash_password(password: str) -> bytes:
    """hash a password"""
    return bcrypt.hashpw(password, bcrypt.gensalt())
