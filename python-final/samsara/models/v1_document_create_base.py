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


class V1DocumentCreateBase(object):
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
        'dispatch_job_id': 'int',
        'notes': 'str',
        'state': 'str'
    }

    attribute_map = {
        'dispatch_job_id': 'dispatchJobId',
        'notes': 'notes',
        'state': 'state'
    }

    def __init__(self, dispatch_job_id=None, notes=None, state='Required', local_vars_configuration=None):  # noqa: E501
        """V1DocumentCreateBase - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dispatch_job_id = None
        self._notes = None
        self._state = None
        self.discriminator = None

        if dispatch_job_id is not None:
            self.dispatch_job_id = dispatch_job_id
        if notes is not None:
            self.notes = notes
        if state is not None:
            self.state = state

    @property
    def dispatch_job_id(self):
        """Gets the dispatch_job_id of this V1DocumentCreateBase.  # noqa: E501

        ID of the Samsara dispatch job for which the document is submitted  # noqa: E501

        :return: The dispatch_job_id of this V1DocumentCreateBase.  # noqa: E501
        :rtype: int
        """
        return self._dispatch_job_id

    @dispatch_job_id.setter
    def dispatch_job_id(self, dispatch_job_id):
        """Sets the dispatch_job_id of this V1DocumentCreateBase.

        ID of the Samsara dispatch job for which the document is submitted  # noqa: E501

        :param dispatch_job_id: The dispatch_job_id of this V1DocumentCreateBase.  # noqa: E501
        :type: int
        """

        self._dispatch_job_id = dispatch_job_id

    @property
    def notes(self):
        """Gets the notes of this V1DocumentCreateBase.  # noqa: E501

        Notes submitted with this document.  # noqa: E501

        :return: The notes of this V1DocumentCreateBase.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this V1DocumentCreateBase.

        Notes submitted with this document.  # noqa: E501

        :param notes: The notes of this V1DocumentCreateBase.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def state(self):
        """Gets the state of this V1DocumentCreateBase.  # noqa: E501

        The condition of the document created for the driver. Can be either `Required` or `Submitted`, if no value is specified, `state` defaults to `Required`. `Required` documents are pre-populated documents for the Driver to fill out in the Driver App.  # noqa: E501

        :return: The state of this V1DocumentCreateBase.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this V1DocumentCreateBase.

        The condition of the document created for the driver. Can be either `Required` or `Submitted`, if no value is specified, `state` defaults to `Required`. `Required` documents are pre-populated documents for the Driver to fill out in the Driver App.  # noqa: E501

        :param state: The state of this V1DocumentCreateBase.  # noqa: E501
        :type: str
        """
        allowed_values = ["Required", "Submitted"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, V1DocumentCreateBase):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DocumentCreateBase):
            return True

        return self.to_dict() != other.to_dict()