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


class Payment(object):
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
        'invno': 'int',
        'date': 'date',
        'due_date': 'date',
        'expenses': 'float',
        'interest': 'float',
        'vat': 'float',
        'amount': 'float',
        'open_amount': 'float',
        'type': 'str',
        'state': 'str',
        'disc_percent': 'float',
        'disc_amount': 'float',
        'reference': 'str'
    }

    attribute_map = {
        'invno': 'invno',
        'date': 'date',
        'due_date': 'dueDate',
        'expenses': 'expenses',
        'interest': 'interest',
        'vat': 'vat',
        'amount': 'amount',
        'open_amount': 'openAmount',
        'type': 'type',
        'state': 'state',
        'disc_percent': 'discPercent',
        'disc_amount': 'discAmount',
        'reference': 'reference'
    }

    def __init__(self, invno=None, date=None, due_date=None, expenses=None, interest=None, vat=None, amount=None, open_amount=None, type=None, state=None, disc_percent=None, disc_amount=None, reference=None):  # noqa: E501
        """Payment - a model defined in OpenAPI"""  # noqa: E501

        self._invno = None
        self._date = None
        self._due_date = None
        self._expenses = None
        self._interest = None
        self._vat = None
        self._amount = None
        self._open_amount = None
        self._type = None
        self._state = None
        self._disc_percent = None
        self._disc_amount = None
        self._reference = None
        self.discriminator = None

        self.invno = invno
        if date is not None:
            self.date = date
        if due_date is not None:
            self.due_date = due_date
        self.expenses = expenses
        self.interest = interest
        self.vat = vat
        self.amount = amount
        self.open_amount = open_amount
        self.type = type
        self.state = state
        if disc_percent is not None:
            self.disc_percent = disc_percent
        if disc_amount is not None:
            self.disc_amount = disc_amount
        if reference is not None:
            self.reference = reference

    @property
    def invno(self):
        """Gets the invno of this Payment.  # noqa: E501

        Payment invoice ID  # noqa: E501

        :return: The invno of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._invno

    @invno.setter
    def invno(self, invno):
        """Sets the invno of this Payment.

        Payment invoice ID  # noqa: E501

        :param invno: The invno of this Payment.  # noqa: E501
        :type: int
        """
        if invno is None:
            raise ValueError("Invalid value for `invno`, must not be `None`")  # noqa: E501
        if invno is not None and invno > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `invno`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if invno is not None and invno < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `invno`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._invno = invno

    @property
    def date(self):
        """Gets the date of this Payment.  # noqa: E501


        :return: The date of this Payment.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Payment.


        :param date: The date of this Payment.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def due_date(self):
        """Gets the due_date of this Payment.  # noqa: E501


        :return: The due_date of this Payment.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Payment.


        :param due_date: The due_date of this Payment.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def expenses(self):
        """Gets the expenses of this Payment.  # noqa: E501

          # noqa: E501

        :return: The expenses of this Payment.  # noqa: E501
        :rtype: float
        """
        return self._expenses

    @expenses.setter
    def expenses(self, expenses):
        """Sets the expenses of this Payment.

          # noqa: E501

        :param expenses: The expenses of this Payment.  # noqa: E501
        :type: float
        """
        if expenses is None:
            raise ValueError("Invalid value for `expenses`, must not be `None`")  # noqa: E501

        self._expenses = expenses

    @property
    def interest(self):
        """Gets the interest of this Payment.  # noqa: E501

          # noqa: E501

        :return: The interest of this Payment.  # noqa: E501
        :rtype: float
        """
        return self._interest

    @interest.setter
    def interest(self, interest):
        """Sets the interest of this Payment.

          # noqa: E501

        :param interest: The interest of this Payment.  # noqa: E501
        :type: float
        """
        if interest is None:
            raise ValueError("Invalid value for `interest`, must not be `None`")  # noqa: E501

        self._interest = interest

    @property
    def vat(self):
        """Gets the vat of this Payment.  # noqa: E501

          # noqa: E501

        :return: The vat of this Payment.  # noqa: E501
        :rtype: float
        """
        return self._vat

    @vat.setter
    def vat(self, vat):
        """Sets the vat of this Payment.

          # noqa: E501

        :param vat: The vat of this Payment.  # noqa: E501
        :type: float
        """
        if vat is None:
            raise ValueError("Invalid value for `vat`, must not be `None`")  # noqa: E501

        self._vat = vat

    @property
    def amount(self):
        """Gets the amount of this Payment.  # noqa: E501

          # noqa: E501

        :return: The amount of this Payment.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Payment.

          # noqa: E501

        :param amount: The amount of this Payment.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def open_amount(self):
        """Gets the open_amount of this Payment.  # noqa: E501

          # noqa: E501

        :return: The open_amount of this Payment.  # noqa: E501
        :rtype: float
        """
        return self._open_amount

    @open_amount.setter
    def open_amount(self, open_amount):
        """Sets the open_amount of this Payment.

          # noqa: E501

        :param open_amount: The open_amount of this Payment.  # noqa: E501
        :type: float
        """
        if open_amount is None:
            raise ValueError("Invalid value for `open_amount`, must not be `None`")  # noqa: E501

        self._open_amount = open_amount

    @property
    def type(self):
        """Gets the type of this Payment.  # noqa: E501


        :return: The type of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Payment.


        :param type: The type of this Payment.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["NormalState", "DirectDebit", "Reminder1", "Reminder2", "ReservedPaymentType1", "Nonpayment", "ReservedPaymentType2", "Reimbursement"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def state(self):
        """Gets the state of this Payment.  # noqa: E501


        :return: The state of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Payment.


        :param state: The state of this Payment.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["PaymentOpen", "PartiallyPaid", "Paid", "Reminded", "Foreclosure", "ReservedPaymentState", "Reimbursed", "CreditLoss"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def disc_percent(self):
        """Gets the disc_percent of this Payment.  # noqa: E501

          # noqa: E501

        :return: The disc_percent of this Payment.  # noqa: E501
        :rtype: float
        """
        return self._disc_percent

    @disc_percent.setter
    def disc_percent(self, disc_percent):
        """Sets the disc_percent of this Payment.

          # noqa: E501

        :param disc_percent: The disc_percent of this Payment.  # noqa: E501
        :type: float
        """

        self._disc_percent = disc_percent

    @property
    def disc_amount(self):
        """Gets the disc_amount of this Payment.  # noqa: E501

          # noqa: E501

        :return: The disc_amount of this Payment.  # noqa: E501
        :rtype: float
        """
        return self._disc_amount

    @disc_amount.setter
    def disc_amount(self, disc_amount):
        """Sets the disc_amount of this Payment.

          # noqa: E501

        :param disc_amount: The disc_amount of this Payment.  # noqa: E501
        :type: float
        """

        self._disc_amount = disc_amount

    @property
    def reference(self):
        """Gets the reference of this Payment.  # noqa: E501

        Reference number  # noqa: E501

        :return: The reference of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Payment.

        Reference number  # noqa: E501

        :param reference: The reference of this Payment.  # noqa: E501
        :type: str
        """

        self._reference = reference

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
        if not isinstance(other, Payment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
