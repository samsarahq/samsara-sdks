# VehicleResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuxInputType1** | Pointer to **string** | The type of aux input that this vehicle has connected to port 1. Setting to \&quot;none\&quot; will remove the configured aux input. | [optional] 
**AuxInputType2** | Pointer to **string** | The type of aux input that this vehicle has connected to port 2. Setting to \&quot;none\&quot; will remove the configured aux input. | [optional] 
**ExternalIds** | Pointer to **map[string]string** | User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (&#x60;\&quot;\&quot;&#x60;). An external ID can be used as a path parameter to retrieve or update that resource. | [optional] 
**HarshAccelerationSettingType** | Pointer to **string** | Enumeration of the harsh acceleration setting types. This setting influences the acceleration sensitivity from which a harsh event is triggered. If set to &#x60;off&#x60;, then no acceleration based harsh events are triggered for the vehicle. | [optional] 
**Id** | Pointer to **string** | Unique Samsara ID for the vehicle. | 
**LicensePlate** | Pointer to **string** | The license plate of this vehicle. | [optional] 
**Make** | Pointer to **string** | Vehicle&#39;s manufacturing make. | [optional] 
**Model** | Pointer to **string** | Vehicle&#39;s manufacturing model. | [optional] 
**Name** | Pointer to **string** | Name of the vehicle. | [optional] 
**Notes** | Pointer to **string** | Notes about a vehicle. Samsara supports a maximum of 255 chars. | [optional] 
**StaticAssignedDriver** | Pointer to [**DriverTinyResponse**](driverTinyResponse.md) |  | [optional] 
**Tags** | Pointer to [**[]TagTinyResponse**](tagTinyResponse.md) | An array of all tag mini-objects that are associated with the given vehicle. | [optional] 
**Vin** | Pointer to **string** | A vehicle identification number. | [optional] 
**Year** | Pointer to **string** | Vehicle&#39;s manufacturing year. | [optional] 

## Methods

### GetAuxInputType1

`func (o *VehicleResponse) GetAuxInputType1() string`

GetAuxInputType1 returns the AuxInputType1 field if non-nil, zero value otherwise.

### GetAuxInputType1Ok

`func (o *VehicleResponse) GetAuxInputType1Ok() (string, bool)`

GetAuxInputType1Ok returns a tuple with the AuxInputType1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuxInputType1

`func (o *VehicleResponse) HasAuxInputType1() bool`

HasAuxInputType1 returns a boolean if a field has been set.

### SetAuxInputType1

`func (o *VehicleResponse) SetAuxInputType1(v string)`

SetAuxInputType1 gets a reference to the given string and assigns it to the AuxInputType1 field.

### GetAuxInputType2

`func (o *VehicleResponse) GetAuxInputType2() string`

GetAuxInputType2 returns the AuxInputType2 field if non-nil, zero value otherwise.

### GetAuxInputType2Ok

`func (o *VehicleResponse) GetAuxInputType2Ok() (string, bool)`

GetAuxInputType2Ok returns a tuple with the AuxInputType2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuxInputType2

`func (o *VehicleResponse) HasAuxInputType2() bool`

HasAuxInputType2 returns a boolean if a field has been set.

### SetAuxInputType2

`func (o *VehicleResponse) SetAuxInputType2(v string)`

SetAuxInputType2 gets a reference to the given string and assigns it to the AuxInputType2 field.

### GetExternalIds

`func (o *VehicleResponse) GetExternalIds() map[string]string`

GetExternalIds returns the ExternalIds field if non-nil, zero value otherwise.

### GetExternalIdsOk

`func (o *VehicleResponse) GetExternalIdsOk() (map[string]string, bool)`

GetExternalIdsOk returns a tuple with the ExternalIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasExternalIds

`func (o *VehicleResponse) HasExternalIds() bool`

HasExternalIds returns a boolean if a field has been set.

### SetExternalIds

`func (o *VehicleResponse) SetExternalIds(v map[string]string)`

SetExternalIds gets a reference to the given map[string]string and assigns it to the ExternalIds field.

### GetHarshAccelerationSettingType

`func (o *VehicleResponse) GetHarshAccelerationSettingType() string`

GetHarshAccelerationSettingType returns the HarshAccelerationSettingType field if non-nil, zero value otherwise.

### GetHarshAccelerationSettingTypeOk

`func (o *VehicleResponse) GetHarshAccelerationSettingTypeOk() (string, bool)`

GetHarshAccelerationSettingTypeOk returns a tuple with the HarshAccelerationSettingType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshAccelerationSettingType

`func (o *VehicleResponse) HasHarshAccelerationSettingType() bool`

HasHarshAccelerationSettingType returns a boolean if a field has been set.

### SetHarshAccelerationSettingType

`func (o *VehicleResponse) SetHarshAccelerationSettingType(v string)`

SetHarshAccelerationSettingType gets a reference to the given string and assigns it to the HarshAccelerationSettingType field.

### GetId

`func (o *VehicleResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *VehicleResponse) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *VehicleResponse) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *VehicleResponse) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetLicensePlate

`func (o *VehicleResponse) GetLicensePlate() string`

GetLicensePlate returns the LicensePlate field if non-nil, zero value otherwise.

### GetLicensePlateOk

`func (o *VehicleResponse) GetLicensePlateOk() (string, bool)`

GetLicensePlateOk returns a tuple with the LicensePlate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLicensePlate

`func (o *VehicleResponse) HasLicensePlate() bool`

HasLicensePlate returns a boolean if a field has been set.

### SetLicensePlate

`func (o *VehicleResponse) SetLicensePlate(v string)`

SetLicensePlate gets a reference to the given string and assigns it to the LicensePlate field.

### GetMake

`func (o *VehicleResponse) GetMake() string`

GetMake returns the Make field if non-nil, zero value otherwise.

### GetMakeOk

`func (o *VehicleResponse) GetMakeOk() (string, bool)`

GetMakeOk returns a tuple with the Make field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMake

`func (o *VehicleResponse) HasMake() bool`

HasMake returns a boolean if a field has been set.

### SetMake

`func (o *VehicleResponse) SetMake(v string)`

SetMake gets a reference to the given string and assigns it to the Make field.

### GetModel

`func (o *VehicleResponse) GetModel() string`

GetModel returns the Model field if non-nil, zero value otherwise.

### GetModelOk

`func (o *VehicleResponse) GetModelOk() (string, bool)`

GetModelOk returns a tuple with the Model field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasModel

`func (o *VehicleResponse) HasModel() bool`

HasModel returns a boolean if a field has been set.

### SetModel

`func (o *VehicleResponse) SetModel(v string)`

SetModel gets a reference to the given string and assigns it to the Model field.

### GetName

`func (o *VehicleResponse) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *VehicleResponse) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *VehicleResponse) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *VehicleResponse) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetNotes

`func (o *VehicleResponse) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *VehicleResponse) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *VehicleResponse) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *VehicleResponse) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetStaticAssignedDriver

`func (o *VehicleResponse) GetStaticAssignedDriver() DriverTinyResponse`

GetStaticAssignedDriver returns the StaticAssignedDriver field if non-nil, zero value otherwise.

### GetStaticAssignedDriverOk

`func (o *VehicleResponse) GetStaticAssignedDriverOk() (DriverTinyResponse, bool)`

GetStaticAssignedDriverOk returns a tuple with the StaticAssignedDriver field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStaticAssignedDriver

`func (o *VehicleResponse) HasStaticAssignedDriver() bool`

HasStaticAssignedDriver returns a boolean if a field has been set.

### SetStaticAssignedDriver

`func (o *VehicleResponse) SetStaticAssignedDriver(v DriverTinyResponse)`

SetStaticAssignedDriver gets a reference to the given DriverTinyResponse and assigns it to the StaticAssignedDriver field.

### GetTags

`func (o *VehicleResponse) GetTags() []TagTinyResponse`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *VehicleResponse) GetTagsOk() ([]TagTinyResponse, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTags

`func (o *VehicleResponse) HasTags() bool`

HasTags returns a boolean if a field has been set.

### SetTags

`func (o *VehicleResponse) SetTags(v []TagTinyResponse)`

SetTags gets a reference to the given []TagTinyResponse and assigns it to the Tags field.

### GetVin

`func (o *VehicleResponse) GetVin() string`

GetVin returns the Vin field if non-nil, zero value otherwise.

### GetVinOk

`func (o *VehicleResponse) GetVinOk() (string, bool)`

GetVinOk returns a tuple with the Vin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVin

`func (o *VehicleResponse) HasVin() bool`

HasVin returns a boolean if a field has been set.

### SetVin

`func (o *VehicleResponse) SetVin(v string)`

SetVin gets a reference to the given string and assigns it to the Vin field.

### GetYear

`func (o *VehicleResponse) GetYear() string`

GetYear returns the Year field if non-nil, zero value otherwise.

### GetYearOk

`func (o *VehicleResponse) GetYearOk() (string, bool)`

GetYearOk returns a tuple with the Year field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasYear

`func (o *VehicleResponse) HasYear() bool`

HasYear returns a boolean if a field has been set.

### SetYear

`func (o *VehicleResponse) SetYear(v string)`

SetYear gets a reference to the given string and assigns it to the Year field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


