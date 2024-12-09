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
        return False
    
    def authorization_header(self, request=None) -> str:
        """ Module of Index views
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """ Module of Index views
        """
        return None
