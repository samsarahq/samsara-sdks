# V1HosLogsSummaryResponsePagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EndCursor** | Pointer to **string** | Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request&#39;s &#39;after&#39; query parameter. | 
**HasNextPage** | Pointer to **bool** | True if there are more pages of results after this response. | 

## Methods

### GetEndCursor

`func (o *V1HosLogsSummaryResponsePagination) GetEndCursor() string`

GetEndCursor returns the EndCursor field if non-nil, zero value otherwise.

### GetEndCursorOk

`func (o *V1HosLogsSummaryResponsePagination) GetEndCursorOk() (string, bool)`

GetEndCursorOk returns a tuple with the EndCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndCursor

`func (o *V1HosLogsSummaryResponsePagination) HasEndCursor() bool`

HasEndCursor returns a boolean if a field has been set.

### SetEndCursor

`func (o *V1HosLogsSummaryResponsePagination) SetEndCursor(v string)`

SetEndCursor gets a reference to the given string and assigns it to the EndCursor field.

### GetHasNextPage

`func (o *V1HosLogsSummaryResponsePagination) GetHasNextPage() bool`

GetHasNextPage returns the HasNextPage field if non-nil, zero value otherwise.

### GetHasNextPageOk

`func (o *V1HosLogsSummaryResponsePagination) GetHasNextPageOk() (bool, bool)`

GetHasNextPageOk returns a tuple with the HasNextPage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHasNextPage

`func (o *V1HosLogsSummaryResponsePagination) HasHasNextPage() bool`

HasHasNextPage returns a boolean if a field has been set.

### SetHasNextPage

`func (o *V1HosLogsSummaryResponsePagination) SetHasNextPage(v bool)`

SetHasNextPage gets a reference to the given bool and assigns it to the HasNextPage field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


