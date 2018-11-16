# coding: utf-8

"""
    Persona

    KSF Media unified login service  # noqa: E501

    OpenAPI spec version: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse4031(object):
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
        'http_code': 'int',
        'access_token_expired': 'InlineResponse4031AccessTokenExpired',
        'http_status': 'str'
    }

    attribute_map = {
        'http_code': 'http_code',
        'access_token_expired': 'access_token_expired',
        'http_status': 'http_status'
    }

    def __init__(self, http_code=None, access_token_expired=None, http_status=None):  # noqa: E501
        """InlineResponse4031 - a model defined in OpenAPI"""  # noqa: E501

        self._http_code = None
        self._access_token_expired = None
        self._http_status = None
        self.discriminator = None

        if http_code is not None:
            self.http_code = http_code
        if access_token_expired is not None:
            self.access_token_expired = access_token_expired
        if http_status is not None:
            self.http_status = http_status

    @property
    def http_code(self):
        """Gets the http_code of this InlineResponse4031.  # noqa: E501


        :return: The http_code of this InlineResponse4031.  # noqa: E501
        :rtype: int
        """
        return self._http_code

    @http_code.setter
    def http_code(self, http_code):
        """Sets the http_code of this InlineResponse4031.


        :param http_code: The http_code of this InlineResponse4031.  # noqa: E501
        :type: int
        """

        self._http_code = http_code

    @property
    def access_token_expired(self):
        """Gets the access_token_expired of this InlineResponse4031.  # noqa: E501


        :return: The access_token_expired of this InlineResponse4031.  # noqa: E501
        :rtype: InlineResponse4031AccessTokenExpired
        """
        return self._access_token_expired

    @access_token_expired.setter
    def access_token_expired(self, access_token_expired):
        """Sets the access_token_expired of this InlineResponse4031.


        :param access_token_expired: The access_token_expired of this InlineResponse4031.  # noqa: E501
        :type: InlineResponse4031AccessTokenExpired
        """

        self._access_token_expired = access_token_expired

    @property
    def http_status(self):
        """Gets the http_status of this InlineResponse4031.  # noqa: E501


        :return: The http_status of this InlineResponse4031.  # noqa: E501
        :rtype: str
        """
        return self._http_status

    @http_status.setter
    def http_status(self, http_status):
        """Sets the http_status of this InlineResponse4031.


        :param http_status: The http_status of this InlineResponse4031.  # noqa: E501
        :type: str
        """
        allowed_values = ["Forbidden"]  # noqa: E501
        if http_status not in allowed_values:
            raise ValueError(
                "Invalid value for `http_status` ({0}), must be one of {1}"  # noqa: E501
                .format(http_status, allowed_values)
            )

        self._http_status = http_status

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
        if not isinstance(other, InlineResponse4031):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
