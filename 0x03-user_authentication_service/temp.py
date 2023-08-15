#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from typing import Union, Optional
from user import Base, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


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

    def add_user(self, email: str, hashed_password: str
                 ) -> Optional[User]:
        """Adds a new user to the database
        Args:
            email (str): the user's email
            hashed_password (str): the encoded password
        Returns:
            Union[User, None]: the user or none
        """
        user = User()
        user.email = email
        user.hashed_password = hashed_password
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kw) -> User:
        """Retrieves a user from the database
        Raises:
            NoResultFound: If no result is found
        Returns:
            User if found
        """
        user = self._session.query(User).filter_by(**kw).one()
        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id: str, **kw) -> None:
        """Updates a user
        Args:
            user_id (str): the user to be updated
        Raises:
            ValueError: if the field doesn't exist for
            the user
        """
        try:
            user = self.find_user_by(id=user_id)
            for k, v in kw.items():
                if hasattr(user, k):
                    print("yes")
                    setattr(user, k, v)
                # else:
                #     raise ValueError
            self._session.commit()
        except:
            return
