# ListUserRolesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | Pointer to [**[]UserRole**](UserRole.md) | A list of user roles | [optional] 
**Pagination** | Pointer to [**PaginationResponse**](paginationResponse.md) |  | [optional] 

## Methods

### GetData

`func (o *ListUserRolesResponse) GetData() []UserRole`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *ListUserRolesResponse) GetDataOk() ([]UserRole, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasData

`func (o *ListUserRolesResponse) HasData() bool`

HasData returns a boolean if a field has been set.

### SetData

`func (o *ListUserRolesResponse) SetData(v []UserRole)`

SetData gets a reference to the given []UserRole and assigns it to the Data field.

### GetPagination

`func (o *ListUserRolesResponse) GetPagination() PaginationResponse`

GetPagination returns the Pagination field if non-nil, zero value otherwise.

### GetPaginationOk

`func (o *ListUserRolesResponse) GetPaginationOk() (PaginationResponse, bool)`

GetPaginationOk returns a tuple with the Pagination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPagination

`func (o *ListUserRolesResponse) HasPagination() bool`

HasPagination returns a boolean if a field has been set.

### SetPagination

`func (o *ListUserRolesResponse) SetPagination(v PaginationResponse)`

SetPagination gets a reference to the given PaginationResponse and assigns it to the Pagination field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


