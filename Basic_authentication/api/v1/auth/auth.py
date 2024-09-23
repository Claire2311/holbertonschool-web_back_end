#!/usr/bin/env python3
"""class to handle basic authentication"""


from flask import request
from typing import List, TypeVar


class Auth:
    """class to handle basic authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """manager authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """manage current user"""
        return None
