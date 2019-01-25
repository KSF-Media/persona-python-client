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


class NewUser(object):
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
        'email_address': 'str',
        'password': 'str',
        'confirm_password': 'str',
        'street_address': 'str',
        'zip_code': 'str',
        'city': 'str',
        'country': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email_address': 'emailAddress',
        'password': 'password',
        'confirm_password': 'confirmPassword',
        'street_address': 'streetAddress',
        'zip_code': 'zipCode',
        'city': 'city',
        'country': 'country',
        'phone': 'phone'
    }

    def __init__(self, first_name=None, last_name=None, email_address=None, password=None, confirm_password=None, street_address=None, zip_code=None, city=None, country=None, phone=None):  # noqa: E501
        """NewUser - a model defined in OpenAPI"""  # noqa: E501

        self._first_name = None
        self._last_name = None
        self._email_address = None
        self._password = None
        self._confirm_password = None
        self._street_address = None
        self._zip_code = None
        self._city = None
        self._country = None
        self._phone = None
        self.discriminator = None

        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.password = password
        self.confirm_password = confirm_password
        if street_address is not None:
            self.street_address = street_address
        if zip_code is not None:
            self.zip_code = zip_code
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if phone is not None:
            self.phone = phone

    @property
    def first_name(self):
        """Gets the first_name of this NewUser.  # noqa: E501


        :return: The first_name of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this NewUser.


        :param first_name: The first_name of this NewUser.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this NewUser.  # noqa: E501


        :return: The last_name of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this NewUser.


        :param last_name: The last_name of this NewUser.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def email_address(self):
        """Gets the email_address of this NewUser.  # noqa: E501


        :return: The email_address of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this NewUser.


        :param email_address: The email_address of this NewUser.  # noqa: E501
        :type: str
        """
        if email_address is None:
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def password(self):
        """Gets the password of this NewUser.  # noqa: E501


        :return: The password of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this NewUser.


        :param password: The password of this NewUser.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def confirm_password(self):
        """Gets the confirm_password of this NewUser.  # noqa: E501


        :return: The confirm_password of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._confirm_password

    @confirm_password.setter
    def confirm_password(self, confirm_password):
        """Sets the confirm_password of this NewUser.


        :param confirm_password: The confirm_password of this NewUser.  # noqa: E501
        :type: str
        """
        if confirm_password is None:
            raise ValueError("Invalid value for `confirm_password`, must not be `None`")  # noqa: E501

        self._confirm_password = confirm_password

    @property
    def street_address(self):
        """Gets the street_address of this NewUser.  # noqa: E501


        :return: The street_address of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this NewUser.


        :param street_address: The street_address of this NewUser.  # noqa: E501
        :type: str
        """

        self._street_address = street_address

    @property
    def zip_code(self):
        """Gets the zip_code of this NewUser.  # noqa: E501


        :return: The zip_code of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this NewUser.


        :param zip_code: The zip_code of this NewUser.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

    @property
    def city(self):
        """Gets the city of this NewUser.  # noqa: E501


        :return: The city of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this NewUser.


        :param city: The city of this NewUser.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this NewUser.  # noqa: E501


        :return: The country of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this NewUser.


        :param country: The country of this NewUser.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def phone(self):
        """Gets the phone of this NewUser.  # noqa: E501


        :return: The phone of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this NewUser.


        :param phone: The phone of this NewUser.  # noqa: E501
        :type: str
        """

        self._phone = phone

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
        if not isinstance(other, NewUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
