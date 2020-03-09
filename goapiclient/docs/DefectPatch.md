# DefectPatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthorId** | Pointer to **string** | The user who is resolving the defect. | 
**IsResolved** | Pointer to **bool** | Resolves the defect. Must be &#x60;true&#x60;. | 
**ResolvedAtTime** | Pointer to **string** | Time when defect was resolved. Defaults to now if not provided. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 

## Methods

### GetAuthorId

`func (o *DefectPatch) GetAuthorId() string`

GetAuthorId returns the AuthorId field if non-nil, zero value otherwise.

### GetAuthorIdOk

`func (o *DefectPatch) GetAuthorIdOk() (string, bool)`

GetAuthorIdOk returns a tuple with the AuthorId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuthorId

`func (o *DefectPatch) HasAuthorId() bool`

HasAuthorId returns a boolean if a field has been set.

### SetAuthorId

`func (o *DefectPatch) SetAuthorId(v string)`

SetAuthorId gets a reference to the given string and assigns it to the AuthorId field.

### GetIsResolved

`func (o *DefectPatch) GetIsResolved() bool`

GetIsResolved returns the IsResolved field if non-nil, zero value otherwise.

### GetIsResolvedOk

`func (o *DefectPatch) GetIsResolvedOk() (bool, bool)`

GetIsResolvedOk returns a tuple with the IsResolved field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasIsResolved

`func (o *DefectPatch) HasIsResolved() bool`

HasIsResolved returns a boolean if a field has been set.

### SetIsResolved

`func (o *DefectPatch) SetIsResolved(v bool)`

SetIsResolved gets a reference to the given bool and assigns it to the IsResolved field.

### GetResolvedAtTime

`func (o *DefectPatch) GetResolvedAtTime() string`

GetResolvedAtTime returns the ResolvedAtTime field if non-nil, zero value otherwise.

### GetResolvedAtTimeOk

`func (o *DefectPatch) GetResolvedAtTimeOk() (string, bool)`

GetResolvedAtTimeOk returns a tuple with the ResolvedAtTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasResolvedAtTime

`func (o *DefectPatch) HasResolvedAtTime() bool`

HasResolvedAtTime returns a boolean if a field has been set.

### SetResolvedAtTime

`func (o *DefectPatch) SetResolvedAtTime(v string)`

SetResolvedAtTime gets a reference to the given string and assigns it to the ResolvedAtTime field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


