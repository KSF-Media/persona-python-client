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


class Package(object):
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
        'id': 'str',
        'name': 'str',
        'paper': 'Paper',
        'products': 'list[Product]',
        'offers': 'list[PackageOffer]',
        'campaigns': 'list[Campaign]',
        'next_delivery': 'date',
        'description': 'PackageDescription'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'paper': 'paper',
        'products': 'products',
        'offers': 'offers',
        'campaigns': 'campaigns',
        'next_delivery': 'nextDelivery',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, paper=None, products=None, offers=None, campaigns=None, next_delivery=None, description=None):  # noqa: E501
        """Package - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._paper = None
        self._products = None
        self._offers = None
        self._campaigns = None
        self._next_delivery = None
        self._description = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.paper = paper
        self.products = products
        self.offers = offers
        self.campaigns = campaigns
        if next_delivery is not None:
            self.next_delivery = next_delivery
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this Package.  # noqa: E501


        :return: The id of this Package.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Package.


        :param id: The id of this Package.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Package.  # noqa: E501


        :return: The name of this Package.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Package.


        :param name: The name of this Package.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def paper(self):
        """Gets the paper of this Package.  # noqa: E501


        :return: The paper of this Package.  # noqa: E501
        :rtype: Paper
        """
        return self._paper

    @paper.setter
    def paper(self, paper):
        """Sets the paper of this Package.


        :param paper: The paper of this Package.  # noqa: E501
        :type: Paper
        """
        if paper is None:
            raise ValueError("Invalid value for `paper`, must not be `None`")  # noqa: E501

        self._paper = paper

    @property
    def products(self):
        """Gets the products of this Package.  # noqa: E501


        :return: The products of this Package.  # noqa: E501
        :rtype: list[Product]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this Package.


        :param products: The products of this Package.  # noqa: E501
        :type: list[Product]
        """
        if products is None:
            raise ValueError("Invalid value for `products`, must not be `None`")  # noqa: E501

        self._products = products

    @property
    def offers(self):
        """Gets the offers of this Package.  # noqa: E501


        :return: The offers of this Package.  # noqa: E501
        :rtype: list[PackageOffer]
        """
        return self._offers

    @offers.setter
    def offers(self, offers):
        """Sets the offers of this Package.


        :param offers: The offers of this Package.  # noqa: E501
        :type: list[PackageOffer]
        """
        if offers is None:
            raise ValueError("Invalid value for `offers`, must not be `None`")  # noqa: E501

        self._offers = offers

    @property
    def campaigns(self):
        """Gets the campaigns of this Package.  # noqa: E501


        :return: The campaigns of this Package.  # noqa: E501
        :rtype: list[Campaign]
        """
        return self._campaigns

    @campaigns.setter
    def campaigns(self, campaigns):
        """Sets the campaigns of this Package.


        :param campaigns: The campaigns of this Package.  # noqa: E501
        :type: list[Campaign]
        """
        if campaigns is None:
            raise ValueError("Invalid value for `campaigns`, must not be `None`")  # noqa: E501

        self._campaigns = campaigns

    @property
    def next_delivery(self):
        """Gets the next_delivery of this Package.  # noqa: E501


        :return: The next_delivery of this Package.  # noqa: E501
        :rtype: date
        """
        return self._next_delivery

    @next_delivery.setter
    def next_delivery(self, next_delivery):
        """Sets the next_delivery of this Package.


        :param next_delivery: The next_delivery of this Package.  # noqa: E501
        :type: date
        """

        self._next_delivery = next_delivery

    @property
    def description(self):
        """Gets the description of this Package.  # noqa: E501


        :return: The description of this Package.  # noqa: E501
        :rtype: PackageDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Package.


        :param description: The description of this Package.  # noqa: E501
        :type: PackageDescription
        """

        self._description = description

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
        if not isinstance(other, Package):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
