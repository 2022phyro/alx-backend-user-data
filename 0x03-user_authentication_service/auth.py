#!/usr/bin/env python3
"""Authentication module"""
import bcrypt


def _hash_password(password: str) -> str:
    """This hashes a password using bcrypt
    Args:
        password (str): the password to be hashed
    Returns:
        bytes: the hashed password in bytes
    """
    pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return pwd
