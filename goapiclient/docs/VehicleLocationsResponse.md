# VehicleLocationsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | Pointer to [**[]VehicleLocationsResponseData**](VehicleLocationsResponse_data.md) | Most recent vehicle locations. | 
**Pagination** | Pointer to [**PaginationResponse**](paginationResponse.md) |  | 

## Methods

### GetData

`func (o *VehicleLocationsResponse) GetData() []VehicleLocationsResponseData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *VehicleLocationsResponse) GetDataOk() ([]VehicleLocationsResponseData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasData

`func (o *VehicleLocationsResponse) HasData() bool`

HasData returns a boolean if a field has been set.

### SetData

`func (o *VehicleLocationsResponse) SetData(v []VehicleLocationsResponseData)`

SetData gets a reference to the given []VehicleLocationsResponseData and assigns it to the Data field.

### GetPagination

`func (o *VehicleLocationsResponse) GetPagination() PaginationResponse`

GetPagination returns the Pagination field if non-nil, zero value otherwise.

### GetPaginationOk

`func (o *VehicleLocationsResponse) GetPaginationOk() (PaginationResponse, bool)`

GetPaginationOk returns a tuple with the Pagination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPagination

`func (o *VehicleLocationsResponse) HasPagination() bool`

HasPagination returns a boolean if a field has been set.

### SetPagination

`func (o *VehicleLocationsResponse) SetPagination(v PaginationResponse)`

SetPagination gets a reference to the given PaginationResponse and assigns it to the Pagination field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


