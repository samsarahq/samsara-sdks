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


class VehicleStatsResponseData(object):
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
        'engine_state': 'VehicleStatsEngineState',
        'fuel_percent': 'VehicleStatsFuelPercent',
        'gps_distance_meters': 'VehicleStatsGpsDistanceMeters',
        'gps_odometer_meters': 'VehicleStatsGpsOdometerMeters',
        'id': 'str',
        'name': 'str',
        'obd_engine_seconds': 'VehicleStatsObdEngineSeconds',
        'obd_odometer_meters': 'VehicleStatsObdOdometerMeters'
    }

    attribute_map = {
        'engine_state': 'engineState',
        'fuel_percent': 'fuelPercent',
        'gps_distance_meters': 'gpsDistanceMeters',
        'gps_odometer_meters': 'gpsOdometerMeters',
        'id': 'id',
        'name': 'name',
        'obd_engine_seconds': 'obdEngineSeconds',
        'obd_odometer_meters': 'obdOdometerMeters'
    }

    def __init__(self, engine_state=None, fuel_percent=None, gps_distance_meters=None, gps_odometer_meters=None, id=None, name=None, obd_engine_seconds=None, obd_odometer_meters=None, local_vars_configuration=None):  # noqa: E501
        """VehicleStatsResponseData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._engine_state = None
        self._fuel_percent = None
        self._gps_distance_meters = None
        self._gps_odometer_meters = None
        self._id = None
        self._name = None
        self._obd_engine_seconds = None
        self._obd_odometer_meters = None
        self.discriminator = None

        if engine_state is not None:
            self.engine_state = engine_state
        if fuel_percent is not None:
            self.fuel_percent = fuel_percent
        if gps_distance_meters is not None:
            self.gps_distance_meters = gps_distance_meters
        if gps_odometer_meters is not None:
            self.gps_odometer_meters = gps_odometer_meters
        self.id = id
        self.name = name
        if obd_engine_seconds is not None:
            self.obd_engine_seconds = obd_engine_seconds
        if obd_odometer_meters is not None:
            self.obd_odometer_meters = obd_odometer_meters

    @property
    def engine_state(self):
        """Gets the engine_state of this VehicleStatsResponseData.  # noqa: E501


        :return: The engine_state of this VehicleStatsResponseData.  # noqa: E501
        :rtype: VehicleStatsEngineState
        """
        return self._engine_state

    @engine_state.setter
    def engine_state(self, engine_state):
        """Sets the engine_state of this VehicleStatsResponseData.


        :param engine_state: The engine_state of this VehicleStatsResponseData.  # noqa: E501
        :type: VehicleStatsEngineState
        """

        self._engine_state = engine_state

    @property
    def fuel_percent(self):
        """Gets the fuel_percent of this VehicleStatsResponseData.  # noqa: E501


        :return: The fuel_percent of this VehicleStatsResponseData.  # noqa: E501
        :rtype: VehicleStatsFuelPercent
        """
        return self._fuel_percent

    @fuel_percent.setter
    def fuel_percent(self, fuel_percent):
        """Sets the fuel_percent of this VehicleStatsResponseData.


        :param fuel_percent: The fuel_percent of this VehicleStatsResponseData.  # noqa: E501
        :type: VehicleStatsFuelPercent
        """

        self._fuel_percent = fuel_percent

    @property
    def gps_distance_meters(self):
        """Gets the gps_distance_meters of this VehicleStatsResponseData.  # noqa: E501


        :return: The gps_distance_meters of this VehicleStatsResponseData.  # noqa: E501
        :rtype: VehicleStatsGpsDistanceMeters
        """
        return self._gps_distance_meters

    @gps_distance_meters.setter
    def gps_distance_meters(self, gps_distance_meters):
        """Sets the gps_distance_meters of this VehicleStatsResponseData.


        :param gps_distance_meters: The gps_distance_meters of this VehicleStatsResponseData.  # noqa: E501
        :type: VehicleStatsGpsDistanceMeters
        """

        self._gps_distance_meters = gps_distance_meters

    @property
    def gps_odometer_meters(self):
        """Gets the gps_odometer_meters of this VehicleStatsResponseData.  # noqa: E501


        :return: The gps_odometer_meters of this VehicleStatsResponseData.  # noqa: E501
        :rtype: VehicleStatsGpsOdometerMeters
        """
        return self._gps_odometer_meters

    @gps_odometer_meters.setter
    def gps_odometer_meters(self, gps_odometer_meters):
        """Sets the gps_odometer_meters of this VehicleStatsResponseData.


        :param gps_odometer_meters: The gps_odometer_meters of this VehicleStatsResponseData.  # noqa: E501
        :type: VehicleStatsGpsOdometerMeters
        """

        self._gps_odometer_meters = gps_odometer_meters

    @property
    def id(self):
        """Gets the id of this VehicleStatsResponseData.  # noqa: E501

        The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed.  # noqa: E501

        :return: The id of this VehicleStatsResponseData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VehicleStatsResponseData.

        The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed.  # noqa: E501

        :param id: The id of this VehicleStatsResponseData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this VehicleStatsResponseData.  # noqa: E501

        The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.  # noqa: E501

        :return: The name of this VehicleStatsResponseData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VehicleStatsResponseData.

        The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.  # noqa: E501

        :param name: The name of this VehicleStatsResponseData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def obd_engine_seconds(self):
        """Gets the obd_engine_seconds of this VehicleStatsResponseData.  # noqa: E501


        :return: The obd_engine_seconds of this VehicleStatsResponseData.  # noqa: E501
        :rtype: VehicleStatsObdEngineSeconds
        """
        return self._obd_engine_seconds

    @obd_engine_seconds.setter
    def obd_engine_seconds(self, obd_engine_seconds):
        """Sets the obd_engine_seconds of this VehicleStatsResponseData.


        :param obd_engine_seconds: The obd_engine_seconds of this VehicleStatsResponseData.  # noqa: E501
        :type: VehicleStatsObdEngineSeconds
        """

        self._obd_engine_seconds = obd_engine_seconds

    @property
    def obd_odometer_meters(self):
        """Gets the obd_odometer_meters of this VehicleStatsResponseData.  # noqa: E501


        :return: The obd_odometer_meters of this VehicleStatsResponseData.  # noqa: E501
        :rtype: VehicleStatsObdOdometerMeters
        """
        return self._obd_odometer_meters

    @obd_odometer_meters.setter
    def obd_odometer_meters(self, obd_odometer_meters):
        """Sets the obd_odometer_meters of this VehicleStatsResponseData.


        :param obd_odometer_meters: The obd_odometer_meters of this VehicleStatsResponseData.  # noqa: E501
        :type: VehicleStatsObdOdometerMeters
        """

        self._obd_odometer_meters = obd_odometer_meters

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
        if not isinstance(other, VehicleStatsResponseData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleStatsResponseData):
            return True

        return self.to_dict() != other.to_dict()
