#!/usr/bin/env python3
""" Module of Index views
"""

from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Placehoder for documentation"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        
        encoded = authorization_header.split(' ', 1)[1]
        return encoded
