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


class DeliveryAddress(object):
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
        'street_address': 'str',
        'zipcode': 'str',
        'city': 'str'
    }

    attribute_map = {
        'street_address': 'streetAddress',
        'zipcode': 'zipcode',
        'city': 'city'
    }

    def __init__(self, street_address=None, zipcode=None, city=None):  # noqa: E501
        """DeliveryAddress - a model defined in OpenAPI"""  # noqa: E501

        self._street_address = None
        self._zipcode = None
        self._city = None
        self.discriminator = None

        self.street_address = street_address
        self.zipcode = zipcode
        self.city = city

    @property
    def street_address(self):
        """Gets the street_address of this DeliveryAddress.  # noqa: E501


        :return: The street_address of this DeliveryAddress.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this DeliveryAddress.


        :param street_address: The street_address of this DeliveryAddress.  # noqa: E501
        :type: str
        """
        if street_address is None:
            raise ValueError("Invalid value for `street_address`, must not be `None`")  # noqa: E501

        self._street_address = street_address

    @property
    def zipcode(self):
        """Gets the zipcode of this DeliveryAddress.  # noqa: E501


        :return: The zipcode of this DeliveryAddress.  # noqa: E501
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """Sets the zipcode of this DeliveryAddress.


        :param zipcode: The zipcode of this DeliveryAddress.  # noqa: E501
        :type: str
        """
        if zipcode is None:
            raise ValueError("Invalid value for `zipcode`, must not be `None`")  # noqa: E501

        self._zipcode = zipcode

    @property
    def city(self):
        """Gets the city of this DeliveryAddress.  # noqa: E501


        :return: The city of this DeliveryAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this DeliveryAddress.


        :param city: The city of this DeliveryAddress.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

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
        if not isinstance(other, DeliveryAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
