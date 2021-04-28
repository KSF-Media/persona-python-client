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


class NewDeliveryReclamation(object):
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
        'paper': 'str',
        'publication_date': 'date',
        'claim': 'str'
    }

    attribute_map = {
        'paper': 'paper',
        'publication_date': 'publicationDate',
        'claim': 'claim'
    }

    def __init__(self, paper=None, publication_date=None, claim=None):  # noqa: E501
        """NewDeliveryReclamation - a model defined in OpenAPI"""  # noqa: E501

        self._paper = None
        self._publication_date = None
        self._claim = None
        self.discriminator = None

        if paper is not None:
            self.paper = paper
        self.publication_date = publication_date
        self.claim = claim

    @property
    def paper(self):
        """Gets the paper of this NewDeliveryReclamation.  # noqa: E501


        :return: The paper of this NewDeliveryReclamation.  # noqa: E501
        :rtype: str
        """
        return self._paper

    @paper.setter
    def paper(self, paper):
        """Sets the paper of this NewDeliveryReclamation.


        :param paper: The paper of this NewDeliveryReclamation.  # noqa: E501
        :type: str
        """

        self._paper = paper

    @property
    def publication_date(self):
        """Gets the publication_date of this NewDeliveryReclamation.  # noqa: E501


        :return: The publication_date of this NewDeliveryReclamation.  # noqa: E501
        :rtype: date
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this NewDeliveryReclamation.


        :param publication_date: The publication_date of this NewDeliveryReclamation.  # noqa: E501
        :type: date
        """
        if publication_date is None:
            raise ValueError("Invalid value for `publication_date`, must not be `None`")  # noqa: E501

        self._publication_date = publication_date

    @property
    def claim(self):
        """Gets the claim of this NewDeliveryReclamation.  # noqa: E501

        The type of claim for the reclamation  # noqa: E501

        :return: The claim of this NewDeliveryReclamation.  # noqa: E501
        :rtype: str
        """
        return self._claim

    @claim.setter
    def claim(self, claim):
        """Sets the claim of this NewDeliveryReclamation.

        The type of claim for the reclamation  # noqa: E501

        :param claim: The claim of this NewDeliveryReclamation.  # noqa: E501
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
        if not isinstance(other, NewDeliveryReclamation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
