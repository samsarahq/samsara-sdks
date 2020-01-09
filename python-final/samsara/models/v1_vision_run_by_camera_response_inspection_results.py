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


class V1VisionRunByCameraResponseInspectionResults(object):
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
        'capture_at_ms': 'float',
        'result': 'str',
        'step_results': 'list[V1VisionRunByCameraResponseStepResults]'
    }

    attribute_map = {
        'capture_at_ms': 'captureAtMs',
        'result': 'result',
        'step_results': 'stepResults'
    }

    def __init__(self, capture_at_ms=None, result=None, step_results=None, local_vars_configuration=None):  # noqa: E501
        """V1VisionRunByCameraResponseInspectionResults - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._capture_at_ms = None
        self._result = None
        self._step_results = None
        self.discriminator = None

        if capture_at_ms is not None:
            self.capture_at_ms = capture_at_ms
        if result is not None:
            self.result = result
        if step_results is not None:
            self.step_results = step_results

    @property
    def capture_at_ms(self):
        """Gets the capture_at_ms of this V1VisionRunByCameraResponseInspectionResults.  # noqa: E501


        :return: The capture_at_ms of this V1VisionRunByCameraResponseInspectionResults.  # noqa: E501
        :rtype: float
        """
        return self._capture_at_ms

    @capture_at_ms.setter
    def capture_at_ms(self, capture_at_ms):
        """Sets the capture_at_ms of this V1VisionRunByCameraResponseInspectionResults.


        :param capture_at_ms: The capture_at_ms of this V1VisionRunByCameraResponseInspectionResults.  # noqa: E501
        :type: float
        """

        self._capture_at_ms = capture_at_ms

    @property
    def result(self):
        """Gets the result of this V1VisionRunByCameraResponseInspectionResults.  # noqa: E501


        :return: The result of this V1VisionRunByCameraResponseInspectionResults.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this V1VisionRunByCameraResponseInspectionResults.


        :param result: The result of this V1VisionRunByCameraResponseInspectionResults.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def step_results(self):
        """Gets the step_results of this V1VisionRunByCameraResponseInspectionResults.  # noqa: E501


        :return: The step_results of this V1VisionRunByCameraResponseInspectionResults.  # noqa: E501
        :rtype: list[V1VisionRunByCameraResponseStepResults]
        """
        return self._step_results

    @step_results.setter
    def step_results(self, step_results):
        """Sets the step_results of this V1VisionRunByCameraResponseInspectionResults.


        :param step_results: The step_results of this V1VisionRunByCameraResponseInspectionResults.  # noqa: E501
        :type: list[V1VisionRunByCameraResponseStepResults]
        """

        self._step_results = step_results

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
        if not isinstance(other, V1VisionRunByCameraResponseInspectionResults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1VisionRunByCameraResponseInspectionResults):
            return True

        return self.to_dict() != other.to_dict()
