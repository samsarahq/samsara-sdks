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


class V1DocumentAllOf(object):
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
        'document_type': 'str',
        'driver_created_at_ms': 'int',
        'driver_id': 'int',
        'fields': 'list[object]',
        'id': 'str',
        'org_id': 'int',
        'server_created_at_ms': 'int',
        'server_updated_at_ms': 'int',
        'vehicle_id': 'int'
    }

    attribute_map = {
        'document_type': 'documentType',
        'driver_created_at_ms': 'driverCreatedAtMs',
        'driver_id': 'driverId',
        'fields': 'fields',
        'id': 'id',
        'org_id': 'orgId',
        'server_created_at_ms': 'serverCreatedAtMs',
        'server_updated_at_ms': 'serverUpdatedAtMs',
        'vehicle_id': 'vehicleId'
    }

    def __init__(self, document_type=None, driver_created_at_ms=None, driver_id=None, fields=None, id=None, org_id=None, server_created_at_ms=None, server_updated_at_ms=None, vehicle_id=None, local_vars_configuration=None):  # noqa: E501
        """V1DocumentAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._document_type = None
        self._driver_created_at_ms = None
        self._driver_id = None
        self._fields = None
        self._id = None
        self._org_id = None
        self._server_created_at_ms = None
        self._server_updated_at_ms = None
        self._vehicle_id = None
        self.discriminator = None

        self.document_type = document_type
        self.driver_created_at_ms = driver_created_at_ms
        self.driver_id = driver_id
        self.fields = fields
        self.id = id
        self.org_id = org_id
        self.server_created_at_ms = server_created_at_ms
        self.server_updated_at_ms = server_updated_at_ms
        if vehicle_id is not None:
            self.vehicle_id = vehicle_id

    @property
    def document_type(self):
        """Gets the document_type of this V1DocumentAllOf.  # noqa: E501

        Descriptive name of this type of document.  # noqa: E501

        :return: The document_type of this V1DocumentAllOf.  # noqa: E501
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this V1DocumentAllOf.

        Descriptive name of this type of document.  # noqa: E501

        :param document_type: The document_type of this V1DocumentAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and document_type is None:  # noqa: E501
            raise ValueError("Invalid value for `document_type`, must not be `None`")  # noqa: E501

        self._document_type = document_type

    @property
    def driver_created_at_ms(self):
        """Gets the driver_created_at_ms of this V1DocumentAllOf.  # noqa: E501

        The time in Unix epoch milliseconds that the document is created on the driver app.  # noqa: E501

        :return: The driver_created_at_ms of this V1DocumentAllOf.  # noqa: E501
        :rtype: int
        """
        return self._driver_created_at_ms

    @driver_created_at_ms.setter
    def driver_created_at_ms(self, driver_created_at_ms):
        """Sets the driver_created_at_ms of this V1DocumentAllOf.

        The time in Unix epoch milliseconds that the document is created on the driver app.  # noqa: E501

        :param driver_created_at_ms: The driver_created_at_ms of this V1DocumentAllOf.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and driver_created_at_ms is None:  # noqa: E501
            raise ValueError("Invalid value for `driver_created_at_ms`, must not be `None`")  # noqa: E501

        self._driver_created_at_ms = driver_created_at_ms

    @property
    def driver_id(self):
        """Gets the driver_id of this V1DocumentAllOf.  # noqa: E501

        ID of the driver for whom the document is submitted  # noqa: E501

        :return: The driver_id of this V1DocumentAllOf.  # noqa: E501
        :rtype: int
        """
        return self._driver_id

    @driver_id.setter
    def driver_id(self, driver_id):
        """Sets the driver_id of this V1DocumentAllOf.

        ID of the driver for whom the document is submitted  # noqa: E501

        :param driver_id: The driver_id of this V1DocumentAllOf.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and driver_id is None:  # noqa: E501
            raise ValueError("Invalid value for `driver_id`, must not be `None`")  # noqa: E501

        self._driver_id = driver_id

    @property
    def fields(self):
        """Gets the fields of this V1DocumentAllOf.  # noqa: E501

        The fields associated with this document.  # noqa: E501

        :return: The fields of this V1DocumentAllOf.  # noqa: E501
        :rtype: list[object]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this V1DocumentAllOf.

        The fields associated with this document.  # noqa: E501

        :param fields: The fields of this V1DocumentAllOf.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and fields is None:  # noqa: E501
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

    @property
    def id(self):
        """Gets the id of this V1DocumentAllOf.  # noqa: E501

        ID of the document  # noqa: E501

        :return: The id of this V1DocumentAllOf.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1DocumentAllOf.

        ID of the document  # noqa: E501

        :param id: The id of this V1DocumentAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def org_id(self):
        """Gets the org_id of this V1DocumentAllOf.  # noqa: E501

        Organization ID that the document & driver who submitted the doc belongs to  # noqa: E501

        :return: The org_id of this V1DocumentAllOf.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this V1DocumentAllOf.

        Organization ID that the document & driver who submitted the doc belongs to  # noqa: E501

        :param org_id: The org_id of this V1DocumentAllOf.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def server_created_at_ms(self):
        """Gets the server_created_at_ms of this V1DocumentAllOf.  # noqa: E501

        The time in Unix epoch milliseconds that the document is created on the server.  # noqa: E501

        :return: The server_created_at_ms of this V1DocumentAllOf.  # noqa: E501
        :rtype: int
        """
        return self._server_created_at_ms

    @server_created_at_ms.setter
    def server_created_at_ms(self, server_created_at_ms):
        """Sets the server_created_at_ms of this V1DocumentAllOf.

        The time in Unix epoch milliseconds that the document is created on the server.  # noqa: E501

        :param server_created_at_ms: The server_created_at_ms of this V1DocumentAllOf.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and server_created_at_ms is None:  # noqa: E501
            raise ValueError("Invalid value for `server_created_at_ms`, must not be `None`")  # noqa: E501

        self._server_created_at_ms = server_created_at_ms

    @property
    def server_updated_at_ms(self):
        """Gets the server_updated_at_ms of this V1DocumentAllOf.  # noqa: E501

        The time in Unix epoch milliseconds that the document is updated on the server.  # noqa: E501

        :return: The server_updated_at_ms of this V1DocumentAllOf.  # noqa: E501
        :rtype: int
        """
        return self._server_updated_at_ms

    @server_updated_at_ms.setter
    def server_updated_at_ms(self, server_updated_at_ms):
        """Sets the server_updated_at_ms of this V1DocumentAllOf.

        The time in Unix epoch milliseconds that the document is updated on the server.  # noqa: E501

        :param server_updated_at_ms: The server_updated_at_ms of this V1DocumentAllOf.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and server_updated_at_ms is None:  # noqa: E501
            raise ValueError("Invalid value for `server_updated_at_ms`, must not be `None`")  # noqa: E501

        self._server_updated_at_ms = server_updated_at_ms

    @property
    def vehicle_id(self):
        """Gets the vehicle_id of this V1DocumentAllOf.  # noqa: E501

        VehicleID of the driver at document creation.  # noqa: E501

        :return: The vehicle_id of this V1DocumentAllOf.  # noqa: E501
        :rtype: int
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        """Sets the vehicle_id of this V1DocumentAllOf.

        VehicleID of the driver at document creation.  # noqa: E501

        :param vehicle_id: The vehicle_id of this V1DocumentAllOf.  # noqa: E501
        :type: int
        """

        self._vehicle_id = vehicle_id

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
        if not isinstance(other, V1DocumentAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DocumentAllOf):
            return True

        return self.to_dict() != other.to_dict()
