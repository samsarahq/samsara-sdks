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

from openapi_client.configuration import Configuration


class V1FleetVehicleLocation(object):
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
        'latitude': 'float',
        'location': 'str',
        'longitude': 'float',
        'speed_miles_per_hour': 'float',
        'time_ms': 'float'
    }

    attribute_map = {
        'latitude': 'latitude',
        'location': 'location',
        'longitude': 'longitude',
        'speed_miles_per_hour': 'speedMilesPerHour',
        'time_ms': 'timeMs'
    }

    def __init__(self, latitude=None, location=None, longitude=None, speed_miles_per_hour=None, time_ms=None, local_vars_configuration=None):  # noqa: E501
        """V1FleetVehicleLocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._latitude = None
        self._location = None
        self._longitude = None
        self._speed_miles_per_hour = None
        self._time_ms = None
        self.discriminator = None

        if latitude is not None:
            self.latitude = latitude
        if location is not None:
            self.location = location
        if longitude is not None:
            self.longitude = longitude
        if speed_miles_per_hour is not None:
            self.speed_miles_per_hour = speed_miles_per_hour
        if time_ms is not None:
            self.time_ms = time_ms

    @property
    def latitude(self):
        """Gets the latitude of this V1FleetVehicleLocation.  # noqa: E501

        The latitude of the location in degrees.  # noqa: E501

        :return: The latitude of this V1FleetVehicleLocation.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this V1FleetVehicleLocation.

        The latitude of the location in degrees.  # noqa: E501

        :param latitude: The latitude of this V1FleetVehicleLocation.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def location(self):
        """Gets the location of this V1FleetVehicleLocation.  # noqa: E501

        The best effort (street,city,state) for the latitude and longitude.  # noqa: E501

        :return: The location of this V1FleetVehicleLocation.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this V1FleetVehicleLocation.

        The best effort (street,city,state) for the latitude and longitude.  # noqa: E501

        :param location: The location of this V1FleetVehicleLocation.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def longitude(self):
        """Gets the longitude of this V1FleetVehicleLocation.  # noqa: E501

        The longitude of the location in degrees.  # noqa: E501

        :return: The longitude of this V1FleetVehicleLocation.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this V1FleetVehicleLocation.

        The longitude of the location in degrees.  # noqa: E501

        :param longitude: The longitude of this V1FleetVehicleLocation.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def speed_miles_per_hour(self):
        """Gets the speed_miles_per_hour of this V1FleetVehicleLocation.  # noqa: E501

        The speed calculated from GPS that the asset was traveling at in miles per hour.  # noqa: E501

        :return: The speed_miles_per_hour of this V1FleetVehicleLocation.  # noqa: E501
        :rtype: float
        """
        return self._speed_miles_per_hour

    @speed_miles_per_hour.setter
    def speed_miles_per_hour(self, speed_miles_per_hour):
        """Sets the speed_miles_per_hour of this V1FleetVehicleLocation.

        The speed calculated from GPS that the asset was traveling at in miles per hour.  # noqa: E501

        :param speed_miles_per_hour: The speed_miles_per_hour of this V1FleetVehicleLocation.  # noqa: E501
        :type: float
        """

        self._speed_miles_per_hour = speed_miles_per_hour

    @property
    def time_ms(self):
        """Gets the time_ms of this V1FleetVehicleLocation.  # noqa: E501

        Time in Unix milliseconds since epoch when the asset was at the location.  # noqa: E501

        :return: The time_ms of this V1FleetVehicleLocation.  # noqa: E501
        :rtype: float
        """
        return self._time_ms

    @time_ms.setter
    def time_ms(self, time_ms):
        """Sets the time_ms of this V1FleetVehicleLocation.

        Time in Unix milliseconds since epoch when the asset was at the location.  # noqa: E501

        :param time_ms: The time_ms of this V1FleetVehicleLocation.  # noqa: E501
        :type: float
        """

        self._time_ms = time_ms

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
        if not isinstance(other, V1FleetVehicleLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1FleetVehicleLocation):
            return True

        return self.to_dict() != other.to_dict()
