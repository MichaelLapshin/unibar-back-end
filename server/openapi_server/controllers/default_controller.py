import connexion
import six
from datetime import datetime, timedelta, timezone
import secrets
from flask import session, make_response, request

from openapi_server.models.body_message import BodyMessage
from openapi_server.models.body_users_register import BodyUsersRegister
from openapi_server.models.body_users_login import BodyUsersLogin
from openapi_server.models.body_user_update import BodyUserUpdate
from openapi_server.models.body_order_create import BodyOrderCreate
from openapi_server.models.body_order_claim import BodyOrderClaim
from openapi_server.models.body_order_cancel import BodyOrderCancel
from openapi_server.models.body_order_unclaim import BodyOrderUnclaim
from openapi_server.models.body_order_report import BodyOrderReport
from openapi_server.models.body_order_complete import BodyOrderComplete
from openapi_server.models.body_admin_login import BodyAdminLogin

from openapi_server.models.message import Message  # noqa: E501
from openapi_server.models.order import Order, order_with_status  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server.models.report import Report  # noqa: E501
from openapi_server import util, server_attr, constants
from openapi_server.logger import log
from openapi_server.database.db_rds import db
from openapi_server.controllers.security_controller_ import AuthInstance
from openapi_server.server import server_thread

def admin_login_post(body: dict):  # noqa: E501
    """admin_login_post

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    log.info(f"Attempting to log in admin.")
    body = BodyAdminLogin.from_dict(body)  # noqa: E501

    # Find user associated with the email
    with db.conn.cursor() as cursor:
        cursor.execute("SELECT admin_id, name FROM Admins WHERE auth_token = %s", [body.admin_token])
        row = cursor.fetchone()
        if not row:
            return "admin with the provided api key does not exist", 400

        admin_id = row["admin_id"]
        name = row["name"]

        # Set cookie and return the response
        log.info(f"Succesfully logged in admin '{name}' ({admin_id}).")
        response = make_response(f"Succesfully logged in admin '{name}'.")
        response.set_cookie("admin_token", body.admin_token)
        return response, 200


def admin_messages_list_get():  # noqa: E501
    """admin_messages_list_get

     # noqa: E501


    :rtype: List[Message]
    """
    with db.conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Messages")
        results = cursor.fetchall()
        messages = [Message.from_dict(res) for res in results]
        return messages, 200


def admin_orders_list_get():  # noqa: E501
    """admin_orders_list_get

     # noqa: E501


    :rtype: List[Order]
    """
    with db.conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Orders")
        results = cursor.fetchall()
        orders = [order_with_status(Order.from_dict(res)) for res in results]
        return orders, 200


def admin_reports_list_get():  # noqa: E501
    """admin_reports_list_get

     # noqa: E501

    :rtype: List[Order]
    """
    with db.conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Reports")
        results = cursor.fetchall()
        reports = [Report.from_dict(res) for res in results]
        return reports, 200


def admin_users_list_get():  # noqa: E501
    """admin_users_list_get

     # noqa: E501

    :rtype: List[User]
    """
    with db.conn.cursor() as cursor:
        cursor.execute("SELECT user_id, name, email, registered_time, delivery_tokens, phone_number, etransfer_email FROM Users")
        results = cursor.fetchall()
        users = [User.from_dict(res) for res in results]
        return users, 200

def shutdown_get():
    """shutdown_get

     # noqa: E501

    :rtype: None
    """
    log.info("Received shutdown command. Exiting the server.")
    return "Shutdown command is not implemented.", 501
    # server_thread.stop()
    # return "Successfully shut down the server.", 200

def deployment_get():  # noqa: E501
    """deployment_get

     # noqa: E501

    :rtype: str
    """
    return f"name: {server_attr.deployment_name}\n" + \
        f"uptime: {datetime.now(timezone.utc) - server_attr.start_time}", 200


def message_post(body: dict):  # noqa: E501
    """message_post

     # noqa: E501

    :param body, REST body contents

    :rtype: None
    """
    body = BodyMessage.from_dict(body)  # noqa: E501

    with db.conn.cursor() as cursor:
        db.conn.begin()
        cursor.execute(
            "INSERT INTO Messages (message_id, user_id, email, message, time) VALUES (%s, %s, %s, %s, %s)", 
            [
                util.generate_uuid(),
                body.user_id,
                body.email,
                body.message,
                datetime.now(timezone.utc)
            ]
        )
        db.conn.commit()

    return "Successfully sent a message to UniBar.", 200


def order_complete_put(user: AuthInstance, body: dict):  # noqa: E501
    """order_complete_put

     # noqa: E501

    :rtype: None
    """
    if user.type != constants.AUTH_TYPE_USER:
        return "requesting order complete by a non-user", 400
    body = BodyOrderComplete.from_dict(body)  # noqa: E501

    with db.conn.cursor() as cursor:
        db.conn.begin()

        # Check that the order is being delivered
        cursor.execute("SELECT * FROM Orders WHERE order_id = %s", [body.order_id])
        order = order_with_status(Order.from_dict(cursor.fetchone()))
        if not order:
            return f"did not find order with ID {body.order_id}", 400
        if order.status != Order.STATUS_CLAIMED:
            return "Order must be first claimed to be complete.", 400
        if order.orderer_id != user.id:
            return "Only the orderer can mark the delivery as complete.", 400

        # Transfer delivery token from orderer to deliverer
        cursor.execute("UPDATE Users SET delivery_tokens = delivery_tokens - 1 WHERE user_id = %s", [order.orderer_id])
        cursor.execute("UPDATE Users SET delivery_tokens = delivery_tokens + 1 WHERE user_id = %s", [order.deliverer_id])
        cursor.execute("UPDATE Orders SET delivered_time = %s WHERE order_id = %s", [datetime.now(timezone.utc), order.order_id])

        db.conn.commit()
        return f"Successfully marked order {order.order_id} as complete.", 200

def order_cancel_put(user: AuthInstance, body: dict):  # noqa: E501
    """order_cancel_put

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if user.type != constants.AUTH_TYPE_USER:
        return "A non-user is attempting to cancel an order.", 400
    body = BodyOrderCancel.from_dict(body)  # noqa: E501

    with db.conn.cursor() as cursor:
        db.conn.begin()

        # Check that the order is available
        cursor.execute("SELECT * FROM Orders WHERE order_id = %s", body.order_id)
        order = order_with_status(Order.from_dict(cursor.fetchone()))
        if not order:
            return f"did not find order with ID {body.order_id}", 400
        if order.orderer_id != user.id:
            return "Users can only cancel their own orders.", 400
        if order.status != Order.STATUS_AVAILABLE:
            return "Only available delivery requests may be cancelled.", 400

        # Cancel the order
        cursor.execute(
            "UPDATE Orders SET cancelled_time = %s WHERE order_id = %s",
            [datetime.now(timezone.utc), body.order_id]
        )
        db.conn.commit()
    
    return "Successfully cancelled the order.", 200

def order_claim_put(user: AuthInstance, body: dict):  # noqa: E501
    """order_claim_put

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if user.type != constants.AUTH_TYPE_USER:
        return "Only users can claim orders.", 400
    body = BodyOrderClaim.from_dict(body)  # noqa: E501

    with db.conn.cursor() as cursor:
        db.conn.begin()

        # Check that the order is available
        cursor.execute("SELECT * FROM Orders WHERE order_id = %s", body.order_id)
        order = order_with_status(Order.from_dict(cursor.fetchone()))
        if not order:
            return f"did not find order with ID {body.order_id}", 400
        if order.status != Order.STATUS_AVAILABLE:
            return "Users may only claim available orders.", 400
        if order.orderer_id == user.id:
            return "Users cannot deliver to themselves.", 400

        # Check that the user has less than (limit) orders
        cursor.execute("SELECT * FROM Orders WHERE deliverer_id = %s", user.id)
        results = cursor.fetchall()
        user_orders = [order_with_status(Order.from_dict(res)) for res in results]
        user_claimed_orders = list(filter(lambda o: o.status == Order.STATUS_CLAIMED, user_orders))
        if len(user_claimed_orders) >= constants.ORDER_MAX_CONCURRENT_CLAIM:
            return f"User may claim at most {constants.ORDER_MAX_CONCURRENT_CLAIM} at any given time.", 400

        # Claim the order
        cursor.execute(
            "UPDATE Orders SET deliverer_id = %s, claimed_time = %s WHERE order_id = %s",
            [user.id, datetime.now(timezone.utc), body.order_id]
        )
        db.conn.commit()
    
    return "Successfully claimed the order.", 200


def order_unclaim_put(user: AuthInstance, body: dict):
    """order_unclaim_put

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if user.type != constants.AUTH_TYPE_USER:
        return "Only users can unclaim orders.", 400
    body = BodyOrderUnclaim.from_dict(body)  # noqa: E501

    with db.conn.cursor() as cursor:
        db.conn.begin()

        # Assert that the order to undeliver is being delivered by the user.
        cursor.execute(
            "SELECT * FROM Orders WHERE order_id = %s", 
            [body.order_id]
        )
        order = order_with_status(Order.from_dict(cursor.fetchone()))
        if not order:
            return f"did not find order with ID {body.order_id}", 400
        if order.deliverer_id != user.id:
            return "Cannot undeliver an order not deliverying.", 400
        if order.status != Order.STATUS_CLAIMED:
            return "Cannot undeliver an unclaimed order.", 400

        # Update the order to nullify the deliverer column
        cursor.execute(
            "UPDATE Orders SET deliverer_id = %s, claimed_time = %s WHERE order_id = %s",
            [None, None, body.order_id]
        )
        db.conn.commit()


    return "Successfully unclaimed the order.", 200


def order_order_id_get(order_id):  # noqa: E501
    """order_order_id_get

     # noqa: E501

    :param order_id: The ID of the order which the client wants to see its info.
    :type order_id: 

    :rtype: Order
    """
    with db.conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Orders WHERE order_id = %s", 
            [order_id]
        )
        order = cursor.fetchone()
        if not order:
            return f"did not find order with ID {order_id}", 400
        return order_with_status(Order.from_dict(order)), 200

def order_report_post(user: AuthInstance, body: dict):  # noqa: E501
    """order_report_post

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if user.type != constants.AUTH_TYPE_USER:
        return "Only users may report.", 400
    body = BodyOrderReport.from_dict(body)  # noqa: E501

    with db.conn.cursor() as cursor:
        db.conn.begin()

        # Validate that the reporter_user_id and reported_user_id are part of the order
        cursor.execute("SELECT * FROM Orders WHERE order_id = %s", [body.order_id])
        order = order_with_status(Order.from_dict(cursor.fetchone()))
        if not order:
            return f"did not find order with ID {body.order_id}", 400
        if not ((order.orderer_id == user.id and order.deliverer_id == body.reported_id) or \
            (order.orderer_id == body.reported_id and order.deliverer_id == user.id)):
            return "User can only report the other in the context of the delivery order.", 400

        # Create order
        cursor.execute(
            "INSERT INTO Reports (report_id, reporter_user_id, reported_user_id, order_id, time, message) VALUES (%s, %s, %s, %s, %s, %s)",
            [
                util.generate_uuid(),
                user.id,
                body.reported_id,
                body.order_id,
                datetime.now(timezone.utc),
                body.message
            ]
        )
        db.conn.commit()

        # TODO: add logic to notify admins of the report

        return f"Successfully reported user {body.reported_id}.", 200
        

def order_create_post(user: AuthInstance, body: dict):  # noqa: E501
    """order_create_post

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    assert user.type == constants.AUTH_TYPE_USER, "not a user"
    body = BodyOrderCreate.from_dict(body)  # noqa: E501

    current_time = datetime.now(timezone.utc)

    with db.conn.cursor() as cursor:
        db.conn.begin()

        cursor.execute( "SELECT * FROM Users WHERE user_id = %s", [user.id])
        user = User.from_dict(cursor.fetchone()) # override auth user
        if not user:
            return f"did not find user with ID {user.user_id}", 400

        # Count number of active orders that user is requesting
        # TODO: make query more efficient by fetching orders using boolean logic instead of fetching all
        cursor.execute("SELECT * FROM Orders WHERE orderer_id = %s", [user.user_id])
        results = cursor.fetchall()
        orders = [order_with_status(Order.from_dict(res)) for res in results]
        active_orders = list(filter(
            lambda o: o.orderer_id == user.user_id and \
                (o.status == Order.STATUS_CLAIMED or o.status == Order.STATUS_AVAILABLE),
            orders
        ))

        # Check if user has tokens to use on the delivery
        if user.delivery_tokens <= len(active_orders):
            return "Not enough delivery tokens.", 400

        # Assert that the deadline must be after
        if body.deadline_time <= current_time:
            return "Deadline must be a later time.", 400

        # Assert that the request is at most x-hours later.
        if body.deadline_time > current_time + timedelta(hours=constants.ORDER_MAX_REQUEST_HOURS):
            return f"Deadline may be set to at most {constants.ORDER_MAX_REQUEST_HOURS}-hours later."

        # Create order
        cursor.execute(
            "INSERT INTO Orders (order_id, orderer_id, creation_time, deadline_time, `order`, source, destination, payment_method) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            [
                util.generate_uuid(),
                user.user_id,
                current_time,
                body.deadline_time,
                body.order,
                body.source,
                body.destination,
                body.payment_method
            ]
        )
        db.conn.commit()

    return "Successfully created a delivery request.", 200


def orders_available_get():  # noqa: E501
    """orders_available_get

     # noqa: E501


    :rtype: List[Order]
    """

    with db.conn.cursor() as cursor:
        # TODO: make query more efficient by fetching orders using boolean logic instead of fetching all
        cursor.execute("SELECT * FROM Orders")
        results = cursor.fetchall()
        orders = [order_with_status(Order.from_dict(res)) for res in results]
        available_orders = list(filter(lambda o: o.status == Order.STATUS_AVAILABLE, orders))
        return available_orders, 200


def ping_get():  # noqa: E501
    """ping_get

     # noqa: E501


    :rtype: str
    """
    log.info("(ping_get) Pinged.")
    return "ping", 200


def user_user_id_get(user_id):  # noqa: E501
    """user_user_id_get

     # noqa: E501

    :param user_id: User ID of the user to identify who&#39;s info to get.
    :type user_id: 

    :rtype: User
    """
    
    with db.conn.cursor() as cursor:
        cursor.execute("SELECT user_id, name, email, registered_time, delivery_tokens, phone_number, etransfer_email FROM Users WHERE user_id = %s", [user_id])
        row = cursor.fetchone()
        if not row:
            return f"did not find user with id {user_id}", 400
        return User.from_dict(row), 200


def user_user_id_orders_claimed_get(user_id):  # noqa: E501
    """user_user_id_orders_claimed_get

     # noqa: E501

    :param user_id: User ID of which we want to see the orders they are currently claiming.
    :type user_id: 

    :rtype: List[Order]
    """

    with db.conn.cursor() as cursor:
        # TODO: make query more efficient by fetching orders using boolean logic instead of fetching all
        cursor.execute("SELECT * FROM Orders WHERE deliverer_id = %s", [user_id])
        results = cursor.fetchall()
        orders = [order_with_status(Order.from_dict(res)) for res in results]
        claimed_orders = list(filter(lambda o: o.status == Order.STATUS_CLAIMED and o.deliverer_id == user_id, orders))
        return claimed_orders, 200


def user_user_id_orders_active_get(user_id):  # noqa: E501
    """user_user_id_orders_active_get

     # noqa: E501

    :param user_id: User ID of which we want to see the orders they are requesting.
    :type user_id: 

    :rtype: List[Order]
    """

    with db.conn.cursor() as cursor:
        # TODO: make query more efficient by fetching orders using boolean logic instead of fetching all
        cursor.execute("SELECT * FROM Orders WHERE orderer_id = %s", [user_id])
        results = cursor.fetchall()
        orders = [order_with_status(Order.from_dict(res)) for res in results]
        active_orders = list(filter(
            lambda o: o.orderer_id == user_id and \
                (o.status == Order.STATUS_CLAIMED or o.status == Order.STATUS_AVAILABLE),
            orders
        ))
        return active_orders, 200


def user_user_id_update_patch(user: AuthInstance, user_id, body: dict):  # noqa: E501
    """user_user_id_update_patch

     # noqa: E501

    :param user_id: User ID of user we are trying to update.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if (user.id != user_id) and (user.type != constants.AUTH_TYPE_ADMIN):
        return "Not authorized to update user's information.", 401

    body = BodyUserUpdate.from_dict(body)  # noqa: E501

    with db.conn.cursor() as cursor:
        db.conn.begin()
        if body.name is not None:
            cursor.execute("UPDATE Users SET name = %s WHERE user_id = %s", [body.name, user_id])
        if body.password is not None:
            cursor.execute("UPDATE Users SET password = %s WHERE user_id = %s", [body.password, user_id])
        if body.phone_number is not None:
            cursor.execute("UPDATE Users SET phone_number = %s WHERE user_id = %s", [body.phone_number, user_id])
        if body.etransfer_email is not None:
            cursor.execute("UPDATE Users SET etransfer_email = %s WHERE user_id = %s", [body.etransfer_email, user_id])
        db.conn.commit()

    return "Successfully updated user information.", 200


def users_login_post(body: dict):  # noqa: E501
    """Log in a user. Set cookie auth token.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """

    log.info(f"Attempting to log in user.")
    body = BodyUsersLogin.from_dict(body)  # noqa: E501

    # Find user associated with the email
    with db.conn.cursor() as cursor:
        cursor.execute("SELECT user_id, name, auth_token, password FROM Users WHERE email = %s", [body.email])
        row = cursor.fetchone()
        if not row:
            return "user with the provided username does not exist", 400

        if row["password"] != body.password:
            return "invalid user credentials", 400
        user_id = row["user_id"]
        name = row["name"]
        auth_token = row["auth_token"]

        # Generate new auth token if does not exist
        if auth_token is None:
            auth_token = secrets.token_hex(16) # 32 chars
            assert len(auth_token) == constants.AUTH_TOKEN_LENGTH

            db.conn.begin()
            cursor.execute(
                "UPDATE Users SET auth_token = %s WHERE user_id = %s",
                [auth_token, user_id]
            )
            db.conn.commit()

        # Set cookie and return the response
        log.info(f"Succesfully logged in user '{name}' ({user_id}).")
        response = make_response(f"Succesfully logged in user '{name}'.")
        response.set_cookie("user_token", auth_token)
        return response, 200


def users_register_post(body: dict):  # noqa: E501
    """Create a new user.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """    
    log.info(f"Registering a new user.")
    body = BodyUsersRegister.from_dict(body)  # noqa: E501

    # TODO: Add email-confirmation logic

    with db.conn.cursor() as cursor:
        db.conn.begin()
        cursor.execute(
            "INSERT INTO Users (user_id, password, name, email, registered_time, delivery_tokens, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            [
                util.generate_uuid(),
                body.password,
                body.name,
                body.email,
                datetime.now(timezone.utc),
                constants.NEW_USER_DELIVERY_TOKENS,
                body.phone_number
            ]
        )
        db.conn.commit()
    
    return f"Successfully registered user {body.name}.", 200
