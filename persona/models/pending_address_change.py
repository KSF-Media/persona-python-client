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


class PendingAddressChange(object):
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
        'address': 'DeliveryAddress',
        'start_date': 'date',
        'end_date': 'date',
        'type': 'str'
    }

    attribute_map = {
        'address': 'address',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'type': 'type'
    }

    def __init__(self, address=None, start_date=None, end_date=None, type=None):  # noqa: E501
        """PendingAddressChange - a model defined in OpenAPI"""  # noqa: E501

        self._address = None
        self._start_date = None
        self._end_date = None
        self._type = None
        self.discriminator = None

        self.address = address
        self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        self.type = type

    @property
    def address(self):
        """Gets the address of this PendingAddressChange.  # noqa: E501


        :return: The address of this PendingAddressChange.  # noqa: E501
        :rtype: DeliveryAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PendingAddressChange.


        :param address: The address of this PendingAddressChange.  # noqa: E501
        :type: DeliveryAddress
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def start_date(self):
        """Gets the start_date of this PendingAddressChange.  # noqa: E501


        :return: The start_date of this PendingAddressChange.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PendingAddressChange.


        :param start_date: The start_date of this PendingAddressChange.  # noqa: E501
        :type: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this PendingAddressChange.  # noqa: E501


        :return: The end_date of this PendingAddressChange.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this PendingAddressChange.


        :param end_date: The end_date of this PendingAddressChange.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def type(self):
        """Gets the type of this PendingAddressChange.  # noqa: E501


        :return: The type of this PendingAddressChange.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PendingAddressChange.


        :param type: The type of this PendingAddressChange.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, PendingAddressChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
