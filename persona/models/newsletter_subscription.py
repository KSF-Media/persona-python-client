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


class NewsletterSubscription(object):
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
        'list_name': 'str',
        'id': 'str',
        'subscribed': 'bool'
    }

    attribute_map = {
        'list_name': 'listName',
        'id': 'id',
        'subscribed': 'subscribed'
    }

    def __init__(self, list_name=None, id=None, subscribed=None):  # noqa: E501
        """NewsletterSubscription - a model defined in OpenAPI"""  # noqa: E501

        self._list_name = None
        self._id = None
        self._subscribed = None
        self.discriminator = None

        self.list_name = list_name
        self.id = id
        self.subscribed = subscribed

    @property
    def list_name(self):
        """Gets the list_name of this NewsletterSubscription.  # noqa: E501


        :return: The list_name of this NewsletterSubscription.  # noqa: E501
        :rtype: str
        """
        return self._list_name

    @list_name.setter
    def list_name(self, list_name):
        """Sets the list_name of this NewsletterSubscription.


        :param list_name: The list_name of this NewsletterSubscription.  # noqa: E501
        :type: str
        """
        if list_name is None:
            raise ValueError("Invalid value for `list_name`, must not be `None`")  # noqa: E501

        self._list_name = list_name

    @property
    def id(self):
        """Gets the id of this NewsletterSubscription.  # noqa: E501


        :return: The id of this NewsletterSubscription.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NewsletterSubscription.


        :param id: The id of this NewsletterSubscription.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def subscribed(self):
        """Gets the subscribed of this NewsletterSubscription.  # noqa: E501


        :return: The subscribed of this NewsletterSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._subscribed

    @subscribed.setter
    def subscribed(self, subscribed):
        """Sets the subscribed of this NewsletterSubscription.


        :param subscribed: The subscribed of this NewsletterSubscription.  # noqa: E501
        :type: bool
        """
        if subscribed is None:
            raise ValueError("Invalid value for `subscribed`, must not be `None`")  # noqa: E501

        self._subscribed = subscribed

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
        if not isinstance(other, NewsletterSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other