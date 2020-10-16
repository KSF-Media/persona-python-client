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


class SubscriptionPayments(object):
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
        'subsno': 'int',
        'name': 'str',
        'start_date': 'date',
        'last_date': 'date',
        'payments': 'list[Payment]'
    }

    attribute_map = {
        'subsno': 'subsno',
        'name': 'name',
        'start_date': 'startDate',
        'last_date': 'lastDate',
        'payments': 'payments'
    }

    def __init__(self, subsno=None, name=None, start_date=None, last_date=None, payments=None):  # noqa: E501
        """SubscriptionPayments - a model defined in OpenAPI"""  # noqa: E501

        self._subsno = None
        self._name = None
        self._start_date = None
        self._last_date = None
        self._payments = None
        self.discriminator = None

        self.subsno = subsno
        self.name = name
        self.start_date = start_date
        self.last_date = last_date
        self.payments = payments

    @property
    def subsno(self):
        """Gets the subsno of this SubscriptionPayments.  # noqa: E501


        :return: The subsno of this SubscriptionPayments.  # noqa: E501
        :rtype: int
        """
        return self._subsno

    @subsno.setter
    def subsno(self, subsno):
        """Sets the subsno of this SubscriptionPayments.


        :param subsno: The subsno of this SubscriptionPayments.  # noqa: E501
        :type: int
        """
        if subsno is None:
            raise ValueError("Invalid value for `subsno`, must not be `None`")  # noqa: E501
        if subsno is not None and subsno > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `subsno`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if subsno is not None and subsno < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `subsno`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._subsno = subsno

    @property
    def name(self):
        """Gets the name of this SubscriptionPayments.  # noqa: E501


        :return: The name of this SubscriptionPayments.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionPayments.


        :param name: The name of this SubscriptionPayments.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def start_date(self):
        """Gets the start_date of this SubscriptionPayments.  # noqa: E501


        :return: The start_date of this SubscriptionPayments.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SubscriptionPayments.


        :param start_date: The start_date of this SubscriptionPayments.  # noqa: E501
        :type: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def last_date(self):
        """Gets the last_date of this SubscriptionPayments.  # noqa: E501


        :return: The last_date of this SubscriptionPayments.  # noqa: E501
        :rtype: date
        """
        return self._last_date

    @last_date.setter
    def last_date(self, last_date):
        """Sets the last_date of this SubscriptionPayments.


        :param last_date: The last_date of this SubscriptionPayments.  # noqa: E501
        :type: date
        """
        if last_date is None:
            raise ValueError("Invalid value for `last_date`, must not be `None`")  # noqa: E501

        self._last_date = last_date

    @property
    def payments(self):
        """Gets the payments of this SubscriptionPayments.  # noqa: E501


        :return: The payments of this SubscriptionPayments.  # noqa: E501
        :rtype: list[Payment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this SubscriptionPayments.


        :param payments: The payments of this SubscriptionPayments.  # noqa: E501
        :type: list[Payment]
        """
        if payments is None:
            raise ValueError("Invalid value for `payments`, must not be `None`")  # noqa: E501

        self._payments = payments

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
        if not isinstance(other, SubscriptionPayments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
