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


class PackageCampaign(object):
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
        'no': 'int',
        'id': 'str',
        'name': 'str',
        'price_eur': 'float',
        'length': 'int',
        'length_unit': 'str',
        'start_day': 'date',
        'end_day': 'date'
    }

    attribute_map = {
        'no': 'no',
        'id': 'id',
        'name': 'name',
        'price_eur': 'priceEur',
        'length': 'length',
        'length_unit': 'lengthUnit',
        'start_day': 'startDay',
        'end_day': 'endDay'
    }

    def __init__(self, no=None, id=None, name=None, price_eur=None, length=None, length_unit=None, start_day=None, end_day=None):  # noqa: E501
        """PackageCampaign - a model defined in OpenAPI"""  # noqa: E501

        self._no = None
        self._id = None
        self._name = None
        self._price_eur = None
        self._length = None
        self._length_unit = None
        self._start_day = None
        self._end_day = None
        self.discriminator = None

        self.no = no
        self.id = id
        self.name = name
        self.price_eur = price_eur
        self.length = length
        self.length_unit = length_unit
        if start_day is not None:
            self.start_day = start_day
        if end_day is not None:
            self.end_day = end_day

    @property
    def no(self):
        """Gets the no of this PackageCampaign.  # noqa: E501

        Campaign number  # noqa: E501

        :return: The no of this PackageCampaign.  # noqa: E501
        :rtype: int
        """
        return self._no

    @no.setter
    def no(self, no):
        """Sets the no of this PackageCampaign.

        Campaign number  # noqa: E501

        :param no: The no of this PackageCampaign.  # noqa: E501
        :type: int
        """
        if no is None:
            raise ValueError("Invalid value for `no`, must not be `None`")  # noqa: E501
        if no is not None and no > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `no`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if no is not None and no < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `no`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._no = no

    @property
    def id(self):
        """Gets the id of this PackageCampaign.  # noqa: E501

        Campaign id  # noqa: E501

        :return: The id of this PackageCampaign.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PackageCampaign.

        Campaign id  # noqa: E501

        :param id: The id of this PackageCampaign.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this PackageCampaign.  # noqa: E501

        Campaign name  # noqa: E501

        :return: The name of this PackageCampaign.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PackageCampaign.

        Campaign name  # noqa: E501

        :param name: The name of this PackageCampaign.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def price_eur(self):
        """Gets the price_eur of this PackageCampaign.  # noqa: E501

        Price of campaign in euros  # noqa: E501

        :return: The price_eur of this PackageCampaign.  # noqa: E501
        :rtype: float
        """
        return self._price_eur

    @price_eur.setter
    def price_eur(self, price_eur):
        """Sets the price_eur of this PackageCampaign.

        Price of campaign in euros  # noqa: E501

        :param price_eur: The price_eur of this PackageCampaign.  # noqa: E501
        :type: float
        """
        if price_eur is None:
            raise ValueError("Invalid value for `price_eur`, must not be `None`")  # noqa: E501

        self._price_eur = price_eur

    @property
    def length(self):
        """Gets the length of this PackageCampaign.  # noqa: E501

        Length of campaign  # noqa: E501

        :return: The length of this PackageCampaign.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this PackageCampaign.

        Length of campaign  # noqa: E501

        :param length: The length of this PackageCampaign.  # noqa: E501
        :type: int
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501
        if length is not None and length > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `length`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if length is not None and length < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `length`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._length = length

    @property
    def length_unit(self):
        """Gets the length_unit of this PackageCampaign.  # noqa: E501

        Unit of length (days, weeks, months, years)  # noqa: E501

        :return: The length_unit of this PackageCampaign.  # noqa: E501
        :rtype: str
        """
        return self._length_unit

    @length_unit.setter
    def length_unit(self, length_unit):
        """Sets the length_unit of this PackageCampaign.

        Unit of length (days, weeks, months, years)  # noqa: E501

        :param length_unit: The length_unit of this PackageCampaign.  # noqa: E501
        :type: str
        """
        if length_unit is None:
            raise ValueError("Invalid value for `length_unit`, must not be `None`")  # noqa: E501
        allowed_values = ["Day", "Week", "Month", "Year"]  # noqa: E501
        if length_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `length_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(length_unit, allowed_values)
            )

        self._length_unit = length_unit

    @property
    def start_day(self):
        """Gets the start_day of this PackageCampaign.  # noqa: E501


        :return: The start_day of this PackageCampaign.  # noqa: E501
        :rtype: date
        """
        return self._start_day

    @start_day.setter
    def start_day(self, start_day):
        """Sets the start_day of this PackageCampaign.


        :param start_day: The start_day of this PackageCampaign.  # noqa: E501
        :type: date
        """

        self._start_day = start_day

    @property
    def end_day(self):
        """Gets the end_day of this PackageCampaign.  # noqa: E501


        :return: The end_day of this PackageCampaign.  # noqa: E501
        :rtype: date
        """
        return self._end_day

    @end_day.setter
    def end_day(self, end_day):
        """Sets the end_day of this PackageCampaign.


        :param end_day: The end_day of this PackageCampaign.  # noqa: E501
        :type: date
        """

        self._end_day = end_day

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
        if not isinstance(other, PackageCampaign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
