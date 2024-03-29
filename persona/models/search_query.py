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


class SearchQuery(object):
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
        'faro_limit': 'int',
        'query': 'str'
    }

    attribute_map = {
        'faro_limit': 'faroLimit',
        'query': 'query'
    }

    def __init__(self, faro_limit=None, query=None):  # noqa: E501
        """SearchQuery - a model defined in OpenAPI"""  # noqa: E501

        self._faro_limit = None
        self._query = None
        self.discriminator = None

        self.faro_limit = faro_limit
        self.query = query

    @property
    def faro_limit(self):
        """Gets the faro_limit of this SearchQuery.  # noqa: E501


        :return: The faro_limit of this SearchQuery.  # noqa: E501
        :rtype: int
        """
        return self._faro_limit

    @faro_limit.setter
    def faro_limit(self, faro_limit):
        """Sets the faro_limit of this SearchQuery.


        :param faro_limit: The faro_limit of this SearchQuery.  # noqa: E501
        :type: int
        """
        if faro_limit is None:
            raise ValueError("Invalid value for `faro_limit`, must not be `None`")  # noqa: E501
        if faro_limit is not None and faro_limit > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `faro_limit`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if faro_limit is not None and faro_limit < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `faro_limit`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._faro_limit = faro_limit

    @property
    def query(self):
        """Gets the query of this SearchQuery.  # noqa: E501


        :return: The query of this SearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SearchQuery.


        :param query: The query of this SearchQuery.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

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
        if not isinstance(other, SearchQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
