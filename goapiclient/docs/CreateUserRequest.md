# CreateUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthType** | Pointer to [**UserAuthType**](UserAuthType.md) |  | 
**Email** | Pointer to **string** | The email address of this user. | 
**Name** | Pointer to **string** | The first and last name of the user. | 
**Roles** | Pointer to [**[]UserRoleAssignmentRequest**](UserRoleAssignmentRequest.md) | The list of roles that applies to this user. A user may have \&quot;organizational\&quot; roles, which apply to the user at the organizational level, and \&quot;tag-specific\&quot; roles, which apply to the user for a given tag. | 

## Methods

### GetAuthType

`func (o *CreateUserRequest) GetAuthType() UserAuthType`

GetAuthType returns the AuthType field if non-nil, zero value otherwise.

### GetAuthTypeOk

`func (o *CreateUserRequest) GetAuthTypeOk() (UserAuthType, bool)`

GetAuthTypeOk returns a tuple with the AuthType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuthType

`func (o *CreateUserRequest) HasAuthType() bool`

HasAuthType returns a boolean if a field has been set.

### SetAuthType

`func (o *CreateUserRequest) SetAuthType(v UserAuthType)`

SetAuthType gets a reference to the given UserAuthType and assigns it to the AuthType field.

### GetEmail

`func (o *CreateUserRequest) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *CreateUserRequest) GetEmailOk() (string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEmail

`func (o *CreateUserRequest) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### SetEmail

`func (o *CreateUserRequest) SetEmail(v string)`

SetEmail gets a reference to the given string and assigns it to the Email field.

### GetName

`func (o *CreateUserRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateUserRequest) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *CreateUserRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *CreateUserRequest) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetRoles

`func (o *CreateUserRequest) GetRoles() []UserRoleAssignmentRequest`

GetRoles returns the Roles field if non-nil, zero value otherwise.

### GetRolesOk

`func (o *CreateUserRequest) GetRolesOk() ([]UserRoleAssignmentRequest, bool)`

GetRolesOk returns a tuple with the Roles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRoles

`func (o *CreateUserRequest) HasRoles() bool`

HasRoles returns a boolean if a field has been set.

### SetRoles

`func (o *CreateUserRequest) SetRoles(v []UserRoleAssignmentRequest)`

SetRoles gets a reference to the given []UserRoleAssignmentRequest and assigns it to the Roles field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


