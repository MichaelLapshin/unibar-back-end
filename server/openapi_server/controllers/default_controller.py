import connexion
import six
from datetime import datetime
import secrets
import logging
from flask import session, make_response, request

from openapi_server.models.body_message import BodyMessage
from openapi_server.models.body_users_register import BodyUsersRegister
from openapi_server.models.body_users_login import BodyUsersLogin
from openapi_server.models.body_user_update import BodyUserUpdate
from openapi_server.models.body_order_create import BodyOrderCreate
from openapi_server.models.body_order_claim import BodyOrderClaim
from openapi_server.models.body_order_unclaim import BodyOrderUnclaim
from openapi_server.models.body_order_report import BodyOrderReport
from openapi_server.models.body_order_complete import BodyOrderComplete
from openapi_server.models.body_admin_login import BodyAdminLogin

from openapi_server.models.message import Message  # noqa: E501
from openapi_server.models.order import Order  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server.models.report import Report  # noqa: E501
from openapi_server import util, server_attr, constants
from openapi_server.database.db_rds import db
from openapi_server.controllers.security_controller_ import AuthInstance

log = logging.getLogger()

def admin_login_post(body):  # noqa: E501
    """admin_login_post

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    
    log.info(f"Attempting to log in admin.")

    if connexion.request.is_json:
        body = BodyAdminLogin.from_dict(connexion.request.get_json())  # noqa: E501

    # Find user associated with the email
    with db.conn().cursor() as cursor:
        cursor.execute("SELECT (admin_id, name) FROM Admins WHERE auth_token = ?", [body.admin_token()])
        row = cursor.fetchone()
        assert row, "admin with the provided api key does not exist"

        admin_id = row["admin_id"]
        name = row["name"]

        # Set cookie and return the response
        log.info(f"Succesfully logged in admin '{name}' ({admin_id}).")
        response = make_response(f"Succesfully logged in admin '{name}'.")
        response.set_cookie("admin_token", body.admin_token())
        return response, 200


def admin_messages_list_get():  # noqa: E501
    """admin_messages_list_get

     # noqa: E501


    :rtype: List[Message]
    """
    with db.conn().cursor() as cursor:
        cursor.execute("SELECT * FROM Messages")
        results = cursor.fetchall()
        messages = [Message.from_dict(res) for res in results]
        return messages, 200


def admin_orders_list_get():  # noqa: E501
    """admin_orders_list_get

     # noqa: E501


    :rtype: List[Order]
    """
    with db.conn().cursor() as cursor:
        cursor.execute("SELECT * FROM Orders")
        results = cursor.fetchall()
        orders = [Order.from_dict(res) for res in results]
        return orders, 200


def admin_reports_list_get():  # noqa: E501
    """admin_reports_list_get

     # noqa: E501

    :rtype: List[Order]
    """
    with db.conn().cursor() as cursor:
        cursor.execute("SELECT * FROM Reports")
        results = cursor.fetchall()
        reports = [Report.from_dict(res) for res in results]
        return reports, 200


def admin_users_list_get():  # noqa: E501
    """admin_users_list_get

     # noqa: E501

    :rtype: List[User]
    """
    with db.conn().cursor() as cursor:
        cursor.execute("SELECT (user_id, name, email, registered_time, delivery_tokens, phone_number, etransfer_email) FROM Users")
        results = cursor.fetchall()
        users = [User.from_dict(res) for res in results]
        return users, 200

def shutdown_get():
    """shutdown_get

     # noqa: E501

    :rtype: None
    """
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Successfully shut down the server.", 200

def deployment_get():  # noqa: E501
    """deployment_get

     # noqa: E501

    :rtype: str
    """
    return f"name: {server_attr.deployment_name}\n" + \
        f"uptime: {datetime.now() - server_attr.start_time}", 200


def message_post(body):  # noqa: E501
    """message_post

     # noqa: E501

    :param body, REST body contents

    :rtype: None
    """

    if connexion.request.is_json:
        body = BodyMessage.from_dict(connexion.request.get_json())  # noqa: E501

    with db.conn().cursor() as cursor:
        cursor.execute(
            "INSERT INTO Messages (message_id, user_id, email, message, time) VALUES (?, ?, ?, ?, ?)", 
            [
                util.generate_uuid(),
                body.user_id(),
                body.email(),
                body.message(),
                datetime.now()
            ]
        )
        cursor.commit()

    return "Successfully sent a message to UniBar.", 200


def order_complete_put(user: AuthInstance, body):  # noqa: E501
    """order_complete_put

     # noqa: E501

    :rtype: None
    """
    assert user.type() == constants.AUTH_TYPE_USER, "requesting order complete by a non-user"
    
    if connexion.request.is_json:
        body = BodyOrderComplete.from_dict(connexion.request.get_json())  # noqa: E501

    with db.conn().cursor() as cursor:
        # Check that the order is being delivered
        cursor.execute("SELECT * FROM Orders WHERE order_id = ?", [body.order_id()])
        order = Order.from_dict(cursor.fetchone())
        assert order.status() == Order.STATUS_CLAIMED, "Order must be first claimed to be complete."
        assert order.orderer_id() == user.id(), "Only the orderer can mark the delivery as complete."

        # Transfer delivery token from orderer to deliverer
        cursor.execute("UPDATE Users SET delivery_tokens = delivery_tokens - 1 WHERE user_id = ?", [order.orderer_id()])
        cursor.execute("UPDATE Users SET delivery_tokens = delivery_tokens + 1 WHERE user_id = ?", [order.deliverer_id()])
        cursor.execute("UDPATE Orders SET delivered_time = ? WHERE order_id = ?", [datetime.now()])
        cursor.commit()

        return f"Successfully marked order {order.order_id()} as complete.", 200


def order_claim_put(user: AuthInstance, body):  # noqa: E501
    """order_claim_put

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    assert user.type() == constants.AUTH_TYPE_USER

    if connexion.request.is_json:
        body = BodyOrderClaim.from_dict(connexion.request.get_json())  # noqa: E501

    with db.conn().cursor() as cursor:
        # Check that the order is available
        cursor.execute("SELECT * FROM Orders WHERE order_id = ?", body.order_id())
        order = Order.from_dict(cursor.fetchone())
        assert order.status() == Order.STATUS_AVAILABLE
        assert order.orderer_id() != user.id(), "Users cannot deliver to themselves."

        # Claim the order
        cursor.execute(
            "UPDATE Orders SET deliverer_id = ?, claimed_time = ? WHERE order_id = ?",
            [user.id(), datetime.now(), body.order_id()]
        )
        cursor.commit()
    
    return "Successfully claimed the order", 200


def order_unclaim_put(user: AuthInstance, body):
    """order_unclaim_put

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        body = BodyOrderUnclaim.from_dict(connexion.request.get_json())  # noqa: E501

    with db.conn().cursor() as cursor:
        # Assert that the order to undeliver is being delivered by the user.
        cursor.execute(
            "SELECT (deliverer_id) FROM Orders WHERE order_id = ?", 
            [body.order_id()]
        )
        order = Order.from_dict(cursor.fetchone())
        assert order.deliverer_id() == user.id(), "Cannot undeliver an order not deliverying."
        assert order.status() == Order.STATUS_CLAIMED, "Cannot undeliver an unclaimed order."

        # Update the order to nullify the deliverer column
        cursor.execute(
            "UPDATE Orders SET deliverer_id = ?, claimed_time = ? WHERE order_id = ?",
            [None, None, body.order_id()]
        )
        cursor.commit()


    return "Successfully unclaimed the order.", 200


def order_order_id_get(order_id):  # noqa: E501
    """order_order_id_get

     # noqa: E501

    :param order_id: The ID of the order which the client wants to see its info.
    :type order_id: 

    :rtype: Order
    """
    with db.conn().cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Orders WHERE order_id = ?", 
            [order_id]
        )
        order = cursor.fetchone()
        assert order, f"did not find order with ID {order_id}"
        return Order.from_dict(order), 200

def order_report_post(user: AuthInstance, body):  # noqa: E501
    """order_report_post

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = BodyOrderReport.from_dict(connexion.request.get_json())  # noqa: E501
    
    assert user.type == constants.AUTH_TYPE_USER, "not a user"

    with db.conn().cursor() as cursor:
        # Validate that the reporter_user_id and reported_user_id are part of the order
        cursor.execute(
            "SELECT (orderer_id, reported_id) FROM Orders WHERE order_id = ?",
            [body.order_id()]
        )
        order = Order.from_dict(cursor.fetchone())
        assert order.orderer_id() == user.id()
        assert order.deliverer_id() == body.reported_id()    

        # Create order
        cursor.execute(
            "INSERT INTO Reports (report_id, reporter_user_id, reported_user_id, order_id, time, message) VALUES (?, ?, ?, ?, ?, ?)",
            [
                util.generate_uuid(),
                user.id(),
                body.reported_id(),
                body.order_id(),
                datetime.now(),
                body.message()
            ]
        )
        cursor.commit()

        # TODO: add logic to notify admins of the report

        return f"Successfully reported user {body.reported_id()}.", 200
        

def order_create_post(user: AuthInstance, body):  # noqa: E501
    """order_create_post

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    assert user.type == constants.AUTH_TYPE_USER, "not a user"

    if connexion.request.is_json:
        body = BodyOrderCreate.from_dict(connexion.request.get_json())  # noqa: E501

    with db.conn().cursor() as cursor:
        # Count number of active orders that user is requesting
        # TODO: make query more efficient by fetching orders using boolean logic instead of fetching all
        cursor.execute("SELECT * FROM Orders WHERE orderer_id = ?", [user.id()])
        results = cursor.fetchall()
        orders = filter(
            [Order.from_dict(res) for res in results], 
            lambda o: o.orderer_id() == user.id() and \
                (o.status() == Order.STATUS_CLAIMED or o.status() == Order.STATUS_AVAILABLE)
        )

        # Check if user has tokens to use on the delivery
        cursor.execute(
            "SELECT (delivery_tokens) FROM Users WHERE user_id = ?",
            [user.id()]
        )
        user = User.from_dict(cursor.fetchone())
        if user.delivery_tokens() <= len(orders):
            return "Not enough delivery tokens.", 406

        # Create order
        cursor.execute(
            "INSERT INTO Orders (order_id, orderer_id, creation_time, deadline_time, order, source, destination, payment_method) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            [
                util.generate_uuid(),
                user.id(),
                datetime.now(),
                body.deadline_time(),
                body.order(),
                body.source(),
                body.destination(),
                body.payment_method()
            ]
        )
        cursor.commit()

    return "Successfully created a delivery request.", 200


def orders_available_get():  # noqa: E501
    """orders_available_get

     # noqa: E501


    :rtype: List[Order]
    """

    with db.conn().cursor() as cursor:
        # TODO: make query more efficient by fetching orders using boolean logic instead of fetching all
        cursor.execute("SELECT * FROM Orders")
        results = cursor.fetchall()
        orders = filter(
            [Order.from_dict(res) for res in results], 
            lambda o: o.status() == Order.STATUS_AVAILABLE
        )
        return orders, 200


def ping_get():  # noqa: E501
    """ping_get

     # noqa: E501


    :rtype: str
    """
    return "ping", 200


def user_user_id_get(user_id):  # noqa: E501
    """user_user_id_get

     # noqa: E501

    :param user_id: User ID of the user to identify who&#39;s info to get.
    :type user_id: 

    :rtype: User
    """
    
    with db.conn().cursor() as cursor:
        cursor.execute("SELECT (user_id, name, email, registered_time, delivery_tokens, phone_number, etransfer_email) FROM Users WHERE user_id = ?", [user_id])
        row = cursor.fetchone()
        assert row, f"Could not find user with id {user_id}"
        return User.from_dict(row), 200


def user_user_id_orders_claimed_get(user_id):  # noqa: E501
    """user_user_id_orders_claimed_get

     # noqa: E501

    :param user_id: User ID of which we want to see the orders they are currently claiming.
    :type user_id: 

    :rtype: List[Order]
    """

    with db.conn().cursor() as cursor:
        # TODO: make query more efficient by fetching orders using boolean logic instead of fetching all
        cursor.execute("SELECT * FROM Orders WHERE deliverer_id = ?", [user_id])
        results = cursor.fetchall()
        orders = filter(
            [Order.from_dict(res) for res in results], 
            lambda o: o.status() == Order.STATUS_CLAIMED and o.deliverer_id() == user_id
        )
        return orders, 200


def user_user_id_orders_active_get(user_id):  # noqa: E501
    """user_user_id_orders_active_get

     # noqa: E501

    :param user_id: User ID of which we want to see the orders they are requesting.
    :type user_id: 

    :rtype: List[Order]
    """

    with db.conn().cursor() as cursor:
        # TODO: make query more efficient by fetching orders using boolean logic instead of fetching all
        cursor.execute("SELECT * FROM Orders WHERE orderer_id = ?", [user_id])
        results = cursor.fetchall()
        orders = filter(
            [Order.from_dict(res) for res in results], 
            lambda o: o.orderer_id() == user_id and \
                (o.status() == Order.STATUS_CLAIMED or o.status() == Order.STATUS_AVAILABLE)
        )
        return orders, 200


def user_user_id_update_put(user: AuthInstance, user_id, body):  # noqa: E501
    """user_user_id_update_put

     # noqa: E501

    :param user_id: User ID of user we are trying to update.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if (user.id() != user_id) and (user.type() != constants.AUTH_TYPE_ADMIN):
        return "Not authorized to update user's information.", 401

    if connexion.request.is_json:
        body = BodyUserUpdate.from_dict(connexion.request.get_json())  # noqa: E501

    with db.conn().cursor() as cursor:
        if body.name() is not None:
            cursor.execute("UPDATE Users SET name = ? WHERE user_id = ?", [body.name(), user_id])
        if body.password() is not None:
            cursor.execute("UPDATE Users SET password = ? WHERE user_id = ?", [body.password(), user_id])
        if body.phone_number() is not None:
            cursor.execute("UPDATE Users SET phone_number = ? WHERE user_id = ?", [body.phone_number(), user_id])
        if body.etransfer_email() is not None:
            cursor.execute("UPDATE Users SET etransfer_email = ? WHERE user_id = ?", [body.etransfer_email(), user_id])
        cursor.commit()

    return "Successfully updated user information.", 200


def users_login_post(body):  # noqa: E501
    """Log in a user. Set cookie auth token.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """

    log.info(f"Attempting to log in user.")

    if connexion.request.is_json:
        body = BodyUsersLogin.from_dict(connexion.request.get_json())  # noqa: E501

    # Find user associated with the email
    with db.conn().cursor() as cursor:
        cursor.execute("SELECT (user_id, name, auth_token, password) FROM Users WHERE email = ?", [body.email()])
        row = cursor.fetchone()
        assert row, "user with the provided username does not exist"

        assert row["password"] == body.password, "invalid user credentials"
        user_id = row["user_id"]
        name = row["name"]
        auth_token = row["auth_token"]

        # Set cookie and return the response
        log.info(f"Succesfully logged in user '{name}' ({user_id}).")
        response = make_response(f"Succesfully logged in user '{name}'.")
        response.set_cookie("user_token", auth_token)
        return response, 200


def users_register_post(body):  # noqa: E501
    """Create a new user.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """    
    log.info(f"Registering a new user.")

    if connexion.request.is_json:
        body = BodyUsersRegister.from_dict(connexion.request.get_json())  # noqa: E501

    # TODO: Add email-confirmation logic

    with db.conn().cursor() as cursor:
        cursor.execute(
            "INSERT INTO Users (user_id, password, name, email, registered_time, delivery_tokens, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?)",
            [
                util.generate_uuid(),
                body.password(),
                body.name(),
                body.email(),
                datetime.now(),
                constants.NEW_USER_DELIVERY_TOKENS,
                body.phone_number()
            ]
        )
        cursor.commit()
    
    return f"Successfully registered user {body.name()}", 200
