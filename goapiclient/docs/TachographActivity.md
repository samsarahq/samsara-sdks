# TachographActivity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EndTime** | Pointer to **string** | End time of state in RFC 3339 format. | [optional] 
**IsManualEntry** | Pointer to **bool** | A flag indicating whether the activity was manually entered by the driver. If this is &#x60;true&#x60;, the state cannot be \&quot;UNKNOWN\&quot; | [optional] 
**StartTime** | Pointer to **string** | Start time of state in RFC 3339 format. | [optional] 
**State** | Pointer to **string** | Tachograph activity state | [optional] 

## Methods

### GetEndTime

`func (o *TachographActivity) GetEndTime() string`

GetEndTime returns the EndTime field if non-nil, zero value otherwise.

### GetEndTimeOk

`func (o *TachographActivity) GetEndTimeOk() (string, bool)`

GetEndTimeOk returns a tuple with the EndTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndTime

`func (o *TachographActivity) HasEndTime() bool`

HasEndTime returns a boolean if a field has been set.

### SetEndTime

`func (o *TachographActivity) SetEndTime(v string)`

SetEndTime gets a reference to the given string and assigns it to the EndTime field.

### GetIsManualEntry

`func (o *TachographActivity) GetIsManualEntry() bool`

GetIsManualEntry returns the IsManualEntry field if non-nil, zero value otherwise.

### GetIsManualEntryOk

`func (o *TachographActivity) GetIsManualEntryOk() (bool, bool)`

GetIsManualEntryOk returns a tuple with the IsManualEntry field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasIsManualEntry

`func (o *TachographActivity) HasIsManualEntry() bool`

HasIsManualEntry returns a boolean if a field has been set.

### SetIsManualEntry

`func (o *TachographActivity) SetIsManualEntry(v bool)`

SetIsManualEntry gets a reference to the given bool and assigns it to the IsManualEntry field.

### GetStartTime

`func (o *TachographActivity) GetStartTime() string`

GetStartTime returns the StartTime field if non-nil, zero value otherwise.

### GetStartTimeOk

`func (o *TachographActivity) GetStartTimeOk() (string, bool)`

GetStartTimeOk returns a tuple with the StartTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartTime

`func (o *TachographActivity) HasStartTime() bool`

HasStartTime returns a boolean if a field has been set.

### SetStartTime

`func (o *TachographActivity) SetStartTime(v string)`

SetStartTime gets a reference to the given string and assigns it to the StartTime field.

### GetState

`func (o *TachographActivity) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *TachographActivity) GetStateOk() (string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasState

`func (o *TachographActivity) HasState() bool`

HasState returns a boolean if a field has been set.

### SetState

`func (o *TachographActivity) SetState(v string)`

SetState gets a reference to the given string and assigns it to the State field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


