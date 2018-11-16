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


class Campaign(object):
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
        'name': 'str'
    }

    attribute_map = {
        'no': 'no',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, no=None, id=None, name=None):  # noqa: E501
        """Campaign - a model defined in OpenAPI"""  # noqa: E501

        self._no = None
        self._id = None
        self._name = None
        self.discriminator = None

        self.no = no
        self.id = id
        self.name = name

    @property
    def no(self):
        """Gets the no of this Campaign.  # noqa: E501


        :return: The no of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._no

    @no.setter
    def no(self, no):
        """Sets the no of this Campaign.


        :param no: The no of this Campaign.  # noqa: E501
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
        """Gets the id of this Campaign.  # noqa: E501


        :return: The id of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Campaign.


        :param id: The id of this Campaign.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Campaign.  # noqa: E501


        :return: The name of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Campaign.


        :param name: The name of this Campaign.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, Campaign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
