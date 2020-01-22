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


class V1AssetReeferResponseReeferStatsAlarms(object):
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
        'alarm_code': 'int',
        'description': 'str',
        'operator_action': 'str',
        'severity': 'int'
    }

    attribute_map = {
        'alarm_code': 'alarmCode',
        'description': 'description',
        'operator_action': 'operatorAction',
        'severity': 'severity'
    }

    def __init__(self, alarm_code=None, description=None, operator_action=None, severity=None, local_vars_configuration=None):  # noqa: E501
        """V1AssetReeferResponseReeferStatsAlarms - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alarm_code = None
        self._description = None
        self._operator_action = None
        self._severity = None
        self.discriminator = None

        if alarm_code is not None:
            self.alarm_code = alarm_code
        if description is not None:
            self.description = description
        if operator_action is not None:
            self.operator_action = operator_action
        if severity is not None:
            self.severity = severity

    @property
    def alarm_code(self):
        """Gets the alarm_code of this V1AssetReeferResponseReeferStatsAlarms.  # noqa: E501

        ID of the alarm  # noqa: E501

        :return: The alarm_code of this V1AssetReeferResponseReeferStatsAlarms.  # noqa: E501
        :rtype: int
        """
        return self._alarm_code

    @alarm_code.setter
    def alarm_code(self, alarm_code):
        """Sets the alarm_code of this V1AssetReeferResponseReeferStatsAlarms.

        ID of the alarm  # noqa: E501

        :param alarm_code: The alarm_code of this V1AssetReeferResponseReeferStatsAlarms.  # noqa: E501
        :type: int
        """

        self._alarm_code = alarm_code

    @property
    def description(self):
        """Gets the description of this V1AssetReeferResponseReeferStatsAlarms.  # noqa: E501

        Description of the alarm  # noqa: E501

        :return: The description of this V1AssetReeferResponseReeferStatsAlarms.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1AssetReeferResponseReeferStatsAlarms.

        Description of the alarm  # noqa: E501

        :param description: The description of this V1AssetReeferResponseReeferStatsAlarms.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def operator_action(self):
        """Gets the operator_action of this V1AssetReeferResponseReeferStatsAlarms.  # noqa: E501

        Recommended operator action  # noqa: E501

        :return: The operator_action of this V1AssetReeferResponseReeferStatsAlarms.  # noqa: E501
        :rtype: str
        """
        return self._operator_action

    @operator_action.setter
    def operator_action(self, operator_action):
        """Sets the operator_action of this V1AssetReeferResponseReeferStatsAlarms.

        Recommended operator action  # noqa: E501

        :param operator_action: The operator_action of this V1AssetReeferResponseReeferStatsAlarms.  # noqa: E501
        :type: str
        """

        self._operator_action = operator_action

    @property
    def severity(self):
        """Gets the severity of this V1AssetReeferResponseReeferStatsAlarms.  # noqa: E501

        Severity of the alarm: 1: OK to run, 2: Check as specified, 3: Take immediate action  # noqa: E501

        :return: The severity of this V1AssetReeferResponseReeferStatsAlarms.  # noqa: E501
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this V1AssetReeferResponseReeferStatsAlarms.

        Severity of the alarm: 1: OK to run, 2: Check as specified, 3: Take immediate action  # noqa: E501

        :param severity: The severity of this V1AssetReeferResponseReeferStatsAlarms.  # noqa: E501
        :type: int
        """

        self._severity = severity

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
        if not isinstance(other, V1AssetReeferResponseReeferStatsAlarms):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1AssetReeferResponseReeferStatsAlarms):
            return True

        return self.to_dict() != other.to_dict()
