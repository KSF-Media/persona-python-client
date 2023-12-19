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
from persona.api.admin_api import AdminApi  # noqa: E501
from persona.rest import ApiException


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self):
        self.api = persona.api.admin_api.AdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_free_pass_delete(self):
        """Test case for admin_free_pass_delete

        Revokes an existing free pass  # noqa: E501
        """
        pass

    def test_admin_free_pass_put(self):
        """Test case for admin_free_pass_put

        Creates a free pass to an article  # noqa: E501
        """
        pass

    def test_admin_free_passes_get(self):
        """Test case for admin_free_passes_get

        Lists all free passes  # noqa: E501
        """
        pass

    def test_admin_search_post(self):
        """Test case for admin_search_post

        Search for users  # noqa: E501
        """
        pass

    def test_admin_transfer_passive_subscribers_listid_post(self):
        """Test case for admin_transfer_passive_subscribers_listid_post

        Transfers passive customers from Kayak to Mailchimp  # noqa: E501
        """
        pass

    def test_admin_user_post(self):
        """Test case for admin_user_post

        Create a new user with admin options.  # noqa: E501
        """
        pass

    def test_admin_user_uuid_delete(self):
        """Test case for admin_user_uuid_delete

        Delete user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
