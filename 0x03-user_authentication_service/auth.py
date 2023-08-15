#!/usr/bin/env python3
"""Authentication module"""
import bcrypt
from db import DB, User, NoResultFound, InvalidRequestError


def _hash_password(password: str) -> str:
    """This hashes a password using bcrypt
    Args:
        password (str): the password to be hashed
    Returns:
        bytes: the hashed password in bytes
    """
    pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return pwd


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pwd = _hash_password(password)
            user = self._db.add_user(email, pwd)
            return user
