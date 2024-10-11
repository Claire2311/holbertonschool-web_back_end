#!/usr/bin/env python3
"""DB module
"""
from typing import Any
from sqlalchemy import create_engine, insert, Column, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add an user in the DB"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs: dict[str, Any]) -> User:
        """
        takes in arbitrary keyword arguments and returns the first row found
        in the users table as filtered by the method’s input arguments
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound
            return user
        except NoResultFound as e:
            raise NoResultFound("No user found with the given criteria") from e
        except InvalidRequestError as e:
            raise InvalidRequestError("Invalid query arguments") from e

    def update_user(self, user_id: int, **kwargs: dict[str, Any]) -> None:
        """Update a user in the DB"""
        try:
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise NoResultFound("No user found with the given criteria")

        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                raise ValueError(f"Invalid attribute: {key}")

        self._session.commit()
