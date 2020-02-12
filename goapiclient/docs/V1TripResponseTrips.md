# V1TripResponseTrips

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssetIds** | Pointer to **[]int64** | List of associated asset IDs | [optional] 
**CodriverIds** | Pointer to **[]int64** | List of codriver IDs | [optional] 
**DistanceMeters** | Pointer to **int32** | Length of the trip in meters. This value is calculated from the GPS data collected by the Samsara Vehicle Gateway. | [optional] 
**DriverId** | Pointer to **int32** | ID of the driver. | [optional] 
**EndAddress** | Pointer to [**V1TripResponseEndAddress**](V1TripResponse_endAddress.md) |  | [optional] 
**EndCoordinates** | Pointer to [**V1TripResponseEndCoordinates**](V1TripResponse_endCoordinates.md) |  | [optional] 
**EndLocation** | Pointer to **string** | Geocoded street address of start (latitude, longitude) coordinates. | [optional] 
**EndMs** | Pointer to **int32** | End of the trip in UNIX milliseconds. Ongoing trips are indicated by an endMs value of 9223372036854775807. | [optional] 
**EndOdometer** | Pointer to **int32** | Odometer reading (in meters) at the end of the trip. This is read from the vehicle&#39;s on-board diagnostics. If Samsara cannot read the vehicle&#39;s odometer values from on-board diagnostics, this value will be 0. | [optional] 
**FuelConsumedMl** | Pointer to **int32** | Amount in milliliters of fuel consumed on this trip. | [optional] 
**StartAddress** | Pointer to [**V1TripResponseStartAddress**](V1TripResponse_startAddress.md) |  | [optional] 
**StartCoordinates** | Pointer to [**V1TripResponseStartCoordinates**](V1TripResponse_startCoordinates.md) |  | [optional] 
**StartLocation** | Pointer to **string** | Geocoded street address of start (latitude, longitude) coordinates. | [optional] 
**StartMs** | Pointer to **int32** | Beginning of the trip in UNIX milliseconds. | [optional] 
**StartOdometer** | Pointer to **int32** | Odometer reading (in meters) at the beginning of the trip. This is read from the vehicle&#39;s on-board diagnostics. If Samsara cannot read the vehicle&#39;s odometer values from on-board diagnostics, this value will be 0. | [optional] 
**TollMeters** | Pointer to **int32** | Length in meters trip spent on toll roads. | [optional] 

## Methods

### GetAssetIds

`func (o *V1TripResponseTrips) GetAssetIds() []int64`

GetAssetIds returns the AssetIds field if non-nil, zero value otherwise.

### GetAssetIdsOk

`func (o *V1TripResponseTrips) GetAssetIdsOk() ([]int64, bool)`

GetAssetIdsOk returns a tuple with the AssetIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAssetIds

`func (o *V1TripResponseTrips) HasAssetIds() bool`

HasAssetIds returns a boolean if a field has been set.

### SetAssetIds

`func (o *V1TripResponseTrips) SetAssetIds(v []int64)`

SetAssetIds gets a reference to the given []int64 and assigns it to the AssetIds field.

### GetCodriverIds

`func (o *V1TripResponseTrips) GetCodriverIds() []int64`

GetCodriverIds returns the CodriverIds field if non-nil, zero value otherwise.

### GetCodriverIdsOk

`func (o *V1TripResponseTrips) GetCodriverIdsOk() ([]int64, bool)`

GetCodriverIdsOk returns a tuple with the CodriverIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCodriverIds

`func (o *V1TripResponseTrips) HasCodriverIds() bool`

HasCodriverIds returns a boolean if a field has been set.

### SetCodriverIds

`func (o *V1TripResponseTrips) SetCodriverIds(v []int64)`

SetCodriverIds gets a reference to the given []int64 and assigns it to the CodriverIds field.

### GetDistanceMeters

`func (o *V1TripResponseTrips) GetDistanceMeters() int32`

GetDistanceMeters returns the DistanceMeters field if non-nil, zero value otherwise.

### GetDistanceMetersOk

`func (o *V1TripResponseTrips) GetDistanceMetersOk() (int32, bool)`

GetDistanceMetersOk returns a tuple with the DistanceMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDistanceMeters

`func (o *V1TripResponseTrips) HasDistanceMeters() bool`

HasDistanceMeters returns a boolean if a field has been set.

### SetDistanceMeters

`func (o *V1TripResponseTrips) SetDistanceMeters(v int32)`

SetDistanceMeters gets a reference to the given int32 and assigns it to the DistanceMeters field.

### GetDriverId

`func (o *V1TripResponseTrips) GetDriverId() int32`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1TripResponseTrips) GetDriverIdOk() (int32, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1TripResponseTrips) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1TripResponseTrips) SetDriverId(v int32)`

SetDriverId gets a reference to the given int32 and assigns it to the DriverId field.

### GetEndAddress

`func (o *V1TripResponseTrips) GetEndAddress() V1TripResponseEndAddress`

GetEndAddress returns the EndAddress field if non-nil, zero value otherwise.

### GetEndAddressOk

`func (o *V1TripResponseTrips) GetEndAddressOk() (V1TripResponseEndAddress, bool)`

GetEndAddressOk returns a tuple with the EndAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndAddress

`func (o *V1TripResponseTrips) HasEndAddress() bool`

HasEndAddress returns a boolean if a field has been set.

### SetEndAddress

`func (o *V1TripResponseTrips) SetEndAddress(v V1TripResponseEndAddress)`

SetEndAddress gets a reference to the given V1TripResponseEndAddress and assigns it to the EndAddress field.

### GetEndCoordinates

`func (o *V1TripResponseTrips) GetEndCoordinates() V1TripResponseEndCoordinates`

GetEndCoordinates returns the EndCoordinates field if non-nil, zero value otherwise.

### GetEndCoordinatesOk

`func (o *V1TripResponseTrips) GetEndCoordinatesOk() (V1TripResponseEndCoordinates, bool)`

GetEndCoordinatesOk returns a tuple with the EndCoordinates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndCoordinates

`func (o *V1TripResponseTrips) HasEndCoordinates() bool`

HasEndCoordinates returns a boolean if a field has been set.

### SetEndCoordinates

`func (o *V1TripResponseTrips) SetEndCoordinates(v V1TripResponseEndCoordinates)`

SetEndCoordinates gets a reference to the given V1TripResponseEndCoordinates and assigns it to the EndCoordinates field.

### GetEndLocation

`func (o *V1TripResponseTrips) GetEndLocation() string`

GetEndLocation returns the EndLocation field if non-nil, zero value otherwise.

### GetEndLocationOk

`func (o *V1TripResponseTrips) GetEndLocationOk() (string, bool)`

GetEndLocationOk returns a tuple with the EndLocation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndLocation

`func (o *V1TripResponseTrips) HasEndLocation() bool`

HasEndLocation returns a boolean if a field has been set.

### SetEndLocation

`func (o *V1TripResponseTrips) SetEndLocation(v string)`

SetEndLocation gets a reference to the given string and assigns it to the EndLocation field.

### GetEndMs

`func (o *V1TripResponseTrips) GetEndMs() int32`

GetEndMs returns the EndMs field if non-nil, zero value otherwise.

### GetEndMsOk

`func (o *V1TripResponseTrips) GetEndMsOk() (int32, bool)`

GetEndMsOk returns a tuple with the EndMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndMs

`func (o *V1TripResponseTrips) HasEndMs() bool`

HasEndMs returns a boolean if a field has been set.

### SetEndMs

`func (o *V1TripResponseTrips) SetEndMs(v int32)`

SetEndMs gets a reference to the given int32 and assigns it to the EndMs field.

### GetEndOdometer

`func (o *V1TripResponseTrips) GetEndOdometer() int32`

GetEndOdometer returns the EndOdometer field if non-nil, zero value otherwise.

### GetEndOdometerOk

`func (o *V1TripResponseTrips) GetEndOdometerOk() (int32, bool)`

GetEndOdometerOk returns a tuple with the EndOdometer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndOdometer

`func (o *V1TripResponseTrips) HasEndOdometer() bool`

HasEndOdometer returns a boolean if a field has been set.

### SetEndOdometer

`func (o *V1TripResponseTrips) SetEndOdometer(v int32)`

SetEndOdometer gets a reference to the given int32 and assigns it to the EndOdometer field.

### GetFuelConsumedMl

`func (o *V1TripResponseTrips) GetFuelConsumedMl() int32`

GetFuelConsumedMl returns the FuelConsumedMl field if non-nil, zero value otherwise.

### GetFuelConsumedMlOk

`func (o *V1TripResponseTrips) GetFuelConsumedMlOk() (int32, bool)`

GetFuelConsumedMlOk returns a tuple with the FuelConsumedMl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFuelConsumedMl

`func (o *V1TripResponseTrips) HasFuelConsumedMl() bool`

HasFuelConsumedMl returns a boolean if a field has been set.

### SetFuelConsumedMl

`func (o *V1TripResponseTrips) SetFuelConsumedMl(v int32)`

SetFuelConsumedMl gets a reference to the given int32 and assigns it to the FuelConsumedMl field.

### GetStartAddress

`func (o *V1TripResponseTrips) GetStartAddress() V1TripResponseStartAddress`

GetStartAddress returns the StartAddress field if non-nil, zero value otherwise.

### GetStartAddressOk

`func (o *V1TripResponseTrips) GetStartAddressOk() (V1TripResponseStartAddress, bool)`

GetStartAddressOk returns a tuple with the StartAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartAddress

`func (o *V1TripResponseTrips) HasStartAddress() bool`

HasStartAddress returns a boolean if a field has been set.

### SetStartAddress

`func (o *V1TripResponseTrips) SetStartAddress(v V1TripResponseStartAddress)`

SetStartAddress gets a reference to the given V1TripResponseStartAddress and assigns it to the StartAddress field.

### GetStartCoordinates

`func (o *V1TripResponseTrips) GetStartCoordinates() V1TripResponseStartCoordinates`

GetStartCoordinates returns the StartCoordinates field if non-nil, zero value otherwise.

### GetStartCoordinatesOk

`func (o *V1TripResponseTrips) GetStartCoordinatesOk() (V1TripResponseStartCoordinates, bool)`

GetStartCoordinatesOk returns a tuple with the StartCoordinates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartCoordinates

`func (o *V1TripResponseTrips) HasStartCoordinates() bool`

HasStartCoordinates returns a boolean if a field has been set.

### SetStartCoordinates

`func (o *V1TripResponseTrips) SetStartCoordinates(v V1TripResponseStartCoordinates)`

SetStartCoordinates gets a reference to the given V1TripResponseStartCoordinates and assigns it to the StartCoordinates field.

### GetStartLocation

`func (o *V1TripResponseTrips) GetStartLocation() string`

GetStartLocation returns the StartLocation field if non-nil, zero value otherwise.

### GetStartLocationOk

`func (o *V1TripResponseTrips) GetStartLocationOk() (string, bool)`

GetStartLocationOk returns a tuple with the StartLocation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartLocation

`func (o *V1TripResponseTrips) HasStartLocation() bool`

HasStartLocation returns a boolean if a field has been set.

### SetStartLocation

`func (o *V1TripResponseTrips) SetStartLocation(v string)`

SetStartLocation gets a reference to the given string and assigns it to the StartLocation field.

### GetStartMs

`func (o *V1TripResponseTrips) GetStartMs() int32`

GetStartMs returns the StartMs field if non-nil, zero value otherwise.

### GetStartMsOk

`func (o *V1TripResponseTrips) GetStartMsOk() (int32, bool)`

GetStartMsOk returns a tuple with the StartMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartMs

`func (o *V1TripResponseTrips) HasStartMs() bool`

HasStartMs returns a boolean if a field has been set.

### SetStartMs

`func (o *V1TripResponseTrips) SetStartMs(v int32)`

SetStartMs gets a reference to the given int32 and assigns it to the StartMs field.

### GetStartOdometer

`func (o *V1TripResponseTrips) GetStartOdometer() int32`

GetStartOdometer returns the StartOdometer field if non-nil, zero value otherwise.

### GetStartOdometerOk

`func (o *V1TripResponseTrips) GetStartOdometerOk() (int32, bool)`

GetStartOdometerOk returns a tuple with the StartOdometer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartOdometer

`func (o *V1TripResponseTrips) HasStartOdometer() bool`

HasStartOdometer returns a boolean if a field has been set.

### SetStartOdometer

`func (o *V1TripResponseTrips) SetStartOdometer(v int32)`

SetStartOdometer gets a reference to the given int32 and assigns it to the StartOdometer field.

### GetTollMeters

`func (o *V1TripResponseTrips) GetTollMeters() int32`

GetTollMeters returns the TollMeters field if non-nil, zero value otherwise.

### GetTollMetersOk

`func (o *V1TripResponseTrips) GetTollMetersOk() (int32, bool)`

GetTollMetersOk returns a tuple with the TollMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTollMeters

`func (o *V1TripResponseTrips) HasTollMeters() bool`

HasTollMeters returns a boolean if a field has been set.

### SetTollMeters

`func (o *V1TripResponseTrips) SetTollMeters(v int32)`

SetTollMeters gets a reference to the given int32 and assigns it to the TollMeters field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


