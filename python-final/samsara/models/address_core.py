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


class AddressCore(object):
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
        'address_types': 'list[str]',
        'formatted_address': 'str',
        'name': 'str',
        'notes': 'str'
    }

    attribute_map = {
        'address_types': 'addressTypes',
        'formatted_address': 'formattedAddress',
        'name': 'name',
        'notes': 'notes'
    }

    def __init__(self, address_types=None, formatted_address=None, name=None, notes=None, local_vars_configuration=None):  # noqa: E501
        """AddressCore - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address_types = None
        self._formatted_address = None
        self._name = None
        self._notes = None
        self.discriminator = None

        if address_types is not None:
            self.address_types = address_types
        if formatted_address is not None:
            self.formatted_address = formatted_address
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes

    @property
    def address_types(self):
        """Gets the address_types of this AddressCore.  # noqa: E501

        Reporting location type associated with the address (used for ELD reporting purposes).  # noqa: E501

        :return: The address_types of this AddressCore.  # noqa: E501
        :rtype: list[str]
        """
        return self._address_types

    @address_types.setter
    def address_types(self, address_types):
        """Sets the address_types of this AddressCore.

        Reporting location type associated with the address (used for ELD reporting purposes).  # noqa: E501

        :param address_types: The address_types of this AddressCore.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["yard", "shortHaul"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(address_types).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `address_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(address_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._address_types = address_types

    @property
    def formatted_address(self):
        """Gets the formatted_address of this AddressCore.  # noqa: E501

        The full street address for this address/geofence, as it might be recognized by Google Maps.  # noqa: E501

        :return: The formatted_address of this AddressCore.  # noqa: E501
        :rtype: str
        """
        return self._formatted_address

    @formatted_address.setter
    def formatted_address(self, formatted_address):
        """Sets the formatted_address of this AddressCore.

        The full street address for this address/geofence, as it might be recognized by Google Maps.  # noqa: E501

        :param formatted_address: The formatted_address of this AddressCore.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                formatted_address is not None and len(formatted_address) > 1024):
            raise ValueError("Invalid value for `formatted_address`, length must be less than or equal to `1024`")  # noqa: E501

        self._formatted_address = formatted_address

    @property
    def name(self):
        """Gets the name of this AddressCore.  # noqa: E501

        Name of the address.  # noqa: E501

        :return: The name of this AddressCore.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddressCore.

        Name of the address.  # noqa: E501

        :param name: The name of this AddressCore.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this AddressCore.  # noqa: E501

        Notes about the address.  # noqa: E501

        :return: The notes of this AddressCore.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this AddressCore.

        Notes about the address.  # noqa: E501

        :param notes: The notes of this AddressCore.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                notes is not None and len(notes) > 280):
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `280`")  # noqa: E501

        self._notes = notes

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
        if not isinstance(other, AddressCore):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddressCore):
            return True

        return self.to_dict() != other.to_dict()
