# coding: utf-8
from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

import logging
from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Order(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """     
    STATUS_AVAILABLE = "available"
    STATUS_CLAIMED = "claimed"
    STATUS_DELIVERED = "delivered"
    STATUS_CANCELLED = "cancelled"
    STATUS_EXPIRED = "expired"

    def __init__(self, order_id=None, orderer_id=None, deliverer_id=None, creation_time=None, deadline_time=None, claimed_time=None, cancelled_time=None, delivered_time=None, order=None, source=None, destination=None, payment_method=None):  # noqa: E501
        """Order - a model defined in OpenAPI

        :param order_id: The order_id of this Order.  # noqa: E501
        :type order_id: str
        :param orderer_id: The orderer_id of this Order.  # noqa: E501
        :type orderer_id: str
        :param deliverer_id: The deliverer_id of this Order.  # noqa: E501
        :type deliverer_id: str
        :param creation_time: The creation_time of this Order.  # noqa: E501
        :type creation_time: str
        :param deadline_time: The deadline_time of this Order.  # noqa: E501
        :type deadline_time: str
        :param claimed_time: The claimed_time of this Order.  # noqa: E501
        :type claimed_time: str
        :param cancelled_time: The cancelled_time of this Order.  # noqa: E501
        :type cancelled_time: str
        :param delivered_time: The delivered_time of this Order.  # noqa: E501
        :type delivered_time: str
        :param order: The order of this Order.  # noqa: E501
        :type order: str
        :param source: The source of this Order.  # noqa: E501
        :type source: str
        :param destination: The destination of this Order.  # noqa: E501
        :type destination: str
        :param payment_method: The payment_method of this Order.  # noqa: E501
        :type payment_method: str
        """
        self.openapi_types = {
            'order_id': str,
            'orderer_id': str,
            'deliverer_id': str,
            'creation_time': str,
            'deadline_time': str,
            'claimed_time': str,
            'cancelled_time': str,
            'delivered_time': str,
            'order': str,
            'source': str,
            'destination': str,
            'payment_method': str,
            'status': str
        }

        self.attribute_map = {
            'order_id': 'order_id',
            'orderer_id': 'orderer_id',
            'deliverer_id': 'deliverer_id',
            'creation_time': 'creation_time',
            'deadline_time': 'deadline_time',
            'claimed_time': 'claimed_time',
            'cancelled_time': 'cancelled_time',
            'delivered_time': 'delivered_time',
            'order': 'order',
            'source': 'source',
            'destination': 'destination',
            'payment_method': 'payment_method',
            'status': 'status'
        }

        self._order_id = order_id
        self._orderer_id = orderer_id
        self._deliverer_id = deliverer_id
        self._creation_time = creation_time
        self._deadline_time = deadline_time
        self._claimed_time = claimed_time
        self._cancelled_time = cancelled_time
        self._delivered_time = delivered_time
        self._order = order
        self._source = source
        self._destination = destination
        self._payment_method = payment_method

        # Determine the status of the order
        self._compute_status()

    def _compute_status(self):
        """Compute the status of the order
        
            Note: the following if-statements may have redundant conditions,
                but it is for ensuring accuracy of the status.
        """

        current_time = datetime.datetime.now()

        # Facts: delivered time is only set if
        # - the order was delivered.
        # (other conditions don't matter since the order was delivered)
        if self._delivered_time != None:
            self._status = Order.STATUS_DELIVERED
            return

        # Facts: an ordered has been cancelled if
        # - order has been cancelled (cancelled_time != NULL)
        # - order has not been delivered (delivered_time = NULL)
        # (ignore other fields as deliverer, creation, and deadline don't matter)
        if self._cancelled_time != None and self._delivered_time == None:
            self._status = Order.STATUS_CANCELLED
            return

        # Facts: an order is claimed if
        # - order has been created (creation_time <= time.now())
        # - order has not been delivered (delivered_time = NULL)
        # - order is claimed by someone (deliverer != NULL && claimed_time != NULL)
        # - order has not been cancelled (cancelled_time = NULL)
        # (order can expire, as long as someone is currently delivering it)
        if self._creation_time <= current_time and \
                self._delivered_time == None and \
                self._deliverer_id != None and self._claimed_time != None and \
                self._cancelled_time == None:
            self._status = Order.STATUS_CLAIMED
            return

        # Facts: an order is available if
        # - order has been created (creation_time <= time.now())
        # - order did not expire (deadline_time > time.now())
        # - order is not being delivered (deliverer_id = NULL && claimed_time = NULL)
        # - order is was not delivered (delivered_time = NULL)
        # - order has not been cancelled (cancelled_time = NULL)
        if self._creation_time <= current_time and \
                self._deadline_time > current_time and \
                self._deliverer_id == None and self._claimed_time == None and \
                self._delivered_time == None and \
                self._cancelled_time == None:
            self._status = Order.STATUS_AVAILABLE
            return

        # Facts: an order is expired if
        # - order has expired (deadline_time <= time.now())
        # - order is active (creation_time <= time.now())
        # - order has not been cancelled (cancelled_time = NULL)
        # - order has not been delivered (delivered = NULL)
        # - order is not currently being delivered (deliverer_id = NULL && claimed_time = NULL)
        if self._deadline_time <= current_time and \
                self._creation_time <= current_time and \
                self._cancelled_time == None and \
                self._delivered_time == None and \
                self._deliverer_id == None and self._claimed_time == None:
            self._status = Order.STATUS_EXPIRED
            return

        logging.error("failed to compute order status")
        raise Exception("invalid order status")

    @classmethod
    def from_dict(cls, dikt) -> 'Order':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Order of this Order.  # noqa: E501
        :rtype: Order
        """
        order = util.deserialize_model(dikt, cls)
        order._compute_status()
        return order

    @property
    def order_id(self):
        """Gets the order_id of this Order.

        Identification of the order.  # noqa: E501

        :return: The order_id of this Order.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Order.

        Identification of the order.  # noqa: E501

        :param order_id: The order_id of this Order.
        :type order_id: str
        """

        self._order_id = order_id

    @property
    def orderer_id(self):
        """Gets the orderer_id of this Order.

        Identification of a user.  # noqa: E501

        :return: The orderer_id of this Order.
        :rtype: str
        """
        return self._orderer_id

    @orderer_id.setter
    def orderer_id(self, orderer_id):
        """Sets the orderer_id of this Order.

        Identification of a user.  # noqa: E501

        :param orderer_id: The orderer_id of this Order.
        :type orderer_id: str
        """

        self._orderer_id = orderer_id

    @property
    def deliverer_id(self):
        """Gets the deliverer_id of this Order.

        Identification of a user.  # noqa: E501

        :return: The deliverer_id of this Order.
        :rtype: str
        """
        return self._deliverer_id

    @deliverer_id.setter
    def deliverer_id(self, deliverer_id):
        """Sets the deliverer_id of this Order.

        Identification of a user.  # noqa: E501

        :param deliverer_id: The deliverer_id of this Order.
        :type deliverer_id: str
        """

        self._deliverer_id = deliverer_id

    @property
    def creation_time(self):
        """Gets the creation_time of this Order.


        :return: The creation_time of this Order.
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Order.


        :param creation_time: The creation_time of this Order.
        :type creation_time: str
        """

        self._creation_time = creation_time

    @property
    def deadline_time(self):
        """Gets the deadline_time of this Order.


        :return: The deadline_time of this Order.
        :rtype: str
        """
        return self._deadline_time

    @deadline_time.setter
    def deadline_time(self, deadline_time):
        """Sets the deadline_time of this Order.


        :param deadline_time: The deadline_time of this Order.
        :type deadline_time: str
        """

        self._deadline_time = deadline_time

    @property
    def claimed_time(self):
        """Gets the claimed_time of this Order.


        :return: The claimed_time of this Order.
        :rtype: str
        """
        return self._claimed_time

    @claimed_time.setter
    def claimed_time(self, claimed_time):
        """Sets the claimed_time of this Order.


        :param claimed_time: The claimed_time of this Order.
        :type claimed_time: str
        """

        self._claimed_time = claimed_time

    @property
    def delivered_time(self):
        """Gets the delivered_time of this Order.


        :return: The delivered_time of this Order.
        :rtype: str
        """
        return self._delivered_time

    @delivered_time.setter
    def delivered_time(self, delivered_time):
        """Sets the delivered_time of this Order.


        :param delivered_time: The delivered_time of this Order.
        :type delivered_time: str
        """

        self._delivered_time = delivered_time

    @property
    def order(self):
        """Gets the order of this Order.


        :return: The order of this Order.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Order.


        :param order: The order of this Order.
        :type order: str
        """

        self._order = order

    @property
    def source(self):
        """Gets the source of this Order.


        :return: The source of this Order.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Order.


        :param source: The source of this Order.
        :type source: str
        """

        self._source = source

    @property
    def destination(self):
        """Gets the destination of this Order.


        :return: The destination of this Order.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this Order.


        :param destination: The destination of this Order.
        :type destination: str
        """

        self._destination = destination

    @property
    def payment_method(self):
        """Gets the payment_method of this Order.


        :return: The payment_method of this Order.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this Order.


        :param payment_method: The payment_method of this Order.
        :type payment_method: str
        """
        allowed_values = ["cash", "etransfer"]  # noqa: E501
        if payment_method not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_method` ({0}), must be one of {1}"
                .format(payment_method, allowed_values)
            )

        self._payment_method = payment_method

    @property
    def status(self):
        """Gets the status of this Order.

        :return: The status of this Order.
        :rtype: str
        """
        return self._status
