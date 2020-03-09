# UpdateUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthType** | Pointer to [**UserAuthType**](UserAuthType.md) |  | [optional] 
**Name** | Pointer to **string** | The first and last name of the user. | [optional] 
**Roles** | Pointer to [**[]UserRoleAssignmentRequest**](UserRoleAssignmentRequest.md) | The list of roles that applies to this user. A user may have \&quot;organizational\&quot; roles, which apply to the user at the organizational level, and \&quot;tag-specific\&quot; roles, which apply to the user for a given tag. | [optional] 

## Methods

### GetAuthType

`func (o *UpdateUserRequest) GetAuthType() UserAuthType`

GetAuthType returns the AuthType field if non-nil, zero value otherwise.

### GetAuthTypeOk

`func (o *UpdateUserRequest) GetAuthTypeOk() (UserAuthType, bool)`

GetAuthTypeOk returns a tuple with the AuthType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuthType

`func (o *UpdateUserRequest) HasAuthType() bool`

HasAuthType returns a boolean if a field has been set.

### SetAuthType

`func (o *UpdateUserRequest) SetAuthType(v UserAuthType)`

SetAuthType gets a reference to the given UserAuthType and assigns it to the AuthType field.

### GetName

`func (o *UpdateUserRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UpdateUserRequest) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *UpdateUserRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *UpdateUserRequest) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetRoles

`func (o *UpdateUserRequest) GetRoles() []UserRoleAssignmentRequest`

GetRoles returns the Roles field if non-nil, zero value otherwise.

### GetRolesOk

`func (o *UpdateUserRequest) GetRolesOk() ([]UserRoleAssignmentRequest, bool)`

GetRolesOk returns a tuple with the Roles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRoles

`func (o *UpdateUserRequest) HasRoles() bool`

HasRoles returns a boolean if a field has been set.

### SetRoles

`func (o *UpdateUserRequest) SetRoles(v []UserRoleAssignmentRequest)`

SetRoles gets a reference to the given []UserRoleAssignmentRequest and assigns it to the Roles field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


