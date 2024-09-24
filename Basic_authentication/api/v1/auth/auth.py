#!/usr/bin/env python3
"""class to handle basic authentication"""


from typing import List, TypeVar
from flask import request


class Auth:
    """class to handle basic authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication"""
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        new_path: str

        if path.endswith('/'):
            new_path = path
        else:
            new_path = path + '/'

        if new_path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """manager authorization header"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """manage current user"""
        return None
