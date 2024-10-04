#!/usr/bin/env python3
"""class to handle basic authentication"""


from os import getenv
from typing import List, TypeVar
from flask import request


class Auth:
    """class to handle basic authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication"""
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        new_path: str

        if path.endswith('/'):
            new_path = path
        else:
            new_path = path + '/'

        if new_path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """manager authorization header"""
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """manage current user"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None

        cookie_name = getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
