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


class V1AssetsReeferReeferStats(object):
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
        'ambient_air_temperature': 'list[V1AssetsReeferReeferStatsAmbientAirTemperature]',
        'discharge_air_temperature': 'list[V1AssetsReeferReeferStatsDischargeAirTemperature]',
        'engine_hours': 'list[V1AssetReeferResponseReeferStatsEngineHours]',
        'fuel_percentage': 'list[V1AssetReeferResponseReeferStatsFuelPercentage]',
        'power_status': 'list[V1AssetsReeferReeferStatsPowerStatus]',
        'reefer_alarms': 'list[V1AssetReeferResponseReeferStatsAlarms1]',
        'return_air_temperature': 'list[V1AssetReeferResponseReeferStatsReturnAirTemp]',
        'set_point': 'list[V1AssetReeferResponseReeferStatsSetPoint]'
    }

    attribute_map = {
        'ambient_air_temperature': 'ambientAirTemperature',
        'discharge_air_temperature': 'dischargeAirTemperature',
        'engine_hours': 'engineHours',
        'fuel_percentage': 'fuelPercentage',
        'power_status': 'powerStatus',
        'reefer_alarms': 'reeferAlarms',
        'return_air_temperature': 'returnAirTemperature',
        'set_point': 'setPoint'
    }

    def __init__(self, ambient_air_temperature=None, discharge_air_temperature=None, engine_hours=None, fuel_percentage=None, power_status=None, reefer_alarms=None, return_air_temperature=None, set_point=None, local_vars_configuration=None):  # noqa: E501
        """V1AssetsReeferReeferStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ambient_air_temperature = None
        self._discharge_air_temperature = None
        self._engine_hours = None
        self._fuel_percentage = None
        self._power_status = None
        self._reefer_alarms = None
        self._return_air_temperature = None
        self._set_point = None
        self.discriminator = None

        if ambient_air_temperature is not None:
            self.ambient_air_temperature = ambient_air_temperature
        if discharge_air_temperature is not None:
            self.discharge_air_temperature = discharge_air_temperature
        if engine_hours is not None:
            self.engine_hours = engine_hours
        if fuel_percentage is not None:
            self.fuel_percentage = fuel_percentage
        if power_status is not None:
            self.power_status = power_status
        if reefer_alarms is not None:
            self.reefer_alarms = reefer_alarms
        if return_air_temperature is not None:
            self.return_air_temperature = return_air_temperature
        if set_point is not None:
            self.set_point = set_point

    @property
    def ambient_air_temperature(self):
        """Gets the ambient_air_temperature of this V1AssetsReeferReeferStats.  # noqa: E501

        Ambient temperature of the reefer. This is the temperature of the air around the Samsara Asset Gateway.  # noqa: E501

        :return: The ambient_air_temperature of this V1AssetsReeferReeferStats.  # noqa: E501
        :rtype: list[V1AssetsReeferReeferStatsAmbientAirTemperature]
        """
        return self._ambient_air_temperature

    @ambient_air_temperature.setter
    def ambient_air_temperature(self, ambient_air_temperature):
        """Sets the ambient_air_temperature of this V1AssetsReeferReeferStats.

        Ambient temperature of the reefer. This is the temperature of the air around the Samsara Asset Gateway.  # noqa: E501

        :param ambient_air_temperature: The ambient_air_temperature of this V1AssetsReeferReeferStats.  # noqa: E501
        :type: list[V1AssetsReeferReeferStatsAmbientAirTemperature]
        """

        self._ambient_air_temperature = ambient_air_temperature

    @property
    def discharge_air_temperature(self):
        """Gets the discharge_air_temperature of this V1AssetsReeferReeferStats.  # noqa: E501

        Discharge air temperature of the reefer. This is the temperature of the air as it leaves the cooling unit.  # noqa: E501

        :return: The discharge_air_temperature of this V1AssetsReeferReeferStats.  # noqa: E501
        :rtype: list[V1AssetsReeferReeferStatsDischargeAirTemperature]
        """
        return self._discharge_air_temperature

    @discharge_air_temperature.setter
    def discharge_air_temperature(self, discharge_air_temperature):
        """Sets the discharge_air_temperature of this V1AssetsReeferReeferStats.

        Discharge air temperature of the reefer. This is the temperature of the air as it leaves the cooling unit.  # noqa: E501

        :param discharge_air_temperature: The discharge_air_temperature of this V1AssetsReeferReeferStats.  # noqa: E501
        :type: list[V1AssetsReeferReeferStatsDischargeAirTemperature]
        """

        self._discharge_air_temperature = discharge_air_temperature

    @property
    def engine_hours(self):
        """Gets the engine_hours of this V1AssetsReeferReeferStats.  # noqa: E501

        Engine hours of the reefer  # noqa: E501

        :return: The engine_hours of this V1AssetsReeferReeferStats.  # noqa: E501
        :rtype: list[V1AssetReeferResponseReeferStatsEngineHours]
        """
        return self._engine_hours

    @engine_hours.setter
    def engine_hours(self, engine_hours):
        """Sets the engine_hours of this V1AssetsReeferReeferStats.

        Engine hours of the reefer  # noqa: E501

        :param engine_hours: The engine_hours of this V1AssetsReeferReeferStats.  # noqa: E501
        :type: list[V1AssetReeferResponseReeferStatsEngineHours]
        """

        self._engine_hours = engine_hours

    @property
    def fuel_percentage(self):
        """Gets the fuel_percentage of this V1AssetsReeferReeferStats.  # noqa: E501

        Fuel percentage of the reefer  # noqa: E501

        :return: The fuel_percentage of this V1AssetsReeferReeferStats.  # noqa: E501
        :rtype: list[V1AssetReeferResponseReeferStatsFuelPercentage]
        """
        return self._fuel_percentage

    @fuel_percentage.setter
    def fuel_percentage(self, fuel_percentage):
        """Sets the fuel_percentage of this V1AssetsReeferReeferStats.

        Fuel percentage of the reefer  # noqa: E501

        :param fuel_percentage: The fuel_percentage of this V1AssetsReeferReeferStats.  # noqa: E501
        :type: list[V1AssetReeferResponseReeferStatsFuelPercentage]
        """

        self._fuel_percentage = fuel_percentage

    @property
    def power_status(self):
        """Gets the power_status of this V1AssetsReeferReeferStats.  # noqa: E501

        Power status of the reefer  # noqa: E501

        :return: The power_status of this V1AssetsReeferReeferStats.  # noqa: E501
        :rtype: list[V1AssetsReeferReeferStatsPowerStatus]
        """
        return self._power_status

    @power_status.setter
    def power_status(self, power_status):
        """Sets the power_status of this V1AssetsReeferReeferStats.

        Power status of the reefer  # noqa: E501

        :param power_status: The power_status of this V1AssetsReeferReeferStats.  # noqa: E501
        :type: list[V1AssetsReeferReeferStatsPowerStatus]
        """

        self._power_status = power_status

    @property
    def reefer_alarms(self):
        """Gets the reefer_alarms of this V1AssetsReeferReeferStats.  # noqa: E501

        Reefer alarms  # noqa: E501

        :return: The reefer_alarms of this V1AssetsReeferReeferStats.  # noqa: E501
        :rtype: list[V1AssetReeferResponseReeferStatsAlarms1]
        """
        return self._reefer_alarms

    @reefer_alarms.setter
    def reefer_alarms(self, reefer_alarms):
        """Sets the reefer_alarms of this V1AssetsReeferReeferStats.

        Reefer alarms  # noqa: E501

        :param reefer_alarms: The reefer_alarms of this V1AssetsReeferReeferStats.  # noqa: E501
        :type: list[V1AssetReeferResponseReeferStatsAlarms1]
        """

        self._reefer_alarms = reefer_alarms

    @property
    def return_air_temperature(self):
        """Gets the return_air_temperature of this V1AssetsReeferReeferStats.  # noqa: E501

        Return air temperature of the reefer. This is the temperature read by the reefer module (Carrier, Thermo King) that shows the temperature of the air as it enters the system.  # noqa: E501

        :return: The return_air_temperature of this V1AssetsReeferReeferStats.  # noqa: E501
        :rtype: list[V1AssetReeferResponseReeferStatsReturnAirTemp]
        """
        return self._return_air_temperature

    @return_air_temperature.setter
    def return_air_temperature(self, return_air_temperature):
        """Sets the return_air_temperature of this V1AssetsReeferReeferStats.

        Return air temperature of the reefer. This is the temperature read by the reefer module (Carrier, Thermo King) that shows the temperature of the air as it enters the system.  # noqa: E501

        :param return_air_temperature: The return_air_temperature of this V1AssetsReeferReeferStats.  # noqa: E501
        :type: list[V1AssetReeferResponseReeferStatsReturnAirTemp]
        """

        self._return_air_temperature = return_air_temperature

    @property
    def set_point(self):
        """Gets the set_point of this V1AssetsReeferReeferStats.  # noqa: E501

        Set point temperature of the reefer  # noqa: E501

        :return: The set_point of this V1AssetsReeferReeferStats.  # noqa: E501
        :rtype: list[V1AssetReeferResponseReeferStatsSetPoint]
        """
        return self._set_point

    @set_point.setter
    def set_point(self, set_point):
        """Sets the set_point of this V1AssetsReeferReeferStats.

        Set point temperature of the reefer  # noqa: E501

        :param set_point: The set_point of this V1AssetsReeferReeferStats.  # noqa: E501
        :type: list[V1AssetReeferResponseReeferStatsSetPoint]
        """

        self._set_point = set_point

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
        if not isinstance(other, V1AssetsReeferReeferStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1AssetsReeferReeferStats):
            return True

        return self.to_dict() != other.to_dict()
