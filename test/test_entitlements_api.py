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
from persona.api.entitlements_api import EntitlementsApi  # noqa: E501
from persona.rest import ApiException


class TestEntitlementsApi(unittest.TestCase):
    """EntitlementsApi unit test stubs"""

    def setUp(self):
        self.api = persona.api.entitlements_api.EntitlementsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_entitlements_allow_post(self):
        """Test case for entitlements_allow_post

        """
        pass

    def test_entitlements_get(self):
        """Test case for entitlements_get

        List all entitlements  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
