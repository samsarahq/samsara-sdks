# coding: utf-8

"""
    Samsara API

    <style type=\"text/css\"> n {     padding: 1em;     width: 100%;     display: block;     margin: 28px 0; } n.info {     background-color: rgba(0, 51, 160, 0.1); } n.warning {     background-color: #fdf6e3; } i:before {     margin-right: 6px; } nh {     font-size: 1.5rem;     font-weight: 700;     line-height: 1.1;     display: block; } nb {     margin-top: 10px;     padding-left: 22px;     display: block; } </style>  # Overview  <n class=\"info\"> <nh> <i class=\"fa fa-info-circle\"></i> Something new! </nh> <nb> Welcome Samsara's new and improved API. Check out our FAQ [here](https://developers.samsara.com/docs/introducing-our-next-generation-api) to see what's changed and learn how to get started.<br> <br> Want to access the legacy API docs? You can find them [here](https://www.samsara.com/api-legacy).<br> <br> *Note: Because this is a new set of APIs, we have not transitioned all endpoints over to this standard. Endpoints that still use the legacy standards are indicated in the reference documentation. If you can't find an API that you're looking for, we encourage you to look for it in our [legacy API docs](https://www.samsara.com/api-legacy) as we continue to transition all endpoints over. Check back here for updates!*<br> <br> Submit your feedback [here](https://forms.gle/r4bs6HQshQAvBuwv6)! </nb> </n>  Samsara provides API endpoints so that you can build powerful applications and custom solutions with sensor data. Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets.  The Samsara API is a [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer). It uses standard [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) authentication, verbs, and response codes, and it returns [JSON](http://www.json.org/) response bodies. If you're familiar with what you can build with a REST API, then this will be your go-to API reference.  Visit [developers.samsara.com](https://developers.samsara.com) to find getting started guides and an API overview.  If you have any questions, reach out to us at [support@samsara.com](mailto:support@samsara.com).  ## Endpoints  All our APIs can be accessed through HTTP requests to URLs like:  ``` https://api.samsara.com/<endpoint> ```  For EU customers, this URL will be:  ``` https://api.eu.samsara.com/<endpoint> ```  <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> Note </nh> <nb> Legacy endpoints will have the URL: `https://api.samsara.com/v1/<endpoint>` or `https://api.eu.samsara.com/v1/<endpoint>` </nb> </n>  ## Authentication  To authenticate your API request you will need to include your secret token. You can manage your API tokens in the [Dashboard](https://cloud.samsara.com). They are visible under `Settings->Organization->API Tokens`.  Your API tokens carry many privileges, so be sure to keep them secure. Do not share your secret API tokens in publicly accessible areas such as GitHub, client-side code, and so on.  Authentication to the API is performed via Bearer Token in the HTTP Authorization header. Provide your API token as the `access_token` value in an `Authorization: Bearer` header. You do not need to provide a password:  ```curl Authorization: Bearer {access_token} ```  All API requests must be made over [HTTPS](https://en.wikipedia.org/wiki/HTTPS). Calls made over plain HTTP or without authentication will fail.  ## Common Patterns  You can find more info about request methods, response codes, error codes, versioning, pagination, timestamps, and mini-objects [here](https://developers.samsara.com/docs/common-structures).   # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class VehicleStatsListResponseData(object):
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
        'engine_states': 'list[VehicleStatsEngineState]',
        'fuel_percent': 'list[VehicleStatsFuelPercent]',
        'gps_distance_meters': 'list[VehicleStatsGpsDistanceMeters]',
        'gps_odometer_meters': 'list[VehicleStatsGpsOdometerMeters]',
        'id': 'str',
        'name': 'str',
        'obd_engine_seconds': 'list[VehicleStatsObdEngineSeconds]',
        'obd_odometer_meters': 'list[VehicleStatsObdOdometerMeters]'
    }

    attribute_map = {
        'engine_states': 'engineStates',
        'fuel_percent': 'fuelPercent',
        'gps_distance_meters': 'gpsDistanceMeters',
        'gps_odometer_meters': 'gpsOdometerMeters',
        'id': 'id',
        'name': 'name',
        'obd_engine_seconds': 'obdEngineSeconds',
        'obd_odometer_meters': 'obdOdometerMeters'
    }

    def __init__(self, engine_states=None, fuel_percent=None, gps_distance_meters=None, gps_odometer_meters=None, id=None, name=None, obd_engine_seconds=None, obd_odometer_meters=None, local_vars_configuration=None):  # noqa: E501
        """VehicleStatsListResponseData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._engine_states = None
        self._fuel_percent = None
        self._gps_distance_meters = None
        self._gps_odometer_meters = None
        self._id = None
        self._name = None
        self._obd_engine_seconds = None
        self._obd_odometer_meters = None
        self.discriminator = None

        if engine_states is not None:
            self.engine_states = engine_states
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
    def engine_states(self):
        """Gets the engine_states of this VehicleStatsListResponseData.  # noqa: E501

        A list of engine state events for the given vehicle.  # noqa: E501

        :return: The engine_states of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsEngineState]
        """
        return self._engine_states

    @engine_states.setter
    def engine_states(self, engine_states):
        """Sets the engine_states of this VehicleStatsListResponseData.

        A list of engine state events for the given vehicle.  # noqa: E501

        :param engine_states: The engine_states of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsEngineState]
        """

        self._engine_states = engine_states

    @property
    def fuel_percent(self):
        """Gets the fuel_percent of this VehicleStatsListResponseData.  # noqa: E501

        A list of fuel percentage readings for the given vehicle.  # noqa: E501

        :return: The fuel_percent of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsFuelPercent]
        """
        return self._fuel_percent

    @fuel_percent.setter
    def fuel_percent(self, fuel_percent):
        """Sets the fuel_percent of this VehicleStatsListResponseData.

        A list of fuel percentage readings for the given vehicle.  # noqa: E501

        :param fuel_percent: The fuel_percent of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsFuelPercent]
        """

        self._fuel_percent = fuel_percent

    @property
    def gps_distance_meters(self):
        """Gets the gps_distance_meters of this VehicleStatsListResponseData.  # noqa: E501

        A list of GPS distance events for the given vehicle.  # noqa: E501

        :return: The gps_distance_meters of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsGpsDistanceMeters]
        """
        return self._gps_distance_meters

    @gps_distance_meters.setter
    def gps_distance_meters(self, gps_distance_meters):
        """Sets the gps_distance_meters of this VehicleStatsListResponseData.

        A list of GPS distance events for the given vehicle.  # noqa: E501

        :param gps_distance_meters: The gps_distance_meters of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsGpsDistanceMeters]
        """

        self._gps_distance_meters = gps_distance_meters

    @property
    def gps_odometer_meters(self):
        """Gets the gps_odometer_meters of this VehicleStatsListResponseData.  # noqa: E501

        A list of GPS odometer events for the given vehicle.  # noqa: E501

        :return: The gps_odometer_meters of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsGpsOdometerMeters]
        """
        return self._gps_odometer_meters

    @gps_odometer_meters.setter
    def gps_odometer_meters(self, gps_odometer_meters):
        """Sets the gps_odometer_meters of this VehicleStatsListResponseData.

        A list of GPS odometer events for the given vehicle.  # noqa: E501

        :param gps_odometer_meters: The gps_odometer_meters of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsGpsOdometerMeters]
        """

        self._gps_odometer_meters = gps_odometer_meters

    @property
    def id(self):
        """Gets the id of this VehicleStatsListResponseData.  # noqa: E501

        The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed.  # noqa: E501

        :return: The id of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VehicleStatsListResponseData.

        The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed.  # noqa: E501

        :param id: The id of this VehicleStatsListResponseData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this VehicleStatsListResponseData.  # noqa: E501

        The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.  # noqa: E501

        :return: The name of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VehicleStatsListResponseData.

        The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.  # noqa: E501

        :param name: The name of this VehicleStatsListResponseData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def obd_engine_seconds(self):
        """Gets the obd_engine_seconds of this VehicleStatsListResponseData.  # noqa: E501

        A list of OBD engine seconds readings for the given vehicle.  # noqa: E501

        :return: The obd_engine_seconds of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsObdEngineSeconds]
        """
        return self._obd_engine_seconds

    @obd_engine_seconds.setter
    def obd_engine_seconds(self, obd_engine_seconds):
        """Sets the obd_engine_seconds of this VehicleStatsListResponseData.

        A list of OBD engine seconds readings for the given vehicle.  # noqa: E501

        :param obd_engine_seconds: The obd_engine_seconds of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsObdEngineSeconds]
        """

        self._obd_engine_seconds = obd_engine_seconds

    @property
    def obd_odometer_meters(self):
        """Gets the obd_odometer_meters of this VehicleStatsListResponseData.  # noqa: E501

        A list of OBD odometer readings for the given vehicle.  # noqa: E501

        :return: The obd_odometer_meters of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsObdOdometerMeters]
        """
        return self._obd_odometer_meters

    @obd_odometer_meters.setter
    def obd_odometer_meters(self, obd_odometer_meters):
        """Sets the obd_odometer_meters of this VehicleStatsListResponseData.

        A list of OBD odometer readings for the given vehicle.  # noqa: E501

        :param obd_odometer_meters: The obd_odometer_meters of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsObdOdometerMeters]
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
        if not isinstance(other, VehicleStatsListResponseData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleStatsListResponseData):
            return True

        return self.to_dict() != other.to_dict()
