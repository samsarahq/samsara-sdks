# VehiclePatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuxInputType1** | Pointer to **string** | The type of aux input that this vehicle has connected to port 1. Setting to \&quot;none\&quot; will remove the configured aux input. | [optional] 
**AuxInputType2** | Pointer to **string** | The type of aux input that this vehicle has connected to port 2. Setting to \&quot;none\&quot; will remove the configured aux input. | [optional] 
**EngineHours** | Pointer to **int32** | Current engine hours value of the vehicle. This is typically pulled automatically from the vehicle, but can be manually overridden when it&#39;s not read automatically. | [optional] 
**ExternalIds** | Pointer to **map[string]string** | User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (&#x60;\&quot;\&quot;&#x60;). An external ID can be used as a path parameter to retrieve or update that resource. | [optional] 
**HarshAccelerationSettingType** | Pointer to **string** | Enumeration of the harsh acceleration setting types. This setting influences the accelereation sensitivity from which a harsh event is triggered. If set to &#x60;off&#x60;, then no acceleration based harsh events are triggered for the vehicle. | [optional] 
**LicensePlate** | Pointer to **string** | License plate number for the vehicle. | [optional] 
**Name** | Pointer to **string** | Name of the vehicle. | [optional] 
**Notes** | Pointer to **string** | Notes about a vehicle with a maximum of 255 characters. | [optional] 
**OdometerMeters** | Pointer to **int32** | Current odometer value of the vehicle. This is typically pulled automatically from the vehicle, but can be manually overridden when it&#39;s not read automatically. | [optional] 
**StaticAssignedDriverId** | Pointer to **NullableString** | ID of driver assigned to the vehicle for static vehicle assignments. An empty string explicitly unsets the assignment. (uncommon). | [optional] 
**TagIds** | Pointer to **[]string** | An array of IDs of tags to associate with this vehicle. | [optional] 
**Vin** | Pointer to **string** | A vehicle identification number. | [optional] 

## Methods

### GetAuxInputType1

`func (o *VehiclePatch) GetAuxInputType1() string`

GetAuxInputType1 returns the AuxInputType1 field if non-nil, zero value otherwise.

### GetAuxInputType1Ok

`func (o *VehiclePatch) GetAuxInputType1Ok() (string, bool)`

GetAuxInputType1Ok returns a tuple with the AuxInputType1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuxInputType1

`func (o *VehiclePatch) HasAuxInputType1() bool`

HasAuxInputType1 returns a boolean if a field has been set.

### SetAuxInputType1

`func (o *VehiclePatch) SetAuxInputType1(v string)`

SetAuxInputType1 gets a reference to the given string and assigns it to the AuxInputType1 field.

### GetAuxInputType2

`func (o *VehiclePatch) GetAuxInputType2() string`

GetAuxInputType2 returns the AuxInputType2 field if non-nil, zero value otherwise.

### GetAuxInputType2Ok

`func (o *VehiclePatch) GetAuxInputType2Ok() (string, bool)`

GetAuxInputType2Ok returns a tuple with the AuxInputType2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuxInputType2

`func (o *VehiclePatch) HasAuxInputType2() bool`

HasAuxInputType2 returns a boolean if a field has been set.

### SetAuxInputType2

`func (o *VehiclePatch) SetAuxInputType2(v string)`

SetAuxInputType2 gets a reference to the given string and assigns it to the AuxInputType2 field.

### GetEngineHours

`func (o *VehiclePatch) GetEngineHours() int32`

GetEngineHours returns the EngineHours field if non-nil, zero value otherwise.

### GetEngineHoursOk

`func (o *VehiclePatch) GetEngineHoursOk() (int32, bool)`

GetEngineHoursOk returns a tuple with the EngineHours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineHours

`func (o *VehiclePatch) HasEngineHours() bool`

HasEngineHours returns a boolean if a field has been set.

### SetEngineHours

`func (o *VehiclePatch) SetEngineHours(v int32)`

SetEngineHours gets a reference to the given int32 and assigns it to the EngineHours field.

### GetExternalIds

`func (o *VehiclePatch) GetExternalIds() map[string]string`

GetExternalIds returns the ExternalIds field if non-nil, zero value otherwise.

### GetExternalIdsOk

`func (o *VehiclePatch) GetExternalIdsOk() (map[string]string, bool)`

GetExternalIdsOk returns a tuple with the ExternalIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasExternalIds

`func (o *VehiclePatch) HasExternalIds() bool`

HasExternalIds returns a boolean if a field has been set.

### SetExternalIds

`func (o *VehiclePatch) SetExternalIds(v map[string]string)`

SetExternalIds gets a reference to the given map[string]string and assigns it to the ExternalIds field.

### GetHarshAccelerationSettingType

`func (o *VehiclePatch) GetHarshAccelerationSettingType() string`

GetHarshAccelerationSettingType returns the HarshAccelerationSettingType field if non-nil, zero value otherwise.

### GetHarshAccelerationSettingTypeOk

`func (o *VehiclePatch) GetHarshAccelerationSettingTypeOk() (string, bool)`

GetHarshAccelerationSettingTypeOk returns a tuple with the HarshAccelerationSettingType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshAccelerationSettingType

`func (o *VehiclePatch) HasHarshAccelerationSettingType() bool`

HasHarshAccelerationSettingType returns a boolean if a field has been set.

### SetHarshAccelerationSettingType

`func (o *VehiclePatch) SetHarshAccelerationSettingType(v string)`

SetHarshAccelerationSettingType gets a reference to the given string and assigns it to the HarshAccelerationSettingType field.

### GetLicensePlate

`func (o *VehiclePatch) GetLicensePlate() string`

GetLicensePlate returns the LicensePlate field if non-nil, zero value otherwise.

### GetLicensePlateOk

`func (o *VehiclePatch) GetLicensePlateOk() (string, bool)`

GetLicensePlateOk returns a tuple with the LicensePlate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLicensePlate

`func (o *VehiclePatch) HasLicensePlate() bool`

HasLicensePlate returns a boolean if a field has been set.

### SetLicensePlate

`func (o *VehiclePatch) SetLicensePlate(v string)`

SetLicensePlate gets a reference to the given string and assigns it to the LicensePlate field.

### GetName

`func (o *VehiclePatch) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *VehiclePatch) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *VehiclePatch) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *VehiclePatch) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetNotes

`func (o *VehiclePatch) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *VehiclePatch) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *VehiclePatch) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *VehiclePatch) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetOdometerMeters

`func (o *VehiclePatch) GetOdometerMeters() int32`

GetOdometerMeters returns the OdometerMeters field if non-nil, zero value otherwise.

### GetOdometerMetersOk

`func (o *VehiclePatch) GetOdometerMetersOk() (int32, bool)`

GetOdometerMetersOk returns a tuple with the OdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOdometerMeters

`func (o *VehiclePatch) HasOdometerMeters() bool`

HasOdometerMeters returns a boolean if a field has been set.

### SetOdometerMeters

`func (o *VehiclePatch) SetOdometerMeters(v int32)`

SetOdometerMeters gets a reference to the given int32 and assigns it to the OdometerMeters field.

### GetStaticAssignedDriverId

`func (o *VehiclePatch) GetStaticAssignedDriverId() NullableString`

GetStaticAssignedDriverId returns the StaticAssignedDriverId field if non-nil, zero value otherwise.

### GetStaticAssignedDriverIdOk

`func (o *VehiclePatch) GetStaticAssignedDriverIdOk() (NullableString, bool)`

GetStaticAssignedDriverIdOk returns a tuple with the StaticAssignedDriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStaticAssignedDriverId

`func (o *VehiclePatch) HasStaticAssignedDriverId() bool`

HasStaticAssignedDriverId returns a boolean if a field has been set.

### SetStaticAssignedDriverId

`func (o *VehiclePatch) SetStaticAssignedDriverId(v NullableString)`

SetStaticAssignedDriverId gets a reference to the given NullableString and assigns it to the StaticAssignedDriverId field.

### SetStaticAssignedDriverIdExplicitNull

`func (o *VehiclePatch) SetStaticAssignedDriverIdExplicitNull(b bool)`

SetStaticAssignedDriverIdExplicitNull (un)sets StaticAssignedDriverId to be considered as explicit "null" value
when serializing to JSON (pass true as argument to set this, false to unset)
The StaticAssignedDriverId value is set to nil even if false is passed
### GetTagIds

`func (o *VehiclePatch) GetTagIds() []string`

GetTagIds returns the TagIds field if non-nil, zero value otherwise.

### GetTagIdsOk

`func (o *VehiclePatch) GetTagIdsOk() ([]string, bool)`

GetTagIdsOk returns a tuple with the TagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTagIds

`func (o *VehiclePatch) HasTagIds() bool`

HasTagIds returns a boolean if a field has been set.

### SetTagIds

`func (o *VehiclePatch) SetTagIds(v []string)`

SetTagIds gets a reference to the given []string and assigns it to the TagIds field.

### GetVin

`func (o *VehiclePatch) GetVin() string`

GetVin returns the Vin field if non-nil, zero value otherwise.

### GetVinOk

`func (o *VehiclePatch) GetVinOk() (string, bool)`

GetVinOk returns a tuple with the Vin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVin

`func (o *VehiclePatch) HasVin() bool`

HasVin returns a boolean if a field has been set.

### SetVin

`func (o *VehiclePatch) SetVin(v string)`

SetVin gets a reference to the given string and assigns it to the Vin field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


