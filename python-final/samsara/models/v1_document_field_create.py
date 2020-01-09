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


class V1DocumentFieldCreate(object):
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
        'date_time_value': 'str',
        'multiple_choice_value': 'list[V1DocumentFieldAllOf1MultipleChoiceValue]',
        'number_value': 'float',
        'photo_value': 'list[V1DocumentFieldAllOf1PhotoValue]',
        'string_value': 'str',
        'value_type': 'str'
    }

    attribute_map = {
        'date_time_value': 'dateTimeValue',
        'multiple_choice_value': 'multipleChoiceValue',
        'number_value': 'numberValue',
        'photo_value': 'photoValue',
        'string_value': 'stringValue',
        'value_type': 'valueType'
    }

    def __init__(self, date_time_value=None, multiple_choice_value=None, number_value=None, photo_value=None, string_value=None, value_type=None, local_vars_configuration=None):  # noqa: E501
        """V1DocumentFieldCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date_time_value = None
        self._multiple_choice_value = None
        self._number_value = None
        self._photo_value = None
        self._string_value = None
        self._value_type = None
        self.discriminator = None

        if date_time_value is not None:
            self.date_time_value = date_time_value
        if multiple_choice_value is not None:
            self.multiple_choice_value = multiple_choice_value
        if number_value is not None:
            self.number_value = number_value
        if photo_value is not None:
            self.photo_value = photo_value
        if string_value is not None:
            self.string_value = string_value
        self.value_type = value_type

    @property
    def date_time_value(self):
        """Gets the date_time_value of this V1DocumentFieldCreate.  # noqa: E501

        Value of this field if this document field has valueType: ValueType_DateTime.  # noqa: E501

        :return: The date_time_value of this V1DocumentFieldCreate.  # noqa: E501
        :rtype: str
        """
        return self._date_time_value

    @date_time_value.setter
    def date_time_value(self, date_time_value):
        """Sets the date_time_value of this V1DocumentFieldCreate.

        Value of this field if this document field has valueType: ValueType_DateTime.  # noqa: E501

        :param date_time_value: The date_time_value of this V1DocumentFieldCreate.  # noqa: E501
        :type: str
        """

        self._date_time_value = date_time_value

    @property
    def multiple_choice_value(self):
        """Gets the multiple_choice_value of this V1DocumentFieldCreate.  # noqa: E501

        Value of this field if this document field has valueType: ValueType_MultipleChoice. Array of objects containing two fields: the string value of the multiple choice option and a boolean representing whether or not the choice was selected  # noqa: E501

        :return: The multiple_choice_value of this V1DocumentFieldCreate.  # noqa: E501
        :rtype: list[V1DocumentFieldAllOf1MultipleChoiceValue]
        """
        return self._multiple_choice_value

    @multiple_choice_value.setter
    def multiple_choice_value(self, multiple_choice_value):
        """Sets the multiple_choice_value of this V1DocumentFieldCreate.

        Value of this field if this document field has valueType: ValueType_MultipleChoice. Array of objects containing two fields: the string value of the multiple choice option and a boolean representing whether or not the choice was selected  # noqa: E501

        :param multiple_choice_value: The multiple_choice_value of this V1DocumentFieldCreate.  # noqa: E501
        :type: list[V1DocumentFieldAllOf1MultipleChoiceValue]
        """

        self._multiple_choice_value = multiple_choice_value

    @property
    def number_value(self):
        """Gets the number_value of this V1DocumentFieldCreate.  # noqa: E501

        Value of this field if this document field has valueType: ValueType_Number.  # noqa: E501

        :return: The number_value of this V1DocumentFieldCreate.  # noqa: E501
        :rtype: float
        """
        return self._number_value

    @number_value.setter
    def number_value(self, number_value):
        """Sets the number_value of this V1DocumentFieldCreate.

        Value of this field if this document field has valueType: ValueType_Number.  # noqa: E501

        :param number_value: The number_value of this V1DocumentFieldCreate.  # noqa: E501
        :type: float
        """

        self._number_value = number_value

    @property
    def photo_value(self):
        """Gets the photo_value of this V1DocumentFieldCreate.  # noqa: E501

        Value of this field if this document field has valueType: ValueType_Photo. Array of photo objects where each object contains a URL for a photo.  # noqa: E501

        :return: The photo_value of this V1DocumentFieldCreate.  # noqa: E501
        :rtype: list[V1DocumentFieldAllOf1PhotoValue]
        """
        return self._photo_value

    @photo_value.setter
    def photo_value(self, photo_value):
        """Sets the photo_value of this V1DocumentFieldCreate.

        Value of this field if this document field has valueType: ValueType_Photo. Array of photo objects where each object contains a URL for a photo.  # noqa: E501

        :param photo_value: The photo_value of this V1DocumentFieldCreate.  # noqa: E501
        :type: list[V1DocumentFieldAllOf1PhotoValue]
        """

        self._photo_value = photo_value

    @property
    def string_value(self):
        """Gets the string_value of this V1DocumentFieldCreate.  # noqa: E501

        Value of this field if this document field has valueType: ValueType_String.  # noqa: E501

        :return: The string_value of this V1DocumentFieldCreate.  # noqa: E501
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value):
        """Sets the string_value of this V1DocumentFieldCreate.

        Value of this field if this document field has valueType: ValueType_String.  # noqa: E501

        :param string_value: The string_value of this V1DocumentFieldCreate.  # noqa: E501
        :type: str
        """

        self._string_value = string_value

    @property
    def value_type(self):
        """Gets the value_type of this V1DocumentFieldCreate.  # noqa: E501

        Determines the type of this field and what type of value this field has. It should be either ValueType_Number, ValueType_String, ValueType_Photo, ValueType_MultipleChoice or ValueType_DateTime.  # noqa: E501

        :return: The value_type of this V1DocumentFieldCreate.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this V1DocumentFieldCreate.

        Determines the type of this field and what type of value this field has. It should be either ValueType_Number, ValueType_String, ValueType_Photo, ValueType_MultipleChoice or ValueType_DateTime.  # noqa: E501

        :param value_type: The value_type of this V1DocumentFieldCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value_type is None:  # noqa: E501
            raise ValueError("Invalid value for `value_type`, must not be `None`")  # noqa: E501

        self._value_type = value_type

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
        if not isinstance(other, V1DocumentFieldCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DocumentFieldCreate):
            return True

        return self.to_dict() != other.to_dict()
