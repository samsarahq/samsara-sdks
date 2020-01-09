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


class InlineObject10(object):
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
        'group_id': 'int',
        'sensors': 'list[int]'
    }

    attribute_map = {
        'group_id': 'groupId',
        'sensors': 'sensors'
    }

    def __init__(self, group_id=None, sensors=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject10 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group_id = None
        self._sensors = None
        self.discriminator = None

        self.group_id = group_id
        self.sensors = sensors

    @property
    def group_id(self):
        """Gets the group_id of this InlineObject10.  # noqa: E501

        Group ID  # noqa: E501

        :return: The group_id of this InlineObject10.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this InlineObject10.

        Group ID  # noqa: E501

        :param group_id: The group_id of this InlineObject10.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and group_id is None:  # noqa: E501
            raise ValueError("Invalid value for `group_id`, must not be `None`")  # noqa: E501

        self._group_id = group_id

    @property
    def sensors(self):
        """Gets the sensors of this InlineObject10.  # noqa: E501

        List of sensor IDs to query.  # noqa: E501

        :return: The sensors of this InlineObject10.  # noqa: E501
        :rtype: list[int]
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        """Sets the sensors of this InlineObject10.

        List of sensor IDs to query.  # noqa: E501

        :param sensors: The sensors of this InlineObject10.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and sensors is None:  # noqa: E501
            raise ValueError("Invalid value for `sensors`, must not be `None`")  # noqa: E501

        self._sensors = sensors

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
        if not isinstance(other, InlineObject10):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject10):
            return True

        return self.to_dict() != other.to_dict()
