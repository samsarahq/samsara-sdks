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


class TagAllOf(object):
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
        'addresses': 'list[TagAllOfAddresses]',
        'assets': 'list[TagAllOfAddresses]',
        'drivers': 'list[TagAllOfAddresses]',
        'machines': 'list[TagAllOfAddresses]',
        'parent_tag': 'TagAllOfParentTag',
        'sensors': 'list[TagAllOfAddresses]',
        'vehicles': 'list[TagAllOfAddresses]'
    }

    attribute_map = {
        'addresses': 'addresses',
        'assets': 'assets',
        'drivers': 'drivers',
        'machines': 'machines',
        'parent_tag': 'parentTag',
        'sensors': 'sensors',
        'vehicles': 'vehicles'
    }

    def __init__(self, addresses=None, assets=None, drivers=None, machines=None, parent_tag=None, sensors=None, vehicles=None, local_vars_configuration=None):  # noqa: E501
        """TagAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._addresses = None
        self._assets = None
        self._drivers = None
        self._machines = None
        self._parent_tag = None
        self._sensors = None
        self._vehicles = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        if assets is not None:
            self.assets = assets
        if drivers is not None:
            self.drivers = drivers
        if machines is not None:
            self.machines = machines
        if parent_tag is not None:
            self.parent_tag = parent_tag
        if sensors is not None:
            self.sensors = sensors
        if vehicles is not None:
            self.vehicles = vehicles

    @property
    def addresses(self):
        """Gets the addresses of this TagAllOf.  # noqa: E501

        The addresses that belong to this tag.  # noqa: E501

        :return: The addresses of this TagAllOf.  # noqa: E501
        :rtype: list[TagAllOfAddresses]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this TagAllOf.

        The addresses that belong to this tag.  # noqa: E501

        :param addresses: The addresses of this TagAllOf.  # noqa: E501
        :type: list[TagAllOfAddresses]
        """

        self._addresses = addresses

    @property
    def assets(self):
        """Gets the assets of this TagAllOf.  # noqa: E501

        The trailers, unpowered, and powered assets that belong to this tag.  # noqa: E501

        :return: The assets of this TagAllOf.  # noqa: E501
        :rtype: list[TagAllOfAddresses]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this TagAllOf.

        The trailers, unpowered, and powered assets that belong to this tag.  # noqa: E501

        :param assets: The assets of this TagAllOf.  # noqa: E501
        :type: list[TagAllOfAddresses]
        """

        self._assets = assets

    @property
    def drivers(self):
        """Gets the drivers of this TagAllOf.  # noqa: E501

        The drivers that belong to this tag.  # noqa: E501

        :return: The drivers of this TagAllOf.  # noqa: E501
        :rtype: list[TagAllOfAddresses]
        """
        return self._drivers

    @drivers.setter
    def drivers(self, drivers):
        """Sets the drivers of this TagAllOf.

        The drivers that belong to this tag.  # noqa: E501

        :param drivers: The drivers of this TagAllOf.  # noqa: E501
        :type: list[TagAllOfAddresses]
        """

        self._drivers = drivers

    @property
    def machines(self):
        """Gets the machines of this TagAllOf.  # noqa: E501

        The machines that belong to thistag.  # noqa: E501

        :return: The machines of this TagAllOf.  # noqa: E501
        :rtype: list[TagAllOfAddresses]
        """
        return self._machines

    @machines.setter
    def machines(self, machines):
        """Sets the machines of this TagAllOf.

        The machines that belong to thistag.  # noqa: E501

        :param machines: The machines of this TagAllOf.  # noqa: E501
        :type: list[TagAllOfAddresses]
        """

        self._machines = machines

    @property
    def parent_tag(self):
        """Gets the parent_tag of this TagAllOf.  # noqa: E501


        :return: The parent_tag of this TagAllOf.  # noqa: E501
        :rtype: TagAllOfParentTag
        """
        return self._parent_tag

    @parent_tag.setter
    def parent_tag(self, parent_tag):
        """Sets the parent_tag of this TagAllOf.


        :param parent_tag: The parent_tag of this TagAllOf.  # noqa: E501
        :type: TagAllOfParentTag
        """

        self._parent_tag = parent_tag

    @property
    def sensors(self):
        """Gets the sensors of this TagAllOf.  # noqa: E501

        The sensors that belong to this tag.  # noqa: E501

        :return: The sensors of this TagAllOf.  # noqa: E501
        :rtype: list[TagAllOfAddresses]
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        """Sets the sensors of this TagAllOf.

        The sensors that belong to this tag.  # noqa: E501

        :param sensors: The sensors of this TagAllOf.  # noqa: E501
        :type: list[TagAllOfAddresses]
        """

        self._sensors = sensors

    @property
    def vehicles(self):
        """Gets the vehicles of this TagAllOf.  # noqa: E501

        The vehicles that belong to this tag.  # noqa: E501

        :return: The vehicles of this TagAllOf.  # noqa: E501
        :rtype: list[TagAllOfAddresses]
        """
        return self._vehicles

    @vehicles.setter
    def vehicles(self, vehicles):
        """Sets the vehicles of this TagAllOf.

        The vehicles that belong to this tag.  # noqa: E501

        :param vehicles: The vehicles of this TagAllOf.  # noqa: E501
        :type: list[TagAllOfAddresses]
        """

        self._vehicles = vehicles

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
        if not isinstance(other, TagAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TagAllOf):
            return True

        return self.to_dict() != other.to_dict()
