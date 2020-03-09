# CreateDriverRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CarrierSettings** | Pointer to [**DriverCarrierSettings**](DriverCarrierSettings.md) |  | [optional] 
**EldAdverseWeatherExemptionEnabled** | Pointer to **bool** | Flag indicating this driver may use Adverse Weather exemptions in ELD logs. | [optional] [default to false]
**EldBigDayExemptionEnabled** | Pointer to **bool** | Flag indicating this driver may use Big Day exemption in ELD logs. | [optional] [default to false]
**EldDayStartHour** | Pointer to **int32** | &#x60;0&#x60; indicating midnight-to-midnight ELD driving hours, &#x60;12&#x60; to indicate noon-to-noon driving hours. | [optional] [default to 0]
**EldExempt** | Pointer to **bool** | Flag indicating this driver is exempt from the Electronic Logging Mandate. | [optional] [default to false]
**EldExemptReason** | Pointer to **string** | Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt). | [optional] 
**EldPcEnabled** | Pointer to **bool** | Flag indicating this driver may select the Personal Conveyance duty status in ELD logs. | [optional] [default to false]
**EldYmEnabled** | Pointer to **bool** | Flag indicating this driver may select the Personal Conveyance duty status in ELD logs. | [optional] [default to false]
**ExternalIds** | Pointer to **map[string]string** | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object. | [optional] 
**LicenseNumber** | Pointer to **string** | Driver&#39;s state issued license number. The combination of this number and &#x60;licenseState&#x60; must be unique. | [optional] 
**LicenseState** | Pointer to **string** | Abbreviation of state that issued driver&#39;s license. | [optional] 
**Locale** | Pointer to [**DriverLocale**](DriverLocale.md) |  | [optional] 
**Name** | Pointer to **string** | Driver&#39;s name. | 
**Notes** | Pointer to **string** | Notes about the driver. | [optional] 
**Password** | Pointer to **string** | Password that the driver can use to login to the Samsara driver app. | 
**Phone** | Pointer to **string** | Phone number of the driver. | [optional] 
**StaticAssignedVehicleId** | Pointer to **string** | ID of vehicle that the driver is permanently assigned to. (uncommon). | [optional] 
**TachographCardNumber** | Pointer to **string** | Driver&#39;s assigned tachograph card number (Europe specific) | [optional] 
**TagIds** | Pointer to **[]string** | IDs of tags the driver is associated with. | [optional] 
**Timezone** | Pointer to **string** | Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs. Driver timezones use [IANA timezone database](https://www.iana.org/time-zones) keys (e.g. &#x60;America/Los_Angeles&#x60;, &#x60;America/New_York&#x60;, &#x60;Europe/London&#x60;, etc.). You can find a mapping of common timezone formats to IANA timezone keys [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html). | [optional] [default to America/Los_Angeles]
**Username** | Pointer to **string** | Driver&#39;s login username into the driver app. The username may not contain spaces or the &#39;@&#39; symbol. The username must be unique. | 
**VehicleGroupTagId** | Pointer to **string** | Tag ID which determines which vehicles a driver will see when selecting vehicles. | [optional] 

## Methods

### GetCarrierSettings

`func (o *CreateDriverRequest) GetCarrierSettings() DriverCarrierSettings`

GetCarrierSettings returns the CarrierSettings field if non-nil, zero value otherwise.

### GetCarrierSettingsOk

`func (o *CreateDriverRequest) GetCarrierSettingsOk() (DriverCarrierSettings, bool)`

GetCarrierSettingsOk returns a tuple with the CarrierSettings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCarrierSettings

`func (o *CreateDriverRequest) HasCarrierSettings() bool`

HasCarrierSettings returns a boolean if a field has been set.

### SetCarrierSettings

`func (o *CreateDriverRequest) SetCarrierSettings(v DriverCarrierSettings)`

SetCarrierSettings gets a reference to the given DriverCarrierSettings and assigns it to the CarrierSettings field.

### GetEldAdverseWeatherExemptionEnabled

`func (o *CreateDriverRequest) GetEldAdverseWeatherExemptionEnabled() bool`

GetEldAdverseWeatherExemptionEnabled returns the EldAdverseWeatherExemptionEnabled field if non-nil, zero value otherwise.

### GetEldAdverseWeatherExemptionEnabledOk

`func (o *CreateDriverRequest) GetEldAdverseWeatherExemptionEnabledOk() (bool, bool)`

GetEldAdverseWeatherExemptionEnabledOk returns a tuple with the EldAdverseWeatherExemptionEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldAdverseWeatherExemptionEnabled

`func (o *CreateDriverRequest) HasEldAdverseWeatherExemptionEnabled() bool`

HasEldAdverseWeatherExemptionEnabled returns a boolean if a field has been set.

### SetEldAdverseWeatherExemptionEnabled

`func (o *CreateDriverRequest) SetEldAdverseWeatherExemptionEnabled(v bool)`

SetEldAdverseWeatherExemptionEnabled gets a reference to the given bool and assigns it to the EldAdverseWeatherExemptionEnabled field.

### GetEldBigDayExemptionEnabled

`func (o *CreateDriverRequest) GetEldBigDayExemptionEnabled() bool`

GetEldBigDayExemptionEnabled returns the EldBigDayExemptionEnabled field if non-nil, zero value otherwise.

### GetEldBigDayExemptionEnabledOk

`func (o *CreateDriverRequest) GetEldBigDayExemptionEnabledOk() (bool, bool)`

GetEldBigDayExemptionEnabledOk returns a tuple with the EldBigDayExemptionEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldBigDayExemptionEnabled

`func (o *CreateDriverRequest) HasEldBigDayExemptionEnabled() bool`

HasEldBigDayExemptionEnabled returns a boolean if a field has been set.

### SetEldBigDayExemptionEnabled

`func (o *CreateDriverRequest) SetEldBigDayExemptionEnabled(v bool)`

SetEldBigDayExemptionEnabled gets a reference to the given bool and assigns it to the EldBigDayExemptionEnabled field.

### GetEldDayStartHour

`func (o *CreateDriverRequest) GetEldDayStartHour() int32`

GetEldDayStartHour returns the EldDayStartHour field if non-nil, zero value otherwise.

### GetEldDayStartHourOk

`func (o *CreateDriverRequest) GetEldDayStartHourOk() (int32, bool)`

GetEldDayStartHourOk returns a tuple with the EldDayStartHour field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldDayStartHour

`func (o *CreateDriverRequest) HasEldDayStartHour() bool`

HasEldDayStartHour returns a boolean if a field has been set.

### SetEldDayStartHour

`func (o *CreateDriverRequest) SetEldDayStartHour(v int32)`

SetEldDayStartHour gets a reference to the given int32 and assigns it to the EldDayStartHour field.

### GetEldExempt

`func (o *CreateDriverRequest) GetEldExempt() bool`

GetEldExempt returns the EldExempt field if non-nil, zero value otherwise.

### GetEldExemptOk

`func (o *CreateDriverRequest) GetEldExemptOk() (bool, bool)`

GetEldExemptOk returns a tuple with the EldExempt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldExempt

`func (o *CreateDriverRequest) HasEldExempt() bool`

HasEldExempt returns a boolean if a field has been set.

### SetEldExempt

`func (o *CreateDriverRequest) SetEldExempt(v bool)`

SetEldExempt gets a reference to the given bool and assigns it to the EldExempt field.

### GetEldExemptReason

`func (o *CreateDriverRequest) GetEldExemptReason() string`

GetEldExemptReason returns the EldExemptReason field if non-nil, zero value otherwise.

### GetEldExemptReasonOk

`func (o *CreateDriverRequest) GetEldExemptReasonOk() (string, bool)`

GetEldExemptReasonOk returns a tuple with the EldExemptReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldExemptReason

`func (o *CreateDriverRequest) HasEldExemptReason() bool`

HasEldExemptReason returns a boolean if a field has been set.

### SetEldExemptReason

`func (o *CreateDriverRequest) SetEldExemptReason(v string)`

SetEldExemptReason gets a reference to the given string and assigns it to the EldExemptReason field.

### GetEldPcEnabled

`func (o *CreateDriverRequest) GetEldPcEnabled() bool`

GetEldPcEnabled returns the EldPcEnabled field if non-nil, zero value otherwise.

### GetEldPcEnabledOk

`func (o *CreateDriverRequest) GetEldPcEnabledOk() (bool, bool)`

GetEldPcEnabledOk returns a tuple with the EldPcEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldPcEnabled

`func (o *CreateDriverRequest) HasEldPcEnabled() bool`

HasEldPcEnabled returns a boolean if a field has been set.

### SetEldPcEnabled

`func (o *CreateDriverRequest) SetEldPcEnabled(v bool)`

SetEldPcEnabled gets a reference to the given bool and assigns it to the EldPcEnabled field.

### GetEldYmEnabled

`func (o *CreateDriverRequest) GetEldYmEnabled() bool`

GetEldYmEnabled returns the EldYmEnabled field if non-nil, zero value otherwise.

### GetEldYmEnabledOk

`func (o *CreateDriverRequest) GetEldYmEnabledOk() (bool, bool)`

GetEldYmEnabledOk returns a tuple with the EldYmEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldYmEnabled

`func (o *CreateDriverRequest) HasEldYmEnabled() bool`

HasEldYmEnabled returns a boolean if a field has been set.

### SetEldYmEnabled

`func (o *CreateDriverRequest) SetEldYmEnabled(v bool)`

SetEldYmEnabled gets a reference to the given bool and assigns it to the EldYmEnabled field.

### GetExternalIds

`func (o *CreateDriverRequest) GetExternalIds() map[string]string`

GetExternalIds returns the ExternalIds field if non-nil, zero value otherwise.

### GetExternalIdsOk

`func (o *CreateDriverRequest) GetExternalIdsOk() (map[string]string, bool)`

GetExternalIdsOk returns a tuple with the ExternalIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasExternalIds

`func (o *CreateDriverRequest) HasExternalIds() bool`

HasExternalIds returns a boolean if a field has been set.

### SetExternalIds

`func (o *CreateDriverRequest) SetExternalIds(v map[string]string)`

SetExternalIds gets a reference to the given map[string]string and assigns it to the ExternalIds field.

### GetLicenseNumber

`func (o *CreateDriverRequest) GetLicenseNumber() string`

GetLicenseNumber returns the LicenseNumber field if non-nil, zero value otherwise.

### GetLicenseNumberOk

`func (o *CreateDriverRequest) GetLicenseNumberOk() (string, bool)`

GetLicenseNumberOk returns a tuple with the LicenseNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLicenseNumber

`func (o *CreateDriverRequest) HasLicenseNumber() bool`

HasLicenseNumber returns a boolean if a field has been set.

### SetLicenseNumber

`func (o *CreateDriverRequest) SetLicenseNumber(v string)`

SetLicenseNumber gets a reference to the given string and assigns it to the LicenseNumber field.

### GetLicenseState

`func (o *CreateDriverRequest) GetLicenseState() string`

GetLicenseState returns the LicenseState field if non-nil, zero value otherwise.

### GetLicenseStateOk

`func (o *CreateDriverRequest) GetLicenseStateOk() (string, bool)`

GetLicenseStateOk returns a tuple with the LicenseState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLicenseState

`func (o *CreateDriverRequest) HasLicenseState() bool`

HasLicenseState returns a boolean if a field has been set.

### SetLicenseState

`func (o *CreateDriverRequest) SetLicenseState(v string)`

SetLicenseState gets a reference to the given string and assigns it to the LicenseState field.

### GetLocale

`func (o *CreateDriverRequest) GetLocale() DriverLocale`

GetLocale returns the Locale field if non-nil, zero value otherwise.

### GetLocaleOk

`func (o *CreateDriverRequest) GetLocaleOk() (DriverLocale, bool)`

GetLocaleOk returns a tuple with the Locale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocale

`func (o *CreateDriverRequest) HasLocale() bool`

HasLocale returns a boolean if a field has been set.

### SetLocale

`func (o *CreateDriverRequest) SetLocale(v DriverLocale)`

SetLocale gets a reference to the given DriverLocale and assigns it to the Locale field.

### GetName

`func (o *CreateDriverRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateDriverRequest) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *CreateDriverRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *CreateDriverRequest) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetNotes

`func (o *CreateDriverRequest) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *CreateDriverRequest) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *CreateDriverRequest) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *CreateDriverRequest) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetPassword

`func (o *CreateDriverRequest) GetPassword() string`

GetPassword returns the Password field if non-nil, zero value otherwise.

### GetPasswordOk

`func (o *CreateDriverRequest) GetPasswordOk() (string, bool)`

GetPasswordOk returns a tuple with the Password field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPassword

`func (o *CreateDriverRequest) HasPassword() bool`

HasPassword returns a boolean if a field has been set.

### SetPassword

`func (o *CreateDriverRequest) SetPassword(v string)`

SetPassword gets a reference to the given string and assigns it to the Password field.

### GetPhone

`func (o *CreateDriverRequest) GetPhone() string`

GetPhone returns the Phone field if non-nil, zero value otherwise.

### GetPhoneOk

`func (o *CreateDriverRequest) GetPhoneOk() (string, bool)`

GetPhoneOk returns a tuple with the Phone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPhone

`func (o *CreateDriverRequest) HasPhone() bool`

HasPhone returns a boolean if a field has been set.

### SetPhone

`func (o *CreateDriverRequest) SetPhone(v string)`

SetPhone gets a reference to the given string and assigns it to the Phone field.

### GetStaticAssignedVehicleId

`func (o *CreateDriverRequest) GetStaticAssignedVehicleId() string`

GetStaticAssignedVehicleId returns the StaticAssignedVehicleId field if non-nil, zero value otherwise.

### GetStaticAssignedVehicleIdOk

`func (o *CreateDriverRequest) GetStaticAssignedVehicleIdOk() (string, bool)`

GetStaticAssignedVehicleIdOk returns a tuple with the StaticAssignedVehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStaticAssignedVehicleId

`func (o *CreateDriverRequest) HasStaticAssignedVehicleId() bool`

HasStaticAssignedVehicleId returns a boolean if a field has been set.

### SetStaticAssignedVehicleId

`func (o *CreateDriverRequest) SetStaticAssignedVehicleId(v string)`

SetStaticAssignedVehicleId gets a reference to the given string and assigns it to the StaticAssignedVehicleId field.

### GetTachographCardNumber

`func (o *CreateDriverRequest) GetTachographCardNumber() string`

GetTachographCardNumber returns the TachographCardNumber field if non-nil, zero value otherwise.

### GetTachographCardNumberOk

`func (o *CreateDriverRequest) GetTachographCardNumberOk() (string, bool)`

GetTachographCardNumberOk returns a tuple with the TachographCardNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTachographCardNumber

`func (o *CreateDriverRequest) HasTachographCardNumber() bool`

HasTachographCardNumber returns a boolean if a field has been set.

### SetTachographCardNumber

`func (o *CreateDriverRequest) SetTachographCardNumber(v string)`

SetTachographCardNumber gets a reference to the given string and assigns it to the TachographCardNumber field.

### GetTagIds

`func (o *CreateDriverRequest) GetTagIds() []string`

GetTagIds returns the TagIds field if non-nil, zero value otherwise.

### GetTagIdsOk

`func (o *CreateDriverRequest) GetTagIdsOk() ([]string, bool)`

GetTagIdsOk returns a tuple with the TagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTagIds

`func (o *CreateDriverRequest) HasTagIds() bool`

HasTagIds returns a boolean if a field has been set.

### SetTagIds

`func (o *CreateDriverRequest) SetTagIds(v []string)`

SetTagIds gets a reference to the given []string and assigns it to the TagIds field.

### GetTimezone

`func (o *CreateDriverRequest) GetTimezone() string`

GetTimezone returns the Timezone field if non-nil, zero value otherwise.

### GetTimezoneOk

`func (o *CreateDriverRequest) GetTimezoneOk() (string, bool)`

GetTimezoneOk returns a tuple with the Timezone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTimezone

`func (o *CreateDriverRequest) HasTimezone() bool`

HasTimezone returns a boolean if a field has been set.

### SetTimezone

`func (o *CreateDriverRequest) SetTimezone(v string)`

SetTimezone gets a reference to the given string and assigns it to the Timezone field.

### GetUsername

`func (o *CreateDriverRequest) GetUsername() string`

GetUsername returns the Username field if non-nil, zero value otherwise.

### GetUsernameOk

`func (o *CreateDriverRequest) GetUsernameOk() (string, bool)`

GetUsernameOk returns a tuple with the Username field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasUsername

`func (o *CreateDriverRequest) HasUsername() bool`

HasUsername returns a boolean if a field has been set.

### SetUsername

`func (o *CreateDriverRequest) SetUsername(v string)`

SetUsername gets a reference to the given string and assigns it to the Username field.

### GetVehicleGroupTagId

`func (o *CreateDriverRequest) GetVehicleGroupTagId() string`

GetVehicleGroupTagId returns the VehicleGroupTagId field if non-nil, zero value otherwise.

### GetVehicleGroupTagIdOk

`func (o *CreateDriverRequest) GetVehicleGroupTagIdOk() (string, bool)`

GetVehicleGroupTagIdOk returns a tuple with the VehicleGroupTagId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleGroupTagId

`func (o *CreateDriverRequest) HasVehicleGroupTagId() bool`

HasVehicleGroupTagId returns a boolean if a field has been set.

### SetVehicleGroupTagId

`func (o *CreateDriverRequest) SetVehicleGroupTagId(v string)`

SetVehicleGroupTagId gets a reference to the given string and assigns it to the VehicleGroupTagId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


