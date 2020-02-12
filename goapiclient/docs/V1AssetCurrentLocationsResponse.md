# V1AssetCurrentLocationsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssetSerialNumber** | Pointer to **string** | Asset serial number | [optional] 
**Cable** | Pointer to [**V1AssetCurrentLocationsResponseCable**](V1AssetCurrentLocationsResponse_cable.md) |  | [optional] 
**EngineHours** | Pointer to **int32** | Engine hours | [optional] 
**Id** | Pointer to **int64** | Asset ID | 
**Location** | Pointer to [**[]V1AssetCurrentLocation**](V1AssetCurrentLocation.md) | Current location of an asset | [optional] 
**Name** | Pointer to **string** | Asset name | [optional] 

## Methods

### GetAssetSerialNumber

`func (o *V1AssetCurrentLocationsResponse) GetAssetSerialNumber() string`

GetAssetSerialNumber returns the AssetSerialNumber field if non-nil, zero value otherwise.

### GetAssetSerialNumberOk

`func (o *V1AssetCurrentLocationsResponse) GetAssetSerialNumberOk() (string, bool)`

GetAssetSerialNumberOk returns a tuple with the AssetSerialNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAssetSerialNumber

`func (o *V1AssetCurrentLocationsResponse) HasAssetSerialNumber() bool`

HasAssetSerialNumber returns a boolean if a field has been set.

### SetAssetSerialNumber

`func (o *V1AssetCurrentLocationsResponse) SetAssetSerialNumber(v string)`

SetAssetSerialNumber gets a reference to the given string and assigns it to the AssetSerialNumber field.

### GetCable

`func (o *V1AssetCurrentLocationsResponse) GetCable() V1AssetCurrentLocationsResponseCable`

GetCable returns the Cable field if non-nil, zero value otherwise.

### GetCableOk

`func (o *V1AssetCurrentLocationsResponse) GetCableOk() (V1AssetCurrentLocationsResponseCable, bool)`

GetCableOk returns a tuple with the Cable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCable

`func (o *V1AssetCurrentLocationsResponse) HasCable() bool`

HasCable returns a boolean if a field has been set.

### SetCable

`func (o *V1AssetCurrentLocationsResponse) SetCable(v V1AssetCurrentLocationsResponseCable)`

SetCable gets a reference to the given V1AssetCurrentLocationsResponseCable and assigns it to the Cable field.

### GetEngineHours

`func (o *V1AssetCurrentLocationsResponse) GetEngineHours() int32`

GetEngineHours returns the EngineHours field if non-nil, zero value otherwise.

### GetEngineHoursOk

`func (o *V1AssetCurrentLocationsResponse) GetEngineHoursOk() (int32, bool)`

GetEngineHoursOk returns a tuple with the EngineHours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineHours

`func (o *V1AssetCurrentLocationsResponse) HasEngineHours() bool`

HasEngineHours returns a boolean if a field has been set.

### SetEngineHours

`func (o *V1AssetCurrentLocationsResponse) SetEngineHours(v int32)`

SetEngineHours gets a reference to the given int32 and assigns it to the EngineHours field.

### GetId

`func (o *V1AssetCurrentLocationsResponse) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1AssetCurrentLocationsResponse) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1AssetCurrentLocationsResponse) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1AssetCurrentLocationsResponse) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetLocation

`func (o *V1AssetCurrentLocationsResponse) GetLocation() []V1AssetCurrentLocation`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *V1AssetCurrentLocationsResponse) GetLocationOk() ([]V1AssetCurrentLocation, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocation

`func (o *V1AssetCurrentLocationsResponse) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### SetLocation

`func (o *V1AssetCurrentLocationsResponse) SetLocation(v []V1AssetCurrentLocation)`

SetLocation gets a reference to the given []V1AssetCurrentLocation and assigns it to the Location field.

### GetName

`func (o *V1AssetCurrentLocationsResponse) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *V1AssetCurrentLocationsResponse) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *V1AssetCurrentLocationsResponse) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *V1AssetCurrentLocationsResponse) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


