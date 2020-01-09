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


class AddressCreateAllOf(object):
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
        'contact_ids': 'list[str]',
        'latitude': 'float',
        'longitude': 'float',
        'tag_ids': 'list[str]'
    }

    attribute_map = {
        'contact_ids': 'contactIds',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'tag_ids': 'tagIds'
    }

    def __init__(self, contact_ids=None, latitude=None, longitude=None, tag_ids=None, local_vars_configuration=None):  # noqa: E501
        """AddressCreateAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._contact_ids = None
        self._latitude = None
        self._longitude = None
        self._tag_ids = None
        self.discriminator = None

        if contact_ids is not None:
            self.contact_ids = contact_ids
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if tag_ids is not None:
            self.tag_ids = tag_ids

    @property
    def contact_ids(self):
        """Gets the contact_ids of this AddressCreateAllOf.  # noqa: E501

        An array of IDs of contacts to associate with this address.  # noqa: E501

        :return: The contact_ids of this AddressCreateAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._contact_ids

    @contact_ids.setter
    def contact_ids(self, contact_ids):
        """Sets the contact_ids of this AddressCreateAllOf.

        An array of IDs of contacts to associate with this address.  # noqa: E501

        :param contact_ids: The contact_ids of this AddressCreateAllOf.  # noqa: E501
        :type: list[str]
        """

        self._contact_ids = contact_ids

    @property
    def latitude(self):
        """Gets the latitude of this AddressCreateAllOf.  # noqa: E501

        Optional latitude field to override the geocoded latitude from the formatted address.  # noqa: E501

        :return: The latitude of this AddressCreateAllOf.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this AddressCreateAllOf.

        Optional latitude field to override the geocoded latitude from the formatted address.  # noqa: E501

        :param latitude: The latitude of this AddressCreateAllOf.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this AddressCreateAllOf.  # noqa: E501

        Optional longitude field to override the geocoded longitude from the formatted address.  # noqa: E501

        :return: The longitude of this AddressCreateAllOf.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this AddressCreateAllOf.

        Optional longitude field to override the geocoded longitude from the formatted address.  # noqa: E501

        :param longitude: The longitude of this AddressCreateAllOf.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def tag_ids(self):
        """Gets the tag_ids of this AddressCreateAllOf.  # noqa: E501

        An array of IDs of tags to associate with this address.  # noqa: E501

        :return: The tag_ids of this AddressCreateAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this AddressCreateAllOf.

        An array of IDs of tags to associate with this address.  # noqa: E501

        :param tag_ids: The tag_ids of this AddressCreateAllOf.  # noqa: E501
        :type: list[str]
        """

        self._tag_ids = tag_ids

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
        if not isinstance(other, AddressCreateAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddressCreateAllOf):
            return True

        return self.to_dict() != other.to_dict()
