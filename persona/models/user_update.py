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


class UserUpdate(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'address': 'UserUpdateAddress'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'address': 'address'
    }

    def __init__(self, first_name=None, last_name=None, address=None):  # noqa: E501
        """UserUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._first_name = None
        self._last_name = None
        self._address = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if address is not None:
            self.address = address

    @property
    def first_name(self):
        """Gets the first_name of this UserUpdate.  # noqa: E501


        :return: The first_name of this UserUpdate.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserUpdate.


        :param first_name: The first_name of this UserUpdate.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserUpdate.  # noqa: E501


        :return: The last_name of this UserUpdate.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserUpdate.


        :param last_name: The last_name of this UserUpdate.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def address(self):
        """Gets the address of this UserUpdate.  # noqa: E501


        :return: The address of this UserUpdate.  # noqa: E501
        :rtype: UserUpdateAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this UserUpdate.


        :param address: The address of this UserUpdate.  # noqa: E501
        :type: UserUpdateAddress
        """

        self._address = address

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
        if not isinstance(other, UserUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
