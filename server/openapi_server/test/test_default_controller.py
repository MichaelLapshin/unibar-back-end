# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.message import Message  # noqa: E501
from openapi_server.models.order import Order  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_admin_messages_list_get(self):
        """Test case for admin_messages_list_get

        
        """
        headers = { 
            'Accept': 'user_ids',
            'AdminToken': 'special-key',
        }
        response = self.client.open(
            '/admin/messages/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_admin_orders_list_get(self):
        """Test case for admin_orders_list_get

        
        """
        headers = { 
            'Accept': 'user_ids',
            'AdminToken': 'special-key',
        }
        response = self.client.open(
            '/admin/orders/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_admin_reports_list_get(self):
        """Test case for admin_reports_list_get

        
        """
        headers = { 
            'Accept': 'user_ids',
            'AdminToken': 'special-key',
        }
        response = self.client.open(
            '/admin/reports/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_admin_user_user_id_get(self):
        """Test case for admin_user_user_id_get

        
        """
        headers = { 
            'Accept': 'user',
            'AdminToken': 'special-key',
        }
        response = self.client.open(
            '/admin/user/{user_id}'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_admin_users_list_get(self):
        """Test case for admin_users_list_get

        
        """
        headers = { 
            'Accept': 'user_ids',
            'AdminToken': 'special-key',
        }
        response = self.client.open(
            '/admin/users/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_deployment_get(self):
        """Test case for deployment_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/deployment',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_message_get(self):
        """Test case for message_get

        
        """
        headers = { 
            'user_id': 'user_id_example',
            'email': 'email_example',
            'message': 'message_example',
        }
        response = self.client.open(
            '/message',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_orders_available_get(self):
        """Test case for orders_available_get

        
        """
        headers = { 
            'Accept': 'orders',
        }
        response = self.client.open(
            '/orders/available',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_orders_order_id_get(self):
        """Test case for orders_order_id_get

        
        """
        headers = { 
            'Accept': 'order',
        }
        response = self.client.open(
            '/orders/{order_id}'.format(order_id='order_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ping_get(self):
        """Test case for ping_get

        
        """
        headers = { 
        }
        response = self.client.open(
            '/ping',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_id_info_get(self):
        """Test case for user_user_id_info_get

        
        """
        headers = { 
            'Accept': 'orders',
            'AdminToken': 'special-key',
            'UserToken': 'special-key',
        }
        response = self.client.open(
            '/user/{user_id}/info'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_id_order_complete_put(self):
        """Test case for user_user_id_order_complete_put

        
        """
        headers = { 
            'order_id': 'order_id_example',
            'AdminToken': 'special-key',
            'UserToken': 'special-key',
        }
        response = self.client.open(
            '/user/{user_id}/order/complete'.format(user_id='user_id_example'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_id_order_deliver_put(self):
        """Test case for user_user_id_order_deliver_put

        
        """
        headers = { 
            'order_id': 'order_id_example',
            'AdminToken': 'special-key',
            'UserToken': 'special-key',
        }
        response = self.client.open(
            '/user/{user_id}/order/deliver'.format(user_id='user_id_example'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_id_order_report_put(self):
        """Test case for user_user_id_order_report_put

        
        """
        headers = { 
            'reported_id': 'reported_id_example',
            'order_id': 'order_id_example',
            'message': 'message_example',
            'AdminToken': 'special-key',
            'UserToken': 'special-key',
        }
        response = self.client.open(
            '/user/{user_id}/order/report'.format(user_id='user_id_example'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_id_order_request_put(self):
        """Test case for user_user_id_order_request_put

        
        """
        headers = { 
            'order': {},
            'AdminToken': 'special-key',
            'UserToken': 'special-key',
        }
        response = self.client.open(
            '/user/{user_id}/order/request'.format(user_id='user_id_example'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_id_orders_delivering_get(self):
        """Test case for user_user_id_orders_delivering_get

        
        """
        headers = { 
            'Accept': 'orders',
            'AdminToken': 'special-key',
            'UserToken': 'special-key',
        }
        response = self.client.open(
            '/user/{user_id}/orders/delivering'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_id_orders_requesting_get(self):
        """Test case for user_user_id_orders_requesting_get

        
        """
        headers = { 
            'Accept': 'orders',
            'AdminToken': 'special-key',
            'UserToken': 'special-key',
        }
        response = self.client.open(
            '/user/{user_id}/orders/requesting'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_login_get(self):
        """Test case for users_login_get

        Log in a user.
        """
        headers = { 
            'Accept': 'user_id',
            'Authorization': 'BasicZm9vOmJhcg==',
        }
        response = self.client.open(
            '/users/login',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_register_post(self):
        """Test case for users_register_post

        Create a new user.
        """
        headers = { 
            'email': 'email_example',
            'password': 'password_example',
            'name': 'name_example',
            'phone_number': 'phone_number_example',
        }
        response = self.client.open(
            '/users/register',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
