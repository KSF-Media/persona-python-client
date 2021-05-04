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


class AdminNewUser(object):
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
        'user': 'NewUser',
        'cusno': 'int'
    }

    attribute_map = {
        'user': 'user',
        'cusno': 'cusno'
    }

    def __init__(self, user=None, cusno=None):  # noqa: E501
        """AdminNewUser - a model defined in OpenAPI"""  # noqa: E501

        self._user = None
        self._cusno = None
        self.discriminator = None

        self.user = user
        if cusno is not None:
            self.cusno = cusno

    @property
    def user(self):
        """Gets the user of this AdminNewUser.  # noqa: E501


        :return: The user of this AdminNewUser.  # noqa: E501
        :rtype: NewUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AdminNewUser.


        :param user: The user of this AdminNewUser.  # noqa: E501
        :type: NewUser
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def cusno(self):
        """Gets the cusno of this AdminNewUser.  # noqa: E501


        :return: The cusno of this AdminNewUser.  # noqa: E501
        :rtype: int
        """
        return self._cusno

    @cusno.setter
    def cusno(self, cusno):
        """Sets the cusno of this AdminNewUser.


        :param cusno: The cusno of this AdminNewUser.  # noqa: E501
        :type: int
        """
        if cusno is not None and cusno > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `cusno`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if cusno is not None and cusno < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `cusno`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._cusno = cusno

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
        if not isinstance(other, AdminNewUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
