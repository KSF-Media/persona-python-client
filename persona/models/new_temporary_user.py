# coding: utf-8

"""
    Persona

    KSF Media unified login service  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class NewTemporaryUser(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'email_address': 'str',
        'legal_consents': 'list[LegalConsent]'
    }

    attribute_map = {
        'email_address': 'emailAddress',
        'legal_consents': 'legalConsents'
    }

    def __init__(self, email_address=None, legal_consents=None):  # noqa: E501
        """NewTemporaryUser - a model defined in OpenAPI"""  # noqa: E501

        self._email_address = None
        self._legal_consents = None
        self.discriminator = None

        self.email_address = email_address
        self.legal_consents = legal_consents

    @property
    def email_address(self):
        """Gets the email_address of this NewTemporaryUser.  # noqa: E501


        :return: The email_address of this NewTemporaryUser.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this NewTemporaryUser.


        :param email_address: The email_address of this NewTemporaryUser.  # noqa: E501
        :type: str
        """
        if email_address is None:
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def legal_consents(self):
        """Gets the legal_consents of this NewTemporaryUser.  # noqa: E501


        :return: The legal_consents of this NewTemporaryUser.  # noqa: E501
        :rtype: list[LegalConsent]
        """
        return self._legal_consents

    @legal_consents.setter
    def legal_consents(self, legal_consents):
        """Sets the legal_consents of this NewTemporaryUser.


        :param legal_consents: The legal_consents of this NewTemporaryUser.  # noqa: E501
        :type: list[LegalConsent]
        """
        if legal_consents is None:
            raise ValueError("Invalid value for `legal_consents`, must not be `None`")  # noqa: E501

        self._legal_consents = legal_consents

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NewTemporaryUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
