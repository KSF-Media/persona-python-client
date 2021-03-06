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


class Address(object):
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
        'city': 'str',
        'street_address': 'str',
        'street_name': 'str',
        'house_no': 'str',
        'staircase': 'str',
        'apartment': 'str'
    }

    attribute_map = {
        'country_code': 'countryCode',
        'zip_code': 'zipCode',
        'city': 'city',
        'street_address': 'streetAddress',
        'street_name': 'streetName',
        'house_no': 'houseNo',
        'staircase': 'staircase',
        'apartment': 'apartment'
    }

    def __init__(self, country_code=None, zip_code=None, city=None, street_address=None, street_name=None, house_no=None, staircase=None, apartment=None):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501

        self._country_code = None
        self._zip_code = None
        self._city = None
        self._street_address = None
        self._street_name = None
        self._house_no = None
        self._staircase = None
        self._apartment = None
        self.discriminator = None

        self.country_code = country_code
        if zip_code is not None:
            self.zip_code = zip_code
        if city is not None:
            self.city = city
        self.street_address = street_address
        if street_name is not None:
            self.street_name = street_name
        if house_no is not None:
            self.house_no = house_no
        if staircase is not None:
            self.staircase = staircase
        if apartment is not None:
            self.apartment = apartment

    @property
    def country_code(self):
        """Gets the country_code of this Address.  # noqa: E501


        :return: The country_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Address.


        :param country_code: The country_code of this Address.  # noqa: E501
        :type: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501

        self._country_code = country_code

    @property
    def zip_code(self):
        """Gets the zip_code of this Address.  # noqa: E501


        :return: The zip_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this Address.


        :param zip_code: The zip_code of this Address.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501


        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.


        :param city: The city of this Address.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def street_address(self):
        """Gets the street_address of this Address.  # noqa: E501


        :return: The street_address of this Address.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this Address.


        :param street_address: The street_address of this Address.  # noqa: E501
        :type: str
        """
        if street_address is None:
            raise ValueError("Invalid value for `street_address`, must not be `None`")  # noqa: E501

        self._street_address = street_address

    @property
    def street_name(self):
        """Gets the street_name of this Address.  # noqa: E501


        :return: The street_name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this Address.


        :param street_name: The street_name of this Address.  # noqa: E501
        :type: str
        """

        self._street_name = street_name

    @property
    def house_no(self):
        """Gets the house_no of this Address.  # noqa: E501


        :return: The house_no of this Address.  # noqa: E501
        :rtype: str
        """
        return self._house_no

    @house_no.setter
    def house_no(self, house_no):
        """Sets the house_no of this Address.


        :param house_no: The house_no of this Address.  # noqa: E501
        :type: str
        """

        self._house_no = house_no

    @property
    def staircase(self):
        """Gets the staircase of this Address.  # noqa: E501


        :return: The staircase of this Address.  # noqa: E501
        :rtype: str
        """
        return self._staircase

    @staircase.setter
    def staircase(self, staircase):
        """Sets the staircase of this Address.


        :param staircase: The staircase of this Address.  # noqa: E501
        :type: str
        """

        self._staircase = staircase

    @property
    def apartment(self):
        """Gets the apartment of this Address.  # noqa: E501


        :return: The apartment of this Address.  # noqa: E501
        :rtype: str
        """
        return self._apartment

    @apartment.setter
    def apartment(self, apartment):
        """Sets the apartment of this Address.


        :param apartment: The apartment of this Address.  # noqa: E501
        :type: str
        """

        self._apartment = apartment

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
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
