import connexion
import six
import datetime
import secrets
import logging
from flask import session, make_response

from openapi_server.models.message import Message  # noqa: E501
from openapi_server.models.order import Order  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util, server_attr, constants
from openapi_server.database.db_rds import conn
from openapi_server.controllers.security_controller_ import AuthInstance

def admin_login_post(auth_token):  # noqa: E501
    """Log in an admin. Set cookie auth token.

     # noqa: E501

    :rtype: str
    """

    logging.info(f"Attempting to log in admin.")

    # Find user associated with the email
    with conn.cursor() as cursor:
        cursor.execute("SELECT (admin_id, name) FROM Admins WHERE auth_token = ?", [auth_token])
        row = cursor.fetchone()
        if not row:
            raise Exception("user with the provided username does not exist")
        admin_id = row["admin_id"]
        name = row["name"]

        # Set cookie and return the response
        logging.info(f"Succesfully logged in admin '{name}' ({admin_id}).")
        response = make_response(f"Succesfully logged in admin '{name}'.")
        response.set_cookie("admin_token", auth_token)
        return response, 200

def admin_messages_list_get(user):  # noqa: E501
    """admin_messages_list_get

     # noqa: E501


    :rtype: List[Message]
    """
    # conn.execute("SELECT () FROM ")
    # conn.commit()

    return [], 501


def admin_orders_list_get(user):  # noqa: E501
    """admin_orders_list_get

     # noqa: E501


    :rtype: List[Order]
    """
    return [], 501


def admin_reports_list_get(user):  # noqa: E501
    """admin_reports_list_get

     # noqa: E501


    :rtype: List[Order]
    """
    return [], 501

def admin_users_list_get(user):  # noqa: E501
    """admin_users_list_get

     # noqa: E501


    :rtype: List[User]
    """
    results = conn.cusor().execute(
        "SELECT (user_id, name, email, registered_time, delivery_tokens, phone_number, etransfer_email) FROM Users"
    )

    users = [
        User(
            user_id=res[0],
            name=res[1],
            email=res[2],
            registered_time=res[3],
            delivery_tokens=res[4],
            phone_number=res[5],
            etransfer_email=res[6]
        ) for res in results
    ]
    return users, 200

def deployment_get():  # noqa: E501
    """deployment_get

     # noqa: E501


    :rtype: str
    """
    return f"name: {server_attr.deployment_name}\n" + \
        f"uptime: {datetime.datetime.now() - server_attr.start_time}", 200


def message_post(message, user_id=None, email=None):  # noqa: E501
    """message_port

     # noqa: E501

    :param message: Message to send to UniBar.
    :type message: str
    :param user_id: User that wants to send a message.
    :type user_id: 
    :param email: Email of the person sending the message.
    :type email: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        email = str.from_dict(connexion.request.get_json())  # noqa: E501

    # with 

    return "message", 501


def orders_available_get():  # noqa: E501
    """orders_available_get

     # noqa: E501


    :rtype: List[Order]
    """
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT (order_id, orderer_id, deliverer_id, creation_time, deadline_time, claimed_time, delivered_time, order, source, destination, payment_method) WHERE ..."
        )
        results = cursor.fetchall()
        available_orders = [Order.from_dict(res) for res in results]
        return available_orders, 501


def orders_order_id_get(order_id):  # noqa: E501
    """orders_order_id_get

     # noqa: E501

    :param order_id: Identification of the order.
    :type order_id: 

    :rtype: Order
    """

    with conn.cusor() as cursor:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT (order_id, orderer_id, deliverer_id, creation_time, deadline_time, claimed_time, delivered_time, order, source, destination, payment_method) WHERE order_id = ?",
            [order_id]
        )
        res = cursor.fetchone()
        return Order.from_dict(res), 200

def ping_get():  # noqa: E501
    """ping_get

     # noqa: E501


    :rtype: None
    """
    return "ping", 200


def user_info_get(user_id):  # noqa: E501
    """user_info_get

     # noqa: E501

    :param user_id: Identifying the user.
    :type user_id: 

    :rtype: User
    """
    user = conn.cursor().execute(
        "SELECT (user_id, name, email, phone_number, delivery_tokens, etransfer_email) FROM Users WHERE user_id = ?",
        [user_id]
    )
    return user, 501

def user_order_complete_put(user_id, order_id):  # noqa: E501
    """user_order_complete_put

     # noqa: E501

    :param user_id: User whose order is complete and is giving a delivery-token to the deliverer.
    :type user_id: 
    :param order_id: Order that is complete and for which a delivery-token must be transfered.
    :type order_id: 

    :rtype: None
    """
    return 'do some magic!', 501


def user_order_deliver_put(user, user_id, order_id):  # noqa: E501
    """user_order_deliver_put

     # noqa: E501

    :param user_id: User to fulfil the order.
    :type user_id: 
    :param order_id: Order to deliver.
    :type order_id: 

    :rtype: None
    """
    return 'do some magic!', 501


def user_order_report_post(user, user_id, reported_id, order_id, message):  # noqa: E501
    """user_order_report_post

     # noqa: E501

    :param user_id: User that is reporting.
    :type user_id: 
    :param reported_id: User that is reported.
    :type reported_id: 
    :param order_id: Order in which the report happened.
    :type order_id: 
    :param message: Report message from the user reporting.
    :type message: 

    :rtype: None
    """
    return 'do some magic!', 501


def user_order_request_post(user, user_id, order):  # noqa: E501
    """user_order_request_post

     # noqa: E501

    :param user_id: Identifying the user.
    :type user_id: 
    :param order: Delivery request order of the user.
    :type order: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        order = Order.from_dict(connexion.request.get_json())  # noqa: E501

    # Check that user does not have more 


    return 'do some magic!', 501


def user_orders_delivering_get(user, user_id):  # noqa: E501
    """user_orders_delivering_get

     # noqa: E501

    :param user_id: Identifying the user.
    :type user_id: 

    :rtype: List[Order]
    """
    return 'do some magic!', 501


def user_orders_requesting_get(user, user_id):  # noqa: E501
    """user_orders_requesting_get

     # noqa: E501

    :param user_id: Identifying the user.
    :type user_id: 

    :rtype: List[Order]
    """
    return 'do some magic!', 501


def user_update_put(user, user_id, name=None, password=None, phone_number=None, etransfer_email=None):
    """Update user information.

     # noqa: E501


    :rtype: str
    """

    if len(password) < constants.MIN_PASSWORD_LENGTH:
        raise Exception("new password is too short")

    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE Users SET name = COAL WHERE user_id = ?",
            [name, password, phone_number, etransfer_email, AuthInstance(user).id]
        )
        cursor.commit()

        return "Successfully updated the user.", 200 

def users_login_post(body):  # noqa: E501
    """Log in a user. Set cookie auth token.

     # noqa: E501

    :rtype: str
    """

    logging.info(f"Attempting to log in user with email {body['email']}")

    # Find user associated with the email
    with conn.cursor() as cursor:
        cursor.execute("SELECT (user_id, password) FROM Admins WHERE email = ?", [body["email"]])
        row = cursor.fetchone()
        if not row:
            raise Exception("user with the provided username does not exist")
        if row["password"] != body["password"]:
            raise Exception("incorrect user credentials")
        user_id = row["user_id"]
    
        # Create and map auth token to the user in the database
        new_auth_token = secrets.token_hex(constants.AUTH_TOKEN_LENGTH)
        cursor.execute("UPDATE Users SET auth_token = ? WHERE user_id = ?", [new_auth_token, user_id])
        cursor.commit()

        # Set cookie and return the response
        logging.info(f"Succesfully logged in user '{user_id}'.")
        response = make_response(f"Succesfully logged in user '{user_id}'.")
        response.set_cookie("user_token", new_auth_token)
        return response, 200

def users_register_post(user, email, password, name, phone_number):  # noqa: E501
    """Create a new user.

     # noqa: E501

    :param email: Email of the user to create.
    :type email: dict | bytes
    :param password: Password used for user to sign-in with.
    :type password: str
    :param name: Name of the new user.
    :type name: str
    :param phone_number: Phone number of the new user.
    :type phone_number: str

    :rtype: None
    """
    if len(password) < constants.MIN_PASSWORD_LENGTH:
        raise Exception("password for new user is too short")

    if connexion.request.is_json:
        email =  str.from_dict(connexion.request.get_json())  # noqa: E501

    user_id=util.generate_uuid(),   

    # Store the user in the database
    conn.cusor().execute(
        "INSERT INTO Users (user_id, password, name, email, registered_time, delivery_tokens, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?)", 
        [user_id, password, name, email, datetime.datetime.now(), constants.NEW_USER_DELIVERY_TOKENS, phone_number]
    )

    return f"Registered new user {user_id}", 200
