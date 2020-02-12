# V1DvirBaseAuthorSignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DriverId** | Pointer to **int64** | ID of the driver who signed the DVIR. Will not be returned if mechanicUserId is returned. | [optional] 
**Email** | Pointer to **string** | Email of the  driver|mechanic who signed the DVIR. | [optional] 
**MechanicUserId** | Pointer to **int64** | ID of the mechanic who signed the DVIR. Will not be returned if driverId is returned. | [optional] 
**Name** | Pointer to **string** | The name of the driver or mechanic who signed the DVIR. | [optional] 
**SignedAt** | Pointer to **int64** | The time in millis when the DVIR was signed | [optional] 
**Type** | Pointer to **string** | Type corresponds to whether the signature corresponds to driver|mechanic. | [optional] 
**Username** | Pointer to **string** | Username of the  driver|mechanic who signed the DVIR. | [optional] 

## Methods

### GetDriverId

`func (o *V1DvirBaseAuthorSignature) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1DvirBaseAuthorSignature) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1DvirBaseAuthorSignature) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1DvirBaseAuthorSignature) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetEmail

`func (o *V1DvirBaseAuthorSignature) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *V1DvirBaseAuthorSignature) GetEmailOk() (string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEmail

`func (o *V1DvirBaseAuthorSignature) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### SetEmail

`func (o *V1DvirBaseAuthorSignature) SetEmail(v string)`

SetEmail gets a reference to the given string and assigns it to the Email field.

### GetMechanicUserId

`func (o *V1DvirBaseAuthorSignature) GetMechanicUserId() int64`

GetMechanicUserId returns the MechanicUserId field if non-nil, zero value otherwise.

### GetMechanicUserIdOk

`func (o *V1DvirBaseAuthorSignature) GetMechanicUserIdOk() (int64, bool)`

GetMechanicUserIdOk returns a tuple with the MechanicUserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMechanicUserId

`func (o *V1DvirBaseAuthorSignature) HasMechanicUserId() bool`

HasMechanicUserId returns a boolean if a field has been set.

### SetMechanicUserId

`func (o *V1DvirBaseAuthorSignature) SetMechanicUserId(v int64)`

SetMechanicUserId gets a reference to the given int64 and assigns it to the MechanicUserId field.

### GetName

`func (o *V1DvirBaseAuthorSignature) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *V1DvirBaseAuthorSignature) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *V1DvirBaseAuthorSignature) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *V1DvirBaseAuthorSignature) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetSignedAt

`func (o *V1DvirBaseAuthorSignature) GetSignedAt() int64`

GetSignedAt returns the SignedAt field if non-nil, zero value otherwise.

### GetSignedAtOk

`func (o *V1DvirBaseAuthorSignature) GetSignedAtOk() (int64, bool)`

GetSignedAtOk returns a tuple with the SignedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSignedAt

`func (o *V1DvirBaseAuthorSignature) HasSignedAt() bool`

HasSignedAt returns a boolean if a field has been set.

### SetSignedAt

`func (o *V1DvirBaseAuthorSignature) SetSignedAt(v int64)`

SetSignedAt gets a reference to the given int64 and assigns it to the SignedAt field.

### GetType

`func (o *V1DvirBaseAuthorSignature) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *V1DvirBaseAuthorSignature) GetTypeOk() (string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasType

`func (o *V1DvirBaseAuthorSignature) HasType() bool`

HasType returns a boolean if a field has been set.

### SetType

`func (o *V1DvirBaseAuthorSignature) SetType(v string)`

SetType gets a reference to the given string and assigns it to the Type field.

### GetUsername

`func (o *V1DvirBaseAuthorSignature) GetUsername() string`

GetUsername returns the Username field if non-nil, zero value otherwise.

### GetUsernameOk

`func (o *V1DvirBaseAuthorSignature) GetUsernameOk() (string, bool)`

GetUsernameOk returns a tuple with the Username field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasUsername

`func (o *V1DvirBaseAuthorSignature) HasUsername() bool`

HasUsername returns a boolean if a field has been set.

### SetUsername

`func (o *V1DvirBaseAuthorSignature) SetUsername(v string)`

SetUsername gets a reference to the given string and assigns it to the Username field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


