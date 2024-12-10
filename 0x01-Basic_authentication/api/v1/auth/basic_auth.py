#!/usr/bin/env python3
""" Module of Index views
"""

from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth

class BasicAuth(Auth):
    pass