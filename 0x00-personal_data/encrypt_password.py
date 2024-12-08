#!/usr/bin/env python3
"""
Module for handling Personal Data
"""
import bcrypt


def hash_password(password:str) -> str:
    """
    Module for handling Personal Data
    """

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password.decode()
