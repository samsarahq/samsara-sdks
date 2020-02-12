# V1Asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssetSerialNumber** | Pointer to **string** | Serial number of the host asset | [optional] 
**Cable** | Pointer to [**[]V1AssetCable**](V1Asset_cable.md) | The cable connected to the asset | [optional] 
**EngineHours** | Pointer to **int32** | Engine hours | [optional] 
**Id** | Pointer to **int64** | Asset ID | 
**Name** | Pointer to **string** | Asset name | [optional] 
**VehicleId** | Pointer to **int64** | The ID of the Vehicle associated to the Asset (if present) | [optional] 

## Methods

### GetAssetSerialNumber

`func (o *V1Asset) GetAssetSerialNumber() string`

GetAssetSerialNumber returns the AssetSerialNumber field if non-nil, zero value otherwise.

### GetAssetSerialNumberOk

`func (o *V1Asset) GetAssetSerialNumberOk() (string, bool)`

GetAssetSerialNumberOk returns a tuple with the AssetSerialNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAssetSerialNumber

`func (o *V1Asset) HasAssetSerialNumber() bool`

HasAssetSerialNumber returns a boolean if a field has been set.

### SetAssetSerialNumber

`func (o *V1Asset) SetAssetSerialNumber(v string)`

SetAssetSerialNumber gets a reference to the given string and assigns it to the AssetSerialNumber field.

### GetCable

`func (o *V1Asset) GetCable() []V1AssetCable`

GetCable returns the Cable field if non-nil, zero value otherwise.

### GetCableOk

`func (o *V1Asset) GetCableOk() ([]V1AssetCable, bool)`

GetCableOk returns a tuple with the Cable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCable

`func (o *V1Asset) HasCable() bool`

HasCable returns a boolean if a field has been set.

### SetCable

`func (o *V1Asset) SetCable(v []V1AssetCable)`

SetCable gets a reference to the given []V1AssetCable and assigns it to the Cable field.

### GetEngineHours

`func (o *V1Asset) GetEngineHours() int32`

GetEngineHours returns the EngineHours field if non-nil, zero value otherwise.

### GetEngineHoursOk

`func (o *V1Asset) GetEngineHoursOk() (int32, bool)`

GetEngineHoursOk returns a tuple with the EngineHours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineHours

`func (o *V1Asset) HasEngineHours() bool`

HasEngineHours returns a boolean if a field has been set.

### SetEngineHours

`func (o *V1Asset) SetEngineHours(v int32)`

SetEngineHours gets a reference to the given int32 and assigns it to the EngineHours field.

### GetId

`func (o *V1Asset) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1Asset) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1Asset) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1Asset) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetName

`func (o *V1Asset) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *V1Asset) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *V1Asset) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *V1Asset) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetVehicleId

`func (o *V1Asset) GetVehicleId() int64`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1Asset) GetVehicleIdOk() (int64, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1Asset) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1Asset) SetVehicleId(v int64)`

SetVehicleId gets a reference to the given int64 and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


