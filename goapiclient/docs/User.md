# User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthType** | Pointer to [**UserAuthType**](UserAuthType.md) |  | 
**Email** | Pointer to **string** | The email address of this user. | 
**Id** | Pointer to **string** | ID of the user. | 
**Name** | Pointer to **string** | The first and last name of the user. | 
**Roles** | Pointer to [**[]UserRoleAssignment**](UserRoleAssignment.md) | The list of roles that applies to this user. A user may have \&quot;organizational\&quot; roles, which apply to the user at the organizational level, and \&quot;tag-specific\&quot; roles, which apply to the user for a given tag. | 

## Methods

### GetAuthType

`func (o *User) GetAuthType() UserAuthType`

GetAuthType returns the AuthType field if non-nil, zero value otherwise.

### GetAuthTypeOk

`func (o *User) GetAuthTypeOk() (UserAuthType, bool)`

GetAuthTypeOk returns a tuple with the AuthType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuthType

`func (o *User) HasAuthType() bool`

HasAuthType returns a boolean if a field has been set.

### SetAuthType

`func (o *User) SetAuthType(v UserAuthType)`

SetAuthType gets a reference to the given UserAuthType and assigns it to the AuthType field.

### GetEmail

`func (o *User) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *User) GetEmailOk() (string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEmail

`func (o *User) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### SetEmail

`func (o *User) SetEmail(v string)`

SetEmail gets a reference to the given string and assigns it to the Email field.

### GetId

`func (o *User) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *User) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *User) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *User) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetName

`func (o *User) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *User) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *User) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *User) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetRoles

`func (o *User) GetRoles() []UserRoleAssignment`

GetRoles returns the Roles field if non-nil, zero value otherwise.

### GetRolesOk

`func (o *User) GetRolesOk() ([]UserRoleAssignment, bool)`

GetRolesOk returns a tuple with the Roles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRoles

`func (o *User) HasRoles() bool`

HasRoles returns a boolean if a field has been set.

### SetRoles

`func (o *User) SetRoles(v []UserRoleAssignment)`

SetRoles gets a reference to the given []UserRoleAssignment and assigns it to the Roles field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


