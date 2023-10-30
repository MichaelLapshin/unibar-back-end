# Define the constants used in the back-end server

NEW_USER_DELIVERY_TOKENS = 1
UUID_LENGTH = 36
ORDER_MAX_REQUEST_HOURS = 12
ORDER_MAX_CONCURRENT_CLAIM = 2
ORDER_MAX_DELIVERY_MINUTES = 60

# Authentication info
'''
    {
        "type": <AUTH_TYPE_ADMIN | AUTH_TYPE_USER>
        "id": <id>
    }
'''
AUTH_TYPE_ADMIN = "admin"
AUTH_TYPE_USER = "user"
AUTH_TOKEN_LENGTH = 32
MIN_PASSWORD_LENGTH = 8
MAX_COOKIE_AGE_HOURS = 24*365