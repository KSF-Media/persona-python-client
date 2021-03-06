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


class GdprConsent(object):
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
        'brand': 'str',
        'consent_key': 'str',
        'value': 'bool'
    }

    attribute_map = {
        'brand': 'brand',
        'consent_key': 'consentKey',
        'value': 'value'
    }

    def __init__(self, brand=None, consent_key=None, value=None):  # noqa: E501
        """GdprConsent - a model defined in OpenAPI"""  # noqa: E501

        self._brand = None
        self._consent_key = None
        self._value = None
        self.discriminator = None

        self.brand = brand
        self.consent_key = consent_key
        self.value = value

    @property
    def brand(self):
        """Gets the brand of this GdprConsent.  # noqa: E501


        :return: The brand of this GdprConsent.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this GdprConsent.


        :param brand: The brand of this GdprConsent.  # noqa: E501
        :type: str
        """
        if brand is None:
            raise ValueError("Invalid value for `brand`, must not be `None`")  # noqa: E501

        self._brand = brand

    @property
    def consent_key(self):
        """Gets the consent_key of this GdprConsent.  # noqa: E501


        :return: The consent_key of this GdprConsent.  # noqa: E501
        :rtype: str
        """
        return self._consent_key

    @consent_key.setter
    def consent_key(self, consent_key):
        """Sets the consent_key of this GdprConsent.


        :param consent_key: The consent_key of this GdprConsent.  # noqa: E501
        :type: str
        """
        if consent_key is None:
            raise ValueError("Invalid value for `consent_key`, must not be `None`")  # noqa: E501

        self._consent_key = consent_key

    @property
    def value(self):
        """Gets the value of this GdprConsent.  # noqa: E501


        :return: The value of this GdprConsent.  # noqa: E501
        :rtype: bool
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GdprConsent.


        :param value: The value of this GdprConsent.  # noqa: E501
        :type: bool
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, GdprConsent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
