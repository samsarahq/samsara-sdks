# coding: utf-8

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class Vehicle(object):
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
        'aux_input_type1': 'VehicleAuxInputType',
        'aux_input_type2': 'VehicleAuxInputType',
        'external_ids': 'dict(str, str)',
        'harsh_acceleration_setting_type': 'VehicleHarshAccelerationSettingType',
        'id': 'str',
        'license_plate': 'str',
        'make': 'str',
        'model': 'str',
        'name': 'str',
        'notes': 'str',
        'static_assigned_driver': 'DriverTinyResponse',
        'tags': 'list[TagTinyResponse]',
        'vin': 'str',
        'year': 'str'
    }

    attribute_map = {
        'aux_input_type1': 'auxInputType1',
        'aux_input_type2': 'auxInputType2',
        'external_ids': 'externalIds',
        'harsh_acceleration_setting_type': 'harshAccelerationSettingType',
        'id': 'id',
        'license_plate': 'licensePlate',
        'make': 'make',
        'model': 'model',
        'name': 'name',
        'notes': 'notes',
        'static_assigned_driver': 'staticAssignedDriver',
        'tags': 'tags',
        'vin': 'vin',
        'year': 'year'
    }

    def __init__(self, aux_input_type1=None, aux_input_type2=None, external_ids=None, harsh_acceleration_setting_type=None, id=None, license_plate=None, make=None, model=None, name=None, notes='', static_assigned_driver=None, tags=None, vin=None, year=None, local_vars_configuration=None):  # noqa: E501
        """Vehicle - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aux_input_type1 = None
        self._aux_input_type2 = None
        self._external_ids = None
        self._harsh_acceleration_setting_type = None
        self._id = None
        self._license_plate = None
        self._make = None
        self._model = None
        self._name = None
        self._notes = None
        self._static_assigned_driver = None
        self._tags = None
        self._vin = None
        self._year = None
        self.discriminator = None

        if aux_input_type1 is not None:
            self.aux_input_type1 = aux_input_type1
        if aux_input_type2 is not None:
            self.aux_input_type2 = aux_input_type2
        if external_ids is not None:
            self.external_ids = external_ids
        if harsh_acceleration_setting_type is not None:
            self.harsh_acceleration_setting_type = harsh_acceleration_setting_type
        self.id = id
        if license_plate is not None:
            self.license_plate = license_plate
        if make is not None:
            self.make = make
        if model is not None:
            self.model = model
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if static_assigned_driver is not None:
            self.static_assigned_driver = static_assigned_driver
        if tags is not None:
            self.tags = tags
        if vin is not None:
            self.vin = vin
        if year is not None:
            self.year = year

    @property
    def aux_input_type1(self):
        """Gets the aux_input_type1 of this Vehicle.  # noqa: E501


        :return: The aux_input_type1 of this Vehicle.  # noqa: E501
        :rtype: VehicleAuxInputType
        """
        return self._aux_input_type1

    @aux_input_type1.setter
    def aux_input_type1(self, aux_input_type1):
        """Sets the aux_input_type1 of this Vehicle.


        :param aux_input_type1: The aux_input_type1 of this Vehicle.  # noqa: E501
        :type: VehicleAuxInputType
        """

        self._aux_input_type1 = aux_input_type1

    @property
    def aux_input_type2(self):
        """Gets the aux_input_type2 of this Vehicle.  # noqa: E501


        :return: The aux_input_type2 of this Vehicle.  # noqa: E501
        :rtype: VehicleAuxInputType
        """
        return self._aux_input_type2

    @aux_input_type2.setter
    def aux_input_type2(self, aux_input_type2):
        """Sets the aux_input_type2 of this Vehicle.


        :param aux_input_type2: The aux_input_type2 of this Vehicle.  # noqa: E501
        :type: VehicleAuxInputType
        """

        self._aux_input_type2 = aux_input_type2

    @property
    def external_ids(self):
        """Gets the external_ids of this Vehicle.  # noqa: E501

        The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.  # noqa: E501

        :return: The external_ids of this Vehicle.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this Vehicle.

        The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.  # noqa: E501

        :param external_ids: The external_ids of this Vehicle.  # noqa: E501
        :type: dict(str, str)
        """

        self._external_ids = external_ids

    @property
    def harsh_acceleration_setting_type(self):
        """Gets the harsh_acceleration_setting_type of this Vehicle.  # noqa: E501


        :return: The harsh_acceleration_setting_type of this Vehicle.  # noqa: E501
        :rtype: VehicleHarshAccelerationSettingType
        """
        return self._harsh_acceleration_setting_type

    @harsh_acceleration_setting_type.setter
    def harsh_acceleration_setting_type(self, harsh_acceleration_setting_type):
        """Sets the harsh_acceleration_setting_type of this Vehicle.


        :param harsh_acceleration_setting_type: The harsh_acceleration_setting_type of this Vehicle.  # noqa: E501
        :type: VehicleHarshAccelerationSettingType
        """

        self._harsh_acceleration_setting_type = harsh_acceleration_setting_type

    @property
    def id(self):
        """Gets the id of this Vehicle.  # noqa: E501

        The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed.  # noqa: E501

        :return: The id of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Vehicle.

        The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed.  # noqa: E501

        :param id: The id of this Vehicle.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def license_plate(self):
        """Gets the license_plate of this Vehicle.  # noqa: E501

        The license plate of the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time.  # noqa: E501

        :return: The license_plate of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._license_plate

    @license_plate.setter
    def license_plate(self, license_plate):
        """Sets the license_plate of this Vehicle.

        The license plate of the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time.  # noqa: E501

        :param license_plate: The license_plate of this Vehicle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                license_plate is not None and len(license_plate) > 12):
            raise ValueError("Invalid value for `license_plate`, length must be less than or equal to `12`")  # noqa: E501

        self._license_plate = license_plate

    @property
    def make(self):
        """Gets the make of this Vehicle.  # noqa: E501

        The Vehicle’s manufacturing make. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set.  # noqa: E501

        :return: The make of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._make

    @make.setter
    def make(self, make):
        """Sets the make of this Vehicle.

        The Vehicle’s manufacturing make. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set.  # noqa: E501

        :param make: The make of this Vehicle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                make is not None and len(make) > 255):
            raise ValueError("Invalid value for `make`, length must be less than or equal to `255`")  # noqa: E501

        self._make = make

    @property
    def model(self):
        """Gets the model of this Vehicle.  # noqa: E501

        The Vehicle’s manufacturing model. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set.  # noqa: E501

        :return: The model of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Vehicle.

        The Vehicle’s manufacturing model. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set.  # noqa: E501

        :param model: The model of this Vehicle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) > 255):
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501

        self._model = model

    @property
    def name(self):
        """Gets the name of this Vehicle.  # noqa: E501

        The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.  # noqa: E501

        :return: The name of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Vehicle.

        The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.  # noqa: E501

        :param name: The name of this Vehicle.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this Vehicle.  # noqa: E501

        These are generic notes about the Vehicle. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time.  # noqa: E501

        :return: The notes of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Vehicle.

        These are generic notes about the Vehicle. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time.  # noqa: E501

        :param notes: The notes of this Vehicle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                notes is not None and len(notes) > 255):
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `255`")  # noqa: E501

        self._notes = notes

    @property
    def static_assigned_driver(self):
        """Gets the static_assigned_driver of this Vehicle.  # noqa: E501


        :return: The static_assigned_driver of this Vehicle.  # noqa: E501
        :rtype: DriverTinyResponse
        """
        return self._static_assigned_driver

    @static_assigned_driver.setter
    def static_assigned_driver(self, static_assigned_driver):
        """Sets the static_assigned_driver of this Vehicle.


        :param static_assigned_driver: The static_assigned_driver of this Vehicle.  # noqa: E501
        :type: DriverTinyResponse
        """

        self._static_assigned_driver = static_assigned_driver

    @property
    def tags(self):
        """Gets the tags of this Vehicle.  # noqa: E501

        The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time.  # noqa: E501

        :return: The tags of this Vehicle.  # noqa: E501
        :rtype: list[TagTinyResponse]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Vehicle.

        The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time.  # noqa: E501

        :param tags: The tags of this Vehicle.  # noqa: E501
        :type: list[TagTinyResponse]
        """

        self._tags = tags

    @property
    def vin(self):
        """Gets the vin of this Vehicle.  # noqa: E501

        The VIN of the Vehicle. Most of the time, this will be automatically read from the engine computer by the Samsara Vehicle Gateway. It will be empty if it cannot be read. It can be set or updated through the Samsara Dashboard or the API at any time.  # noqa: E501

        :return: The vin of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._vin

    @vin.setter
    def vin(self, vin):
        """Sets the vin of this Vehicle.

        The VIN of the Vehicle. Most of the time, this will be automatically read from the engine computer by the Samsara Vehicle Gateway. It will be empty if it cannot be read. It can be set or updated through the Samsara Dashboard or the API at any time.  # noqa: E501

        :param vin: The vin of this Vehicle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                vin is not None and len(vin) > 17):
            raise ValueError("Invalid value for `vin`, length must be less than or equal to `17`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                vin is not None and len(vin) < 11):
            raise ValueError("Invalid value for `vin`, length must be greater than or equal to `11`")  # noqa: E501

        self._vin = vin

    @property
    def year(self):
        """Gets the year of this Vehicle.  # noqa: E501

        The Vehicle’s manufacturing model. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set.  # noqa: E501

        :return: The year of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Vehicle.

        The Vehicle’s manufacturing model. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set.  # noqa: E501

        :param year: The year of this Vehicle.  # noqa: E501
        :type: str
        """

        self._year = year

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
        if not isinstance(other, Vehicle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Vehicle):
            return True

        return self.to_dict() != other.to_dict()
