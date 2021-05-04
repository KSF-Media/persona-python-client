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
from persona.api.users_api import UsersApi  # noqa: E501
from persona.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = persona.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_admin_post(self):
        """Test case for users_admin_post

        Create a new user with admin options.  # noqa: E501
        """
        pass

    def test_users_post(self):
        """Test case for users_post

        Create a new user.  # noqa: E501
        """
        pass

    def test_users_search_get(self):
        """Test case for users_search_get

        Search for users  # noqa: E501
        """
        pass

    def test_users_temporary_post(self):
        """Test case for users_temporary_post

        Create a new user with email.  # noqa: E501
        """
        pass

    def test_users_uuid_entitlement_get(self):
        """Test case for users_uuid_entitlement_get

        Get users entitlements.  # noqa: E501
        """
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

    def test_users_uuid_legal_put(self):
        """Test case for users_uuid_legal_put

        Updates the legal consent settings for a given user.  # noqa: E501
        """
        pass

    def test_users_uuid_password_put(self):
        """Test case for users_uuid_password_put

        Set / Change user password  # noqa: E501
        """
        pass

    def test_users_uuid_patch(self):
        """Test case for users_uuid_patch

        Update a user  # noqa: E501
        """
        pass

    def test_users_uuid_payments_get(self):
        """Test case for users_uuid_payments_get

        Get user's subscriptions and payment events  # noqa: E501
        """
        pass

    def test_users_uuid_subscriptions_subsno_address_change_delete(self):
        """Test case for users_uuid_subscriptions_subsno_address_change_delete

        Delete temporary address change for subscription  # noqa: E501
        """
        pass

    def test_users_uuid_subscriptions_subsno_address_change_patch(self):
        """Test case for users_uuid_subscriptions_subsno_address_change_patch

        Edit temporary address change dates of a subscription  # noqa: E501
        """
        pass

    def test_users_uuid_subscriptions_subsno_address_change_post(self):
        """Test case for users_uuid_subscriptions_subsno_address_change_post

        Make a temporary address change for a subscription  # noqa: E501
        """
        pass

    def test_users_uuid_subscriptions_subsno_cancel_put(self):
        """Test case for users_uuid_subscriptions_subsno_cancel_put

        Cancels user subscription  # noqa: E501
        """
        pass

    def test_users_uuid_subscriptions_subsno_pause_patch(self):
        """Test case for users_uuid_subscriptions_subsno_pause_patch

        Edit pause duration  # noqa: E501
        """
        pass

    def test_users_uuid_subscriptions_subsno_pause_post(self):
        """Test case for users_uuid_subscriptions_subsno_pause_post

        Pause users subscription  # noqa: E501
        """
        pass

    def test_users_uuid_subscriptions_subsno_reclamation_post(self):
        """Test case for users_uuid_subscriptions_subsno_reclamation_post

        Create a new delivery reclamation for a subscription  # noqa: E501
        """
        pass

    def test_users_uuid_subscriptions_subsno_reclamations_reclaimno_get(self):
        """Test case for users_uuid_subscriptions_subsno_reclamations_reclaimno_get

        Get a delivery reclamation  # noqa: E501
        """
        pass

    def test_users_uuid_subscriptions_subsno_unpause_post(self):
        """Test case for users_uuid_subscriptions_subsno_unpause_post

        Pause users subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
