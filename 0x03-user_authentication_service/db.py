#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError


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
        """ Placeholder for documentation"""
        
        for key in kwargs.keys():
            if not hasattr(User, key):
                raise InvalidRequestError
        
        user = self.__session.query(User).filter_by(**kwargs).first()

        if user:
            return user
        raise NoResultFound
