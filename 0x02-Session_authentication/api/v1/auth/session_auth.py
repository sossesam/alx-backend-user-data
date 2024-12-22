#!/usr/bin/env python3
""" Module of Index views
"""
from api.v1.auth.auth import Auth
import uuid

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

        
