#!/usr/bin/env python3
"""
Module for handling Personal Data
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Module for handling Personal Data
    """

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates the provided password matches the hashed password """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
