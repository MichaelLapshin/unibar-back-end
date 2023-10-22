# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime, timezone  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.payment_method import PaymentMethod
from openapi_server import util

from openapi_server.models.payment_method import PaymentMethod  # noqa: E501

class BodyOrderCreate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, deadline_time=None, order=None, source=None, destination=None, payment_method=None):  # noqa: E501
        """BodyOrderCreate - a model defined in OpenAPI

        :param deadline_time: The deadline_time of this BodyOrderCreate.  # noqa: E501
        :type deadline_time: datetime
        :param order: The order of this BodyOrderCreate.  # noqa: E501
        :type order: str
        :param source: The source of this BodyOrderCreate.  # noqa: E501
        :type source: str
        :param destination: The destination of this BodyOrderCreate.  # noqa: E501
        :type destination: str
        :param payment_method: The payment_method of this BodyOrderCreate.  # noqa: E501
        :type payment_method: PaymentMethod
        """
        self.openapi_types = {
            'deadline_time': datetime,
            'order': str,
            'source': str,
            'destination': str,
            'payment_method': PaymentMethod
        }

        self.attribute_map = {
            'deadline_time': 'deadline_time',
            'order': 'order',
            'source': 'source',
            'destination': 'destination',
            'payment_method': 'payment_method'
        }

        self._deadline_time = deadline_time.replace(tzinfo=timezone.utc) if deadline_time is not None else None
        self._order = order
        self._source = source
        self._destination = destination
        self._payment_method = payment_method

    @classmethod
    def from_dict(cls, dikt) -> 'BodyOrderCreate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_4 of this BodyOrderCreate.  # noqa: E501
        :rtype: BodyOrderCreate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def deadline_time(self):
        """Gets the deadline_time of this BodyOrderCreate.


        :return: The deadline_time of this BodyOrderCreate.
        :rtype: datetime
        """
        return self._deadline_time

    @deadline_time.setter
    def deadline_time(self, deadline_time):
        """Sets the deadline_time of this BodyOrderCreate.


        :param deadline_time: The deadline_time of this BodyOrderCreate.
        :type deadline_time: datetime
        """
        if deadline_time is None:
            raise ValueError("Invalid value for `deadline_time`, must not be `None`")  # noqa: E501

        self._deadline_time = deadline_time.replace(tzinfo=timezone.utc) if deadline_time is not None else None

    @property
    def order(self):
        """Gets the order of this BodyOrderCreate.


        :return: The order of this BodyOrderCreate.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this BodyOrderCreate.


        :param order: The order of this BodyOrderCreate.
        :type order: str
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")  # noqa: E501

        self._order = order

    @property
    def source(self):
        """Gets the source of this BodyOrderCreate.


        :return: The source of this BodyOrderCreate.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this BodyOrderCreate.


        :param source: The source of this BodyOrderCreate.
        :type source: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def destination(self):
        """Gets the destination of this BodyOrderCreate.


        :return: The destination of this BodyOrderCreate.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this BodyOrderCreate.


        :param destination: The destination of this BodyOrderCreate.
        :type destination: str
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def payment_method(self):
        """Gets the payment_method of this BodyOrderCreate.


        :return: The payment_method of this BodyOrderCreate.
        :rtype: PaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this BodyOrderCreate.


        :param payment_method: The payment_method of this BodyOrderCreate.
        :type payment_method: PaymentMethod
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method
