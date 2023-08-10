#!/usr/bin/env python3
"""Basic authentication using sessions"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """SessionAuth class"""
    user_id_by_session_id = {}

    def create_session(self,
                       user_id: str = None) -> str:
        """Creates a new session
        Args:
            user_id (str, optional): the current user. Defaults to None.
        Returns:
            str: the session_id
        """
        if not ((user_id) and
                (isinstance(user_id, str))):
            return None
        ses_id = uuid.uuid4()
        self.user_id_by_session_id[str(ses_id)] = user_id
        return str(ses_id)
