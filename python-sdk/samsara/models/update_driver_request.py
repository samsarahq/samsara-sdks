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


class UpdateDriverRequest(object):
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
        'carrier_settings': 'DriverCarrierSettings',
        'eld_adverse_weather_exemption_enabled': 'bool',
        'eld_big_day_exemption_enabled': 'bool',
        'eld_day_start_hour': 'int',
        'eld_exempt': 'bool',
        'eld_exempt_reason': 'str',
        'eld_pc_enabled': 'bool',
        'eld_ym_enabled': 'bool',
        'external_ids': 'dict(str, str)',
        'license_number': 'str',
        'license_state': 'str',
        'locale': 'DriverLocale',
        'name': 'str',
        'notes': 'str',
        'password': 'str',
        'phone': 'str',
        'static_assigned_vehicle_id': 'str',
        'tachograph_card_number': 'str',
        'tag_ids': 'list[str]',
        'timezone': 'str',
        'username': 'str',
        'vehicle_group_tag_id': 'str'
    }

    attribute_map = {
        'carrier_settings': 'carrierSettings',
        'eld_adverse_weather_exemption_enabled': 'eldAdverseWeatherExemptionEnabled',
        'eld_big_day_exemption_enabled': 'eldBigDayExemptionEnabled',
        'eld_day_start_hour': 'eldDayStartHour',
        'eld_exempt': 'eldExempt',
        'eld_exempt_reason': 'eldExemptReason',
        'eld_pc_enabled': 'eldPcEnabled',
        'eld_ym_enabled': 'eldYmEnabled',
        'external_ids': 'externalIds',
        'license_number': 'licenseNumber',
        'license_state': 'licenseState',
        'locale': 'locale',
        'name': 'name',
        'notes': 'notes',
        'password': 'password',
        'phone': 'phone',
        'static_assigned_vehicle_id': 'staticAssignedVehicleId',
        'tachograph_card_number': 'tachographCardNumber',
        'tag_ids': 'tagIds',
        'timezone': 'timezone',
        'username': 'username',
        'vehicle_group_tag_id': 'vehicleGroupTagId'
    }

    def __init__(self, carrier_settings=None, eld_adverse_weather_exemption_enabled=False, eld_big_day_exemption_enabled=False, eld_day_start_hour=0, eld_exempt=False, eld_exempt_reason=None, eld_pc_enabled=False, eld_ym_enabled=False, external_ids=None, license_number=None, license_state=None, locale=None, name=None, notes=None, password=None, phone=None, static_assigned_vehicle_id=None, tachograph_card_number=None, tag_ids=None, timezone='America/Los_Angeles', username=None, vehicle_group_tag_id=None, local_vars_configuration=None):  # noqa: E501
        """UpdateDriverRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._carrier_settings = None
        self._eld_adverse_weather_exemption_enabled = None
        self._eld_big_day_exemption_enabled = None
        self._eld_day_start_hour = None
        self._eld_exempt = None
        self._eld_exempt_reason = None
        self._eld_pc_enabled = None
        self._eld_ym_enabled = None
        self._external_ids = None
        self._license_number = None
        self._license_state = None
        self._locale = None
        self._name = None
        self._notes = None
        self._password = None
        self._phone = None
        self._static_assigned_vehicle_id = None
        self._tachograph_card_number = None
        self._tag_ids = None
        self._timezone = None
        self._username = None
        self._vehicle_group_tag_id = None
        self.discriminator = None

        if carrier_settings is not None:
            self.carrier_settings = carrier_settings
        if eld_adverse_weather_exemption_enabled is not None:
            self.eld_adverse_weather_exemption_enabled = eld_adverse_weather_exemption_enabled
        if eld_big_day_exemption_enabled is not None:
            self.eld_big_day_exemption_enabled = eld_big_day_exemption_enabled
        if eld_day_start_hour is not None:
            self.eld_day_start_hour = eld_day_start_hour
        if eld_exempt is not None:
            self.eld_exempt = eld_exempt
        if eld_exempt_reason is not None:
            self.eld_exempt_reason = eld_exempt_reason
        if eld_pc_enabled is not None:
            self.eld_pc_enabled = eld_pc_enabled
        if eld_ym_enabled is not None:
            self.eld_ym_enabled = eld_ym_enabled
        if external_ids is not None:
            self.external_ids = external_ids
        if license_number is not None:
            self.license_number = license_number
        if license_state is not None:
            self.license_state = license_state
        if locale is not None:
            self.locale = locale
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if password is not None:
            self.password = password
        if phone is not None:
            self.phone = phone
        if static_assigned_vehicle_id is not None:
            self.static_assigned_vehicle_id = static_assigned_vehicle_id
        if tachograph_card_number is not None:
            self.tachograph_card_number = tachograph_card_number
        if tag_ids is not None:
            self.tag_ids = tag_ids
        if timezone is not None:
            self.timezone = timezone
        if username is not None:
            self.username = username
        if vehicle_group_tag_id is not None:
            self.vehicle_group_tag_id = vehicle_group_tag_id

    @property
    def carrier_settings(self):
        """Gets the carrier_settings of this UpdateDriverRequest.  # noqa: E501


        :return: The carrier_settings of this UpdateDriverRequest.  # noqa: E501
        :rtype: DriverCarrierSettings
        """
        return self._carrier_settings

    @carrier_settings.setter
    def carrier_settings(self, carrier_settings):
        """Sets the carrier_settings of this UpdateDriverRequest.


        :param carrier_settings: The carrier_settings of this UpdateDriverRequest.  # noqa: E501
        :type: DriverCarrierSettings
        """

        self._carrier_settings = carrier_settings

    @property
    def eld_adverse_weather_exemption_enabled(self):
        """Gets the eld_adverse_weather_exemption_enabled of this UpdateDriverRequest.  # noqa: E501

        Flag indicating this driver may use Adverse Weather exemptions in ELD logs.  # noqa: E501

        :return: The eld_adverse_weather_exemption_enabled of this UpdateDriverRequest.  # noqa: E501
        :rtype: bool
        """
        return self._eld_adverse_weather_exemption_enabled

    @eld_adverse_weather_exemption_enabled.setter
    def eld_adverse_weather_exemption_enabled(self, eld_adverse_weather_exemption_enabled):
        """Sets the eld_adverse_weather_exemption_enabled of this UpdateDriverRequest.

        Flag indicating this driver may use Adverse Weather exemptions in ELD logs.  # noqa: E501

        :param eld_adverse_weather_exemption_enabled: The eld_adverse_weather_exemption_enabled of this UpdateDriverRequest.  # noqa: E501
        :type: bool
        """

        self._eld_adverse_weather_exemption_enabled = eld_adverse_weather_exemption_enabled

    @property
    def eld_big_day_exemption_enabled(self):
        """Gets the eld_big_day_exemption_enabled of this UpdateDriverRequest.  # noqa: E501

        Flag indicating this driver may use Big Day exemption in ELD logs.  # noqa: E501

        :return: The eld_big_day_exemption_enabled of this UpdateDriverRequest.  # noqa: E501
        :rtype: bool
        """
        return self._eld_big_day_exemption_enabled

    @eld_big_day_exemption_enabled.setter
    def eld_big_day_exemption_enabled(self, eld_big_day_exemption_enabled):
        """Sets the eld_big_day_exemption_enabled of this UpdateDriverRequest.

        Flag indicating this driver may use Big Day exemption in ELD logs.  # noqa: E501

        :param eld_big_day_exemption_enabled: The eld_big_day_exemption_enabled of this UpdateDriverRequest.  # noqa: E501
        :type: bool
        """

        self._eld_big_day_exemption_enabled = eld_big_day_exemption_enabled

    @property
    def eld_day_start_hour(self):
        """Gets the eld_day_start_hour of this UpdateDriverRequest.  # noqa: E501

        `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate noon-to-noon driving hours.  # noqa: E501

        :return: The eld_day_start_hour of this UpdateDriverRequest.  # noqa: E501
        :rtype: int
        """
        return self._eld_day_start_hour

    @eld_day_start_hour.setter
    def eld_day_start_hour(self, eld_day_start_hour):
        """Sets the eld_day_start_hour of this UpdateDriverRequest.

        `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate noon-to-noon driving hours.  # noqa: E501

        :param eld_day_start_hour: The eld_day_start_hour of this UpdateDriverRequest.  # noqa: E501
        :type: int
        """

        self._eld_day_start_hour = eld_day_start_hour

    @property
    def eld_exempt(self):
        """Gets the eld_exempt of this UpdateDriverRequest.  # noqa: E501

        Flag indicating this driver is exempt from the Electronic Logging Mandate.  # noqa: E501

        :return: The eld_exempt of this UpdateDriverRequest.  # noqa: E501
        :rtype: bool
        """
        return self._eld_exempt

    @eld_exempt.setter
    def eld_exempt(self, eld_exempt):
        """Sets the eld_exempt of this UpdateDriverRequest.

        Flag indicating this driver is exempt from the Electronic Logging Mandate.  # noqa: E501

        :param eld_exempt: The eld_exempt of this UpdateDriverRequest.  # noqa: E501
        :type: bool
        """

        self._eld_exempt = eld_exempt

    @property
    def eld_exempt_reason(self):
        """Gets the eld_exempt_reason of this UpdateDriverRequest.  # noqa: E501

        Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt).  # noqa: E501

        :return: The eld_exempt_reason of this UpdateDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._eld_exempt_reason

    @eld_exempt_reason.setter
    def eld_exempt_reason(self, eld_exempt_reason):
        """Sets the eld_exempt_reason of this UpdateDriverRequest.

        Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt).  # noqa: E501

        :param eld_exempt_reason: The eld_exempt_reason of this UpdateDriverRequest.  # noqa: E501
        :type: str
        """

        self._eld_exempt_reason = eld_exempt_reason

    @property
    def eld_pc_enabled(self):
        """Gets the eld_pc_enabled of this UpdateDriverRequest.  # noqa: E501

        Flag indicating this driver may select the Personal Conveyance duty status in ELD logs.  # noqa: E501

        :return: The eld_pc_enabled of this UpdateDriverRequest.  # noqa: E501
        :rtype: bool
        """
        return self._eld_pc_enabled

    @eld_pc_enabled.setter
    def eld_pc_enabled(self, eld_pc_enabled):
        """Sets the eld_pc_enabled of this UpdateDriverRequest.

        Flag indicating this driver may select the Personal Conveyance duty status in ELD logs.  # noqa: E501

        :param eld_pc_enabled: The eld_pc_enabled of this UpdateDriverRequest.  # noqa: E501
        :type: bool
        """

        self._eld_pc_enabled = eld_pc_enabled

    @property
    def eld_ym_enabled(self):
        """Gets the eld_ym_enabled of this UpdateDriverRequest.  # noqa: E501

        Flag indicating this driver may select the Yard Move duty status in ELD logs.  # noqa: E501

        :return: The eld_ym_enabled of this UpdateDriverRequest.  # noqa: E501
        :rtype: bool
        """
        return self._eld_ym_enabled

    @eld_ym_enabled.setter
    def eld_ym_enabled(self, eld_ym_enabled):
        """Sets the eld_ym_enabled of this UpdateDriverRequest.

        Flag indicating this driver may select the Yard Move duty status in ELD logs.  # noqa: E501

        :param eld_ym_enabled: The eld_ym_enabled of this UpdateDriverRequest.  # noqa: E501
        :type: bool
        """

        self._eld_ym_enabled = eld_ym_enabled

    @property
    def external_ids(self):
        """Gets the external_ids of this UpdateDriverRequest.  # noqa: E501

        The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.  # noqa: E501

        :return: The external_ids of this UpdateDriverRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this UpdateDriverRequest.

        The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.  # noqa: E501

        :param external_ids: The external_ids of this UpdateDriverRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._external_ids = external_ids

    @property
    def license_number(self):
        """Gets the license_number of this UpdateDriverRequest.  # noqa: E501

        Driver's state issued license number. The combination of this number and `licenseState` must be unique.  # noqa: E501

        :return: The license_number of this UpdateDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._license_number

    @license_number.setter
    def license_number(self, license_number):
        """Sets the license_number of this UpdateDriverRequest.

        Driver's state issued license number. The combination of this number and `licenseState` must be unique.  # noqa: E501

        :param license_number: The license_number of this UpdateDriverRequest.  # noqa: E501
        :type: str
        """

        self._license_number = license_number

    @property
    def license_state(self):
        """Gets the license_state of this UpdateDriverRequest.  # noqa: E501

        Abbreviation of state that issued driver's license.  # noqa: E501

        :return: The license_state of this UpdateDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._license_state

    @license_state.setter
    def license_state(self, license_state):
        """Sets the license_state of this UpdateDriverRequest.

        Abbreviation of state that issued driver's license.  # noqa: E501

        :param license_state: The license_state of this UpdateDriverRequest.  # noqa: E501
        :type: str
        """

        self._license_state = license_state

    @property
    def locale(self):
        """Gets the locale of this UpdateDriverRequest.  # noqa: E501


        :return: The locale of this UpdateDriverRequest.  # noqa: E501
        :rtype: DriverLocale
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this UpdateDriverRequest.


        :param locale: The locale of this UpdateDriverRequest.  # noqa: E501
        :type: DriverLocale
        """

        self._locale = locale

    @property
    def name(self):
        """Gets the name of this UpdateDriverRequest.  # noqa: E501

        Driver's name.  # noqa: E501

        :return: The name of this UpdateDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateDriverRequest.

        Driver's name.  # noqa: E501

        :param name: The name of this UpdateDriverRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this UpdateDriverRequest.  # noqa: E501

        Notes about the driver.  # noqa: E501

        :return: The notes of this UpdateDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this UpdateDriverRequest.

        Notes about the driver.  # noqa: E501

        :param notes: The notes of this UpdateDriverRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                notes is not None and len(notes) > 4096):
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `4096`")  # noqa: E501

        self._notes = notes

    @property
    def password(self):
        """Gets the password of this UpdateDriverRequest.  # noqa: E501

        Password that the driver can use to login to the Samsara driver app.  # noqa: E501

        :return: The password of this UpdateDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateDriverRequest.

        Password that the driver can use to login to the Samsara driver app.  # noqa: E501

        :param password: The password of this UpdateDriverRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def phone(self):
        """Gets the phone of this UpdateDriverRequest.  # noqa: E501

        Phone number of the driver.  # noqa: E501

        :return: The phone of this UpdateDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UpdateDriverRequest.

        Phone number of the driver.  # noqa: E501

        :param phone: The phone of this UpdateDriverRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                phone is not None and len(phone) > 255):
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `255`")  # noqa: E501

        self._phone = phone

    @property
    def static_assigned_vehicle_id(self):
        """Gets the static_assigned_vehicle_id of this UpdateDriverRequest.  # noqa: E501

        ID of vehicle that the driver is permanently assigned to. (uncommon).  # noqa: E501

        :return: The static_assigned_vehicle_id of this UpdateDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._static_assigned_vehicle_id

    @static_assigned_vehicle_id.setter
    def static_assigned_vehicle_id(self, static_assigned_vehicle_id):
        """Sets the static_assigned_vehicle_id of this UpdateDriverRequest.

        ID of vehicle that the driver is permanently assigned to. (uncommon).  # noqa: E501

        :param static_assigned_vehicle_id: The static_assigned_vehicle_id of this UpdateDriverRequest.  # noqa: E501
        :type: str
        """

        self._static_assigned_vehicle_id = static_assigned_vehicle_id

    @property
    def tachograph_card_number(self):
        """Gets the tachograph_card_number of this UpdateDriverRequest.  # noqa: E501

        Driver's assigned tachograph card number (Europe specific)  # noqa: E501

        :return: The tachograph_card_number of this UpdateDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._tachograph_card_number

    @tachograph_card_number.setter
    def tachograph_card_number(self, tachograph_card_number):
        """Sets the tachograph_card_number of this UpdateDriverRequest.

        Driver's assigned tachograph card number (Europe specific)  # noqa: E501

        :param tachograph_card_number: The tachograph_card_number of this UpdateDriverRequest.  # noqa: E501
        :type: str
        """

        self._tachograph_card_number = tachograph_card_number

    @property
    def tag_ids(self):
        """Gets the tag_ids of this UpdateDriverRequest.  # noqa: E501

        IDs of tags the driver is associated with.  # noqa: E501

        :return: The tag_ids of this UpdateDriverRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this UpdateDriverRequest.

        IDs of tags the driver is associated with.  # noqa: E501

        :param tag_ids: The tag_ids of this UpdateDriverRequest.  # noqa: E501
        :type: list[str]
        """

        self._tag_ids = tag_ids

    @property
    def timezone(self):
        """Gets the timezone of this UpdateDriverRequest.  # noqa: E501

        Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs. Driver timezones use [IANA timezone database](https://www.iana.org/time-zones) keys (e.g. `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find a mapping of common timezone formats to IANA timezone keys [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).  # noqa: E501

        :return: The timezone of this UpdateDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this UpdateDriverRequest.

        Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs. Driver timezones use [IANA timezone database](https://www.iana.org/time-zones) keys (e.g. `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find a mapping of common timezone formats to IANA timezone keys [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).  # noqa: E501

        :param timezone: The timezone of this UpdateDriverRequest.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def username(self):
        """Gets the username of this UpdateDriverRequest.  # noqa: E501

        Driver's login username into the driver app. The username may not contain spaces or the '@' symbol. The username must be unique.  # noqa: E501

        :return: The username of this UpdateDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UpdateDriverRequest.

        Driver's login username into the driver app. The username may not contain spaces or the '@' symbol. The username must be unique.  # noqa: E501

        :param username: The username of this UpdateDriverRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) > 189):
            raise ValueError("Invalid value for `username`, length must be less than or equal to `189`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) < 1):
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

    @property
    def vehicle_group_tag_id(self):
        """Gets the vehicle_group_tag_id of this UpdateDriverRequest.  # noqa: E501

        Tag ID which determines which vehicles a driver will see when selecting vehicles.  # noqa: E501

        :return: The vehicle_group_tag_id of this UpdateDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_group_tag_id

    @vehicle_group_tag_id.setter
    def vehicle_group_tag_id(self, vehicle_group_tag_id):
        """Sets the vehicle_group_tag_id of this UpdateDriverRequest.

        Tag ID which determines which vehicles a driver will see when selecting vehicles.  # noqa: E501

        :param vehicle_group_tag_id: The vehicle_group_tag_id of this UpdateDriverRequest.  # noqa: E501
        :type: str
        """

        self._vehicle_group_tag_id = vehicle_group_tag_id

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
        if not isinstance(other, UpdateDriverRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateDriverRequest):
            return True

        return self.to_dict() != other.to_dict()
