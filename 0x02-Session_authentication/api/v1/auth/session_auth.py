#!/usr/bin/env python3
"""THis module sotrs our basic session auth class"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid
from typing import TypeVar


class SessionAuth(Auth):
    """A session authentication method"""
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

    def user_id_for_session_id(self,
                               session_id: str = None) -> str:
        """Gets the user_id for a particular session
        Args:
            session_id (str, optional): the session id. Defaults to None.
        Returns:
            str: the user associated with the session id
        """
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user
        Returns:
            _type_: the User instance
        """
        s_od = self.session_cookie(request)
        if not s_od:
            return None
        user_id = self.user_id_for_session_id(s_od)
        if not user_id:
            return None
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """Destroys or deletes a session

        Args:
            request (_type_, optional): the request.

        Returns:
            bool: if the session was deleted
        """
        if not request:
            return False
        session = self.session_cookie(request)
        if not session:
            return False
        user_id = self.user_id_for_session_id(session)
        if not user_id:
            return False
        self.user_id_by_session_id.pop(session)
        return True
