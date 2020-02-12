# User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthType** | Pointer to **string** | The authentication type the user uses to authenticate. To use SAML this organization must have a configured SAML integration. | 
**Email** | Pointer to **string** | The email address of this user. | 
**Id** | Pointer to **string** | Unique ID for the user. | 
**Name** | Pointer to **string** | The first and last name of the user. | 
**Roles** | Pointer to [**[]UserRoleResponse**](UserRoleResponse.md) |  | 

## Methods

### GetAuthType

`func (o *User) GetAuthType() string`

GetAuthType returns the AuthType field if non-nil, zero value otherwise.

### GetAuthTypeOk

`func (o *User) GetAuthTypeOk() (string, bool)`

GetAuthTypeOk returns a tuple with the AuthType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuthType

`func (o *User) HasAuthType() bool`

HasAuthType returns a boolean if a field has been set.

### SetAuthType

`func (o *User) SetAuthType(v string)`

SetAuthType gets a reference to the given string and assigns it to the AuthType field.

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

`func (o *User) GetRoles() []UserRoleResponse`

GetRoles returns the Roles field if non-nil, zero value otherwise.

### GetRolesOk

`func (o *User) GetRolesOk() ([]UserRoleResponse, bool)`

GetRolesOk returns a tuple with the Roles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRoles

`func (o *User) HasRoles() bool`

HasRoles returns a boolean if a field has been set.

### SetRoles

`func (o *User) SetRoles(v []UserRoleResponse)`

SetRoles gets a reference to the given []UserRoleResponse and assigns it to the Roles field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


