# This file enforces formats

import re
from openapi_server import constants

def enforce_phone_number(phone_number: str, ignoreNone: bool):
    if ignoreNone and phone_number == None:
        return
    if phone_number is not None and not re.search(r'^\d{10}$', phone_number):  # noqa: E501
        raise ValueError("Invalid value for `phone_number`, must be 10 digits long.")  # noqa: E501

def enforce_password(password: str, ignoreNone: bool):
    if ignoreNone and password == None:
        return
    if len(password) < constants.MIN_PASSWORD_LENGTH:
        raise ValueError(f"Password is too short, must be at least {constants.MIN_PASSWORD_LENGTH} characters long.")
