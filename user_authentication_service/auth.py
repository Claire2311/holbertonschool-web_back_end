#!/usr/bin/env python3
"""Management of authorization"""


import uuid
import bcrypt
from typing import Optional
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """hash password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """generate a new uuid"""
    return str(uuid.uuid4())


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

    def create_session(self, email: str) -> str:
        """create ID session"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """find user by session ID """
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """reset password token"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                new_token = _generate_uuid()
                self._db.update_user(user.id, reset_token=new_token)
                return new_token
        except NoResultFound:
            raise ValueError

    def destroy_session(self, user_id: int) -> None:
        """destroy the current session"""
        self._db.update_user(user_id, session_id=None)
