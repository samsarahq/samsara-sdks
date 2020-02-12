# InlineResponse2009

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | Pointer to [**[]ListDataInputsResponse**](ListDataInputsResponse.md) | An array of data input objects. Each object contains the data input&#39;s name, ID, and other metadata. | [optional] 
**Pagination** | Pointer to [**PaginationResponse**](paginationResponse.md) |  | [optional] 

## Methods

### GetData

`func (o *InlineResponse2009) GetData() []ListDataInputsResponse`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *InlineResponse2009) GetDataOk() ([]ListDataInputsResponse, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasData

`func (o *InlineResponse2009) HasData() bool`

HasData returns a boolean if a field has been set.

### SetData

`func (o *InlineResponse2009) SetData(v []ListDataInputsResponse)`

SetData gets a reference to the given []ListDataInputsResponse and assigns it to the Data field.

### GetPagination

`func (o *InlineResponse2009) GetPagination() PaginationResponse`

GetPagination returns the Pagination field if non-nil, zero value otherwise.

### GetPaginationOk

`func (o *InlineResponse2009) GetPaginationOk() (PaginationResponse, bool)`

GetPaginationOk returns a tuple with the Pagination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPagination

`func (o *InlineResponse2009) HasPagination() bool`

HasPagination returns a boolean if a field has been set.

### SetPagination

`func (o *InlineResponse2009) SetPagination(v PaginationResponse)`

SetPagination gets a reference to the given PaginationResponse and assigns it to the Pagination field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


