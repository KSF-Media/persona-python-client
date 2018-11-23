# coding: utf-8

"""
    Persona

    KSF Media unified login service  # noqa: E501

    OpenAPI spec version: 1.2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import persona_client
from persona_client.api.users_api import UsersApi  # noqa: E501
from persona_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = persona_client.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_uuid_gdpr_put(self):
        """Test case for users_uuid_gdpr_put

        Updates the GDPR consent settings for a given user.  # noqa: E501
        """
        pass

    def test_users_uuid_get(self):
        """Test case for users_uuid_get

        Get user by UUID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
