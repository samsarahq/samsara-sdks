# VehicleFuelPercent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Time** | Pointer to **string** | UTC timestamp in RFC 3339 milliseconds format. | [optional] 
**Value** | Pointer to **int32** | Percent of fuel in the vehicle as read by the vehicle gateway. | [optional] 

## Methods

### GetTime

`func (o *VehicleFuelPercent) GetTime() string`

GetTime returns the Time field if non-nil, zero value otherwise.

### GetTimeOk

`func (o *VehicleFuelPercent) GetTimeOk() (string, bool)`

GetTimeOk returns a tuple with the Time field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTime

`func (o *VehicleFuelPercent) HasTime() bool`

HasTime returns a boolean if a field has been set.

### SetTime

`func (o *VehicleFuelPercent) SetTime(v string)`

SetTime gets a reference to the given string and assigns it to the Time field.

### GetValue

`func (o *VehicleFuelPercent) GetValue() int32`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *VehicleFuelPercent) GetValueOk() (int32, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasValue

`func (o *VehicleFuelPercent) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValue

`func (o *VehicleFuelPercent) SetValue(v int32)`

SetValue gets a reference to the given int32 and assigns it to the Value field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


