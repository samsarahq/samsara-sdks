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


class VehicleLocationsWrapper(object):
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
        'locations': 'list[object]',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'locations': 'locations',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, locations=None, id=None, name=None, local_vars_configuration=None):  # noqa: E501
        """VehicleLocationsWrapper - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._locations = None
        self._id = None
        self._name = None
        self.discriminator = None

        if locations is not None:
            self.locations = locations
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def locations(self):
        """Gets the locations of this VehicleLocationsWrapper.  # noqa: E501


        :return: The locations of this VehicleLocationsWrapper.  # noqa: E501
        :rtype: list[object]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this VehicleLocationsWrapper.


        :param locations: The locations of this VehicleLocationsWrapper.  # noqa: E501
        :type: list[object]
        """

        self._locations = locations

    @property
    def id(self):
        """Gets the id of this VehicleLocationsWrapper.  # noqa: E501

        ID of the vehicle.  # noqa: E501

        :return: The id of this VehicleLocationsWrapper.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VehicleLocationsWrapper.

        ID of the vehicle.  # noqa: E501

        :param id: The id of this VehicleLocationsWrapper.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VehicleLocationsWrapper.  # noqa: E501

        Name of the vehicle.  # noqa: E501

        :return: The name of this VehicleLocationsWrapper.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VehicleLocationsWrapper.

        Name of the vehicle.  # noqa: E501

        :param name: The name of this VehicleLocationsWrapper.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, VehicleLocationsWrapper):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleLocationsWrapper):
            return True

        return self.to_dict() != other.to_dict()
