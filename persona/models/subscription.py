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


class Subscription(object):
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
        'extno': 'int',
        'cusno': 'int',
        'paycusno': 'int',
        'kind': 'str',
        'state': 'str',
        'pricegroup': 'str',
        'package': 'Package',
        'dates': 'SubscriptionDates',
        'extsubsexists': 'bool',
        'campaign': 'Campaign',
        'paused': 'list[PausedSubscription]',
        'receiver': 'str',
        'delivery_address': 'DeliveryAddress',
        'pending_address_changes': 'list[PendingAddressChange]',
        'order_number': 'str',
        'payment_method': 'str',
        'payment_method_id': 'int'
    }

    attribute_map = {
        'subsno': 'subsno',
        'extno': 'extno',
        'cusno': 'cusno',
        'paycusno': 'paycusno',
        'kind': 'kind',
        'state': 'state',
        'pricegroup': 'pricegroup',
        'package': 'package',
        'dates': 'dates',
        'extsubsexists': 'extsubsexists',
        'campaign': 'campaign',
        'paused': 'paused',
        'receiver': 'receiver',
        'delivery_address': 'deliveryAddress',
        'pending_address_changes': 'pendingAddressChanges',
        'order_number': 'orderNumber',
        'payment_method': 'paymentMethod',
        'payment_method_id': 'paymentMethodId'
    }

    def __init__(self, subsno=None, extno=None, cusno=None, paycusno=None, kind=None, state=None, pricegroup=None, package=None, dates=None, extsubsexists=None, campaign=None, paused=None, receiver=None, delivery_address=None, pending_address_changes=None, order_number=None, payment_method=None, payment_method_id=None):  # noqa: E501
        """Subscription - a model defined in OpenAPI"""  # noqa: E501

        self._subsno = None
        self._extno = None
        self._cusno = None
        self._paycusno = None
        self._kind = None
        self._state = None
        self._pricegroup = None
        self._package = None
        self._dates = None
        self._extsubsexists = None
        self._campaign = None
        self._paused = None
        self._receiver = None
        self._delivery_address = None
        self._pending_address_changes = None
        self._order_number = None
        self._payment_method = None
        self._payment_method_id = None
        self.discriminator = None

        self.subsno = subsno
        self.extno = extno
        self.cusno = cusno
        self.paycusno = paycusno
        self.kind = kind
        self.state = state
        if pricegroup is not None:
            self.pricegroup = pricegroup
        self.package = package
        self.dates = dates
        self.extsubsexists = extsubsexists
        if campaign is not None:
            self.campaign = campaign
        if paused is not None:
            self.paused = paused
        if receiver is not None:
            self.receiver = receiver
        if delivery_address is not None:
            self.delivery_address = delivery_address
        if pending_address_changes is not None:
            self.pending_address_changes = pending_address_changes
        if order_number is not None:
            self.order_number = order_number
        if payment_method is not None:
            self.payment_method = payment_method
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id

    @property
    def subsno(self):
        """Gets the subsno of this Subscription.  # noqa: E501


        :return: The subsno of this Subscription.  # noqa: E501
        :rtype: int
        """
        return self._subsno

    @subsno.setter
    def subsno(self, subsno):
        """Sets the subsno of this Subscription.


        :param subsno: The subsno of this Subscription.  # noqa: E501
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
    def extno(self):
        """Gets the extno of this Subscription.  # noqa: E501


        :return: The extno of this Subscription.  # noqa: E501
        :rtype: int
        """
        return self._extno

    @extno.setter
    def extno(self, extno):
        """Sets the extno of this Subscription.


        :param extno: The extno of this Subscription.  # noqa: E501
        :type: int
        """
        if extno is None:
            raise ValueError("Invalid value for `extno`, must not be `None`")  # noqa: E501
        if extno is not None and extno > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `extno`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if extno is not None and extno < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `extno`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._extno = extno

    @property
    def cusno(self):
        """Gets the cusno of this Subscription.  # noqa: E501


        :return: The cusno of this Subscription.  # noqa: E501
        :rtype: int
        """
        return self._cusno

    @cusno.setter
    def cusno(self, cusno):
        """Sets the cusno of this Subscription.


        :param cusno: The cusno of this Subscription.  # noqa: E501
        :type: int
        """
        if cusno is None:
            raise ValueError("Invalid value for `cusno`, must not be `None`")  # noqa: E501
        if cusno is not None and cusno > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `cusno`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if cusno is not None and cusno < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `cusno`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._cusno = cusno

    @property
    def paycusno(self):
        """Gets the paycusno of this Subscription.  # noqa: E501


        :return: The paycusno of this Subscription.  # noqa: E501
        :rtype: int
        """
        return self._paycusno

    @paycusno.setter
    def paycusno(self, paycusno):
        """Sets the paycusno of this Subscription.


        :param paycusno: The paycusno of this Subscription.  # noqa: E501
        :type: int
        """
        if paycusno is None:
            raise ValueError("Invalid value for `paycusno`, must not be `None`")  # noqa: E501
        if paycusno is not None and paycusno > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `paycusno`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if paycusno is not None and paycusno < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `paycusno`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._paycusno = paycusno

    @property
    def kind(self):
        """Gets the kind of this Subscription.  # noqa: E501


        :return: The kind of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Subscription.


        :param kind: The kind of this Subscription.  # noqa: E501
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def state(self):
        """Gets the state of this Subscription.  # noqa: E501


        :return: The state of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Subscription.


        :param state: The state of this Subscription.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def pricegroup(self):
        """Gets the pricegroup of this Subscription.  # noqa: E501


        :return: The pricegroup of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._pricegroup

    @pricegroup.setter
    def pricegroup(self, pricegroup):
        """Sets the pricegroup of this Subscription.


        :param pricegroup: The pricegroup of this Subscription.  # noqa: E501
        :type: str
        """

        self._pricegroup = pricegroup

    @property
    def package(self):
        """Gets the package of this Subscription.  # noqa: E501


        :return: The package of this Subscription.  # noqa: E501
        :rtype: Package
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this Subscription.


        :param package: The package of this Subscription.  # noqa: E501
        :type: Package
        """
        if package is None:
            raise ValueError("Invalid value for `package`, must not be `None`")  # noqa: E501

        self._package = package

    @property
    def dates(self):
        """Gets the dates of this Subscription.  # noqa: E501


        :return: The dates of this Subscription.  # noqa: E501
        :rtype: SubscriptionDates
        """
        return self._dates

    @dates.setter
    def dates(self, dates):
        """Sets the dates of this Subscription.


        :param dates: The dates of this Subscription.  # noqa: E501
        :type: SubscriptionDates
        """
        if dates is None:
            raise ValueError("Invalid value for `dates`, must not be `None`")  # noqa: E501

        self._dates = dates

    @property
    def extsubsexists(self):
        """Gets the extsubsexists of this Subscription.  # noqa: E501


        :return: The extsubsexists of this Subscription.  # noqa: E501
        :rtype: bool
        """
        return self._extsubsexists

    @extsubsexists.setter
    def extsubsexists(self, extsubsexists):
        """Sets the extsubsexists of this Subscription.


        :param extsubsexists: The extsubsexists of this Subscription.  # noqa: E501
        :type: bool
        """
        if extsubsexists is None:
            raise ValueError("Invalid value for `extsubsexists`, must not be `None`")  # noqa: E501

        self._extsubsexists = extsubsexists

    @property
    def campaign(self):
        """Gets the campaign of this Subscription.  # noqa: E501


        :return: The campaign of this Subscription.  # noqa: E501
        :rtype: Campaign
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """Sets the campaign of this Subscription.


        :param campaign: The campaign of this Subscription.  # noqa: E501
        :type: Campaign
        """

        self._campaign = campaign

    @property
    def paused(self):
        """Gets the paused of this Subscription.  # noqa: E501


        :return: The paused of this Subscription.  # noqa: E501
        :rtype: list[PausedSubscription]
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this Subscription.


        :param paused: The paused of this Subscription.  # noqa: E501
        :type: list[PausedSubscription]
        """

        self._paused = paused

    @property
    def receiver(self):
        """Gets the receiver of this Subscription.  # noqa: E501


        :return: The receiver of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this Subscription.


        :param receiver: The receiver of this Subscription.  # noqa: E501
        :type: str
        """

        self._receiver = receiver

    @property
    def delivery_address(self):
        """Gets the delivery_address of this Subscription.  # noqa: E501


        :return: The delivery_address of this Subscription.  # noqa: E501
        :rtype: DeliveryAddress
        """
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, delivery_address):
        """Sets the delivery_address of this Subscription.


        :param delivery_address: The delivery_address of this Subscription.  # noqa: E501
        :type: DeliveryAddress
        """

        self._delivery_address = delivery_address

    @property
    def pending_address_changes(self):
        """Gets the pending_address_changes of this Subscription.  # noqa: E501


        :return: The pending_address_changes of this Subscription.  # noqa: E501
        :rtype: list[PendingAddressChange]
        """
        return self._pending_address_changes

    @pending_address_changes.setter
    def pending_address_changes(self, pending_address_changes):
        """Sets the pending_address_changes of this Subscription.


        :param pending_address_changes: The pending_address_changes of this Subscription.  # noqa: E501
        :type: list[PendingAddressChange]
        """

        self._pending_address_changes = pending_address_changes

    @property
    def order_number(self):
        """Gets the order_number of this Subscription.  # noqa: E501


        :return: The order_number of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this Subscription.


        :param order_number: The order_number of this Subscription.  # noqa: E501
        :type: str
        """

        self._order_number = order_number

    @property
    def payment_method(self):
        """Gets the payment_method of this Subscription.  # noqa: E501


        :return: The payment_method of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this Subscription.


        :param payment_method: The payment_method of this Subscription.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this Subscription.  # noqa: E501


        :return: The payment_method_id of this Subscription.  # noqa: E501
        :rtype: int
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this Subscription.


        :param payment_method_id: The payment_method_id of this Subscription.  # noqa: E501
        :type: int
        """
        if payment_method_id is not None and payment_method_id > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `payment_method_id`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if payment_method_id is not None and payment_method_id < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `payment_method_id`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._payment_method_id = payment_method_id

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
        if not isinstance(other, Subscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
