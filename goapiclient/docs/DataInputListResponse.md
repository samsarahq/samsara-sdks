# DataInputListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | Pointer to [**[]DataInputResponse**](DataInputResponse.md) | An array of data input data points. Each object in the array represents a data input and will contain its associated data points. | [optional] 
**Pagination** | Pointer to [**PaginationResponse**](paginationResponse.md) |  | [optional] 

## Methods

### GetData

`func (o *DataInputListResponse) GetData() []DataInputResponse`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *DataInputListResponse) GetDataOk() ([]DataInputResponse, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasData

`func (o *DataInputListResponse) HasData() bool`

HasData returns a boolean if a field has been set.

### SetData

`func (o *DataInputListResponse) SetData(v []DataInputResponse)`

SetData gets a reference to the given []DataInputResponse and assigns it to the Data field.

### GetPagination

`func (o *DataInputListResponse) GetPagination() PaginationResponse`

GetPagination returns the Pagination field if non-nil, zero value otherwise.

### GetPaginationOk

`func (o *DataInputListResponse) GetPaginationOk() (PaginationResponse, bool)`

GetPaginationOk returns a tuple with the Pagination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPagination

`func (o *DataInputListResponse) HasPagination() bool`

HasPagination returns a boolean if a field has been set.

### SetPagination

`func (o *DataInputListResponse) SetPagination(v PaginationResponse)`

SetPagination gets a reference to the given PaginationResponse and assigns it to the Pagination field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


