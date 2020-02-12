# VehicleGpsOdometerMeters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Time** | Pointer to **string** | UTC timestamp in RFC 3339 milliseconds format. | [optional] 
**Value** | Pointer to **int32** | Number of meters the vehicle has traveled according to the GPS distance reported by the vehicle gateway and the manually-specified odometer reading. | [optional] 

## Methods

### GetTime

`func (o *VehicleGpsOdometerMeters) GetTime() string`

GetTime returns the Time field if non-nil, zero value otherwise.

### GetTimeOk

`func (o *VehicleGpsOdometerMeters) GetTimeOk() (string, bool)`

GetTimeOk returns a tuple with the Time field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTime

`func (o *VehicleGpsOdometerMeters) HasTime() bool`

HasTime returns a boolean if a field has been set.

### SetTime

`func (o *VehicleGpsOdometerMeters) SetTime(v string)`

SetTime gets a reference to the given string and assigns it to the Time field.

### GetValue

`func (o *VehicleGpsOdometerMeters) GetValue() int32`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *VehicleGpsOdometerMeters) GetValueOk() (int32, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasValue

`func (o *VehicleGpsOdometerMeters) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValue

`func (o *VehicleGpsOdometerMeters) SetValue(v int32)`

SetValue gets a reference to the given int32 and assigns it to the Value field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


