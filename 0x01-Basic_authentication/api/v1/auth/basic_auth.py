#!/usr/bin/env python3
""" Module of Index views
"""

from flask import request
from typing import TypeVar, List, Tuple
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Placehoder for documentation"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Placehoder for documentation"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None

        encoded = authorization_header.split(' ', 1)[1]
        return encoded

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Placehoder for documentation"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None

        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = base64.b64decode(encoded)
            decoded = decoded64.decode('utf-8')

            return decoded
        except BaseException:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> Tuple[str, str]:
        """
        Returns the user email and password from the
        Base64 decoded value
        """

        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)

        return credentials[0], credentials[1]
