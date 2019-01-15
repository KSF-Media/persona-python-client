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


class User(object):
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
        'uuid': 'str',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'address': 'Address',
        'cusno': 'str',
        'subs': 'list[Subscription]',
        'consent': 'list[GdprConsent]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'address': 'address',
        'cusno': 'cusno',
        'subs': 'subs',
        'consent': 'consent'
    }

    def __init__(self, uuid=None, email=None, first_name=None, last_name=None, address=None, cusno=None, subs=None, consent=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501

        self._uuid = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._address = None
        self._cusno = None
        self._subs = None
        self._consent = None
        self.discriminator = None

        self.uuid = uuid
        self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if address is not None:
            self.address = address
        self.cusno = cusno
        self.subs = subs
        self.consent = consent

    @property
    def uuid(self):
        """Gets the uuid of this User.  # noqa: E501


        :return: The uuid of this User.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this User.


        :param uuid: The uuid of this User.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501


        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501


        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def address(self):
        """Gets the address of this User.  # noqa: E501


        :return: The address of this User.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this User.


        :param address: The address of this User.  # noqa: E501
        :type: Address
        """

        self._address = address

    @property
    def cusno(self):
        """Gets the cusno of this User.  # noqa: E501


        :return: The cusno of this User.  # noqa: E501
        :rtype: str
        """
        return self._cusno

    @cusno.setter
    def cusno(self, cusno):
        """Sets the cusno of this User.


        :param cusno: The cusno of this User.  # noqa: E501
        :type: str
        """
        if cusno is None:
            raise ValueError("Invalid value for `cusno`, must not be `None`")  # noqa: E501

        self._cusno = cusno

    @property
    def subs(self):
        """Gets the subs of this User.  # noqa: E501


        :return: The subs of this User.  # noqa: E501
        :rtype: list[Subscription]
        """
        return self._subs

    @subs.setter
    def subs(self, subs):
        """Sets the subs of this User.


        :param subs: The subs of this User.  # noqa: E501
        :type: list[Subscription]
        """
        if subs is None:
            raise ValueError("Invalid value for `subs`, must not be `None`")  # noqa: E501

        self._subs = subs

    @property
    def consent(self):
        """Gets the consent of this User.  # noqa: E501


        :return: The consent of this User.  # noqa: E501
        :rtype: list[GdprConsent]
        """
        return self._consent

    @consent.setter
    def consent(self, consent):
        """Sets the consent of this User.


        :param consent: The consent of this User.  # noqa: E501
        :type: list[GdprConsent]
        """
        if consent is None:
            raise ValueError("Invalid value for `consent`, must not be `None`")  # noqa: E501

        self._consent = consent

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
