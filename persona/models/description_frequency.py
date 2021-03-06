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


class DescriptionFrequency(object):
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
        'amount': 'int',
        'unit': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'unit': 'unit'
    }

    def __init__(self, amount=None, unit=None):  # noqa: E501
        """DescriptionFrequency - a model defined in OpenAPI"""  # noqa: E501

        self._amount = None
        self._unit = None
        self.discriminator = None

        self.amount = amount
        self.unit = unit

    @property
    def amount(self):
        """Gets the amount of this DescriptionFrequency.  # noqa: E501


        :return: The amount of this DescriptionFrequency.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this DescriptionFrequency.


        :param amount: The amount of this DescriptionFrequency.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501
        if amount is not None and amount > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if amount is not None and amount < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._amount = amount

    @property
    def unit(self):
        """Gets the unit of this DescriptionFrequency.  # noqa: E501


        :return: The unit of this DescriptionFrequency.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this DescriptionFrequency.


        :param unit: The unit of this DescriptionFrequency.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

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
        if not isinstance(other, DescriptionFrequency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
