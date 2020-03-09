# UpdateDvirRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthorId** | Pointer to **string** | The user who is resolving the dvir. | 
**IsResolved** | Pointer to **bool** | Resolves the DVIR. Must be &#x60;true&#x60;. | 
**MechanicNotes** | Pointer to **string** | The mechanics notes on the DVIR. | [optional] 
**SignedAtTime** | Pointer to [**time.Time**](time.Time.md) | Time when user signed this DVIR. Defaults to now. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 

## Methods

### GetAuthorId

`func (o *UpdateDvirRequest) GetAuthorId() string`

GetAuthorId returns the AuthorId field if non-nil, zero value otherwise.

### GetAuthorIdOk

`func (o *UpdateDvirRequest) GetAuthorIdOk() (string, bool)`

GetAuthorIdOk returns a tuple with the AuthorId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuthorId

`func (o *UpdateDvirRequest) HasAuthorId() bool`

HasAuthorId returns a boolean if a field has been set.

### SetAuthorId

`func (o *UpdateDvirRequest) SetAuthorId(v string)`

SetAuthorId gets a reference to the given string and assigns it to the AuthorId field.

### GetIsResolved

`func (o *UpdateDvirRequest) GetIsResolved() bool`

GetIsResolved returns the IsResolved field if non-nil, zero value otherwise.

### GetIsResolvedOk

`func (o *UpdateDvirRequest) GetIsResolvedOk() (bool, bool)`

GetIsResolvedOk returns a tuple with the IsResolved field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasIsResolved

`func (o *UpdateDvirRequest) HasIsResolved() bool`

HasIsResolved returns a boolean if a field has been set.

### SetIsResolved

`func (o *UpdateDvirRequest) SetIsResolved(v bool)`

SetIsResolved gets a reference to the given bool and assigns it to the IsResolved field.

### GetMechanicNotes

`func (o *UpdateDvirRequest) GetMechanicNotes() string`

GetMechanicNotes returns the MechanicNotes field if non-nil, zero value otherwise.

### GetMechanicNotesOk

`func (o *UpdateDvirRequest) GetMechanicNotesOk() (string, bool)`

GetMechanicNotesOk returns a tuple with the MechanicNotes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMechanicNotes

`func (o *UpdateDvirRequest) HasMechanicNotes() bool`

HasMechanicNotes returns a boolean if a field has been set.

### SetMechanicNotes

`func (o *UpdateDvirRequest) SetMechanicNotes(v string)`

SetMechanicNotes gets a reference to the given string and assigns it to the MechanicNotes field.

### GetSignedAtTime

`func (o *UpdateDvirRequest) GetSignedAtTime() time.Time`

GetSignedAtTime returns the SignedAtTime field if non-nil, zero value otherwise.

### GetSignedAtTimeOk

`func (o *UpdateDvirRequest) GetSignedAtTimeOk() (time.Time, bool)`

GetSignedAtTimeOk returns a tuple with the SignedAtTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSignedAtTime

`func (o *UpdateDvirRequest) HasSignedAtTime() bool`

HasSignedAtTime returns a boolean if a field has been set.

### SetSignedAtTime

`func (o *UpdateDvirRequest) SetSignedAtTime(v time.Time)`

SetSignedAtTime gets a reference to the given time.Time and assigns it to the SignedAtTime field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


