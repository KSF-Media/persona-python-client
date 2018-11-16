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


class InlineResponse4032EmailAddressInUse(object):
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
        'merge_token': 'str',
        'description': 'str',
        'existing_provider': 'str'
    }

    attribute_map = {
        'merge_token': 'merge_token',
        'description': 'description',
        'existing_provider': 'existing_provider'
    }

    def __init__(self, merge_token=None, description=None, existing_provider=None):  # noqa: E501
        """InlineResponse4032EmailAddressInUse - a model defined in OpenAPI"""  # noqa: E501

        self._merge_token = None
        self._description = None
        self._existing_provider = None
        self.discriminator = None

        if merge_token is not None:
            self.merge_token = merge_token
        if description is not None:
            self.description = description
        if existing_provider is not None:
            self.existing_provider = existing_provider

    @property
    def merge_token(self):
        """Gets the merge_token of this InlineResponse4032EmailAddressInUse.  # noqa: E501


        :return: The merge_token of this InlineResponse4032EmailAddressInUse.  # noqa: E501
        :rtype: str
        """
        return self._merge_token

    @merge_token.setter
    def merge_token(self, merge_token):
        """Sets the merge_token of this InlineResponse4032EmailAddressInUse.


        :param merge_token: The merge_token of this InlineResponse4032EmailAddressInUse.  # noqa: E501
        :type: str
        """

        self._merge_token = merge_token

    @property
    def description(self):
        """Gets the description of this InlineResponse4032EmailAddressInUse.  # noqa: E501


        :return: The description of this InlineResponse4032EmailAddressInUse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse4032EmailAddressInUse.


        :param description: The description of this InlineResponse4032EmailAddressInUse.  # noqa: E501
        :type: str
        """
        allowed_values = ["User has another record registered. Please merge the accounts."]  # noqa: E501
        if description not in allowed_values:
            raise ValueError(
                "Invalid value for `description` ({0}), must be one of {1}"  # noqa: E501
                .format(description, allowed_values)
            )

        self._description = description

    @property
    def existing_provider(self):
        """Gets the existing_provider of this InlineResponse4032EmailAddressInUse.  # noqa: E501


        :return: The existing_provider of this InlineResponse4032EmailAddressInUse.  # noqa: E501
        :rtype: str
        """
        return self._existing_provider

    @existing_provider.setter
    def existing_provider(self, existing_provider):
        """Sets the existing_provider of this InlineResponse4032EmailAddressInUse.


        :param existing_provider: The existing_provider of this InlineResponse4032EmailAddressInUse.  # noqa: E501
        :type: str
        """

        self._existing_provider = existing_provider

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
        if not isinstance(other, InlineResponse4032EmailAddressInUse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
