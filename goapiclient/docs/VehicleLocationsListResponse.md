# VehicleLocationsListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | Pointer to [**[]VehicleLocationsListResponseData**](VehicleLocationsListResponse_data.md) | A list of vehicles and an array of location events for each vehicle. | 
**Pagination** | Pointer to [**PaginationResponse**](paginationResponse.md) |  | 

## Methods

### GetData

`func (o *VehicleLocationsListResponse) GetData() []VehicleLocationsListResponseData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *VehicleLocationsListResponse) GetDataOk() ([]VehicleLocationsListResponseData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasData

`func (o *VehicleLocationsListResponse) HasData() bool`

HasData returns a boolean if a field has been set.

### SetData

`func (o *VehicleLocationsListResponse) SetData(v []VehicleLocationsListResponseData)`

SetData gets a reference to the given []VehicleLocationsListResponseData and assigns it to the Data field.

### GetPagination

`func (o *VehicleLocationsListResponse) GetPagination() PaginationResponse`

GetPagination returns the Pagination field if non-nil, zero value otherwise.

### GetPaginationOk

`func (o *VehicleLocationsListResponse) GetPaginationOk() (PaginationResponse, bool)`

GetPaginationOk returns a tuple with the Pagination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPagination

`func (o *VehicleLocationsListResponse) HasPagination() bool`

HasPagination returns a boolean if a field has been set.

### SetPagination

`func (o *VehicleLocationsListResponse) SetPagination(v PaginationResponse)`

SetPagination gets a reference to the given PaginationResponse and assigns it to the Pagination field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


