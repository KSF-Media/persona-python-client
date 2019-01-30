# coding: utf-8

"""
    Persona

    KSF Media unified login service  # noqa: E501

    OpenAPI spec version: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class UserUpdateAddress(object):
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
        'country_code': 'str',
        'zip_code': 'str',
        'street_address': 'str'
    }

    attribute_map = {
        'country_code': 'countryCode',
        'zip_code': 'zipCode',
        'street_address': 'streetAddress'
    }

    def __init__(self, country_code=None, zip_code=None, street_address=None):  # noqa: E501
        """UserUpdateAddress - a model defined in OpenAPI"""  # noqa: E501

        self._country_code = None
        self._zip_code = None
        self._street_address = None
        self.discriminator = None

        self.country_code = country_code
        self.zip_code = zip_code
        self.street_address = street_address

    @property
    def country_code(self):
        """Gets the country_code of this UserUpdateAddress.  # noqa: E501


        :return: The country_code of this UserUpdateAddress.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this UserUpdateAddress.


        :param country_code: The country_code of this UserUpdateAddress.  # noqa: E501
        :type: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501

        self._country_code = country_code

    @property
    def zip_code(self):
        """Gets the zip_code of this UserUpdateAddress.  # noqa: E501


        :return: The zip_code of this UserUpdateAddress.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this UserUpdateAddress.


        :param zip_code: The zip_code of this UserUpdateAddress.  # noqa: E501
        :type: str
        """
        if zip_code is None:
            raise ValueError("Invalid value for `zip_code`, must not be `None`")  # noqa: E501

        self._zip_code = zip_code

    @property
    def street_address(self):
        """Gets the street_address of this UserUpdateAddress.  # noqa: E501


        :return: The street_address of this UserUpdateAddress.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this UserUpdateAddress.


        :param street_address: The street_address of this UserUpdateAddress.  # noqa: E501
        :type: str
        """
        if street_address is None:
            raise ValueError("Invalid value for `street_address`, must not be `None`")  # noqa: E501

        self._street_address = street_address

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
        if not isinstance(other, UserUpdateAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
