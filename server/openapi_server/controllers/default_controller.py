import connexion
import six
import datetime

from openapi_server.models.message import Message  # noqa: E501
from openapi_server.models.order import Order  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util, server_attr

def admin_messages_list_get():  # noqa: E501
    """admin_messages_list_get

     # noqa: E501


    :rtype: List[Message]
    """
    return [], 501


def admin_orders_list_get():  # noqa: E501
    """admin_orders_list_get

     # noqa: E501


    :rtype: List[Order]
    """
    return [], 501


def admin_reports_list_get():  # noqa: E501
    """admin_reports_list_get

     # noqa: E501


    :rtype: List[Order]
    """
    return [], 501


def admin_user_user_id_get(user_id):  # noqa: E501
    """admin_user_user_id_get

     # noqa: E501

    :param user_id: User of which to fetch information about.
    :type user_id: 

    :rtype: User
    """
    return User(), 501


def admin_users_list_get():  # noqa: E501
    """admin_users_list_get

     # noqa: E501


    :rtype: List[User]
    """
    return [], 501

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
        email =  str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!', 501


def orders_available_get():  # noqa: E501
    """orders_available_get

     # noqa: E501


    :rtype: List[Order]
    """
    return [], 501


def orders_order_id_get(order_id):  # noqa: E501
    """orders_order_id_get

     # noqa: E501

    :param order_id: Identification of the order.
    :type order_id: 

    :rtype: Order
    """
    return Order(), 501

def ping_get():  # noqa: E501
    """ping_get

     # noqa: E501


    :rtype: None
    """
    return "ping", 200


def user_user_id_info_get(user_id):  # noqa: E501
    """user_user_id_info_get

     # noqa: E501

    :param user_id: Identifying the user.
    :type user_id: 

    :rtype: User
    """
    return 'do some magic!', 501


def user_user_id_order_complete_put(user_id, order_id):  # noqa: E501
    """user_user_id_order_complete_put

     # noqa: E501

    :param user_id: User whose order is complete and is giving a delivery-token to the deliverer.
    :type user_id: 
    :param order_id: Order that is complete and for which a delivery-token must be transfered.
    :type order_id: 

    :rtype: None
    """
    return 'do some magic!', 501


def user_user_id_order_deliver_put(user_id, order_id):  # noqa: E501
    """user_user_id_order_deliver_put

     # noqa: E501

    :param user_id: User to fulfil the order.
    :type user_id: 
    :param order_id: Order to deliver.
    :type order_id: 

    :rtype: None
    """
    return 'do some magic!', 501


def user_user_id_order_report_post(user_id, reported_id, order_id, message):  # noqa: E501
    """user_user_id_order_report_post

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


def user_user_id_order_request_post(user_id, order):  # noqa: E501
    """user_user_id_order_request_post

     # noqa: E501

    :param user_id: Identifying the user.
    :type user_id: 
    :param order: Delivery request order of the user.
    :type order: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        order =  Order.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!', 501


def user_user_id_orders_delivering_get(user_id):  # noqa: E501
    """user_user_id_orders_delivering_get

     # noqa: E501

    :param user_id: Identifying the user.
    :type user_id: 

    :rtype: List[Order]
    """
    return 'do some magic!', 501


def user_user_id_orders_requesting_get(user_id):  # noqa: E501
    """user_user_id_orders_requesting_get

     # noqa: E501

    :param user_id: Identifying the user.
    :type user_id: 

    :rtype: List[Order]
    """
    return 'do some magic!', 501


def user_update_put(user_id, name=None, password=None, phone_numer=None, etransfer_email=None):
    """Update user information.

     # noqa: E501


    :rtype: str
    """
    return 'do some magic!', 501 

def users_login_get():  # noqa: E501
    """Log in a user.

     # noqa: E501


    :rtype: str
    """
    return 'do some magic!', 501


def users_register_post(email, password, name, phone_number):  # noqa: E501
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
    if connexion.request.is_json:
        email =  str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!', 501
