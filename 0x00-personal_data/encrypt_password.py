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
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

    return bytes(hashed_password)
