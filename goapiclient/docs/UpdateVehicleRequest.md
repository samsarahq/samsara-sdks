# UpdateVehicleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuxInputType1** | Pointer to [**VehicleAuxInputType**](VehicleAuxInputType.md) |  | [optional] 
**AuxInputType2** | Pointer to [**VehicleAuxInputType**](VehicleAuxInputType.md) |  | [optional] 
**EngineHours** | Pointer to **int64** | A manual override for the vehicle&#39;s engine hours. You may only override a vehicle&#39;s engine hours if it cannot be read from on-board diagnostics. When you provide a manual engine hours override, Samsara will begin updating a vehicle&#39;s engine hours based on when the Samsara Vehicle Gateway is recieving power or not. | [optional] 
**ExternalIds** | Pointer to **map[string]string** | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object. | [optional] 
**HarshAccelerationSettingType** | Pointer to [**VehicleHarshAccelerationSettingType**](VehicleHarshAccelerationSettingType.md) |  | [optional] 
**LicensePlate** | Pointer to **string** | The license plate of the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time. | [optional] 
**Name** | Pointer to **string** | The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time. | [optional] 
**Notes** | Pointer to **string** | These are generic notes about the Vehicle. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time. | [optional] [default to ]
**OdometerMeters** | Pointer to **int64** | A manual override for the vehicle&#39;s odometer. You may only override a vehicle&#39;s odometer if it cannot be read from on-board diagnostics. When you provide a manual odometer override, Samsara will begin updating a vehicle&#39;s odometer using GPS distance traveled since this override was set. See [here](https://kb.samsara.com/hc/en-us/articles/115005273667) for more details. | [optional] 
**StaticAssignedDriverId** | Pointer to **string** | ID for the static assigned driver of the vehicle. | [optional] 
**TagIds** | Pointer to **[]string** | An array of IDs of tags to associate with this vehicle. | [optional] 
**Vin** | Pointer to **string** | The VIN of the Vehicle. Most of the time, this will be automatically read from the engine computer by the Samsara Vehicle Gateway. It will be empty if it cannot be read. It can be set or updated through the Samsara Dashboard or the API at any time. | [optional] 

## Methods

### GetAuxInputType1

`func (o *UpdateVehicleRequest) GetAuxInputType1() VehicleAuxInputType`

GetAuxInputType1 returns the AuxInputType1 field if non-nil, zero value otherwise.

### GetAuxInputType1Ok

`func (o *UpdateVehicleRequest) GetAuxInputType1Ok() (VehicleAuxInputType, bool)`

GetAuxInputType1Ok returns a tuple with the AuxInputType1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuxInputType1

`func (o *UpdateVehicleRequest) HasAuxInputType1() bool`

HasAuxInputType1 returns a boolean if a field has been set.

### SetAuxInputType1

`func (o *UpdateVehicleRequest) SetAuxInputType1(v VehicleAuxInputType)`

SetAuxInputType1 gets a reference to the given VehicleAuxInputType and assigns it to the AuxInputType1 field.

### GetAuxInputType2

`func (o *UpdateVehicleRequest) GetAuxInputType2() VehicleAuxInputType`

GetAuxInputType2 returns the AuxInputType2 field if non-nil, zero value otherwise.

### GetAuxInputType2Ok

`func (o *UpdateVehicleRequest) GetAuxInputType2Ok() (VehicleAuxInputType, bool)`

GetAuxInputType2Ok returns a tuple with the AuxInputType2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuxInputType2

`func (o *UpdateVehicleRequest) HasAuxInputType2() bool`

HasAuxInputType2 returns a boolean if a field has been set.

### SetAuxInputType2

`func (o *UpdateVehicleRequest) SetAuxInputType2(v VehicleAuxInputType)`

SetAuxInputType2 gets a reference to the given VehicleAuxInputType and assigns it to the AuxInputType2 field.

### GetEngineHours

`func (o *UpdateVehicleRequest) GetEngineHours() int64`

GetEngineHours returns the EngineHours field if non-nil, zero value otherwise.

### GetEngineHoursOk

`func (o *UpdateVehicleRequest) GetEngineHoursOk() (int64, bool)`

GetEngineHoursOk returns a tuple with the EngineHours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineHours

`func (o *UpdateVehicleRequest) HasEngineHours() bool`

HasEngineHours returns a boolean if a field has been set.

### SetEngineHours

`func (o *UpdateVehicleRequest) SetEngineHours(v int64)`

SetEngineHours gets a reference to the given int64 and assigns it to the EngineHours field.

### GetExternalIds

`func (o *UpdateVehicleRequest) GetExternalIds() map[string]string`

GetExternalIds returns the ExternalIds field if non-nil, zero value otherwise.

### GetExternalIdsOk

`func (o *UpdateVehicleRequest) GetExternalIdsOk() (map[string]string, bool)`

GetExternalIdsOk returns a tuple with the ExternalIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasExternalIds

`func (o *UpdateVehicleRequest) HasExternalIds() bool`

HasExternalIds returns a boolean if a field has been set.

### SetExternalIds

`func (o *UpdateVehicleRequest) SetExternalIds(v map[string]string)`

SetExternalIds gets a reference to the given map[string]string and assigns it to the ExternalIds field.

### GetHarshAccelerationSettingType

`func (o *UpdateVehicleRequest) GetHarshAccelerationSettingType() VehicleHarshAccelerationSettingType`

GetHarshAccelerationSettingType returns the HarshAccelerationSettingType field if non-nil, zero value otherwise.

### GetHarshAccelerationSettingTypeOk

`func (o *UpdateVehicleRequest) GetHarshAccelerationSettingTypeOk() (VehicleHarshAccelerationSettingType, bool)`

GetHarshAccelerationSettingTypeOk returns a tuple with the HarshAccelerationSettingType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshAccelerationSettingType

`func (o *UpdateVehicleRequest) HasHarshAccelerationSettingType() bool`

HasHarshAccelerationSettingType returns a boolean if a field has been set.

### SetHarshAccelerationSettingType

`func (o *UpdateVehicleRequest) SetHarshAccelerationSettingType(v VehicleHarshAccelerationSettingType)`

SetHarshAccelerationSettingType gets a reference to the given VehicleHarshAccelerationSettingType and assigns it to the HarshAccelerationSettingType field.

### GetLicensePlate

`func (o *UpdateVehicleRequest) GetLicensePlate() string`

GetLicensePlate returns the LicensePlate field if non-nil, zero value otherwise.

### GetLicensePlateOk

`func (o *UpdateVehicleRequest) GetLicensePlateOk() (string, bool)`

GetLicensePlateOk returns a tuple with the LicensePlate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLicensePlate

`func (o *UpdateVehicleRequest) HasLicensePlate() bool`

HasLicensePlate returns a boolean if a field has been set.

### SetLicensePlate

`func (o *UpdateVehicleRequest) SetLicensePlate(v string)`

SetLicensePlate gets a reference to the given string and assigns it to the LicensePlate field.

### GetName

`func (o *UpdateVehicleRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UpdateVehicleRequest) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *UpdateVehicleRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *UpdateVehicleRequest) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetNotes

`func (o *UpdateVehicleRequest) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *UpdateVehicleRequest) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *UpdateVehicleRequest) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *UpdateVehicleRequest) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetOdometerMeters

`func (o *UpdateVehicleRequest) GetOdometerMeters() int64`

GetOdometerMeters returns the OdometerMeters field if non-nil, zero value otherwise.

### GetOdometerMetersOk

`func (o *UpdateVehicleRequest) GetOdometerMetersOk() (int64, bool)`

GetOdometerMetersOk returns a tuple with the OdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOdometerMeters

`func (o *UpdateVehicleRequest) HasOdometerMeters() bool`

HasOdometerMeters returns a boolean if a field has been set.

### SetOdometerMeters

`func (o *UpdateVehicleRequest) SetOdometerMeters(v int64)`

SetOdometerMeters gets a reference to the given int64 and assigns it to the OdometerMeters field.

### GetStaticAssignedDriverId

`func (o *UpdateVehicleRequest) GetStaticAssignedDriverId() string`

GetStaticAssignedDriverId returns the StaticAssignedDriverId field if non-nil, zero value otherwise.

### GetStaticAssignedDriverIdOk

`func (o *UpdateVehicleRequest) GetStaticAssignedDriverIdOk() (string, bool)`

GetStaticAssignedDriverIdOk returns a tuple with the StaticAssignedDriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStaticAssignedDriverId

`func (o *UpdateVehicleRequest) HasStaticAssignedDriverId() bool`

HasStaticAssignedDriverId returns a boolean if a field has been set.

### SetStaticAssignedDriverId

`func (o *UpdateVehicleRequest) SetStaticAssignedDriverId(v string)`

SetStaticAssignedDriverId gets a reference to the given string and assigns it to the StaticAssignedDriverId field.

### GetTagIds

`func (o *UpdateVehicleRequest) GetTagIds() []string`

GetTagIds returns the TagIds field if non-nil, zero value otherwise.

### GetTagIdsOk

`func (o *UpdateVehicleRequest) GetTagIdsOk() ([]string, bool)`

GetTagIdsOk returns a tuple with the TagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTagIds

`func (o *UpdateVehicleRequest) HasTagIds() bool`

HasTagIds returns a boolean if a field has been set.

### SetTagIds

`func (o *UpdateVehicleRequest) SetTagIds(v []string)`

SetTagIds gets a reference to the given []string and assigns it to the TagIds field.

### GetVin

`func (o *UpdateVehicleRequest) GetVin() string`

GetVin returns the Vin field if non-nil, zero value otherwise.

### GetVinOk

`func (o *UpdateVehicleRequest) GetVinOk() (string, bool)`

GetVinOk returns a tuple with the Vin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVin

`func (o *UpdateVehicleRequest) HasVin() bool`

HasVin returns a boolean if a field has been set.

### SetVin

`func (o *UpdateVehicleRequest) SetVin(v string)`

SetVin gets a reference to the given string and assigns it to the Vin field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


