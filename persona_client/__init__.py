# coding: utf-8

# flake8: noqa

"""
    Persona

    KSF Media unified login service  # noqa: E501

    OpenAPI spec version: 1.2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from persona_client.api.login_api import LoginApi
from persona_client.api.users_api import UsersApi

# import ApiClient
from persona_client.api_client import ApiClient
from persona_client.configuration import Configuration
# import models into sdk package
from persona_client.models.active_days import ActiveDays
from persona_client.models.address import Address
from persona_client.models.campaign import Campaign
from persona_client.models.description_frequency import DescriptionFrequency
from persona_client.models.gdpr_consent import GdprConsent
from persona_client.models.inline_response400 import InlineResponse400
from persona_client.models.inline_response400_invalid_request_body import InlineResponse400InvalidRequestBody
from persona_client.models.inline_response403 import InlineResponse403
from persona_client.models.inline_response4031 import InlineResponse4031
from persona_client.models.inline_response4031_access_token_expired import InlineResponse4031AccessTokenExpired
from persona_client.models.inline_response4032 import InlineResponse4032
from persona_client.models.inline_response4032_email_address_in_use import InlineResponse4032EmailAddressInUse
from persona_client.models.inline_response4032_email_not_authorized import InlineResponse4032EmailNotAuthorized
from persona_client.models.inline_response4032_oauth_failed import InlineResponse4032OauthFailed
from persona_client.models.inline_response403_invalid_credentials import InlineResponse403InvalidCredentials
from persona_client.models.inline_response415 import InlineResponse415
from persona_client.models.inline_response415_unsupported_media_type import InlineResponse415UnsupportedMediaType
from persona_client.models.inline_response500 import InlineResponse500
from persona_client.models.inline_response500_internal_server_error import InlineResponse500InternalServerError
from persona_client.models.login_data import LoginData
from persona_client.models.login_data_sso import LoginDataSSO
from persona_client.models.login_data_so_me import LoginDataSoMe
from persona_client.models.login_response import LoginResponse
from persona_client.models.package import Package
from persona_client.models.package_description import PackageDescription
from persona_client.models.package_offer import PackageOffer
from persona_client.models.paper import Paper
from persona_client.models.product import Product
from persona_client.models.subscription import Subscription
from persona_client.models.subscription_dates import SubscriptionDates
from persona_client.models.user import User
