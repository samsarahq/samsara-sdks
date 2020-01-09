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


class V1VisionRunByCameraResponseContour(object):
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
        'angle_degrees': 'int',
        'angle_tolerance': 'int',
        'match_percentage': 'int',
        'match_threshold': 'int'
    }

    attribute_map = {
        'angle_degrees': 'angleDegrees',
        'angle_tolerance': 'angleTolerance',
        'match_percentage': 'matchPercentage',
        'match_threshold': 'matchThreshold'
    }

    def __init__(self, angle_degrees=None, angle_tolerance=None, match_percentage=None, match_threshold=None, local_vars_configuration=None):  # noqa: E501
        """V1VisionRunByCameraResponseContour - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._angle_degrees = None
        self._angle_tolerance = None
        self._match_percentage = None
        self._match_threshold = None
        self.discriminator = None

        if angle_degrees is not None:
            self.angle_degrees = angle_degrees
        if angle_tolerance is not None:
            self.angle_tolerance = angle_tolerance
        if match_percentage is not None:
            self.match_percentage = match_percentage
        if match_threshold is not None:
            self.match_threshold = match_threshold

    @property
    def angle_degrees(self):
        """Gets the angle_degrees of this V1VisionRunByCameraResponseContour.  # noqa: E501

        The rotation angle found  # noqa: E501

        :return: The angle_degrees of this V1VisionRunByCameraResponseContour.  # noqa: E501
        :rtype: int
        """
        return self._angle_degrees

    @angle_degrees.setter
    def angle_degrees(self, angle_degrees):
        """Sets the angle_degrees of this V1VisionRunByCameraResponseContour.

        The rotation angle found  # noqa: E501

        :param angle_degrees: The angle_degrees of this V1VisionRunByCameraResponseContour.  # noqa: E501
        :type: int
        """

        self._angle_degrees = angle_degrees

    @property
    def angle_tolerance(self):
        """Gets the angle_tolerance of this V1VisionRunByCameraResponseContour.  # noqa: E501

        The rotation angle allowance  # noqa: E501

        :return: The angle_tolerance of this V1VisionRunByCameraResponseContour.  # noqa: E501
        :rtype: int
        """
        return self._angle_tolerance

    @angle_tolerance.setter
    def angle_tolerance(self, angle_tolerance):
        """Sets the angle_tolerance of this V1VisionRunByCameraResponseContour.

        The rotation angle allowance  # noqa: E501

        :param angle_tolerance: The angle_tolerance of this V1VisionRunByCameraResponseContour.  # noqa: E501
        :type: int
        """

        self._angle_tolerance = angle_tolerance

    @property
    def match_percentage(self):
        """Gets the match_percentage of this V1VisionRunByCameraResponseContour.  # noqa: E501

        The contour match percentage with the configured contour  # noqa: E501

        :return: The match_percentage of this V1VisionRunByCameraResponseContour.  # noqa: E501
        :rtype: int
        """
        return self._match_percentage

    @match_percentage.setter
    def match_percentage(self, match_percentage):
        """Sets the match_percentage of this V1VisionRunByCameraResponseContour.

        The contour match percentage with the configured contour  # noqa: E501

        :param match_percentage: The match_percentage of this V1VisionRunByCameraResponseContour.  # noqa: E501
        :type: int
        """

        self._match_percentage = match_percentage

    @property
    def match_threshold(self):
        """Gets the match_threshold of this V1VisionRunByCameraResponseContour.  # noqa: E501

        The configured match threshold for contours  # noqa: E501

        :return: The match_threshold of this V1VisionRunByCameraResponseContour.  # noqa: E501
        :rtype: int
        """
        return self._match_threshold

    @match_threshold.setter
    def match_threshold(self, match_threshold):
        """Sets the match_threshold of this V1VisionRunByCameraResponseContour.

        The configured match threshold for contours  # noqa: E501

        :param match_threshold: The match_threshold of this V1VisionRunByCameraResponseContour.  # noqa: E501
        :type: int
        """

        self._match_threshold = match_threshold

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
        if not isinstance(other, V1VisionRunByCameraResponseContour):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1VisionRunByCameraResponseContour):
            return True

        return self.to_dict() != other.to_dict()