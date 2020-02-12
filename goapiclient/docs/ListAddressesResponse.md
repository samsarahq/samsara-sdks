# ListAddressesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | Pointer to [**[]Address**](Address.md) | A list of Addresses. | 
**Pagination** | Pointer to [**PaginationResponse**](paginationResponse.md) |  | 

## Methods

### GetData

`func (o *ListAddressesResponse) GetData() []Address`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *ListAddressesResponse) GetDataOk() ([]Address, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasData

`func (o *ListAddressesResponse) HasData() bool`

HasData returns a boolean if a field has been set.

### SetData

`func (o *ListAddressesResponse) SetData(v []Address)`

SetData gets a reference to the given []Address and assigns it to the Data field.

### GetPagination

`func (o *ListAddressesResponse) GetPagination() PaginationResponse`

GetPagination returns the Pagination field if non-nil, zero value otherwise.

### GetPaginationOk

`func (o *ListAddressesResponse) GetPaginationOk() (PaginationResponse, bool)`

GetPaginationOk returns a tuple with the Pagination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPagination

`func (o *ListAddressesResponse) HasPagination() bool`

HasPagination returns a boolean if a field has been set.

### SetPagination

`func (o *ListAddressesResponse) SetPagination(v PaginationResponse)`

SetPagination gets a reference to the given PaginationResponse and assigns it to the Pagination field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


