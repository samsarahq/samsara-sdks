# InlineObject9

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EndMs** | Pointer to **int32** | End of the time range, specified in milliseconds UNIX time. | 
**FillMissing** | Pointer to **string** |  | [optional] [default to FILL_MISSING_WITH_NULL]
**Series** | Pointer to [**[]V1SensorsHistorySeries**](_v1_sensors_history_series.md) |  | 
**StartMs** | Pointer to **int32** | Beginning of the time range, specified in milliseconds UNIX time. | 
**StepMs** | Pointer to **int32** | Time resolution for which data should be returned, in milliseconds. Specifying 3600000 will return data at hour intervals. | 

## Methods

### GetEndMs

`func (o *InlineObject9) GetEndMs() int32`

GetEndMs returns the EndMs field if non-nil, zero value otherwise.

### GetEndMsOk

`func (o *InlineObject9) GetEndMsOk() (int32, bool)`

GetEndMsOk returns a tuple with the EndMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndMs

`func (o *InlineObject9) HasEndMs() bool`

HasEndMs returns a boolean if a field has been set.

### SetEndMs

`func (o *InlineObject9) SetEndMs(v int32)`

SetEndMs gets a reference to the given int32 and assigns it to the EndMs field.

### GetFillMissing

`func (o *InlineObject9) GetFillMissing() string`

GetFillMissing returns the FillMissing field if non-nil, zero value otherwise.

### GetFillMissingOk

`func (o *InlineObject9) GetFillMissingOk() (string, bool)`

GetFillMissingOk returns a tuple with the FillMissing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFillMissing

`func (o *InlineObject9) HasFillMissing() bool`

HasFillMissing returns a boolean if a field has been set.

### SetFillMissing

`func (o *InlineObject9) SetFillMissing(v string)`

SetFillMissing gets a reference to the given string and assigns it to the FillMissing field.

### GetSeries

`func (o *InlineObject9) GetSeries() []V1SensorsHistorySeries`

GetSeries returns the Series field if non-nil, zero value otherwise.

### GetSeriesOk

`func (o *InlineObject9) GetSeriesOk() ([]V1SensorsHistorySeries, bool)`

GetSeriesOk returns a tuple with the Series field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSeries

`func (o *InlineObject9) HasSeries() bool`

HasSeries returns a boolean if a field has been set.

### SetSeries

`func (o *InlineObject9) SetSeries(v []V1SensorsHistorySeries)`

SetSeries gets a reference to the given []V1SensorsHistorySeries and assigns it to the Series field.

### GetStartMs

`func (o *InlineObject9) GetStartMs() int32`

GetStartMs returns the StartMs field if non-nil, zero value otherwise.

### GetStartMsOk

`func (o *InlineObject9) GetStartMsOk() (int32, bool)`

GetStartMsOk returns a tuple with the StartMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartMs

`func (o *InlineObject9) HasStartMs() bool`

HasStartMs returns a boolean if a field has been set.

### SetStartMs

`func (o *InlineObject9) SetStartMs(v int32)`

SetStartMs gets a reference to the given int32 and assigns it to the StartMs field.

### GetStepMs

`func (o *InlineObject9) GetStepMs() int32`

GetStepMs returns the StepMs field if non-nil, zero value otherwise.

### GetStepMsOk

`func (o *InlineObject9) GetStepMsOk() (int32, bool)`

GetStepMsOk returns a tuple with the StepMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStepMs

`func (o *InlineObject9) HasStepMs() bool`

HasStepMs returns a boolean if a field has been set.

### SetStepMs

`func (o *InlineObject9) SetStepMs(v int32)`

SetStepMs gets a reference to the given int32 and assigns it to the StepMs field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


