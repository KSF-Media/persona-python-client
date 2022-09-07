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


class DeliveryReclamation(object):
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
        'number': 'int',
        'customer_number': 'int',
        'subscription_number': 'int',
        'date': 'date',
        'paper': 'str',
        'publication_date': 'date',
        'claim': 'str',
        'door_code': 'str'
    }

    attribute_map = {
        'number': 'number',
        'customer_number': 'customerNumber',
        'subscription_number': 'subscriptionNumber',
        'date': 'date',
        'paper': 'paper',
        'publication_date': 'publicationDate',
        'claim': 'claim',
        'door_code': 'doorCode'
    }

    def __init__(self, number=None, customer_number=None, subscription_number=None, date=None, paper=None, publication_date=None, claim=None, door_code=None):  # noqa: E501
        """DeliveryReclamation - a model defined in OpenAPI"""  # noqa: E501

        self._number = None
        self._customer_number = None
        self._subscription_number = None
        self._date = None
        self._paper = None
        self._publication_date = None
        self._claim = None
        self._door_code = None
        self.discriminator = None

        self.number = number
        self.customer_number = customer_number
        self.subscription_number = subscription_number
        self.date = date
        if paper is not None:
            self.paper = paper
        self.publication_date = publication_date
        self.claim = claim
        if door_code is not None:
            self.door_code = door_code

    @property
    def number(self):
        """Gets the number of this DeliveryReclamation.  # noqa: E501

        The reclamation identifier  # noqa: E501

        :return: The number of this DeliveryReclamation.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this DeliveryReclamation.

        The reclamation identifier  # noqa: E501

        :param number: The number of this DeliveryReclamation.  # noqa: E501
        :type: int
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501
        if number is not None and number > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `number`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if number is not None and number < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `number`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._number = number

    @property
    def customer_number(self):
        """Gets the customer_number of this DeliveryReclamation.  # noqa: E501

        The identifier of the customer that made reclamation  # noqa: E501

        :return: The customer_number of this DeliveryReclamation.  # noqa: E501
        :rtype: int
        """
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        """Sets the customer_number of this DeliveryReclamation.

        The identifier of the customer that made reclamation  # noqa: E501

        :param customer_number: The customer_number of this DeliveryReclamation.  # noqa: E501
        :type: int
        """
        if customer_number is None:
            raise ValueError("Invalid value for `customer_number`, must not be `None`")  # noqa: E501
        if customer_number is not None and customer_number > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `customer_number`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if customer_number is not None and customer_number < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `customer_number`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._customer_number = customer_number

    @property
    def subscription_number(self):
        """Gets the subscription_number of this DeliveryReclamation.  # noqa: E501

        The identifier of the subscription for which reclamation was made  # noqa: E501

        :return: The subscription_number of this DeliveryReclamation.  # noqa: E501
        :rtype: int
        """
        return self._subscription_number

    @subscription_number.setter
    def subscription_number(self, subscription_number):
        """Sets the subscription_number of this DeliveryReclamation.

        The identifier of the subscription for which reclamation was made  # noqa: E501

        :param subscription_number: The subscription_number of this DeliveryReclamation.  # noqa: E501
        :type: int
        """
        if subscription_number is None:
            raise ValueError("Invalid value for `subscription_number`, must not be `None`")  # noqa: E501
        if subscription_number is not None and subscription_number > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `subscription_number`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if subscription_number is not None and subscription_number < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `subscription_number`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._subscription_number = subscription_number

    @property
    def date(self):
        """Gets the date of this DeliveryReclamation.  # noqa: E501


        :return: The date of this DeliveryReclamation.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this DeliveryReclamation.


        :param date: The date of this DeliveryReclamation.  # noqa: E501
        :type: date
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def paper(self):
        """Gets the paper of this DeliveryReclamation.  # noqa: E501


        :return: The paper of this DeliveryReclamation.  # noqa: E501
        :rtype: str
        """
        return self._paper

    @paper.setter
    def paper(self, paper):
        """Sets the paper of this DeliveryReclamation.


        :param paper: The paper of this DeliveryReclamation.  # noqa: E501
        :type: str
        """

        self._paper = paper

    @property
    def publication_date(self):
        """Gets the publication_date of this DeliveryReclamation.  # noqa: E501


        :return: The publication_date of this DeliveryReclamation.  # noqa: E501
        :rtype: date
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this DeliveryReclamation.


        :param publication_date: The publication_date of this DeliveryReclamation.  # noqa: E501
        :type: date
        """
        if publication_date is None:
            raise ValueError("Invalid value for `publication_date`, must not be `None`")  # noqa: E501

        self._publication_date = publication_date

    @property
    def claim(self):
        """Gets the claim of this DeliveryReclamation.  # noqa: E501


        :return: The claim of this DeliveryReclamation.  # noqa: E501
        :rtype: str
        """
        return self._claim

    @claim.setter
    def claim(self, claim):
        """Sets the claim of this DeliveryReclamation.


        :param claim: The claim of this DeliveryReclamation.  # noqa: E501
        :type: str
        """
        if claim is None:
            raise ValueError("Invalid value for `claim`, must not be `None`")  # noqa: E501
        allowed_values = ["Extension", "NewDelivery"]  # noqa: E501
        if claim not in allowed_values:
            raise ValueError(
                "Invalid value for `claim` ({0}), must be one of {1}"  # noqa: E501
                .format(claim, allowed_values)
            )

        self._claim = claim

    @property
    def door_code(self):
        """Gets the door_code of this DeliveryReclamation.  # noqa: E501

        Door code for redelivery  # noqa: E501

        :return: The door_code of this DeliveryReclamation.  # noqa: E501
        :rtype: str
        """
        return self._door_code

    @door_code.setter
    def door_code(self, door_code):
        """Sets the door_code of this DeliveryReclamation.

        Door code for redelivery  # noqa: E501

        :param door_code: The door_code of this DeliveryReclamation.  # noqa: E501
        :type: str
        """

        self._door_code = door_code

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
        if not isinstance(other, DeliveryReclamation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
