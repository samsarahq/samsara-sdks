# V1Pagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EndCursor** | Pointer to **string** | Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request&#39;s &#39;startingAfter&#39; query parameter. | 
**HasNextPage** | Pointer to **bool** | True if there are more pages of results after this response. | 
**HasPrevPage** | Pointer to **bool** | True if there are more pages of results before this response. | 
**StartCursor** | Pointer to **string** | Cursor identifier representing the first element in the response. This value should be used in conjunction with a subsequent request&#39;s &#39;ending_before&#39; query parameter. | 

## Methods

### GetEndCursor

`func (o *V1Pagination) GetEndCursor() string`

GetEndCursor returns the EndCursor field if non-nil, zero value otherwise.

### GetEndCursorOk

`func (o *V1Pagination) GetEndCursorOk() (string, bool)`

GetEndCursorOk returns a tuple with the EndCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndCursor

`func (o *V1Pagination) HasEndCursor() bool`

HasEndCursor returns a boolean if a field has been set.

### SetEndCursor

`func (o *V1Pagination) SetEndCursor(v string)`

SetEndCursor gets a reference to the given string and assigns it to the EndCursor field.

### GetHasNextPage

`func (o *V1Pagination) GetHasNextPage() bool`

GetHasNextPage returns the HasNextPage field if non-nil, zero value otherwise.

### GetHasNextPageOk

`func (o *V1Pagination) GetHasNextPageOk() (bool, bool)`

GetHasNextPageOk returns a tuple with the HasNextPage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHasNextPage

`func (o *V1Pagination) HasHasNextPage() bool`

HasHasNextPage returns a boolean if a field has been set.

### SetHasNextPage

`func (o *V1Pagination) SetHasNextPage(v bool)`

SetHasNextPage gets a reference to the given bool and assigns it to the HasNextPage field.

### GetHasPrevPage

`func (o *V1Pagination) GetHasPrevPage() bool`

GetHasPrevPage returns the HasPrevPage field if non-nil, zero value otherwise.

### GetHasPrevPageOk

`func (o *V1Pagination) GetHasPrevPageOk() (bool, bool)`

GetHasPrevPageOk returns a tuple with the HasPrevPage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHasPrevPage

`func (o *V1Pagination) HasHasPrevPage() bool`

HasHasPrevPage returns a boolean if a field has been set.

### SetHasPrevPage

`func (o *V1Pagination) SetHasPrevPage(v bool)`

SetHasPrevPage gets a reference to the given bool and assigns it to the HasPrevPage field.

### GetStartCursor

`func (o *V1Pagination) GetStartCursor() string`

GetStartCursor returns the StartCursor field if non-nil, zero value otherwise.

### GetStartCursorOk

`func (o *V1Pagination) GetStartCursorOk() (string, bool)`

GetStartCursorOk returns a tuple with the StartCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartCursor

`func (o *V1Pagination) HasStartCursor() bool`

HasStartCursor returns a boolean if a field has been set.

### SetStartCursor

`func (o *V1Pagination) SetStartCursor(v string)`

SetStartCursor gets a reference to the given string and assigns it to the StartCursor field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


