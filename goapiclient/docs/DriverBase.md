# DriverBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CarrierSettings** | Pointer to [**DriverBaseCarrierSettings**](DriverBase_carrierSettings.md) |  | [optional] 
**EldAdverseWeatherExemptionEnabled** | Pointer to **bool** | Flag indicating this driver may use Adverse Weather exemptions in ELD logs. | [optional] 
**EldBigDayExemptionEnabled** | Pointer to **bool** | Flag indicating this driver may use Big Day exemption in ELD logs. | [optional] 
**EldDayStartHour** | Pointer to **int32** | &#x60;0&#x60; indicating midnight-to-midnight ELD driving hours, &#x60;12&#x60; to indicate noon-to-noon driving hours. | [optional] 
**EldExempt** | Pointer to **bool** | Flag indicating this driver is exempt from the Electronic Logging Mandate. | [optional] 
**EldExemptReason** | Pointer to **string** | Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt). | [optional] 
**EldPcEnabled** | Pointer to **bool** | Flag indicating this driver may select the Personal Conveyance duty status in ELD logs. | [optional] [default to false]
**EldYmEnabled** | Pointer to **bool** | Flag indicating this driver may select the Yard Move duty status in ELD logs. | [optional] [default to false]
**ExternalIds** | Pointer to **map[string]string** | User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (&#x60;\&quot;\&quot;&#x60;). An external ID can be used as a path parameter to retrieve or update that resource. | [optional] 
**IsDeactivated** | Pointer to **bool** | A boolean that indicates whether or not this driver is deactivated. | [optional] 
**LicenseNumber** | Pointer to **string** | Driver&#39;s state issued license number. The combination of this number and &#x60;licenseState&#x60; must be unique. | [optional] 
**LicenseState** | Pointer to **string** | Abbreviation of state that issued driver&#39;s license. | [optional] 
**Locale** | Pointer to **string** | Locale override (uncommon). | [optional] 
**Name** | Pointer to **string** | Driver&#39;s name. | [optional] 
**Notes** | Pointer to **string** | Notes about the driver. | [optional] 
**Phone** | Pointer to **string** | Driver&#39;s phone number. | [optional] 
**TachographCardNumber** | Pointer to **string** | Driver&#39;s assigned tachograph card number (Europe specific) | [optional] 
**Timezone** | Pointer to **string** | Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs. | [optional] 
**Username** | Pointer to **string** | Driver&#39;s login username into the driver app. The username may not contain spaces or the &#39;@&#39; symbol. The username must be unique. | [optional] 

## Methods

### GetCarrierSettings

`func (o *DriverBase) GetCarrierSettings() DriverBaseCarrierSettings`

GetCarrierSettings returns the CarrierSettings field if non-nil, zero value otherwise.

### GetCarrierSettingsOk

`func (o *DriverBase) GetCarrierSettingsOk() (DriverBaseCarrierSettings, bool)`

GetCarrierSettingsOk returns a tuple with the CarrierSettings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCarrierSettings

`func (o *DriverBase) HasCarrierSettings() bool`

HasCarrierSettings returns a boolean if a field has been set.

### SetCarrierSettings

`func (o *DriverBase) SetCarrierSettings(v DriverBaseCarrierSettings)`

SetCarrierSettings gets a reference to the given DriverBaseCarrierSettings and assigns it to the CarrierSettings field.

### GetEldAdverseWeatherExemptionEnabled

`func (o *DriverBase) GetEldAdverseWeatherExemptionEnabled() bool`

GetEldAdverseWeatherExemptionEnabled returns the EldAdverseWeatherExemptionEnabled field if non-nil, zero value otherwise.

### GetEldAdverseWeatherExemptionEnabledOk

`func (o *DriverBase) GetEldAdverseWeatherExemptionEnabledOk() (bool, bool)`

GetEldAdverseWeatherExemptionEnabledOk returns a tuple with the EldAdverseWeatherExemptionEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldAdverseWeatherExemptionEnabled

`func (o *DriverBase) HasEldAdverseWeatherExemptionEnabled() bool`

HasEldAdverseWeatherExemptionEnabled returns a boolean if a field has been set.

### SetEldAdverseWeatherExemptionEnabled

`func (o *DriverBase) SetEldAdverseWeatherExemptionEnabled(v bool)`

SetEldAdverseWeatherExemptionEnabled gets a reference to the given bool and assigns it to the EldAdverseWeatherExemptionEnabled field.

### GetEldBigDayExemptionEnabled

`func (o *DriverBase) GetEldBigDayExemptionEnabled() bool`

GetEldBigDayExemptionEnabled returns the EldBigDayExemptionEnabled field if non-nil, zero value otherwise.

### GetEldBigDayExemptionEnabledOk

`func (o *DriverBase) GetEldBigDayExemptionEnabledOk() (bool, bool)`

GetEldBigDayExemptionEnabledOk returns a tuple with the EldBigDayExemptionEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldBigDayExemptionEnabled

`func (o *DriverBase) HasEldBigDayExemptionEnabled() bool`

HasEldBigDayExemptionEnabled returns a boolean if a field has been set.

### SetEldBigDayExemptionEnabled

`func (o *DriverBase) SetEldBigDayExemptionEnabled(v bool)`

SetEldBigDayExemptionEnabled gets a reference to the given bool and assigns it to the EldBigDayExemptionEnabled field.

### GetEldDayStartHour

`func (o *DriverBase) GetEldDayStartHour() int32`

GetEldDayStartHour returns the EldDayStartHour field if non-nil, zero value otherwise.

### GetEldDayStartHourOk

`func (o *DriverBase) GetEldDayStartHourOk() (int32, bool)`

GetEldDayStartHourOk returns a tuple with the EldDayStartHour field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldDayStartHour

`func (o *DriverBase) HasEldDayStartHour() bool`

HasEldDayStartHour returns a boolean if a field has been set.

### SetEldDayStartHour

`func (o *DriverBase) SetEldDayStartHour(v int32)`

SetEldDayStartHour gets a reference to the given int32 and assigns it to the EldDayStartHour field.

### GetEldExempt

`func (o *DriverBase) GetEldExempt() bool`

GetEldExempt returns the EldExempt field if non-nil, zero value otherwise.

### GetEldExemptOk

`func (o *DriverBase) GetEldExemptOk() (bool, bool)`

GetEldExemptOk returns a tuple with the EldExempt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldExempt

`func (o *DriverBase) HasEldExempt() bool`

HasEldExempt returns a boolean if a field has been set.

### SetEldExempt

`func (o *DriverBase) SetEldExempt(v bool)`

SetEldExempt gets a reference to the given bool and assigns it to the EldExempt field.

### GetEldExemptReason

`func (o *DriverBase) GetEldExemptReason() string`

GetEldExemptReason returns the EldExemptReason field if non-nil, zero value otherwise.

### GetEldExemptReasonOk

`func (o *DriverBase) GetEldExemptReasonOk() (string, bool)`

GetEldExemptReasonOk returns a tuple with the EldExemptReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldExemptReason

`func (o *DriverBase) HasEldExemptReason() bool`

HasEldExemptReason returns a boolean if a field has been set.

### SetEldExemptReason

`func (o *DriverBase) SetEldExemptReason(v string)`

SetEldExemptReason gets a reference to the given string and assigns it to the EldExemptReason field.

### GetEldPcEnabled

`func (o *DriverBase) GetEldPcEnabled() bool`

GetEldPcEnabled returns the EldPcEnabled field if non-nil, zero value otherwise.

### GetEldPcEnabledOk

`func (o *DriverBase) GetEldPcEnabledOk() (bool, bool)`

GetEldPcEnabledOk returns a tuple with the EldPcEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldPcEnabled

`func (o *DriverBase) HasEldPcEnabled() bool`

HasEldPcEnabled returns a boolean if a field has been set.

### SetEldPcEnabled

`func (o *DriverBase) SetEldPcEnabled(v bool)`

SetEldPcEnabled gets a reference to the given bool and assigns it to the EldPcEnabled field.

### GetEldYmEnabled

`func (o *DriverBase) GetEldYmEnabled() bool`

GetEldYmEnabled returns the EldYmEnabled field if non-nil, zero value otherwise.

### GetEldYmEnabledOk

`func (o *DriverBase) GetEldYmEnabledOk() (bool, bool)`

GetEldYmEnabledOk returns a tuple with the EldYmEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldYmEnabled

`func (o *DriverBase) HasEldYmEnabled() bool`

HasEldYmEnabled returns a boolean if a field has been set.

### SetEldYmEnabled

`func (o *DriverBase) SetEldYmEnabled(v bool)`

SetEldYmEnabled gets a reference to the given bool and assigns it to the EldYmEnabled field.

### GetExternalIds

`func (o *DriverBase) GetExternalIds() map[string]string`

GetExternalIds returns the ExternalIds field if non-nil, zero value otherwise.

### GetExternalIdsOk

`func (o *DriverBase) GetExternalIdsOk() (map[string]string, bool)`

GetExternalIdsOk returns a tuple with the ExternalIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasExternalIds

`func (o *DriverBase) HasExternalIds() bool`

HasExternalIds returns a boolean if a field has been set.

### SetExternalIds

`func (o *DriverBase) SetExternalIds(v map[string]string)`

SetExternalIds gets a reference to the given map[string]string and assigns it to the ExternalIds field.

### GetIsDeactivated

`func (o *DriverBase) GetIsDeactivated() bool`

GetIsDeactivated returns the IsDeactivated field if non-nil, zero value otherwise.

### GetIsDeactivatedOk

`func (o *DriverBase) GetIsDeactivatedOk() (bool, bool)`

GetIsDeactivatedOk returns a tuple with the IsDeactivated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasIsDeactivated

`func (o *DriverBase) HasIsDeactivated() bool`

HasIsDeactivated returns a boolean if a field has been set.

### SetIsDeactivated

`func (o *DriverBase) SetIsDeactivated(v bool)`

SetIsDeactivated gets a reference to the given bool and assigns it to the IsDeactivated field.

### GetLicenseNumber

`func (o *DriverBase) GetLicenseNumber() string`

GetLicenseNumber returns the LicenseNumber field if non-nil, zero value otherwise.

### GetLicenseNumberOk

`func (o *DriverBase) GetLicenseNumberOk() (string, bool)`

GetLicenseNumberOk returns a tuple with the LicenseNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLicenseNumber

`func (o *DriverBase) HasLicenseNumber() bool`

HasLicenseNumber returns a boolean if a field has been set.

### SetLicenseNumber

`func (o *DriverBase) SetLicenseNumber(v string)`

SetLicenseNumber gets a reference to the given string and assigns it to the LicenseNumber field.

### GetLicenseState

`func (o *DriverBase) GetLicenseState() string`

GetLicenseState returns the LicenseState field if non-nil, zero value otherwise.

### GetLicenseStateOk

`func (o *DriverBase) GetLicenseStateOk() (string, bool)`

GetLicenseStateOk returns a tuple with the LicenseState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLicenseState

`func (o *DriverBase) HasLicenseState() bool`

HasLicenseState returns a boolean if a field has been set.

### SetLicenseState

`func (o *DriverBase) SetLicenseState(v string)`

SetLicenseState gets a reference to the given string and assigns it to the LicenseState field.

### GetLocale

`func (o *DriverBase) GetLocale() string`

GetLocale returns the Locale field if non-nil, zero value otherwise.

### GetLocaleOk

`func (o *DriverBase) GetLocaleOk() (string, bool)`

GetLocaleOk returns a tuple with the Locale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocale

`func (o *DriverBase) HasLocale() bool`

HasLocale returns a boolean if a field has been set.

### SetLocale

`func (o *DriverBase) SetLocale(v string)`

SetLocale gets a reference to the given string and assigns it to the Locale field.

### GetName

`func (o *DriverBase) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *DriverBase) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *DriverBase) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *DriverBase) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetNotes

`func (o *DriverBase) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *DriverBase) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *DriverBase) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *DriverBase) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetPhone

`func (o *DriverBase) GetPhone() string`

GetPhone returns the Phone field if non-nil, zero value otherwise.

### GetPhoneOk

`func (o *DriverBase) GetPhoneOk() (string, bool)`

GetPhoneOk returns a tuple with the Phone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPhone

`func (o *DriverBase) HasPhone() bool`

HasPhone returns a boolean if a field has been set.

### SetPhone

`func (o *DriverBase) SetPhone(v string)`

SetPhone gets a reference to the given string and assigns it to the Phone field.

### GetTachographCardNumber

`func (o *DriverBase) GetTachographCardNumber() string`

GetTachographCardNumber returns the TachographCardNumber field if non-nil, zero value otherwise.

### GetTachographCardNumberOk

`func (o *DriverBase) GetTachographCardNumberOk() (string, bool)`

GetTachographCardNumberOk returns a tuple with the TachographCardNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTachographCardNumber

`func (o *DriverBase) HasTachographCardNumber() bool`

HasTachographCardNumber returns a boolean if a field has been set.

### SetTachographCardNumber

`func (o *DriverBase) SetTachographCardNumber(v string)`

SetTachographCardNumber gets a reference to the given string and assigns it to the TachographCardNumber field.

### GetTimezone

`func (o *DriverBase) GetTimezone() string`

GetTimezone returns the Timezone field if non-nil, zero value otherwise.

### GetTimezoneOk

`func (o *DriverBase) GetTimezoneOk() (string, bool)`

GetTimezoneOk returns a tuple with the Timezone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTimezone

`func (o *DriverBase) HasTimezone() bool`

HasTimezone returns a boolean if a field has been set.

### SetTimezone

`func (o *DriverBase) SetTimezone(v string)`

SetTimezone gets a reference to the given string and assigns it to the Timezone field.

### GetUsername

`func (o *DriverBase) GetUsername() string`

GetUsername returns the Username field if non-nil, zero value otherwise.

### GetUsernameOk

`func (o *DriverBase) GetUsernameOk() (string, bool)`

GetUsernameOk returns a tuple with the Username field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasUsername

`func (o *DriverBase) HasUsername() bool`

HasUsername returns a boolean if a field has been set.

### SetUsername

`func (o *DriverBase) SetUsername(v string)`

SetUsername gets a reference to the given string and assigns it to the Username field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


