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


class V1VisionRunByCameraResponseAngleCheck(object):
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
        'angle_configured': 'V1VisionRunByCameraResponseAngleCheckAngleConfigured',
        'angle_found': 'int',
        'end_step_name': 'str',
        'start_step_name': 'str'
    }

    attribute_map = {
        'angle_configured': 'angleConfigured',
        'angle_found': 'angleFound',
        'end_step_name': 'endStepName',
        'start_step_name': 'startStepName'
    }

    def __init__(self, angle_configured=None, angle_found=None, end_step_name=None, start_step_name=None, local_vars_configuration=None):  # noqa: E501
        """V1VisionRunByCameraResponseAngleCheck - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._angle_configured = None
        self._angle_found = None
        self._end_step_name = None
        self._start_step_name = None
        self.discriminator = None

        if angle_configured is not None:
            self.angle_configured = angle_configured
        if angle_found is not None:
            self.angle_found = angle_found
        if end_step_name is not None:
            self.end_step_name = end_step_name
        if start_step_name is not None:
            self.start_step_name = start_step_name

    @property
    def angle_configured(self):
        """Gets the angle_configured of this V1VisionRunByCameraResponseAngleCheck.  # noqa: E501


        :return: The angle_configured of this V1VisionRunByCameraResponseAngleCheck.  # noqa: E501
        :rtype: V1VisionRunByCameraResponseAngleCheckAngleConfigured
        """
        return self._angle_configured

    @angle_configured.setter
    def angle_configured(self, angle_configured):
        """Sets the angle_configured of this V1VisionRunByCameraResponseAngleCheck.


        :param angle_configured: The angle_configured of this V1VisionRunByCameraResponseAngleCheck.  # noqa: E501
        :type: V1VisionRunByCameraResponseAngleCheckAngleConfigured
        """

        self._angle_configured = angle_configured

    @property
    def angle_found(self):
        """Gets the angle_found of this V1VisionRunByCameraResponseAngleCheck.  # noqa: E501

        The counter-clockwise angle detected from the first edge to the second edge  # noqa: E501

        :return: The angle_found of this V1VisionRunByCameraResponseAngleCheck.  # noqa: E501
        :rtype: int
        """
        return self._angle_found

    @angle_found.setter
    def angle_found(self, angle_found):
        """Sets the angle_found of this V1VisionRunByCameraResponseAngleCheck.

        The counter-clockwise angle detected from the first edge to the second edge  # noqa: E501

        :param angle_found: The angle_found of this V1VisionRunByCameraResponseAngleCheck.  # noqa: E501
        :type: int
        """

        self._angle_found = angle_found

    @property
    def end_step_name(self):
        """Gets the end_step_name of this V1VisionRunByCameraResponseAngleCheck.  # noqa: E501

        The name of the second reference step used to check the angle  # noqa: E501

        :return: The end_step_name of this V1VisionRunByCameraResponseAngleCheck.  # noqa: E501
        :rtype: str
        """
        return self._end_step_name

    @end_step_name.setter
    def end_step_name(self, end_step_name):
        """Sets the end_step_name of this V1VisionRunByCameraResponseAngleCheck.

        The name of the second reference step used to check the angle  # noqa: E501

        :param end_step_name: The end_step_name of this V1VisionRunByCameraResponseAngleCheck.  # noqa: E501
        :type: str
        """

        self._end_step_name = end_step_name

    @property
    def start_step_name(self):
        """Gets the start_step_name of this V1VisionRunByCameraResponseAngleCheck.  # noqa: E501

        The name of the first reference step used to check the angle  # noqa: E501

        :return: The start_step_name of this V1VisionRunByCameraResponseAngleCheck.  # noqa: E501
        :rtype: str
        """
        return self._start_step_name

    @start_step_name.setter
    def start_step_name(self, start_step_name):
        """Sets the start_step_name of this V1VisionRunByCameraResponseAngleCheck.

        The name of the first reference step used to check the angle  # noqa: E501

        :param start_step_name: The start_step_name of this V1VisionRunByCameraResponseAngleCheck.  # noqa: E501
        :type: str
        """

        self._start_step_name = start_step_name

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
        if not isinstance(other, V1VisionRunByCameraResponseAngleCheck):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1VisionRunByCameraResponseAngleCheck):
            return True

        return self.to_dict() != other.to_dict()