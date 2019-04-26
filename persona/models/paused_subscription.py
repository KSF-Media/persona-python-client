# coding: utf-8

"""
    Persona

    KSF Media unified login service  # noqa: E501

    OpenAPI spec version: 1.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PausedSubscription(object):
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
        'sleep_startdate': 'date',
        'sleep_end_date': 'date',
        'credit_type': 'str',
        'credit_amount': 'int',
        'sleep_type': 'str',
        'credited': 'bool',
        'credit_invno': 'int',
        'booking_date': 'str',
        'allow_webpaper': 'bool',
        'receive_type': 'str',
        'confirm_status': 'str',
        'stamp_user': 'str'
    }

    attribute_map = {
        'subsno': 'subsno',
        'sleep_startdate': 'sleepStartdate',
        'sleep_end_date': 'sleepEndDate',
        'credit_type': 'creditType',
        'credit_amount': 'creditAmount',
        'sleep_type': 'sleepType',
        'credited': 'credited',
        'credit_invno': 'creditInvno',
        'booking_date': 'bookingDate',
        'allow_webpaper': 'allowWebpaper',
        'receive_type': 'receiveType',
        'confirm_status': 'confirmStatus',
        'stamp_user': 'stampUser'
    }

    def __init__(self, subsno=None, sleep_startdate=None, sleep_end_date=None, credit_type=None, credit_amount=None, sleep_type=None, credited=None, credit_invno=None, booking_date=None, allow_webpaper=None, receive_type=None, confirm_status=None, stamp_user=None):  # noqa: E501
        """PausedSubscription - a model defined in OpenAPI"""  # noqa: E501

        self._subsno = None
        self._sleep_startdate = None
        self._sleep_end_date = None
        self._credit_type = None
        self._credit_amount = None
        self._sleep_type = None
        self._credited = None
        self._credit_invno = None
        self._booking_date = None
        self._allow_webpaper = None
        self._receive_type = None
        self._confirm_status = None
        self._stamp_user = None
        self.discriminator = None

        self.subsno = subsno
        self.sleep_startdate = sleep_startdate
        self.sleep_end_date = sleep_end_date
        self.credit_type = credit_type
        self.credit_amount = credit_amount
        self.sleep_type = sleep_type
        self.credited = credited
        self.credit_invno = credit_invno
        self.booking_date = booking_date
        self.allow_webpaper = allow_webpaper
        self.receive_type = receive_type
        self.confirm_status = confirm_status
        self.stamp_user = stamp_user

    @property
    def subsno(self):
        """Gets the subsno of this PausedSubscription.  # noqa: E501


        :return: The subsno of this PausedSubscription.  # noqa: E501
        :rtype: int
        """
        return self._subsno

    @subsno.setter
    def subsno(self, subsno):
        """Sets the subsno of this PausedSubscription.


        :param subsno: The subsno of this PausedSubscription.  # noqa: E501
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
    def sleep_startdate(self):
        """Gets the sleep_startdate of this PausedSubscription.  # noqa: E501


        :return: The sleep_startdate of this PausedSubscription.  # noqa: E501
        :rtype: date
        """
        return self._sleep_startdate

    @sleep_startdate.setter
    def sleep_startdate(self, sleep_startdate):
        """Sets the sleep_startdate of this PausedSubscription.


        :param sleep_startdate: The sleep_startdate of this PausedSubscription.  # noqa: E501
        :type: date
        """
        if sleep_startdate is None:
            raise ValueError("Invalid value for `sleep_startdate`, must not be `None`")  # noqa: E501

        self._sleep_startdate = sleep_startdate

    @property
    def sleep_end_date(self):
        """Gets the sleep_end_date of this PausedSubscription.  # noqa: E501


        :return: The sleep_end_date of this PausedSubscription.  # noqa: E501
        :rtype: date
        """
        return self._sleep_end_date

    @sleep_end_date.setter
    def sleep_end_date(self, sleep_end_date):
        """Sets the sleep_end_date of this PausedSubscription.


        :param sleep_end_date: The sleep_end_date of this PausedSubscription.  # noqa: E501
        :type: date
        """
        if sleep_end_date is None:
            raise ValueError("Invalid value for `sleep_end_date`, must not be `None`")  # noqa: E501

        self._sleep_end_date = sleep_end_date

    @property
    def credit_type(self):
        """Gets the credit_type of this PausedSubscription.  # noqa: E501


        :return: The credit_type of this PausedSubscription.  # noqa: E501
        :rtype: str
        """
        return self._credit_type

    @credit_type.setter
    def credit_type(self, credit_type):
        """Sets the credit_type of this PausedSubscription.


        :param credit_type: The credit_type of this PausedSubscription.  # noqa: E501
        :type: str
        """
        if credit_type is None:
            raise ValueError("Invalid value for `credit_type`, must not be `None`")  # noqa: E501

        self._credit_type = credit_type

    @property
    def credit_amount(self):
        """Gets the credit_amount of this PausedSubscription.  # noqa: E501


        :return: The credit_amount of this PausedSubscription.  # noqa: E501
        :rtype: int
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """Sets the credit_amount of this PausedSubscription.


        :param credit_amount: The credit_amount of this PausedSubscription.  # noqa: E501
        :type: int
        """
        if credit_amount is None:
            raise ValueError("Invalid value for `credit_amount`, must not be `None`")  # noqa: E501
        if credit_amount is not None and credit_amount > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `credit_amount`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if credit_amount is not None and credit_amount < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `credit_amount`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._credit_amount = credit_amount

    @property
    def sleep_type(self):
        """Gets the sleep_type of this PausedSubscription.  # noqa: E501


        :return: The sleep_type of this PausedSubscription.  # noqa: E501
        :rtype: str
        """
        return self._sleep_type

    @sleep_type.setter
    def sleep_type(self, sleep_type):
        """Sets the sleep_type of this PausedSubscription.


        :param sleep_type: The sleep_type of this PausedSubscription.  # noqa: E501
        :type: str
        """
        if sleep_type is None:
            raise ValueError("Invalid value for `sleep_type`, must not be `None`")  # noqa: E501

        self._sleep_type = sleep_type

    @property
    def credited(self):
        """Gets the credited of this PausedSubscription.  # noqa: E501


        :return: The credited of this PausedSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._credited

    @credited.setter
    def credited(self, credited):
        """Sets the credited of this PausedSubscription.


        :param credited: The credited of this PausedSubscription.  # noqa: E501
        :type: bool
        """
        if credited is None:
            raise ValueError("Invalid value for `credited`, must not be `None`")  # noqa: E501

        self._credited = credited

    @property
    def credit_invno(self):
        """Gets the credit_invno of this PausedSubscription.  # noqa: E501


        :return: The credit_invno of this PausedSubscription.  # noqa: E501
        :rtype: int
        """
        return self._credit_invno

    @credit_invno.setter
    def credit_invno(self, credit_invno):
        """Sets the credit_invno of this PausedSubscription.


        :param credit_invno: The credit_invno of this PausedSubscription.  # noqa: E501
        :type: int
        """
        if credit_invno is None:
            raise ValueError("Invalid value for `credit_invno`, must not be `None`")  # noqa: E501
        if credit_invno is not None and credit_invno > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `credit_invno`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if credit_invno is not None and credit_invno < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `credit_invno`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._credit_invno = credit_invno

    @property
    def booking_date(self):
        """Gets the booking_date of this PausedSubscription.  # noqa: E501


        :return: The booking_date of this PausedSubscription.  # noqa: E501
        :rtype: str
        """
        return self._booking_date

    @booking_date.setter
    def booking_date(self, booking_date):
        """Sets the booking_date of this PausedSubscription.


        :param booking_date: The booking_date of this PausedSubscription.  # noqa: E501
        :type: str
        """
        if booking_date is None:
            raise ValueError("Invalid value for `booking_date`, must not be `None`")  # noqa: E501

        self._booking_date = booking_date

    @property
    def allow_webpaper(self):
        """Gets the allow_webpaper of this PausedSubscription.  # noqa: E501


        :return: The allow_webpaper of this PausedSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._allow_webpaper

    @allow_webpaper.setter
    def allow_webpaper(self, allow_webpaper):
        """Sets the allow_webpaper of this PausedSubscription.


        :param allow_webpaper: The allow_webpaper of this PausedSubscription.  # noqa: E501
        :type: bool
        """
        if allow_webpaper is None:
            raise ValueError("Invalid value for `allow_webpaper`, must not be `None`")  # noqa: E501

        self._allow_webpaper = allow_webpaper

    @property
    def receive_type(self):
        """Gets the receive_type of this PausedSubscription.  # noqa: E501


        :return: The receive_type of this PausedSubscription.  # noqa: E501
        :rtype: str
        """
        return self._receive_type

    @receive_type.setter
    def receive_type(self, receive_type):
        """Sets the receive_type of this PausedSubscription.


        :param receive_type: The receive_type of this PausedSubscription.  # noqa: E501
        :type: str
        """
        if receive_type is None:
            raise ValueError("Invalid value for `receive_type`, must not be `None`")  # noqa: E501

        self._receive_type = receive_type

    @property
    def confirm_status(self):
        """Gets the confirm_status of this PausedSubscription.  # noqa: E501


        :return: The confirm_status of this PausedSubscription.  # noqa: E501
        :rtype: str
        """
        return self._confirm_status

    @confirm_status.setter
    def confirm_status(self, confirm_status):
        """Sets the confirm_status of this PausedSubscription.


        :param confirm_status: The confirm_status of this PausedSubscription.  # noqa: E501
        :type: str
        """
        if confirm_status is None:
            raise ValueError("Invalid value for `confirm_status`, must not be `None`")  # noqa: E501

        self._confirm_status = confirm_status

    @property
    def stamp_user(self):
        """Gets the stamp_user of this PausedSubscription.  # noqa: E501


        :return: The stamp_user of this PausedSubscription.  # noqa: E501
        :rtype: str
        """
        return self._stamp_user

    @stamp_user.setter
    def stamp_user(self, stamp_user):
        """Sets the stamp_user of this PausedSubscription.


        :param stamp_user: The stamp_user of this PausedSubscription.  # noqa: E501
        :type: str
        """
        if stamp_user is None:
            raise ValueError("Invalid value for `stamp_user`, must not be `None`")  # noqa: E501

        self._stamp_user = stamp_user

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
        if not isinstance(other, PausedSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
