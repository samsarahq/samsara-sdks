# VehicleGpsDistanceMeters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Time** | Pointer to **string** | UTC timestamp in RFC 3339 milliseconds format. | [optional] 
**Value** | Pointer to **float64** | Number of meters the vehicle has traveled since the gateway was installed. | [optional] 

## Methods

### GetTime

`func (o *VehicleGpsDistanceMeters) GetTime() string`

GetTime returns the Time field if non-nil, zero value otherwise.

### GetTimeOk

`func (o *VehicleGpsDistanceMeters) GetTimeOk() (string, bool)`

GetTimeOk returns a tuple with the Time field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTime

`func (o *VehicleGpsDistanceMeters) HasTime() bool`

HasTime returns a boolean if a field has been set.

### SetTime

`func (o *VehicleGpsDistanceMeters) SetTime(v string)`

SetTime gets a reference to the given string and assigns it to the Time field.

### GetValue

`func (o *VehicleGpsDistanceMeters) GetValue() float64`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *VehicleGpsDistanceMeters) GetValueOk() (float64, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasValue

`func (o *VehicleGpsDistanceMeters) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValue

`func (o *VehicleGpsDistanceMeters) SetValue(v float64)`

SetValue gets a reference to the given float64 and assigns it to the Value field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


