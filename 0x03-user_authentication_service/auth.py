#!/usr/bin/env python3
"""Authentication module"""
import bcrypt
from db import DB
from user import User
import uuid


def _hash_password(password: str) -> bytes:
    """This hashes a password using bcrypt
    Args:
        password (str): the password to be hashed
    Returns:
        bytes: the hashed password in bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
