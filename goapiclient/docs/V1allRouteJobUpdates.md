# V1allRouteJobUpdates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**JobUpdates** | Pointer to [**[]V1jobUpdateObject**](V1jobUpdateObject.md) |  | [optional] 
**SequenceId** | Pointer to **string** | Sequence ID of the last update returned in the response | [optional] 

## Methods

### GetJobUpdates

`func (o *V1allRouteJobUpdates) GetJobUpdates() []V1jobUpdateObject`

GetJobUpdates returns the JobUpdates field if non-nil, zero value otherwise.

### GetJobUpdatesOk

`func (o *V1allRouteJobUpdates) GetJobUpdatesOk() ([]V1jobUpdateObject, bool)`

GetJobUpdatesOk returns a tuple with the JobUpdates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasJobUpdates

`func (o *V1allRouteJobUpdates) HasJobUpdates() bool`

HasJobUpdates returns a boolean if a field has been set.

### SetJobUpdates

`func (o *V1allRouteJobUpdates) SetJobUpdates(v []V1jobUpdateObject)`

SetJobUpdates gets a reference to the given []V1jobUpdateObject and assigns it to the JobUpdates field.

### GetSequenceId

`func (o *V1allRouteJobUpdates) GetSequenceId() string`

GetSequenceId returns the SequenceId field if non-nil, zero value otherwise.

### GetSequenceIdOk

`func (o *V1allRouteJobUpdates) GetSequenceIdOk() (string, bool)`

GetSequenceIdOk returns a tuple with the SequenceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSequenceId

`func (o *V1allRouteJobUpdates) HasSequenceId() bool`

HasSequenceId returns a boolean if a field has been set.

### SetSequenceId

`func (o *V1allRouteJobUpdates) SetSequenceId(v string)`

SetSequenceId gets a reference to the given string and assigns it to the SequenceId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


