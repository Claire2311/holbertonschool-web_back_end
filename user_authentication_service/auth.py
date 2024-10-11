#!/usr/bin/env python3
"""Management of authorization"""


import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """hash password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register an user in DB"""
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        hashed_password = _hash_password(password)
        user = self._db.add_user(email, hashed_password)
        return user
# Nous utilisons try/catch car si find_user_by ne trouve pas d'utilisateur,
# une exception NoResultFound serait levée, interrompant le programme.
# Le bloc try/except permet d'éviter cela en capturant l'exception
# et en permettant la création d'un nouvel utilisateur.

    def valid_login(self, email: str, password: str) -> bool:
        """check password"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                if bcrypt.checkpw(password.encode(), user.hashed_password):
                    return True
                else:
                    return False
        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        """generate a new uuid"""
        return uuid.uuid4()
