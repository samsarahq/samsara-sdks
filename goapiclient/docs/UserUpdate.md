# UserUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthType** | Pointer to **string** | The authentication type the user uses to authenticate. To use SAML this organization must have a configured SAML integration. | [optional] 
**Name** | Pointer to **string** | The first and last name of the user. | [optional] 
**Roles** | Pointer to [**[]UserRoleInput**](UserRoleInput.md) | The roles for this user. Users must have at least a single role to be a part of an organization. | [optional] 

## Methods

### GetAuthType

`func (o *UserUpdate) GetAuthType() string`

GetAuthType returns the AuthType field if non-nil, zero value otherwise.

### GetAuthTypeOk

`func (o *UserUpdate) GetAuthTypeOk() (string, bool)`

GetAuthTypeOk returns a tuple with the AuthType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuthType

`func (o *UserUpdate) HasAuthType() bool`

HasAuthType returns a boolean if a field has been set.

### SetAuthType

`func (o *UserUpdate) SetAuthType(v string)`

SetAuthType gets a reference to the given string and assigns it to the AuthType field.

### GetName

`func (o *UserUpdate) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UserUpdate) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *UserUpdate) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *UserUpdate) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetRoles

`func (o *UserUpdate) GetRoles() []UserRoleInput`

GetRoles returns the Roles field if non-nil, zero value otherwise.

### GetRolesOk

`func (o *UserUpdate) GetRolesOk() ([]UserRoleInput, bool)`

GetRolesOk returns a tuple with the Roles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRoles

`func (o *UserUpdate) HasRoles() bool`

HasRoles returns a boolean if a field has been set.

### SetRoles

`func (o *UserUpdate) SetRoles(v []UserRoleInput)`

SetRoles gets a reference to the given []UserRoleInput and assigns it to the Roles field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


