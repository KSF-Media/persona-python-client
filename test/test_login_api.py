# coding: utf-8

"""
    Persona

    KSF Media unified login service  # noqa: E501

    OpenAPI spec version: 1.2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.login_api import LoginApi  # noqa: E501
from openapi_client.rest import ApiException


class TestLoginApi(unittest.TestCase):
    """LoginApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.login_api.LoginApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_login_post(self):
        """Test case for login_post

        Login with email and password  # noqa: E501
        """
        pass

    def test_login_some_post(self):
        """Test case for login_some_post

        Login with social media  # noqa: E501
        """
        pass

    def test_login_sso_post(self):
        """Test case for login_sso_post

        Login with the AccessToken given by the SSO auth  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
