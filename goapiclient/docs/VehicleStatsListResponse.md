# VehicleStatsListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | Pointer to [**[]VehicleStatsList**](VehicleStatsList.md) | An array of vehicle stat objects. Each object in the array represents a vehicle and will contain an array of stat object updates (a timestamp and value of the requested stat type). | [optional] 
**Pagination** | Pointer to [**PaginationResponse**](paginationResponse.md) |  | [optional] 

## Methods

### GetData

`func (o *VehicleStatsListResponse) GetData() []VehicleStatsList`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *VehicleStatsListResponse) GetDataOk() ([]VehicleStatsList, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasData

`func (o *VehicleStatsListResponse) HasData() bool`

HasData returns a boolean if a field has been set.

### SetData

`func (o *VehicleStatsListResponse) SetData(v []VehicleStatsList)`

SetData gets a reference to the given []VehicleStatsList and assigns it to the Data field.

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


