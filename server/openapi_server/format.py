# This file enforces formats

import re
from openapi_server import constants

def enforce_phone_number(phone_number: str):
    if phone_number is not None and not re.search(r'^\d{10}$', phone_number):  # noqa: E501
        raise ValueError("Invalid value for `phone_number`, must be a follow pattern or equal to `/^\d{10}$/`")  # noqa: E501

def enforce_password(password: str):
    if len(password) < constants.MIN_PASSWORD_LENGTH:
        raise ValueError("Password is not of sufficient length.")
