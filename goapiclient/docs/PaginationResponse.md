# PaginationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EndCursor** | Pointer to **string** | Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request&#39;s &#39;after&#39; query parameter. This may be an empty string if there are no more pages left to view. | 
**HasNextPage** | Pointer to **bool** | True if there are more pages of results immediately available after this endCursor. | 

## Methods

### GetEndCursor

`func (o *PaginationResponse) GetEndCursor() string`

GetEndCursor returns the EndCursor field if non-nil, zero value otherwise.

### GetEndCursorOk

`func (o *PaginationResponse) GetEndCursorOk() (string, bool)`

GetEndCursorOk returns a tuple with the EndCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndCursor

`func (o *PaginationResponse) HasEndCursor() bool`

HasEndCursor returns a boolean if a field has been set.

### SetEndCursor

`func (o *PaginationResponse) SetEndCursor(v string)`

SetEndCursor gets a reference to the given string and assigns it to the EndCursor field.

### GetHasNextPage

`func (o *PaginationResponse) GetHasNextPage() bool`

GetHasNextPage returns the HasNextPage field if non-nil, zero value otherwise.

### GetHasNextPageOk

`func (o *PaginationResponse) GetHasNextPageOk() (bool, bool)`

GetHasNextPageOk returns a tuple with the HasNextPage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHasNextPage

`func (o *PaginationResponse) HasHasNextPage() bool`

HasHasNextPage returns a boolean if a field has been set.

### SetHasNextPage

`func (o *PaginationResponse) SetHasNextPage(v bool)`

SetHasNextPage gets a reference to the given bool and assigns it to the HasNextPage field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


