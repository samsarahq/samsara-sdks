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


class V1HosLogsSummaryResponseDrivers(object):
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
        'current_duty_status_code': 'str',
        'cycle_remaining': 'int',
        'cycle_tomorrow': 'int',
        'drive_ms_today': 'float',
        'driver_id': 'int',
        'driver_name': 'str',
        'driving_in_violation_cycle': 'int',
        'driving_in_violation_today': 'int',
        'on_duty_ms_today': 'float',
        'pending_drive_ms_today': 'float',
        'pending_on_duty_ms_today': 'float',
        'shift_drive_remaining': 'int',
        'shift_remaining': 'int',
        'time_in_current_status': 'int',
        'time_until_break': 'int',
        'vehicle_name': 'str'
    }

    attribute_map = {
        'current_duty_status_code': 'currentDutyStatusCode',
        'cycle_remaining': 'cycleRemaining',
        'cycle_tomorrow': 'cycleTomorrow',
        'drive_ms_today': 'driveMsToday',
        'driver_id': 'driverId',
        'driver_name': 'driverName',
        'driving_in_violation_cycle': 'drivingInViolationCycle',
        'driving_in_violation_today': 'drivingInViolationToday',
        'on_duty_ms_today': 'onDutyMsToday',
        'pending_drive_ms_today': 'pendingDriveMsToday',
        'pending_on_duty_ms_today': 'pendingOnDutyMsToday',
        'shift_drive_remaining': 'shiftDriveRemaining',
        'shift_remaining': 'shiftRemaining',
        'time_in_current_status': 'timeInCurrentStatus',
        'time_until_break': 'timeUntilBreak',
        'vehicle_name': 'vehicleName'
    }

    def __init__(self, current_duty_status_code=None, cycle_remaining=None, cycle_tomorrow=None, drive_ms_today=None, driver_id=None, driver_name=None, driving_in_violation_cycle=None, driving_in_violation_today=None, on_duty_ms_today=None, pending_drive_ms_today=None, pending_on_duty_ms_today=None, shift_drive_remaining=None, shift_remaining=None, time_in_current_status=None, time_until_break=None, vehicle_name=None, local_vars_configuration=None):  # noqa: E501
        """V1HosLogsSummaryResponseDrivers - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._current_duty_status_code = None
        self._cycle_remaining = None
        self._cycle_tomorrow = None
        self._drive_ms_today = None
        self._driver_id = None
        self._driver_name = None
        self._driving_in_violation_cycle = None
        self._driving_in_violation_today = None
        self._on_duty_ms_today = None
        self._pending_drive_ms_today = None
        self._pending_on_duty_ms_today = None
        self._shift_drive_remaining = None
        self._shift_remaining = None
        self._time_in_current_status = None
        self._time_until_break = None
        self._vehicle_name = None
        self.discriminator = None

        if current_duty_status_code is not None:
            self.current_duty_status_code = current_duty_status_code
        if cycle_remaining is not None:
            self.cycle_remaining = cycle_remaining
        if cycle_tomorrow is not None:
            self.cycle_tomorrow = cycle_tomorrow
        if drive_ms_today is not None:
            self.drive_ms_today = drive_ms_today
        if driver_id is not None:
            self.driver_id = driver_id
        if driver_name is not None:
            self.driver_name = driver_name
        if driving_in_violation_cycle is not None:
            self.driving_in_violation_cycle = driving_in_violation_cycle
        if driving_in_violation_today is not None:
            self.driving_in_violation_today = driving_in_violation_today
        if on_duty_ms_today is not None:
            self.on_duty_ms_today = on_duty_ms_today
        if pending_drive_ms_today is not None:
            self.pending_drive_ms_today = pending_drive_ms_today
        if pending_on_duty_ms_today is not None:
            self.pending_on_duty_ms_today = pending_on_duty_ms_today
        if shift_drive_remaining is not None:
            self.shift_drive_remaining = shift_drive_remaining
        if shift_remaining is not None:
            self.shift_remaining = shift_remaining
        if time_in_current_status is not None:
            self.time_in_current_status = time_in_current_status
        if time_until_break is not None:
            self.time_until_break = time_until_break
        if vehicle_name is not None:
            self.vehicle_name = vehicle_name

    @property
    def current_duty_status_code(self):
        """Gets the current_duty_status_code of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        The Hours of Service status type.  # noqa: E501

        :return: The current_duty_status_code of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: str
        """
        return self._current_duty_status_code

    @current_duty_status_code.setter
    def current_duty_status_code(self, current_duty_status_code):
        """Sets the current_duty_status_code of this V1HosLogsSummaryResponseDrivers.

        The Hours of Service status type.  # noqa: E501

        :param current_duty_status_code: The current_duty_status_code of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTO_DUTY", "DRIVING", "OFF_DUTY", "ON_DUTY", "PERSONAL_CONVEYANCE", "SLEEPER_BED", "YARD_MOVE", "WAITING_TIME"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and current_duty_status_code not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `current_duty_status_code` ({0}), must be one of {1}"  # noqa: E501
                .format(current_duty_status_code, allowed_values)
            )

        self._current_duty_status_code = current_duty_status_code

    @property
    def cycle_remaining(self):
        """Gets the cycle_remaining of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        The amount of remaining cycle time (in ms).  # noqa: E501

        :return: The cycle_remaining of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: int
        """
        return self._cycle_remaining

    @cycle_remaining.setter
    def cycle_remaining(self, cycle_remaining):
        """Sets the cycle_remaining of this V1HosLogsSummaryResponseDrivers.

        The amount of remaining cycle time (in ms).  # noqa: E501

        :param cycle_remaining: The cycle_remaining of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: int
        """

        self._cycle_remaining = cycle_remaining

    @property
    def cycle_tomorrow(self):
        """Gets the cycle_tomorrow of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        The amount of cycle time (in ms) available tomorrow.  # noqa: E501

        :return: The cycle_tomorrow of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: int
        """
        return self._cycle_tomorrow

    @cycle_tomorrow.setter
    def cycle_tomorrow(self, cycle_tomorrow):
        """Sets the cycle_tomorrow of this V1HosLogsSummaryResponseDrivers.

        The amount of cycle time (in ms) available tomorrow.  # noqa: E501

        :param cycle_tomorrow: The cycle_tomorrow of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: int
        """

        self._cycle_tomorrow = cycle_tomorrow

    @property
    def drive_ms_today(self):
        """Gets the drive_ms_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        The amount of driving time today (in ms).  # noqa: E501

        :return: The drive_ms_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: float
        """
        return self._drive_ms_today

    @drive_ms_today.setter
    def drive_ms_today(self, drive_ms_today):
        """Sets the drive_ms_today of this V1HosLogsSummaryResponseDrivers.

        The amount of driving time today (in ms).  # noqa: E501

        :param drive_ms_today: The drive_ms_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: float
        """

        self._drive_ms_today = drive_ms_today

    @property
    def driver_id(self):
        """Gets the driver_id of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        ID of the driver.  # noqa: E501

        :return: The driver_id of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: int
        """
        return self._driver_id

    @driver_id.setter
    def driver_id(self, driver_id):
        """Sets the driver_id of this V1HosLogsSummaryResponseDrivers.

        ID of the driver.  # noqa: E501

        :param driver_id: The driver_id of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: int
        """

        self._driver_id = driver_id

    @property
    def driver_name(self):
        """Gets the driver_name of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        Name of the driver.  # noqa: E501

        :return: The driver_name of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: str
        """
        return self._driver_name

    @driver_name.setter
    def driver_name(self, driver_name):
        """Sets the driver_name of this V1HosLogsSummaryResponseDrivers.

        Name of the driver.  # noqa: E501

        :param driver_name: The driver_name of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: str
        """

        self._driver_name = driver_name

    @property
    def driving_in_violation_cycle(self):
        """Gets the driving_in_violation_cycle of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        The amount of driving time in violation in this cycle (in ms).  # noqa: E501

        :return: The driving_in_violation_cycle of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: int
        """
        return self._driving_in_violation_cycle

    @driving_in_violation_cycle.setter
    def driving_in_violation_cycle(self, driving_in_violation_cycle):
        """Sets the driving_in_violation_cycle of this V1HosLogsSummaryResponseDrivers.

        The amount of driving time in violation in this cycle (in ms).  # noqa: E501

        :param driving_in_violation_cycle: The driving_in_violation_cycle of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: int
        """

        self._driving_in_violation_cycle = driving_in_violation_cycle

    @property
    def driving_in_violation_today(self):
        """Gets the driving_in_violation_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        The amount of driving time in violation today (in ms).  # noqa: E501

        :return: The driving_in_violation_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: int
        """
        return self._driving_in_violation_today

    @driving_in_violation_today.setter
    def driving_in_violation_today(self, driving_in_violation_today):
        """Sets the driving_in_violation_today of this V1HosLogsSummaryResponseDrivers.

        The amount of driving time in violation today (in ms).  # noqa: E501

        :param driving_in_violation_today: The driving_in_violation_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: int
        """

        self._driving_in_violation_today = driving_in_violation_today

    @property
    def on_duty_ms_today(self):
        """Gets the on_duty_ms_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        The amount of on duty time today (in ms).  # noqa: E501

        :return: The on_duty_ms_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: float
        """
        return self._on_duty_ms_today

    @on_duty_ms_today.setter
    def on_duty_ms_today(self, on_duty_ms_today):
        """Sets the on_duty_ms_today of this V1HosLogsSummaryResponseDrivers.

        The amount of on duty time today (in ms).  # noqa: E501

        :param on_duty_ms_today: The on_duty_ms_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: float
        """

        self._on_duty_ms_today = on_duty_ms_today

    @property
    def pending_drive_ms_today(self):
        """Gets the pending_drive_ms_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        The amount of driving time today for pending logs (in ms).  # noqa: E501

        :return: The pending_drive_ms_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: float
        """
        return self._pending_drive_ms_today

    @pending_drive_ms_today.setter
    def pending_drive_ms_today(self, pending_drive_ms_today):
        """Sets the pending_drive_ms_today of this V1HosLogsSummaryResponseDrivers.

        The amount of driving time today for pending logs (in ms).  # noqa: E501

        :param pending_drive_ms_today: The pending_drive_ms_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: float
        """

        self._pending_drive_ms_today = pending_drive_ms_today

    @property
    def pending_on_duty_ms_today(self):
        """Gets the pending_on_duty_ms_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        The amount of on duty time today for pending logs (in ms).  # noqa: E501

        :return: The pending_on_duty_ms_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: float
        """
        return self._pending_on_duty_ms_today

    @pending_on_duty_ms_today.setter
    def pending_on_duty_ms_today(self, pending_on_duty_ms_today):
        """Sets the pending_on_duty_ms_today of this V1HosLogsSummaryResponseDrivers.

        The amount of on duty time today for pending logs (in ms).  # noqa: E501

        :param pending_on_duty_ms_today: The pending_on_duty_ms_today of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: float
        """

        self._pending_on_duty_ms_today = pending_on_duty_ms_today

    @property
    def shift_drive_remaining(self):
        """Gets the shift_drive_remaining of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        The amount of remaining shift drive time (in ms).  # noqa: E501

        :return: The shift_drive_remaining of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: int
        """
        return self._shift_drive_remaining

    @shift_drive_remaining.setter
    def shift_drive_remaining(self, shift_drive_remaining):
        """Sets the shift_drive_remaining of this V1HosLogsSummaryResponseDrivers.

        The amount of remaining shift drive time (in ms).  # noqa: E501

        :param shift_drive_remaining: The shift_drive_remaining of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: int
        """

        self._shift_drive_remaining = shift_drive_remaining

    @property
    def shift_remaining(self):
        """Gets the shift_remaining of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        The amount of remaining shift time (in ms).  # noqa: E501

        :return: The shift_remaining of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: int
        """
        return self._shift_remaining

    @shift_remaining.setter
    def shift_remaining(self, shift_remaining):
        """Sets the shift_remaining of this V1HosLogsSummaryResponseDrivers.

        The amount of remaining shift time (in ms).  # noqa: E501

        :param shift_remaining: The shift_remaining of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: int
        """

        self._shift_remaining = shift_remaining

    @property
    def time_in_current_status(self):
        """Gets the time_in_current_status of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        The amount of time (in ms) that the driver has been in the current `dutyStatus`.  # noqa: E501

        :return: The time_in_current_status of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: int
        """
        return self._time_in_current_status

    @time_in_current_status.setter
    def time_in_current_status(self, time_in_current_status):
        """Sets the time_in_current_status of this V1HosLogsSummaryResponseDrivers.

        The amount of time (in ms) that the driver has been in the current `dutyStatus`.  # noqa: E501

        :param time_in_current_status: The time_in_current_status of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: int
        """

        self._time_in_current_status = time_in_current_status

    @property
    def time_until_break(self):
        """Gets the time_until_break of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        The amount of time (in ms) remaining until the driver cannot drive without a rest break.  # noqa: E501

        :return: The time_until_break of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: int
        """
        return self._time_until_break

    @time_until_break.setter
    def time_until_break(self, time_until_break):
        """Sets the time_until_break of this V1HosLogsSummaryResponseDrivers.

        The amount of time (in ms) remaining until the driver cannot drive without a rest break.  # noqa: E501

        :param time_until_break: The time_until_break of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: int
        """

        self._time_until_break = time_until_break

    @property
    def vehicle_name(self):
        """Gets the vehicle_name of this V1HosLogsSummaryResponseDrivers.  # noqa: E501

        Name of the vehicle.  # noqa: E501

        :return: The vehicle_name of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_name

    @vehicle_name.setter
    def vehicle_name(self, vehicle_name):
        """Sets the vehicle_name of this V1HosLogsSummaryResponseDrivers.

        Name of the vehicle.  # noqa: E501

        :param vehicle_name: The vehicle_name of this V1HosLogsSummaryResponseDrivers.  # noqa: E501
        :type: str
        """

        self._vehicle_name = vehicle_name

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
        if not isinstance(other, V1HosLogsSummaryResponseDrivers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1HosLogsSummaryResponseDrivers):
            return True

        return self.to_dict() != other.to_dict()
