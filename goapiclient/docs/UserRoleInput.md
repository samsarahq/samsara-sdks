# UserRoleInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RoleId** | Pointer to **string** | The id of the role the user has been granted. | 
**TagId** | Pointer to **string** | The id of the tag used to grant a role. If no tag is specified, this role applies at the organization level. | [optional] 

## Methods

### GetRoleId

`func (o *UserRoleInput) GetRoleId() string`

GetRoleId returns the RoleId field if non-nil, zero value otherwise.

### GetRoleIdOk

`func (o *UserRoleInput) GetRoleIdOk() (string, bool)`

GetRoleIdOk returns a tuple with the RoleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRoleId

`func (o *UserRoleInput) HasRoleId() bool`

HasRoleId returns a boolean if a field has been set.

### SetRoleId

`func (o *UserRoleInput) SetRoleId(v string)`

SetRoleId gets a reference to the given string and assigns it to the RoleId field.

### GetTagId

`func (o *UserRoleInput) GetTagId() string`

GetTagId returns the TagId field if non-nil, zero value otherwise.

### GetTagIdOk

`func (o *UserRoleInput) GetTagIdOk() (string, bool)`

GetTagIdOk returns a tuple with the TagId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTagId

`func (o *UserRoleInput) HasTagId() bool`

HasTagId returns a boolean if a field has been set.

### SetTagId

`func (o *UserRoleInput) SetTagId(v string)`

SetTagId gets a reference to the given string and assigns it to the TagId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


