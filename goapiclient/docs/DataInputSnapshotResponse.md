# DataInputSnapshotResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | Pointer to [**[]DataInputSnapshot**](DataInputSnapshot.md) | An array of data inputs&#39; latest data points. Each object in the array represents a data input and its most recent data point. | [optional] 
**Pagination** | Pointer to [**PaginationResponse**](paginationResponse.md) |  | [optional] 

## Methods

### GetData

`func (o *DataInputSnapshotResponse) GetData() []DataInputSnapshot`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *DataInputSnapshotResponse) GetDataOk() ([]DataInputSnapshot, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasData

`func (o *DataInputSnapshotResponse) HasData() bool`

HasData returns a boolean if a field has been set.

### SetData

`func (o *DataInputSnapshotResponse) SetData(v []DataInputSnapshot)`

SetData gets a reference to the given []DataInputSnapshot and assigns it to the Data field.

### GetPagination

`func (o *DataInputSnapshotResponse) GetPagination() PaginationResponse`

GetPagination returns the Pagination field if non-nil, zero value otherwise.

### GetPaginationOk

`func (o *DataInputSnapshotResponse) GetPaginationOk() (PaginationResponse, bool)`

GetPaginationOk returns a tuple with the Pagination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPagination

`func (o *DataInputSnapshotResponse) HasPagination() bool`

HasPagination returns a boolean if a field has been set.

### SetPagination

`func (o *DataInputSnapshotResponse) SetPagination(v PaginationResponse)`

SetPagination gets a reference to the given PaginationResponse and assigns it to the Pagination field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


