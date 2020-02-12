# UserCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthType** | Pointer to **string** | The authentication type the user uses to authenticate. To use SAML this organization must have a configured SAML integration. | 
**Email** | Pointer to **string** | The email address of this user. This cannot be changed after creation. | 
**Name** | Pointer to **string** | The first and last name of the user. | 
**Roles** | Pointer to [**[]UserRoleInput**](UserRoleInput.md) | The roles for this user. Users must have at least a single role to be a part of an organization. Roles without an associated &#x60;tagId&#x60; are considered \&quot;Organization Level\&quot; roles and will apply to the user at the organization level. Each user can only have one \&quot;Organization Level\&quot; role. Roles with a &#x60;tagId&#x60; will be roles specific to that tag. Users can only have one role per tag. Users can have different roles at the organization and tag level, and users can have different roles for different tags. | 

## Methods

### GetAuthType

`func (o *UserCreate) GetAuthType() string`

GetAuthType returns the AuthType field if non-nil, zero value otherwise.

### GetAuthTypeOk

`func (o *UserCreate) GetAuthTypeOk() (string, bool)`

GetAuthTypeOk returns a tuple with the AuthType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuthType

`func (o *UserCreate) HasAuthType() bool`

HasAuthType returns a boolean if a field has been set.

### SetAuthType

`func (o *UserCreate) SetAuthType(v string)`

SetAuthType gets a reference to the given string and assigns it to the AuthType field.

### GetEmail

`func (o *UserCreate) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *UserCreate) GetEmailOk() (string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEmail

`func (o *UserCreate) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### SetEmail

`func (o *UserCreate) SetEmail(v string)`

SetEmail gets a reference to the given string and assigns it to the Email field.

### GetName

`func (o *UserCreate) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UserCreate) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *UserCreate) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *UserCreate) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetRoles

`func (o *UserCreate) GetRoles() []UserRoleInput`

GetRoles returns the Roles field if non-nil, zero value otherwise.

### GetRolesOk

`func (o *UserCreate) GetRolesOk() ([]UserRoleInput, bool)`

GetRolesOk returns a tuple with the Roles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRoles

`func (o *UserCreate) HasRoles() bool`

HasRoles returns a boolean if a field has been set.

### SetRoles

`func (o *UserCreate) SetRoles(v []UserRoleInput)`

SetRoles gets a reference to the given []UserRoleInput and assigns it to the Roles field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


