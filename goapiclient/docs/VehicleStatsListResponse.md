# VehicleStatsListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | Pointer to [**[]VehicleStatsListResponseData**](VehicleStatsListResponse_data.md) | A list of vehicles and an array of stat events for each vehicle. | 
**Pagination** | Pointer to [**PaginationResponse**](paginationResponse.md) |  | 

## Methods

### GetData

`func (o *VehicleStatsListResponse) GetData() []VehicleStatsListResponseData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *VehicleStatsListResponse) GetDataOk() ([]VehicleStatsListResponseData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasData

`func (o *VehicleStatsListResponse) HasData() bool`

HasData returns a boolean if a field has been set.

### SetData

`func (o *VehicleStatsListResponse) SetData(v []VehicleStatsListResponseData)`

SetData gets a reference to the given []VehicleStatsListResponseData and assigns it to the Data field.

### GetPagination

`func (o *VehicleStatsListResponse) GetPagination() PaginationResponse`

GetPagination returns the Pagination field if non-nil, zero value otherwise.

### GetPaginationOk

`func (o *VehicleStatsListResponse) GetPaginationOk() (PaginationResponse, bool)`

GetPaginationOk returns a tuple with the Pagination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPagination

`func (o *VehicleStatsListResponse) HasPagination() bool`

HasPagination returns a boolean if a field has been set.

### SetPagination

`func (o *VehicleStatsListResponse) SetPagination(v PaginationResponse)`

SetPagination gets a reference to the given PaginationResponse and assigns it to the Pagination field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


