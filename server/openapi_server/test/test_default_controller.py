# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.body_message import BodyMessage  # noqa: E501
from openapi_server.models.body_users_register import BodyUsersRegister  # noqa: E501
from openapi_server.models.body_users_login import BodyUsersLogin  # noqa: E501
from openapi_server.models.body_user_update import BodyUserUpdate  # noqa: E501
from openapi_server.models.body_order_create import BodyOrderCreate  # noqa: E501
from openapi_server.models.body_order_claim import BodyOrderClaim  # noqa: E501
from openapi_server.models.body_order_unclaim import BodyOrderUnclaim
from openapi_server.models.body_order_report import BodyOrderReport  # noqa: E501
from openapi_server.models.body_order_complete import BodyOrderComplete  # noqa: E501
from openapi_server.models.body_admin_login import BodyAdminLogin  # noqa: E501
from openapi_server.models.message import Message  # noqa: E501
from openapi_server.models.order import Order  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_admin_login_post(self):
        """Test case for admin_login_post

        
        """
        inline_object8 = {}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/admin/login',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object8),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_admin_messages_list_get(self):
        """Test case for admin_messages_list_get

        
        """
        headers = { 
            'Accept': 'application/json',
            'AdminAuth': 'special-key',
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
            'Accept': 'application/json',
            'AdminAuth': 'special-key',
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
            'Accept': 'application/json',
            'AdminAuth': 'special-key',
        }
        response = self.client.open(
            '/admin/reports/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_admin_users_list_get(self):
        """Test case for admin_users_list_get

        
        """
        headers = { 
            'Accept': 'application/json',
            'AdminAuth': 'special-key',
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
            'Accept': 'text/plain',
        }
        response = self.client.open(
            '/deployment',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_message_post(self):
        """Test case for message_post

        
        """
        inline_object = {}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/message',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_order_complete_put(self):
        """Test case for order_complete_put

        
        """
        inline_object7 = {}
        headers = { 
            'Content-Type': 'application/json',
            'UserAuth': 'special-key',
        }
        response = self.client.open(
            '/order/complete',
            method='PUT',
            headers=headers,
            data=json.dumps(inline_object7),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_order_deliver_put(self):
        """Test case for order_deliver_put

        
        """
        inline_object5 = {}
        headers = { 
            'Content-Type': 'application/json',
            'UserAuth': 'special-key',
        }
        response = self.client.open(
            '/order/deliver',
            method='PUT',
            headers=headers,
            data=json.dumps(inline_object5),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_order_undeliver_put(self):
        """Test case for order_undeliver_put

        
        """
        inline_object5 = {}
        headers = { 
            'Content-Type': 'application/json',
            'UserAuth': 'special-key',
        }
        response = self.client.open(
            '/order/undeliver',
            method='PUT',
            headers=headers,
            data=json.dumps(inline_object5),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


    def test_order_order_id_get(self):
        """Test case for order_order_id_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/order/{order_id}'.format(order_id='order_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_order_report_post(self):
        """Test case for order_report_post

        
        """
        inline_object6 = {}
        headers = { 
            'Content-Type': 'application/json',
            'UserAuth': 'special-key',
        }
        response = self.client.open(
            '/order/report',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object6),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_order_request_post(self):
        """Test case for order_request_post

        
        """
        inline_object4 = {}
        headers = { 
            'Content-Type': 'application/json',
            'UserAuth': 'special-key',
        }
        response = self.client.open(
            '/order/request',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object4),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_orders_available_get(self):
        """Test case for orders_available_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/orders/available',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ping_get(self):
        """Test case for ping_get

        
        """
        headers = { 
            'Accept': 'text/plain',
        }
        response = self.client.open(
            '/ping',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_id_get(self):
        """Test case for user_user_id_get

        
        """
        headers = { 
            'Accept': 'application/json',
            'AdminAuth': 'special-key',
            'UserAuth': 'special-key',
        }
        response = self.client.open(
            '/user/{user_id}'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_id_orders_delivering_get(self):
        """Test case for user_user_id_orders_delivering_get

        
        """
        headers = { 
            'Accept': 'application/json',
            'AdminAuth': 'special-key',
            'UserAuth': 'special-key',
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
            'Accept': 'application/json',
            'AdminAuth': 'special-key',
            'UserAuth': 'special-key',
        }
        response = self.client.open(
            '/user/{user_id}/orders/requesting'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_id_update_put(self):
        """Test case for user_user_id_update_put

        
        """
        inline_object3 = {}
        headers = { 
            'Content-Type': 'application/json',
            'UserAuth': 'special-key',
        }
        response = self.client.open(
            '/user/{user_id}/update'.format(user_id='user_id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(inline_object3),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_login_post(self):
        """Test case for users_login_post

        Log in a user. Set cookie auth token.
        """
        inline_object2 = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/users/login',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object2),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_register_post(self):
        """Test case for users_register_post

        Create a new user.
        """
        inline_object1 = {}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/users/register',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object1),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
