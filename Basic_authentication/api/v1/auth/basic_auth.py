#!/usr/bin/env python3
"""class to handle basic authentication"""

import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """class that handles basic authentication"""

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        returns the Base64 part of the Authorization header
        """
        if (authorization_header is None or
                not isinstance(authorization_header, str) or
                not authorization_header.startswith('Basic ')):
            return None
        else:
            return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        returns the decoded value of a Base64 string
        base64_authorization_header
        """
        if (base64_authorization_header is None or 
                not isinstance(base64_authorization_header, str)):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """returns the user email and password from the Base64 decoded value"""
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str) or
                ':' not in decoded_base64_authorization_header):
            return None, None
        else:
            user_credentials = decoded_base64_authorization_header.split(":")
            return user_credentials[0], user_credentials[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        user = User()
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            user_search = User.search({'email': user_email})
        except Exception:
            return None

        for user in user_search:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieves the User instance"""
        auth_header = self.authorization_header(request)
        print('auth_header', auth_header)
        b64_auth = self.extract_base64_authorization_header(auth_header)
        print('b64_auth', b64_auth)
        decoded_auth = self.decode_base64_authorization_header(b64_auth)
        print('decoded_auth', decoded_auth)
        email, password = self.extract_user_credentials(decoded_auth)
        print('email', email)
        print('password', password)
        return self.user_object_from_credentials(email, password)
