import logging
import secrets

from typing import List
from flask import session, make_response

from openapi_server.database.db_rds import conn
from openapi_server import constants

# For better authenticating users vs. admins
class AuthInstance(object):
    def __init__(self, type, id) -> None:
        # Sanity check that everything's good
        if type != constants.AUTH_TYPE_ADMIN or type != constants.AUTH_TYPE_USER:
            raise Exception("Provided auth type for object is invalid.")
        if len(id) != constants.UUID_LENGTH:
            raise Exception("Provided id is of not correct length.")
        self._type = type
        self._id = id
    
    def type(self) -> str:
        return self._type

    def id(self) -> str:
        return self._id

# Security functions
def info_from_AdminToken(api_key, required_scopes):
    """
    Check and retrieve authentication information from api_key.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.

    :param api_key API key provided by Authorization header
    :type api_key: str
    :param required_scopes Always None. Used for other authentication method
    :type required_scopes: None
    :return: Information attached to provided api_key or None if api_key is invalid or does not allow access to called API
    :rtype: dict | None
    """

    # Compare the admin token to what's stored in the database
    logging.info("Attempting to log in an admin.")
    
    if not api_key:
        raise Exception("an empty apikey was provided when trying to auth an admin")

    with conn.cursor() as cursor:
        cursor.execute("SELECT (admin_id) FROM Admins WHERE auth_token = ?", [api_key])
        row = cursor.fetchone()
        if not row:
            raise Exception("auth token does not map to an admin")

        admin_id = row["admin_id"]
        logging.info(f"Matched admin auth token against admin_id '{admin_id}'")
        return {'sub': AuthInstance(type=constants.AUTH_TYPE_ADMIN, id=admin_id)}

def info_from_UserLogin(username, password, required_scopes):
    """
    Check and retrieve authentication information from basic auth.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.

    :param username login provided by Authorization header
    :type username: str
    :param password password provided by Authorization header
    :type password: str
    :param required_scopes Always None. Used for other authentication method
    :type required_scopes: None
    :return: Information attached to user or None if credentials are invalid or does not allow access to called API
    :rtype: dict | None
    """
    logging.info(f"Logged in user with username '{username}'")
    
    logging.info("Attempting to log in an admin.")
    
    with conn.cursor() as cursor:
        cursor.execute("SELECT (user_id, password) FROM Admins WHERE username = ?", [username])
        row = cursor.fetchone()
        if not row:
            raise Exception("user with the provided username does not exist")
        if row["password"] != password:
            raise Exception("incorrect user credentials")
        
        user_id = row["user_id"]
        logging.info(f"Matched admin api token against user_id '{user_id}'")
        return {'sub': AuthInstance(type=constants.AUTH_TYPE_USER, id=user_id)}

def info_from_UserAuth(api_key, required_scopes):
    """
    Check and retrieve authentication information from api_key.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.

    :param api_key API key provided by Authorization header
    :type api_key: str
    :param required_scopes Always None. Used for other authentication method
    :type required_scopes: None
    :return: Information attached to provided api_key or None if api_key is invalid or does not allow access to called API
    :rtype: dict | None
    """

    # Compare the admin token to what's stored in the database
    logging.info("Attempting to log in a user.")
    
    if not api_key:
        raise Exception("an empty apikey was provided when trying to auth a user")

    with conn.cursor() as cursor:
        cursor.execute("SELECT (used_id) FROM Users WHERE auth_token = ?", [api_key])
        row = cursor.fetchone()
        if not row:
            raise Exception("auth token does not map to user")

        used_id = row["used_id"]
        logging.info(f"Matched admin auth token against used_id '{used_id}'")
        return {'sub': AuthInstance(type=constants.AUTH_TYPE_USER, id=used_id)}
