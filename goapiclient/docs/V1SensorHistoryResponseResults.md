# V1SensorHistoryResponseResults

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Series** | Pointer to **[]int64** | List of datapoints, one for each requested (sensor, field) pair. | [optional] 
**TimeMs** | Pointer to **int32** | Timestamp in UNIX milliseconds. | [optional] 

## Methods

### GetSeries

`func (o *V1SensorHistoryResponseResults) GetSeries() []int64`

GetSeries returns the Series field if non-nil, zero value otherwise.

### GetSeriesOk

`func (o *V1SensorHistoryResponseResults) GetSeriesOk() ([]int64, bool)`

GetSeriesOk returns a tuple with the Series field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSeries

`func (o *V1SensorHistoryResponseResults) HasSeries() bool`

HasSeries returns a boolean if a field has been set.

### SetSeries

`func (o *V1SensorHistoryResponseResults) SetSeries(v []int64)`

SetSeries gets a reference to the given []int64 and assigns it to the Series field.

### GetTimeMs

`func (o *V1SensorHistoryResponseResults) GetTimeMs() int32`

GetTimeMs returns the TimeMs field if non-nil, zero value otherwise.

### GetTimeMsOk

`func (o *V1SensorHistoryResponseResults) GetTimeMsOk() (int32, bool)`

GetTimeMsOk returns a tuple with the TimeMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTimeMs

`func (o *V1SensorHistoryResponseResults) HasTimeMs() bool`

HasTimeMs returns a boolean if a field has been set.

### SetTimeMs

`func (o *V1SensorHistoryResponseResults) SetTimeMs(v int32)`

SetTimeMs gets a reference to the given int32 and assigns it to the TimeMs field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


