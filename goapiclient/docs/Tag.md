# Tag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | Unique Samsara ID of this tag. | [optional] 
**Name** | Pointer to **string** | Name of this tag. | [optional] 
**Addresses** | Pointer to [**[]TaggedObject**](TaggedObject.md) | The addresses that belong to this tag. | [optional] 
**Assets** | Pointer to [**[]TaggedObject**](TaggedObject.md) | The trailers, unpowered, and powered assets that belong to this tag. | [optional] 
**Drivers** | Pointer to [**[]TaggedObject**](TaggedObject.md) | The drivers that belong to this tag. | [optional] 
**Machines** | Pointer to [**[]TaggedObject**](TaggedObject.md) | The machines that belong to thistag. | [optional] 
**ParentTag** | Pointer to [**ParentTag**](ParentTag.md) |  | [optional] 
**Sensors** | Pointer to [**[]TaggedObject**](TaggedObject.md) | The sensors that belong to this tag. | [optional] 
**Vehicles** | Pointer to [**[]TaggedObject**](TaggedObject.md) | The vehicles that belong to this tag. | [optional] 

## Methods

### GetId

`func (o *Tag) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Tag) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *Tag) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *Tag) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetName

`func (o *Tag) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Tag) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *Tag) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *Tag) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetAddresses

`func (o *Tag) GetAddresses() []TaggedObject`

GetAddresses returns the Addresses field if non-nil, zero value otherwise.

### GetAddressesOk

`func (o *Tag) GetAddressesOk() ([]TaggedObject, bool)`

GetAddressesOk returns a tuple with the Addresses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAddresses

`func (o *Tag) HasAddresses() bool`

HasAddresses returns a boolean if a field has been set.

### SetAddresses

`func (o *Tag) SetAddresses(v []TaggedObject)`

SetAddresses gets a reference to the given []TaggedObject and assigns it to the Addresses field.

### GetAssets

`func (o *Tag) GetAssets() []TaggedObject`

GetAssets returns the Assets field if non-nil, zero value otherwise.

### GetAssetsOk

`func (o *Tag) GetAssetsOk() ([]TaggedObject, bool)`

GetAssetsOk returns a tuple with the Assets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAssets

`func (o *Tag) HasAssets() bool`

HasAssets returns a boolean if a field has been set.

### SetAssets

`func (o *Tag) SetAssets(v []TaggedObject)`

SetAssets gets a reference to the given []TaggedObject and assigns it to the Assets field.

### GetDrivers

`func (o *Tag) GetDrivers() []TaggedObject`

GetDrivers returns the Drivers field if non-nil, zero value otherwise.

### GetDriversOk

`func (o *Tag) GetDriversOk() ([]TaggedObject, bool)`

GetDriversOk returns a tuple with the Drivers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDrivers

`func (o *Tag) HasDrivers() bool`

HasDrivers returns a boolean if a field has been set.

### SetDrivers

`func (o *Tag) SetDrivers(v []TaggedObject)`

SetDrivers gets a reference to the given []TaggedObject and assigns it to the Drivers field.

### GetMachines

`func (o *Tag) GetMachines() []TaggedObject`

GetMachines returns the Machines field if non-nil, zero value otherwise.

### GetMachinesOk

`func (o *Tag) GetMachinesOk() ([]TaggedObject, bool)`

GetMachinesOk returns a tuple with the Machines field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMachines

`func (o *Tag) HasMachines() bool`

HasMachines returns a boolean if a field has been set.

### SetMachines

`func (o *Tag) SetMachines(v []TaggedObject)`

SetMachines gets a reference to the given []TaggedObject and assigns it to the Machines field.

### GetParentTag

`func (o *Tag) GetParentTag() ParentTag`

GetParentTag returns the ParentTag field if non-nil, zero value otherwise.

### GetParentTagOk

`func (o *Tag) GetParentTagOk() (ParentTag, bool)`

GetParentTagOk returns a tuple with the ParentTag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasParentTag

`func (o *Tag) HasParentTag() bool`

HasParentTag returns a boolean if a field has been set.

### SetParentTag

`func (o *Tag) SetParentTag(v ParentTag)`

SetParentTag gets a reference to the given ParentTag and assigns it to the ParentTag field.

### GetSensors

`func (o *Tag) GetSensors() []TaggedObject`

GetSensors returns the Sensors field if non-nil, zero value otherwise.

### GetSensorsOk

`func (o *Tag) GetSensorsOk() ([]TaggedObject, bool)`

GetSensorsOk returns a tuple with the Sensors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSensors

`func (o *Tag) HasSensors() bool`

HasSensors returns a boolean if a field has been set.

### SetSensors

`func (o *Tag) SetSensors(v []TaggedObject)`

SetSensors gets a reference to the given []TaggedObject and assigns it to the Sensors field.

### GetVehicles

`func (o *Tag) GetVehicles() []TaggedObject`

GetVehicles returns the Vehicles field if non-nil, zero value otherwise.

### GetVehiclesOk

`func (o *Tag) GetVehiclesOk() ([]TaggedObject, bool)`

GetVehiclesOk returns a tuple with the Vehicles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicles

`func (o *Tag) HasVehicles() bool`

HasVehicles returns a boolean if a field has been set.

### SetVehicles

`func (o *Tag) SetVehicles(v []TaggedObject)`

SetVehicles gets a reference to the given []TaggedObject and assigns it to the Vehicles field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


