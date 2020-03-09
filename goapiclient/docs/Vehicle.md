# Vehicle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuxInputType1** | Pointer to [**VehicleAuxInputType**](VehicleAuxInputType.md) |  | [optional] 
**AuxInputType2** | Pointer to [**VehicleAuxInputType**](VehicleAuxInputType.md) |  | [optional] 
**ExternalIds** | Pointer to **map[string]string** | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object. | [optional] 
**HarshAccelerationSettingType** | Pointer to [**VehicleHarshAccelerationSettingType**](VehicleHarshAccelerationSettingType.md) |  | [optional] 
**Id** | Pointer to **string** | The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed. | 
**LicensePlate** | Pointer to **string** | The license plate of the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time. | [optional] 
**Make** | Pointer to **string** | The Vehicle’s manufacturing make. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set. | [optional] 
**Model** | Pointer to **string** | The Vehicle’s manufacturing model. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set. | [optional] 
**Name** | Pointer to **string** | The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time. | [optional] 
**Notes** | Pointer to **string** | These are generic notes about the Vehicle. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time. | [optional] [default to ]
**StaticAssignedDriver** | Pointer to [**DriverTinyResponse**](driverTinyResponse.md) |  | [optional] 
**Tags** | Pointer to [**[]TagTinyResponse**](tagTinyResponse.md) | The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time. | [optional] 
**Vin** | Pointer to **string** | The VIN of the Vehicle. Most of the time, this will be automatically read from the engine computer by the Samsara Vehicle Gateway. It will be empty if it cannot be read. It can be set or updated through the Samsara Dashboard or the API at any time. | [optional] 
**Year** | Pointer to **string** | The Vehicle’s manufacturing model. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set. | [optional] 

## Methods

### GetAuxInputType1

`func (o *Vehicle) GetAuxInputType1() VehicleAuxInputType`

GetAuxInputType1 returns the AuxInputType1 field if non-nil, zero value otherwise.

### GetAuxInputType1Ok

`func (o *Vehicle) GetAuxInputType1Ok() (VehicleAuxInputType, bool)`

GetAuxInputType1Ok returns a tuple with the AuxInputType1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuxInputType1

`func (o *Vehicle) HasAuxInputType1() bool`

HasAuxInputType1 returns a boolean if a field has been set.

### SetAuxInputType1

`func (o *Vehicle) SetAuxInputType1(v VehicleAuxInputType)`

SetAuxInputType1 gets a reference to the given VehicleAuxInputType and assigns it to the AuxInputType1 field.

### GetAuxInputType2

`func (o *Vehicle) GetAuxInputType2() VehicleAuxInputType`

GetAuxInputType2 returns the AuxInputType2 field if non-nil, zero value otherwise.

### GetAuxInputType2Ok

`func (o *Vehicle) GetAuxInputType2Ok() (VehicleAuxInputType, bool)`

GetAuxInputType2Ok returns a tuple with the AuxInputType2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuxInputType2

`func (o *Vehicle) HasAuxInputType2() bool`

HasAuxInputType2 returns a boolean if a field has been set.

### SetAuxInputType2

`func (o *Vehicle) SetAuxInputType2(v VehicleAuxInputType)`

SetAuxInputType2 gets a reference to the given VehicleAuxInputType and assigns it to the AuxInputType2 field.

### GetExternalIds

`func (o *Vehicle) GetExternalIds() map[string]string`

GetExternalIds returns the ExternalIds field if non-nil, zero value otherwise.

### GetExternalIdsOk

`func (o *Vehicle) GetExternalIdsOk() (map[string]string, bool)`

GetExternalIdsOk returns a tuple with the ExternalIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasExternalIds

`func (o *Vehicle) HasExternalIds() bool`

HasExternalIds returns a boolean if a field has been set.

### SetExternalIds

`func (o *Vehicle) SetExternalIds(v map[string]string)`

SetExternalIds gets a reference to the given map[string]string and assigns it to the ExternalIds field.

### GetHarshAccelerationSettingType

`func (o *Vehicle) GetHarshAccelerationSettingType() VehicleHarshAccelerationSettingType`

GetHarshAccelerationSettingType returns the HarshAccelerationSettingType field if non-nil, zero value otherwise.

### GetHarshAccelerationSettingTypeOk

`func (o *Vehicle) GetHarshAccelerationSettingTypeOk() (VehicleHarshAccelerationSettingType, bool)`

GetHarshAccelerationSettingTypeOk returns a tuple with the HarshAccelerationSettingType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshAccelerationSettingType

`func (o *Vehicle) HasHarshAccelerationSettingType() bool`

HasHarshAccelerationSettingType returns a boolean if a field has been set.

### SetHarshAccelerationSettingType

`func (o *Vehicle) SetHarshAccelerationSettingType(v VehicleHarshAccelerationSettingType)`

SetHarshAccelerationSettingType gets a reference to the given VehicleHarshAccelerationSettingType and assigns it to the HarshAccelerationSettingType field.

### GetId

`func (o *Vehicle) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Vehicle) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *Vehicle) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *Vehicle) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetLicensePlate

`func (o *Vehicle) GetLicensePlate() string`

GetLicensePlate returns the LicensePlate field if non-nil, zero value otherwise.

### GetLicensePlateOk

`func (o *Vehicle) GetLicensePlateOk() (string, bool)`

GetLicensePlateOk returns a tuple with the LicensePlate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLicensePlate

`func (o *Vehicle) HasLicensePlate() bool`

HasLicensePlate returns a boolean if a field has been set.

### SetLicensePlate

`func (o *Vehicle) SetLicensePlate(v string)`

SetLicensePlate gets a reference to the given string and assigns it to the LicensePlate field.

### GetMake

`func (o *Vehicle) GetMake() string`

GetMake returns the Make field if non-nil, zero value otherwise.

### GetMakeOk

`func (o *Vehicle) GetMakeOk() (string, bool)`

GetMakeOk returns a tuple with the Make field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMake

`func (o *Vehicle) HasMake() bool`

HasMake returns a boolean if a field has been set.

### SetMake

`func (o *Vehicle) SetMake(v string)`

SetMake gets a reference to the given string and assigns it to the Make field.

### GetModel

`func (o *Vehicle) GetModel() string`

GetModel returns the Model field if non-nil, zero value otherwise.

### GetModelOk

`func (o *Vehicle) GetModelOk() (string, bool)`

GetModelOk returns a tuple with the Model field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasModel

`func (o *Vehicle) HasModel() bool`

HasModel returns a boolean if a field has been set.

### SetModel

`func (o *Vehicle) SetModel(v string)`

SetModel gets a reference to the given string and assigns it to the Model field.

### GetName

`func (o *Vehicle) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Vehicle) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *Vehicle) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *Vehicle) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetNotes

`func (o *Vehicle) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *Vehicle) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *Vehicle) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *Vehicle) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetStaticAssignedDriver

`func (o *Vehicle) GetStaticAssignedDriver() DriverTinyResponse`

GetStaticAssignedDriver returns the StaticAssignedDriver field if non-nil, zero value otherwise.

### GetStaticAssignedDriverOk

`func (o *Vehicle) GetStaticAssignedDriverOk() (DriverTinyResponse, bool)`

GetStaticAssignedDriverOk returns a tuple with the StaticAssignedDriver field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStaticAssignedDriver

`func (o *Vehicle) HasStaticAssignedDriver() bool`

HasStaticAssignedDriver returns a boolean if a field has been set.

### SetStaticAssignedDriver

`func (o *Vehicle) SetStaticAssignedDriver(v DriverTinyResponse)`

SetStaticAssignedDriver gets a reference to the given DriverTinyResponse and assigns it to the StaticAssignedDriver field.

### GetTags

`func (o *Vehicle) GetTags() []TagTinyResponse`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *Vehicle) GetTagsOk() ([]TagTinyResponse, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTags

`func (o *Vehicle) HasTags() bool`

HasTags returns a boolean if a field has been set.

### SetTags

`func (o *Vehicle) SetTags(v []TagTinyResponse)`

SetTags gets a reference to the given []TagTinyResponse and assigns it to the Tags field.

### GetVin

`func (o *Vehicle) GetVin() string`

GetVin returns the Vin field if non-nil, zero value otherwise.

### GetVinOk

`func (o *Vehicle) GetVinOk() (string, bool)`

GetVinOk returns a tuple with the Vin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVin

`func (o *Vehicle) HasVin() bool`

HasVin returns a boolean if a field has been set.

### SetVin

`func (o *Vehicle) SetVin(v string)`

SetVin gets a reference to the given string and assigns it to the Vin field.

### GetYear

`func (o *Vehicle) GetYear() string`

GetYear returns the Year field if non-nil, zero value otherwise.

### GetYearOk

`func (o *Vehicle) GetYearOk() (string, bool)`

GetYearOk returns a tuple with the Year field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasYear

`func (o *Vehicle) HasYear() bool`

HasYear returns a boolean if a field has been set.

### SetYear

`func (o *Vehicle) SetYear(v string)`

SetYear gets a reference to the given string and assigns it to the Year field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


