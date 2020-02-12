# DriverTachographActivityResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | Pointer to [**[]TachographActivityListWrapper**](TachographActivityListWrapper.md) |  | [optional] 
**Pagination** | Pointer to [**PaginationResponse**](paginationResponse.md) |  | [optional] 

## Methods

### GetData

`func (o *DriverTachographActivityResponse) GetData() []TachographActivityListWrapper`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *DriverTachographActivityResponse) GetDataOk() ([]TachographActivityListWrapper, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasData

`func (o *DriverTachographActivityResponse) HasData() bool`

HasData returns a boolean if a field has been set.

### SetData

`func (o *DriverTachographActivityResponse) SetData(v []TachographActivityListWrapper)`

SetData gets a reference to the given []TachographActivityListWrapper and assigns it to the Data field.

### GetPagination

`func (o *DriverTachographActivityResponse) GetPagination() PaginationResponse`

GetPagination returns the Pagination field if non-nil, zero value otherwise.

### GetPaginationOk

`func (o *DriverTachographActivityResponse) GetPaginationOk() (PaginationResponse, bool)`

GetPaginationOk returns a tuple with the Pagination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPagination

`func (o *DriverTachographActivityResponse) HasPagination() bool`

HasPagination returns a boolean if a field has been set.

### SetPagination

`func (o *DriverTachographActivityResponse) SetPagination(v PaginationResponse)`

SetPagination gets a reference to the given PaginationResponse and assigns it to the Pagination field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


