# DvirSecondSignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SignatoryUser** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 
**SignedAtTime** | Pointer to [**time.Time**](time.Time.md) | The time when the DVIR was signed. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**Type** | Pointer to **string** | Whether the DVIR was submitted by a &#x60;driver&#x60; or &#x60;mechanic&#x60;. | [optional] [default to TYPE_DRIVER]

## Methods

### GetSignatoryUser

`func (o *DvirSecondSignature) GetSignatoryUser() map[string]interface{}`

GetSignatoryUser returns the SignatoryUser field if non-nil, zero value otherwise.

### GetSignatoryUserOk

`func (o *DvirSecondSignature) GetSignatoryUserOk() (map[string]interface{}, bool)`

GetSignatoryUserOk returns a tuple with the SignatoryUser field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSignatoryUser

`func (o *DvirSecondSignature) HasSignatoryUser() bool`

HasSignatoryUser returns a boolean if a field has been set.

### SetSignatoryUser

`func (o *DvirSecondSignature) SetSignatoryUser(v map[string]interface{})`

SetSignatoryUser gets a reference to the given map[string]interface{} and assigns it to the SignatoryUser field.

### GetSignedAtTime

`func (o *DvirSecondSignature) GetSignedAtTime() time.Time`

GetSignedAtTime returns the SignedAtTime field if non-nil, zero value otherwise.

### GetSignedAtTimeOk

`func (o *DvirSecondSignature) GetSignedAtTimeOk() (time.Time, bool)`

GetSignedAtTimeOk returns a tuple with the SignedAtTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSignedAtTime

`func (o *DvirSecondSignature) HasSignedAtTime() bool`

HasSignedAtTime returns a boolean if a field has been set.

### SetSignedAtTime

`func (o *DvirSecondSignature) SetSignedAtTime(v time.Time)`

SetSignedAtTime gets a reference to the given time.Time and assigns it to the SignedAtTime field.

### GetType

`func (o *DvirSecondSignature) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *DvirSecondSignature) GetTypeOk() (string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasType

`func (o *DvirSecondSignature) HasType() bool`

HasType returns a boolean if a field has been set.

### SetType

`func (o *DvirSecondSignature) SetType(v string)`

SetType gets a reference to the given string and assigns it to the Type field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


