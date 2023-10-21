from typing import List

from openapi_server.database.db_rds import db
from openapi_server import constants
from openapi_server.logger import log

# For better authenticating users and admins
class AuthInstance(object):
    def __init__(self, type: str, id: str) -> None:
        # Sanity check that everything's good
        if type != constants.AUTH_TYPE_ADMIN and type != constants.AUTH_TYPE_USER:
            raise Exception("Provided auth type for object is invalid.")
        if len(id) != constants.UUID_LENGTH:
            raise Exception("Provided id is of not correct length.")
        self._type = type
        self._id = id
    
    @property
    def type(self) -> str:
        return self._type

    @property
    def id(self) -> str:
        return self._id

def info_from_AdminAuth(api_key: str, required_scopes):
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
    log.info("Authenticating an admin...")
    assert api_key, "an empty apikey was provided when trying to auth an admin"

    with db.conn.cursor() as cursor:
        cursor.execute("SELECT admin_id, name FROM Admins WHERE auth_token = %s", [api_key])
        row = cursor.fetchone()
        assert row, "auth token does not map to an admin"

        admin_id = row["admin_id"]
        name = row["name"]
        log.info(f"Successfully authenticated admin '{name}' ({admin_id}).")
        return {'sub': AuthInstance(type=constants.AUTH_TYPE_ADMIN, id=admin_id)}

def info_from_UserAuth(api_key: str, required_scopes):
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
    log.info("Authenticating a user...")
    assert api_key, "an empty apikey was provided when trying to auth a user"

    with db.conn.cursor() as cursor:
        cursor.execute("SELECT user_id, name FROM Users WHERE auth_token = %s", [api_key])
        row = cursor.fetchone()
        assert row, "auth token does not map to a user"

        user_id = row["user_id"]
        name = row["name"]
        log.info(f"Successfully authenticated user '{name}' ({user_id}).")
        return {'sub': AuthInstance(type=constants.AUTH_TYPE_USER, id=user_id)}
