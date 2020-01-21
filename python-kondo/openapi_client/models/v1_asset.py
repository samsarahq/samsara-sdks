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


class V1Asset(object):
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
        'asset_serial_number': 'str',
        'cable': 'list[V1AssetCable]',
        'engine_hours': 'int',
        'id': 'int',
        'name': 'str',
        'vehicle_id': 'int'
    }

    attribute_map = {
        'asset_serial_number': 'assetSerialNumber',
        'cable': 'cable',
        'engine_hours': 'engineHours',
        'id': 'id',
        'name': 'name',
        'vehicle_id': 'vehicleId'
    }

    def __init__(self, asset_serial_number=None, cable=None, engine_hours=None, id=None, name=None, vehicle_id=None, local_vars_configuration=None):  # noqa: E501
        """V1Asset - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_serial_number = None
        self._cable = None
        self._engine_hours = None
        self._id = None
        self._name = None
        self._vehicle_id = None
        self.discriminator = None

        if asset_serial_number is not None:
            self.asset_serial_number = asset_serial_number
        if cable is not None:
            self.cable = cable
        if engine_hours is not None:
            self.engine_hours = engine_hours
        self.id = id
        if name is not None:
            self.name = name
        if vehicle_id is not None:
            self.vehicle_id = vehicle_id

    @property
    def asset_serial_number(self):
        """Gets the asset_serial_number of this V1Asset.  # noqa: E501

        Serial number of the host asset  # noqa: E501

        :return: The asset_serial_number of this V1Asset.  # noqa: E501
        :rtype: str
        """
        return self._asset_serial_number

    @asset_serial_number.setter
    def asset_serial_number(self, asset_serial_number):
        """Sets the asset_serial_number of this V1Asset.

        Serial number of the host asset  # noqa: E501

        :param asset_serial_number: The asset_serial_number of this V1Asset.  # noqa: E501
        :type: str
        """

        self._asset_serial_number = asset_serial_number

    @property
    def cable(self):
        """Gets the cable of this V1Asset.  # noqa: E501

        The cable connected to the asset  # noqa: E501

        :return: The cable of this V1Asset.  # noqa: E501
        :rtype: list[V1AssetCable]
        """
        return self._cable

    @cable.setter
    def cable(self, cable):
        """Sets the cable of this V1Asset.

        The cable connected to the asset  # noqa: E501

        :param cable: The cable of this V1Asset.  # noqa: E501
        :type: list[V1AssetCable]
        """

        self._cable = cable

    @property
    def engine_hours(self):
        """Gets the engine_hours of this V1Asset.  # noqa: E501

        Engine hours  # noqa: E501

        :return: The engine_hours of this V1Asset.  # noqa: E501
        :rtype: int
        """
        return self._engine_hours

    @engine_hours.setter
    def engine_hours(self, engine_hours):
        """Sets the engine_hours of this V1Asset.

        Engine hours  # noqa: E501

        :param engine_hours: The engine_hours of this V1Asset.  # noqa: E501
        :type: int
        """

        self._engine_hours = engine_hours

    @property
    def id(self):
        """Gets the id of this V1Asset.  # noqa: E501

        Asset ID  # noqa: E501

        :return: The id of this V1Asset.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1Asset.

        Asset ID  # noqa: E501

        :param id: The id of this V1Asset.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this V1Asset.  # noqa: E501

        Asset name  # noqa: E501

        :return: The name of this V1Asset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1Asset.

        Asset name  # noqa: E501

        :param name: The name of this V1Asset.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def vehicle_id(self):
        """Gets the vehicle_id of this V1Asset.  # noqa: E501

        The ID of the Vehicle associated to the Asset (if present)  # noqa: E501

        :return: The vehicle_id of this V1Asset.  # noqa: E501
        :rtype: int
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        """Sets the vehicle_id of this V1Asset.

        The ID of the Vehicle associated to the Asset (if present)  # noqa: E501

        :param vehicle_id: The vehicle_id of this V1Asset.  # noqa: E501
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
        if not isinstance(other, V1Asset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Asset):
            return True

        return self.to_dict() != other.to_dict()
