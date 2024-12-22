#!/usr/bin/env python3
""" Module of Index views
"""

from flask import request
from typing import TypeVar, List
from os import getenv


class Auth:
    """ Module of Index views
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires auth """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        for link in excluded_paths:
            if link[-1] != "/":
                link = link + "/"

        if path[-1] != "/":
            path = path + "/"

        if path in excluded_paths:
            return False
        else:
            return True

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

    def session_cookie(self, request=None):
        """ Module of Index views
        """
        if request is None:
            return None

        session_name = getenv("SESSION_NAME")
        session_cookie = request.cookies.get(session_name)
        return session_cookie
