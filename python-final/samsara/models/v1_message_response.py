# coding: utf-8

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-11-19
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class V1MessageResponse(object):
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
        'driver_id': 'int',
        'is_read': 'bool',
        'sender': 'V1MessageResponseSender',
        'sent_at_ms': 'int',
        'text': 'str'
    }

    attribute_map = {
        'driver_id': 'driverId',
        'is_read': 'isRead',
        'sender': 'sender',
        'sent_at_ms': 'sentAtMs',
        'text': 'text'
    }

    def __init__(self, driver_id=None, is_read=None, sender=None, sent_at_ms=None, text=None, local_vars_configuration=None):  # noqa: E501
        """V1MessageResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._driver_id = None
        self._is_read = None
        self._sender = None
        self._sent_at_ms = None
        self._text = None
        self.discriminator = None

        self.driver_id = driver_id
        self.is_read = is_read
        self.sender = sender
        self.sent_at_ms = sent_at_ms
        self.text = text

    @property
    def driver_id(self):
        """Gets the driver_id of this V1MessageResponse.  # noqa: E501

        ID of the driver for whom the message is sent to or sent by.  # noqa: E501

        :return: The driver_id of this V1MessageResponse.  # noqa: E501
        :rtype: int
        """
        return self._driver_id

    @driver_id.setter
    def driver_id(self, driver_id):
        """Sets the driver_id of this V1MessageResponse.

        ID of the driver for whom the message is sent to or sent by.  # noqa: E501

        :param driver_id: The driver_id of this V1MessageResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and driver_id is None:  # noqa: E501
            raise ValueError("Invalid value for `driver_id`, must not be `None`")  # noqa: E501

        self._driver_id = driver_id

    @property
    def is_read(self):
        """Gets the is_read of this V1MessageResponse.  # noqa: E501

        True if the message was read by the recipient.  # noqa: E501

        :return: The is_read of this V1MessageResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_read

    @is_read.setter
    def is_read(self, is_read):
        """Sets the is_read of this V1MessageResponse.

        True if the message was read by the recipient.  # noqa: E501

        :param is_read: The is_read of this V1MessageResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_read is None:  # noqa: E501
            raise ValueError("Invalid value for `is_read`, must not be `None`")  # noqa: E501

        self._is_read = is_read

    @property
    def sender(self):
        """Gets the sender of this V1MessageResponse.  # noqa: E501


        :return: The sender of this V1MessageResponse.  # noqa: E501
        :rtype: V1MessageResponseSender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this V1MessageResponse.


        :param sender: The sender of this V1MessageResponse.  # noqa: E501
        :type: V1MessageResponseSender
        """
        if self.local_vars_configuration.client_side_validation and sender is None:  # noqa: E501
            raise ValueError("Invalid value for `sender`, must not be `None`")  # noqa: E501

        self._sender = sender

    @property
    def sent_at_ms(self):
        """Gets the sent_at_ms of this V1MessageResponse.  # noqa: E501

        The time in Unix epoch milliseconds that the message is sent to the recipient.  # noqa: E501

        :return: The sent_at_ms of this V1MessageResponse.  # noqa: E501
        :rtype: int
        """
        return self._sent_at_ms

    @sent_at_ms.setter
    def sent_at_ms(self, sent_at_ms):
        """Sets the sent_at_ms of this V1MessageResponse.

        The time in Unix epoch milliseconds that the message is sent to the recipient.  # noqa: E501

        :param sent_at_ms: The sent_at_ms of this V1MessageResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and sent_at_ms is None:  # noqa: E501
            raise ValueError("Invalid value for `sent_at_ms`, must not be `None`")  # noqa: E501

        self._sent_at_ms = sent_at_ms

    @property
    def text(self):
        """Gets the text of this V1MessageResponse.  # noqa: E501

        The text sent in the message.  # noqa: E501

        :return: The text of this V1MessageResponse.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this V1MessageResponse.

        The text sent in the message.  # noqa: E501

        :param text: The text of this V1MessageResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

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
        if not isinstance(other, V1MessageResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1MessageResponse):
            return True

        return self.to_dict() != other.to_dict()
