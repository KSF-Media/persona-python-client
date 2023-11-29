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


class JanrainUser(object):
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
        'cusno': 'str',
        'other_cusnos': 'list[str]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'cusno': 'cusno',
        'other_cusnos': 'otherCusnos'
    }

    def __init__(self, uuid=None, email=None, first_name=None, last_name=None, cusno=None, other_cusnos=None):  # noqa: E501
        """JanrainUser - a model defined in OpenAPI"""  # noqa: E501

        self._uuid = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._cusno = None
        self._other_cusnos = None
        self.discriminator = None

        self.uuid = uuid
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if cusno is not None:
            self.cusno = cusno
        if other_cusnos is not None:
            self.other_cusnos = other_cusnos

    @property
    def uuid(self):
        """Gets the uuid of this JanrainUser.  # noqa: E501


        :return: The uuid of this JanrainUser.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this JanrainUser.


        :param uuid: The uuid of this JanrainUser.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def email(self):
        """Gets the email of this JanrainUser.  # noqa: E501


        :return: The email of this JanrainUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this JanrainUser.


        :param email: The email of this JanrainUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this JanrainUser.  # noqa: E501


        :return: The first_name of this JanrainUser.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this JanrainUser.


        :param first_name: The first_name of this JanrainUser.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this JanrainUser.  # noqa: E501


        :return: The last_name of this JanrainUser.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this JanrainUser.


        :param last_name: The last_name of this JanrainUser.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def cusno(self):
        """Gets the cusno of this JanrainUser.  # noqa: E501


        :return: The cusno of this JanrainUser.  # noqa: E501
        :rtype: str
        """
        return self._cusno

    @cusno.setter
    def cusno(self, cusno):
        """Sets the cusno of this JanrainUser.


        :param cusno: The cusno of this JanrainUser.  # noqa: E501
        :type: str
        """

        self._cusno = cusno

    @property
    def other_cusnos(self):
        """Gets the other_cusnos of this JanrainUser.  # noqa: E501


        :return: The other_cusnos of this JanrainUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._other_cusnos

    @other_cusnos.setter
    def other_cusnos(self, other_cusnos):
        """Sets the other_cusnos of this JanrainUser.


        :param other_cusnos: The other_cusnos of this JanrainUser.  # noqa: E501
        :type: list[str]
        """

        self._other_cusnos = other_cusnos

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
        if not isinstance(other, JanrainUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
