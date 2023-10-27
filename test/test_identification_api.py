# coding: utf-8

"""
    Persona

    KSF Media unified login service  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import persona
from persona.api.identification_api import IdentificationApi  # noqa: E501
from persona.rest import ApiException


class TestIdentificationApi(unittest.TestCase):
    """IdentificationApi unit test stubs"""

    def setUp(self):
        self.api = persona.api.identification_api.IdentificationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_identification_login_get(self):
        """Test case for identification_login_get

        Authenticate with OpenID Connect  # noqa: E501
        """
        pass

    def test_identification_login_monitor_get(self):
        """Test case for identification_login_monitor_get

        Get token for off band response login flow monitor  # noqa: E501
        """
        pass

    def test_identification_login_return_get(self):
        """Test case for identification_login_return_get

        Redirect endpoint for OpenID Connect  # noqa: E501
        """
        pass

    def test_identification_user_stamp_uuid_post(self):
        """Test case for identification_user_stamp_uuid_post

        Query when the strong identification was last updated  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
