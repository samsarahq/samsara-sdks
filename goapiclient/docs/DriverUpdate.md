# DriverUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Password** | Pointer to **string** | Password that the driver can use to login to the Samsara driver app. | [optional] 
**StaticAssignedVehicleId** | Pointer to **string** | ID of vehicle assigned to the driver for static vehicle assignments. (uncommon). | [optional] 
**TagIds** | Pointer to **[]string** | IDs of tags the driver is associated with. | [optional] 
**VehicleGroupTagId** | Pointer to **string** | Tag ID which determines which vehicles a driver will see when selecting vehicles. | [optional] 
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

### GetPassword

`func (o *DriverUpdate) GetPassword() string`

GetPassword returns the Password field if non-nil, zero value otherwise.

### GetPasswordOk

`func (o *DriverUpdate) GetPasswordOk() (string, bool)`

GetPasswordOk returns a tuple with the Password field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPassword

`func (o *DriverUpdate) HasPassword() bool`

HasPassword returns a boolean if a field has been set.

### SetPassword

`func (o *DriverUpdate) SetPassword(v string)`

SetPassword gets a reference to the given string and assigns it to the Password field.

### GetStaticAssignedVehicleId

`func (o *DriverUpdate) GetStaticAssignedVehicleId() string`

GetStaticAssignedVehicleId returns the StaticAssignedVehicleId field if non-nil, zero value otherwise.

### GetStaticAssignedVehicleIdOk

`func (o *DriverUpdate) GetStaticAssignedVehicleIdOk() (string, bool)`

GetStaticAssignedVehicleIdOk returns a tuple with the StaticAssignedVehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStaticAssignedVehicleId

`func (o *DriverUpdate) HasStaticAssignedVehicleId() bool`

HasStaticAssignedVehicleId returns a boolean if a field has been set.

### SetStaticAssignedVehicleId

`func (o *DriverUpdate) SetStaticAssignedVehicleId(v string)`

SetStaticAssignedVehicleId gets a reference to the given string and assigns it to the StaticAssignedVehicleId field.

### GetTagIds

`func (o *DriverUpdate) GetTagIds() []string`

GetTagIds returns the TagIds field if non-nil, zero value otherwise.

### GetTagIdsOk

`func (o *DriverUpdate) GetTagIdsOk() ([]string, bool)`

GetTagIdsOk returns a tuple with the TagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTagIds

`func (o *DriverUpdate) HasTagIds() bool`

HasTagIds returns a boolean if a field has been set.

### SetTagIds

`func (o *DriverUpdate) SetTagIds(v []string)`

SetTagIds gets a reference to the given []string and assigns it to the TagIds field.

### GetVehicleGroupTagId

`func (o *DriverUpdate) GetVehicleGroupTagId() string`

GetVehicleGroupTagId returns the VehicleGroupTagId field if non-nil, zero value otherwise.

### GetVehicleGroupTagIdOk

`func (o *DriverUpdate) GetVehicleGroupTagIdOk() (string, bool)`

GetVehicleGroupTagIdOk returns a tuple with the VehicleGroupTagId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleGroupTagId

`func (o *DriverUpdate) HasVehicleGroupTagId() bool`

HasVehicleGroupTagId returns a boolean if a field has been set.

### SetVehicleGroupTagId

`func (o *DriverUpdate) SetVehicleGroupTagId(v string)`

SetVehicleGroupTagId gets a reference to the given string and assigns it to the VehicleGroupTagId field.

### GetCarrierSettings

`func (o *DriverUpdate) GetCarrierSettings() DriverBaseCarrierSettings`

GetCarrierSettings returns the CarrierSettings field if non-nil, zero value otherwise.

### GetCarrierSettingsOk

`func (o *DriverUpdate) GetCarrierSettingsOk() (DriverBaseCarrierSettings, bool)`

GetCarrierSettingsOk returns a tuple with the CarrierSettings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCarrierSettings

`func (o *DriverUpdate) HasCarrierSettings() bool`

HasCarrierSettings returns a boolean if a field has been set.

### SetCarrierSettings

`func (o *DriverUpdate) SetCarrierSettings(v DriverBaseCarrierSettings)`

SetCarrierSettings gets a reference to the given DriverBaseCarrierSettings and assigns it to the CarrierSettings field.

### GetEldAdverseWeatherExemptionEnabled

`func (o *DriverUpdate) GetEldAdverseWeatherExemptionEnabled() bool`

GetEldAdverseWeatherExemptionEnabled returns the EldAdverseWeatherExemptionEnabled field if non-nil, zero value otherwise.

### GetEldAdverseWeatherExemptionEnabledOk

`func (o *DriverUpdate) GetEldAdverseWeatherExemptionEnabledOk() (bool, bool)`

GetEldAdverseWeatherExemptionEnabledOk returns a tuple with the EldAdverseWeatherExemptionEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldAdverseWeatherExemptionEnabled

`func (o *DriverUpdate) HasEldAdverseWeatherExemptionEnabled() bool`

HasEldAdverseWeatherExemptionEnabled returns a boolean if a field has been set.

### SetEldAdverseWeatherExemptionEnabled

`func (o *DriverUpdate) SetEldAdverseWeatherExemptionEnabled(v bool)`

SetEldAdverseWeatherExemptionEnabled gets a reference to the given bool and assigns it to the EldAdverseWeatherExemptionEnabled field.

### GetEldBigDayExemptionEnabled

`func (o *DriverUpdate) GetEldBigDayExemptionEnabled() bool`

GetEldBigDayExemptionEnabled returns the EldBigDayExemptionEnabled field if non-nil, zero value otherwise.

### GetEldBigDayExemptionEnabledOk

`func (o *DriverUpdate) GetEldBigDayExemptionEnabledOk() (bool, bool)`

GetEldBigDayExemptionEnabledOk returns a tuple with the EldBigDayExemptionEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldBigDayExemptionEnabled

`func (o *DriverUpdate) HasEldBigDayExemptionEnabled() bool`

HasEldBigDayExemptionEnabled returns a boolean if a field has been set.

### SetEldBigDayExemptionEnabled

`func (o *DriverUpdate) SetEldBigDayExemptionEnabled(v bool)`

SetEldBigDayExemptionEnabled gets a reference to the given bool and assigns it to the EldBigDayExemptionEnabled field.

### GetEldDayStartHour

`func (o *DriverUpdate) GetEldDayStartHour() int32`

GetEldDayStartHour returns the EldDayStartHour field if non-nil, zero value otherwise.

### GetEldDayStartHourOk

`func (o *DriverUpdate) GetEldDayStartHourOk() (int32, bool)`

GetEldDayStartHourOk returns a tuple with the EldDayStartHour field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldDayStartHour

`func (o *DriverUpdate) HasEldDayStartHour() bool`

HasEldDayStartHour returns a boolean if a field has been set.

### SetEldDayStartHour

`func (o *DriverUpdate) SetEldDayStartHour(v int32)`

SetEldDayStartHour gets a reference to the given int32 and assigns it to the EldDayStartHour field.

### GetEldExempt

`func (o *DriverUpdate) GetEldExempt() bool`

GetEldExempt returns the EldExempt field if non-nil, zero value otherwise.

### GetEldExemptOk

`func (o *DriverUpdate) GetEldExemptOk() (bool, bool)`

GetEldExemptOk returns a tuple with the EldExempt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldExempt

`func (o *DriverUpdate) HasEldExempt() bool`

HasEldExempt returns a boolean if a field has been set.

### SetEldExempt

`func (o *DriverUpdate) SetEldExempt(v bool)`

SetEldExempt gets a reference to the given bool and assigns it to the EldExempt field.

### GetEldExemptReason

`func (o *DriverUpdate) GetEldExemptReason() string`

GetEldExemptReason returns the EldExemptReason field if non-nil, zero value otherwise.

### GetEldExemptReasonOk

`func (o *DriverUpdate) GetEldExemptReasonOk() (string, bool)`

GetEldExemptReasonOk returns a tuple with the EldExemptReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldExemptReason

`func (o *DriverUpdate) HasEldExemptReason() bool`

HasEldExemptReason returns a boolean if a field has been set.

### SetEldExemptReason

`func (o *DriverUpdate) SetEldExemptReason(v string)`

SetEldExemptReason gets a reference to the given string and assigns it to the EldExemptReason field.

### GetEldPcEnabled

`func (o *DriverUpdate) GetEldPcEnabled() bool`

GetEldPcEnabled returns the EldPcEnabled field if non-nil, zero value otherwise.

### GetEldPcEnabledOk

`func (o *DriverUpdate) GetEldPcEnabledOk() (bool, bool)`

GetEldPcEnabledOk returns a tuple with the EldPcEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldPcEnabled

`func (o *DriverUpdate) HasEldPcEnabled() bool`

HasEldPcEnabled returns a boolean if a field has been set.

### SetEldPcEnabled

`func (o *DriverUpdate) SetEldPcEnabled(v bool)`

SetEldPcEnabled gets a reference to the given bool and assigns it to the EldPcEnabled field.

### GetEldYmEnabled

`func (o *DriverUpdate) GetEldYmEnabled() bool`

GetEldYmEnabled returns the EldYmEnabled field if non-nil, zero value otherwise.

### GetEldYmEnabledOk

`func (o *DriverUpdate) GetEldYmEnabledOk() (bool, bool)`

GetEldYmEnabledOk returns a tuple with the EldYmEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEldYmEnabled

`func (o *DriverUpdate) HasEldYmEnabled() bool`

HasEldYmEnabled returns a boolean if a field has been set.

### SetEldYmEnabled

`func (o *DriverUpdate) SetEldYmEnabled(v bool)`

SetEldYmEnabled gets a reference to the given bool and assigns it to the EldYmEnabled field.

### GetExternalIds

`func (o *DriverUpdate) GetExternalIds() map[string]string`

GetExternalIds returns the ExternalIds field if non-nil, zero value otherwise.

### GetExternalIdsOk

`func (o *DriverUpdate) GetExternalIdsOk() (map[string]string, bool)`

GetExternalIdsOk returns a tuple with the ExternalIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasExternalIds

`func (o *DriverUpdate) HasExternalIds() bool`

HasExternalIds returns a boolean if a field has been set.

### SetExternalIds

`func (o *DriverUpdate) SetExternalIds(v map[string]string)`

SetExternalIds gets a reference to the given map[string]string and assigns it to the ExternalIds field.

### GetIsDeactivated

`func (o *DriverUpdate) GetIsDeactivated() bool`

GetIsDeactivated returns the IsDeactivated field if non-nil, zero value otherwise.

### GetIsDeactivatedOk

`func (o *DriverUpdate) GetIsDeactivatedOk() (bool, bool)`

GetIsDeactivatedOk returns a tuple with the IsDeactivated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasIsDeactivated

`func (o *DriverUpdate) HasIsDeactivated() bool`

HasIsDeactivated returns a boolean if a field has been set.

### SetIsDeactivated

`func (o *DriverUpdate) SetIsDeactivated(v bool)`

SetIsDeactivated gets a reference to the given bool and assigns it to the IsDeactivated field.

### GetLicenseNumber

`func (o *DriverUpdate) GetLicenseNumber() string`

GetLicenseNumber returns the LicenseNumber field if non-nil, zero value otherwise.

### GetLicenseNumberOk

`func (o *DriverUpdate) GetLicenseNumberOk() (string, bool)`

GetLicenseNumberOk returns a tuple with the LicenseNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLicenseNumber

`func (o *DriverUpdate) HasLicenseNumber() bool`

HasLicenseNumber returns a boolean if a field has been set.

### SetLicenseNumber

`func (o *DriverUpdate) SetLicenseNumber(v string)`

SetLicenseNumber gets a reference to the given string and assigns it to the LicenseNumber field.

### GetLicenseState

`func (o *DriverUpdate) GetLicenseState() string`

GetLicenseState returns the LicenseState field if non-nil, zero value otherwise.

### GetLicenseStateOk

`func (o *DriverUpdate) GetLicenseStateOk() (string, bool)`

GetLicenseStateOk returns a tuple with the LicenseState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLicenseState

`func (o *DriverUpdate) HasLicenseState() bool`

HasLicenseState returns a boolean if a field has been set.

### SetLicenseState

`func (o *DriverUpdate) SetLicenseState(v string)`

SetLicenseState gets a reference to the given string and assigns it to the LicenseState field.

### GetLocale

`func (o *DriverUpdate) GetLocale() string`

GetLocale returns the Locale field if non-nil, zero value otherwise.

### GetLocaleOk

`func (o *DriverUpdate) GetLocaleOk() (string, bool)`

GetLocaleOk returns a tuple with the Locale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocale

`func (o *DriverUpdate) HasLocale() bool`

HasLocale returns a boolean if a field has been set.

### SetLocale

`func (o *DriverUpdate) SetLocale(v string)`

SetLocale gets a reference to the given string and assigns it to the Locale field.

### GetName

`func (o *DriverUpdate) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *DriverUpdate) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *DriverUpdate) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *DriverUpdate) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetNotes

`func (o *DriverUpdate) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *DriverUpdate) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *DriverUpdate) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *DriverUpdate) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetPhone

`func (o *DriverUpdate) GetPhone() string`

GetPhone returns the Phone field if non-nil, zero value otherwise.

### GetPhoneOk

`func (o *DriverUpdate) GetPhoneOk() (string, bool)`

GetPhoneOk returns a tuple with the Phone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPhone

`func (o *DriverUpdate) HasPhone() bool`

HasPhone returns a boolean if a field has been set.

### SetPhone

`func (o *DriverUpdate) SetPhone(v string)`

SetPhone gets a reference to the given string and assigns it to the Phone field.

### GetTachographCardNumber

`func (o *DriverUpdate) GetTachographCardNumber() string`

GetTachographCardNumber returns the TachographCardNumber field if non-nil, zero value otherwise.

### GetTachographCardNumberOk

`func (o *DriverUpdate) GetTachographCardNumberOk() (string, bool)`

GetTachographCardNumberOk returns a tuple with the TachographCardNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTachographCardNumber

`func (o *DriverUpdate) HasTachographCardNumber() bool`

HasTachographCardNumber returns a boolean if a field has been set.

### SetTachographCardNumber

`func (o *DriverUpdate) SetTachographCardNumber(v string)`

SetTachographCardNumber gets a reference to the given string and assigns it to the TachographCardNumber field.

### GetTimezone

`func (o *DriverUpdate) GetTimezone() string`

GetTimezone returns the Timezone field if non-nil, zero value otherwise.

### GetTimezoneOk

`func (o *DriverUpdate) GetTimezoneOk() (string, bool)`

GetTimezoneOk returns a tuple with the Timezone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTimezone

`func (o *DriverUpdate) HasTimezone() bool`

HasTimezone returns a boolean if a field has been set.

### SetTimezone

`func (o *DriverUpdate) SetTimezone(v string)`

SetTimezone gets a reference to the given string and assigns it to the Timezone field.

### GetUsername

`func (o *DriverUpdate) GetUsername() string`

GetUsername returns the Username field if non-nil, zero value otherwise.

### GetUsernameOk

`func (o *DriverUpdate) GetUsernameOk() (string, bool)`

GetUsernameOk returns a tuple with the Username field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasUsername

`func (o *DriverUpdate) HasUsername() bool`

HasUsername returns a boolean if a field has been set.

### SetUsername

`func (o *DriverUpdate) SetUsername(v string)`

SetUsername gets a reference to the given string and assigns it to the Username field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


