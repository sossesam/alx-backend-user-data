#!/usr/bin/env python3
""" Module of Index views
"""
from api.v1.auth.auth import Auth
import uuid
from os import getenv
from models.user import User


class SessionAuth(Auth):
    """ Module of Index views
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Module of Index views
        """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None

        self.session_id = str(uuid.uuid4())
        self.user_id_by_session_id[self.session_id] = user_id
        return self.session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Module of Index views
        """
        if session_id is None:
            return None

        if type(session_id) is not str:
            return None

        if session_id in self.user_id_by_session_id.keys():
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Module of Index views
        """
        session_id = self.session_cookie(request)
        if not session_id:
            return
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)

        return user

    def destroy_session(self, request=None):
        """
        Deletes a user session
        """
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_cookie]
        return True
