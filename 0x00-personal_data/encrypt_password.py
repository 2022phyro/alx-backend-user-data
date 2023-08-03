#!/usr/bin/env python3
"""This file deals with password validation
"""
from bcrypt import hashpw, gensalt, checkpw


def hash_password(password: str) -> bytes:
    """This function hashes a password using bcrypt
    hashpw and gensalt
    Args:
        password (str): the password to be hashed
    Returns:
        bytes: the hashed password
    """
    result = hashpw(password.encode('utf-8'), gensalt())
    return result


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if a password is the same as the hashed password
    Args:
        hashed_password (bytes): the password which is the yardstick
        password (str): the password to check
    Returns:
        bool: True or false depending on outcome
    """
    return checkpw(password.encode('utf-8'), hashed_password)
