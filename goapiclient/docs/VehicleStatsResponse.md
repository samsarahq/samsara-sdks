# VehicleStatsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | Pointer to [**[]VehicleStatsResponseData**](VehicleStatsResponse_data.md) | List of the most recent stats for the specified vehicles and stat types. | 
**Pagination** | Pointer to [**PaginationResponse**](paginationResponse.md) |  | 

## Methods

### GetData

`func (o *VehicleStatsResponse) GetData() []VehicleStatsResponseData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *VehicleStatsResponse) GetDataOk() ([]VehicleStatsResponseData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasData

`func (o *VehicleStatsResponse) HasData() bool`

HasData returns a boolean if a field has been set.

### SetData

`func (o *VehicleStatsResponse) SetData(v []VehicleStatsResponseData)`

SetData gets a reference to the given []VehicleStatsResponseData and assigns it to the Data field.

### GetPagination

`func (o *VehicleStatsResponse) GetPagination() PaginationResponse`

GetPagination returns the Pagination field if non-nil, zero value otherwise.

### GetPaginationOk

`func (o *VehicleStatsResponse) GetPaginationOk() (PaginationResponse, bool)`

GetPaginationOk returns a tuple with the Pagination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPagination

`func (o *VehicleStatsResponse) HasPagination() bool`

HasPagination returns a boolean if a field has been set.

### SetPagination

`func (o *VehicleStatsResponse) SetPagination(v PaginationResponse)`

SetPagination gets a reference to the given PaginationResponse and assigns it to the Pagination field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


