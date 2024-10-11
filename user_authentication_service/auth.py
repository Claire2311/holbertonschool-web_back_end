#!/usr/bin/env python3
"""Management of authorization"""


import bcrypt


def _hash_password(password: str) -> bytes:
    """hash password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
