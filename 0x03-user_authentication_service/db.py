#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, tuple_
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
        """ Placeholder for documentation"""
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
        except Exception:
            self._session.rollback()
            new_user = None
            raise
        else:
            self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Finds a user based on a set of filters.

        """
        for key, value in kwargs.items():
            if hasattr(User, key):
                user = self.__session.query(User).filter_by(**kwargs).first()
                if user is None:
                    raise NoResultFound
                else:
                    return user

            else:
                raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user based on a set of filters.

        """

        user = self.find_user_by(id=user_id)
        if user is None:
            return
        update_source = {}
        for key, value in kwargs.items():
            if hasattr(User, key):
                update_source[getattr(User, key)] = value
            else:
                raise ValueError()
        self._session.query(User).filter(User.id == user_id).update(
            update_source,
            synchronize_session=False,
        )
        self._session.commit()
