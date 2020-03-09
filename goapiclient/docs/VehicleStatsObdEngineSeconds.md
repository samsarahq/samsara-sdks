# VehicleStatsObdEngineSeconds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Time** | Pointer to [**time.Time**](time.Time.md) | UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | 
**Value** | Pointer to **int64** | Number of seconds the vehicle&#39;s engine has been on according to the on-baord diagnostics. | 

## Methods

### GetTime

`func (o *VehicleStatsObdEngineSeconds) GetTime() time.Time`

GetTime returns the Time field if non-nil, zero value otherwise.

### GetTimeOk

`func (o *VehicleStatsObdEngineSeconds) GetTimeOk() (time.Time, bool)`

GetTimeOk returns a tuple with the Time field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTime

`func (o *VehicleStatsObdEngineSeconds) HasTime() bool`

HasTime returns a boolean if a field has been set.

### SetTime

`func (o *VehicleStatsObdEngineSeconds) SetTime(v time.Time)`

SetTime gets a reference to the given time.Time and assigns it to the Time field.

### GetValue

`func (o *VehicleStatsObdEngineSeconds) GetValue() int64`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *VehicleStatsObdEngineSeconds) GetValueOk() (int64, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasValue

`func (o *VehicleStatsObdEngineSeconds) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValue

`func (o *VehicleStatsObdEngineSeconds) SetValue(v int64)`

SetValue gets a reference to the given int64 and assigns it to the Value field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


