#!/usr/bin/env python3
""" Module of Index views
"""

from flask import request
from typing import TypeVar, List


class Auth:
    """ Module of Index views
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Module of Index views
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[len(path)-1] != "/":
            path += "/"

        if path in excluded_paths:
            return False
        if path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """ Module of Index views
        """
        key = "Authorization"
        if request is None or key not in request.headers:
            return None
        
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> None:
        """ Module of Index views
        """
        return None
