# coding: utf-8

"""
    Persona

    KSF Media unified login service  # noqa: E501

    OpenAPI spec version: 1.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PackageOffer(object):
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
        'months': 'int',
        'total_price': 'int',
        'monthly_price': 'int'
    }

    attribute_map = {
        'months': 'months',
        'total_price': 'totalPrice',
        'monthly_price': 'monthlyPrice'
    }

    def __init__(self, months=None, total_price=None, monthly_price=None):  # noqa: E501
        """PackageOffer - a model defined in OpenAPI"""  # noqa: E501

        self._months = None
        self._total_price = None
        self._monthly_price = None
        self.discriminator = None

        self.months = months
        self.total_price = total_price
        self.monthly_price = monthly_price

    @property
    def months(self):
        """Gets the months of this PackageOffer.  # noqa: E501


        :return: The months of this PackageOffer.  # noqa: E501
        :rtype: int
        """
        return self._months

    @months.setter
    def months(self, months):
        """Sets the months of this PackageOffer.


        :param months: The months of this PackageOffer.  # noqa: E501
        :type: int
        """
        if months is None:
            raise ValueError("Invalid value for `months`, must not be `None`")  # noqa: E501
        if months is not None and months > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `months`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if months is not None and months < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `months`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._months = months

    @property
    def total_price(self):
        """Gets the total_price of this PackageOffer.  # noqa: E501


        :return: The total_price of this PackageOffer.  # noqa: E501
        :rtype: int
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this PackageOffer.


        :param total_price: The total_price of this PackageOffer.  # noqa: E501
        :type: int
        """
        if total_price is None:
            raise ValueError("Invalid value for `total_price`, must not be `None`")  # noqa: E501
        if total_price is not None and total_price > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `total_price`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if total_price is not None and total_price < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `total_price`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._total_price = total_price

    @property
    def monthly_price(self):
        """Gets the monthly_price of this PackageOffer.  # noqa: E501


        :return: The monthly_price of this PackageOffer.  # noqa: E501
        :rtype: int
        """
        return self._monthly_price

    @monthly_price.setter
    def monthly_price(self, monthly_price):
        """Sets the monthly_price of this PackageOffer.


        :param monthly_price: The monthly_price of this PackageOffer.  # noqa: E501
        :type: int
        """
        if monthly_price is None:
            raise ValueError("Invalid value for `monthly_price`, must not be `None`")  # noqa: E501
        if monthly_price is not None and monthly_price > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `monthly_price`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if monthly_price is not None and monthly_price < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `monthly_price`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._monthly_price = monthly_price

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
        if not isinstance(other, PackageOffer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
