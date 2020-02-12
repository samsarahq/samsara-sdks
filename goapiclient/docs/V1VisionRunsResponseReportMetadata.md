# V1VisionRunsResponseReportMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ItemsPerMinute** | Pointer to **float32** | Returns average scanned items per minute. Should be used instead of scanRate. | [optional] 
**NoReadCount** | Pointer to **int64** | Returns no read count for the run. Should be used instead of noReadScansCount | [optional] 
**RejectCount** | Pointer to **int64** | Returns reject count for the run. Should be used instead of failedScansCount | [optional] 
**SuccessCount** | Pointer to **int64** | Returns success count for the run. Should be used instead of successfulScansCount | [optional] 

## Methods

### GetItemsPerMinute

`func (o *V1VisionRunsResponseReportMetadata) GetItemsPerMinute() float32`

GetItemsPerMinute returns the ItemsPerMinute field if non-nil, zero value otherwise.

### GetItemsPerMinuteOk

`func (o *V1VisionRunsResponseReportMetadata) GetItemsPerMinuteOk() (float32, bool)`

GetItemsPerMinuteOk returns a tuple with the ItemsPerMinute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasItemsPerMinute

`func (o *V1VisionRunsResponseReportMetadata) HasItemsPerMinute() bool`

HasItemsPerMinute returns a boolean if a field has been set.

### SetItemsPerMinute

`func (o *V1VisionRunsResponseReportMetadata) SetItemsPerMinute(v float32)`

SetItemsPerMinute gets a reference to the given float32 and assigns it to the ItemsPerMinute field.

### GetNoReadCount

`func (o *V1VisionRunsResponseReportMetadata) GetNoReadCount() int64`

GetNoReadCount returns the NoReadCount field if non-nil, zero value otherwise.

### GetNoReadCountOk

`func (o *V1VisionRunsResponseReportMetadata) GetNoReadCountOk() (int64, bool)`

GetNoReadCountOk returns a tuple with the NoReadCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNoReadCount

`func (o *V1VisionRunsResponseReportMetadata) HasNoReadCount() bool`

HasNoReadCount returns a boolean if a field has been set.

### SetNoReadCount

`func (o *V1VisionRunsResponseReportMetadata) SetNoReadCount(v int64)`

SetNoReadCount gets a reference to the given int64 and assigns it to the NoReadCount field.

### GetRejectCount

`func (o *V1VisionRunsResponseReportMetadata) GetRejectCount() int64`

GetRejectCount returns the RejectCount field if non-nil, zero value otherwise.

### GetRejectCountOk

`func (o *V1VisionRunsResponseReportMetadata) GetRejectCountOk() (int64, bool)`

GetRejectCountOk returns a tuple with the RejectCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRejectCount

`func (o *V1VisionRunsResponseReportMetadata) HasRejectCount() bool`

HasRejectCount returns a boolean if a field has been set.

### SetRejectCount

`func (o *V1VisionRunsResponseReportMetadata) SetRejectCount(v int64)`

SetRejectCount gets a reference to the given int64 and assigns it to the RejectCount field.

### GetSuccessCount

`func (o *V1VisionRunsResponseReportMetadata) GetSuccessCount() int64`

GetSuccessCount returns the SuccessCount field if non-nil, zero value otherwise.

### GetSuccessCountOk

`func (o *V1VisionRunsResponseReportMetadata) GetSuccessCountOk() (int64, bool)`

GetSuccessCountOk returns a tuple with the SuccessCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSuccessCount

`func (o *V1VisionRunsResponseReportMetadata) HasSuccessCount() bool`

HasSuccessCount returns a boolean if a field has been set.

### SetSuccessCount

`func (o *V1VisionRunsResponseReportMetadata) SetSuccessCount(v int64)`

SetSuccessCount gets a reference to the given int64 and assigns it to the SuccessCount field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


