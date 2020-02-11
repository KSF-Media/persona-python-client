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
        'new_user_first_name': 'str',
        'new_user_last_name': 'str',
        'new_user_email_address': 'str',
        'new_user_password': 'str',
        'new_user_confirm_password': 'str',
        'new_user_street_address': 'str',
        'new_user_zip_code': 'str',
        'new_user_city': 'str',
        'new_user_country': 'str',
        'new_user_phone': 'str'
    }

    attribute_map = {
        'new_user_first_name': 'newUserFirstName',
        'new_user_last_name': 'newUserLastName',
        'new_user_email_address': 'newUserEmailAddress',
        'new_user_password': 'newUserPassword',
        'new_user_confirm_password': 'newUserConfirmPassword',
        'new_user_street_address': 'newUserStreetAddress',
        'new_user_zip_code': 'newUserZipCode',
        'new_user_city': 'newUserCity',
        'new_user_country': 'newUserCountry',
        'new_user_phone': 'newUserPhone'
    }

    def __init__(self, new_user_first_name=None, new_user_last_name=None, new_user_email_address=None, new_user_password=None, new_user_confirm_password=None, new_user_street_address=None, new_user_zip_code=None, new_user_city=None, new_user_country=None, new_user_phone=None):  # noqa: E501
        """NewUser - a model defined in OpenAPI"""  # noqa: E501

        self._new_user_first_name = None
        self._new_user_last_name = None
        self._new_user_email_address = None
        self._new_user_password = None
        self._new_user_confirm_password = None
        self._new_user_street_address = None
        self._new_user_zip_code = None
        self._new_user_city = None
        self._new_user_country = None
        self._new_user_phone = None
        self.discriminator = None

        if new_user_first_name is not None:
            self.new_user_first_name = new_user_first_name
        if new_user_last_name is not None:
            self.new_user_last_name = new_user_last_name
        self.new_user_email_address = new_user_email_address
        self.new_user_password = new_user_password
        self.new_user_confirm_password = new_user_confirm_password
        if new_user_street_address is not None:
            self.new_user_street_address = new_user_street_address
        if new_user_zip_code is not None:
            self.new_user_zip_code = new_user_zip_code
        if new_user_city is not None:
            self.new_user_city = new_user_city
        if new_user_country is not None:
            self.new_user_country = new_user_country
        if new_user_phone is not None:
            self.new_user_phone = new_user_phone

    @property
    def new_user_first_name(self):
        """Gets the new_user_first_name of this NewUser.  # noqa: E501


        :return: The new_user_first_name of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._new_user_first_name

    @new_user_first_name.setter
    def new_user_first_name(self, new_user_first_name):
        """Sets the new_user_first_name of this NewUser.


        :param new_user_first_name: The new_user_first_name of this NewUser.  # noqa: E501
        :type: str
        """

        self._new_user_first_name = new_user_first_name

    @property
    def new_user_last_name(self):
        """Gets the new_user_last_name of this NewUser.  # noqa: E501


        :return: The new_user_last_name of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._new_user_last_name

    @new_user_last_name.setter
    def new_user_last_name(self, new_user_last_name):
        """Sets the new_user_last_name of this NewUser.


        :param new_user_last_name: The new_user_last_name of this NewUser.  # noqa: E501
        :type: str
        """

        self._new_user_last_name = new_user_last_name

    @property
    def new_user_email_address(self):
        """Gets the new_user_email_address of this NewUser.  # noqa: E501


        :return: The new_user_email_address of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._new_user_email_address

    @new_user_email_address.setter
    def new_user_email_address(self, new_user_email_address):
        """Sets the new_user_email_address of this NewUser.


        :param new_user_email_address: The new_user_email_address of this NewUser.  # noqa: E501
        :type: str
        """
        if new_user_email_address is None:
            raise ValueError("Invalid value for `new_user_email_address`, must not be `None`")  # noqa: E501

        self._new_user_email_address = new_user_email_address

    @property
    def new_user_password(self):
        """Gets the new_user_password of this NewUser.  # noqa: E501


        :return: The new_user_password of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._new_user_password

    @new_user_password.setter
    def new_user_password(self, new_user_password):
        """Sets the new_user_password of this NewUser.


        :param new_user_password: The new_user_password of this NewUser.  # noqa: E501
        :type: str
        """
        if new_user_password is None:
            raise ValueError("Invalid value for `new_user_password`, must not be `None`")  # noqa: E501

        self._new_user_password = new_user_password

    @property
    def new_user_confirm_password(self):
        """Gets the new_user_confirm_password of this NewUser.  # noqa: E501


        :return: The new_user_confirm_password of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._new_user_confirm_password

    @new_user_confirm_password.setter
    def new_user_confirm_password(self, new_user_confirm_password):
        """Sets the new_user_confirm_password of this NewUser.


        :param new_user_confirm_password: The new_user_confirm_password of this NewUser.  # noqa: E501
        :type: str
        """
        if new_user_confirm_password is None:
            raise ValueError("Invalid value for `new_user_confirm_password`, must not be `None`")  # noqa: E501

        self._new_user_confirm_password = new_user_confirm_password

    @property
    def new_user_street_address(self):
        """Gets the new_user_street_address of this NewUser.  # noqa: E501


        :return: The new_user_street_address of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._new_user_street_address

    @new_user_street_address.setter
    def new_user_street_address(self, new_user_street_address):
        """Sets the new_user_street_address of this NewUser.


        :param new_user_street_address: The new_user_street_address of this NewUser.  # noqa: E501
        :type: str
        """

        self._new_user_street_address = new_user_street_address

    @property
    def new_user_zip_code(self):
        """Gets the new_user_zip_code of this NewUser.  # noqa: E501


        :return: The new_user_zip_code of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._new_user_zip_code

    @new_user_zip_code.setter
    def new_user_zip_code(self, new_user_zip_code):
        """Sets the new_user_zip_code of this NewUser.


        :param new_user_zip_code: The new_user_zip_code of this NewUser.  # noqa: E501
        :type: str
        """

        self._new_user_zip_code = new_user_zip_code

    @property
    def new_user_city(self):
        """Gets the new_user_city of this NewUser.  # noqa: E501


        :return: The new_user_city of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._new_user_city

    @new_user_city.setter
    def new_user_city(self, new_user_city):
        """Sets the new_user_city of this NewUser.


        :param new_user_city: The new_user_city of this NewUser.  # noqa: E501
        :type: str
        """

        self._new_user_city = new_user_city

    @property
    def new_user_country(self):
        """Gets the new_user_country of this NewUser.  # noqa: E501


        :return: The new_user_country of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._new_user_country

    @new_user_country.setter
    def new_user_country(self, new_user_country):
        """Sets the new_user_country of this NewUser.


        :param new_user_country: The new_user_country of this NewUser.  # noqa: E501
        :type: str
        """

        self._new_user_country = new_user_country

    @property
    def new_user_phone(self):
        """Gets the new_user_phone of this NewUser.  # noqa: E501


        :return: The new_user_phone of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._new_user_phone

    @new_user_phone.setter
    def new_user_phone(self, new_user_phone):
        """Sets the new_user_phone of this NewUser.


        :param new_user_phone: The new_user_phone of this NewUser.  # noqa: E501
        :type: str
        """

        self._new_user_phone = new_user_phone

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
