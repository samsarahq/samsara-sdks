# V1TrailerAssignmentResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DriverId** | Pointer to **int64** | The ID of the driver associated with this trailer. | [optional] 
**EndMs** | Pointer to **int64** | The time at which the driver ended the assignment. If the assignment is current, this value will be omitted. | [optional] 
**StartMs** | Pointer to **int64** | The time at which the driver started the assignment | [optional] 

## Methods

### GetDriverId

`func (o *V1TrailerAssignmentResponse) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1TrailerAssignmentResponse) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1TrailerAssignmentResponse) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1TrailerAssignmentResponse) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetEndMs

`func (o *V1TrailerAssignmentResponse) GetEndMs() int64`

GetEndMs returns the EndMs field if non-nil, zero value otherwise.

### GetEndMsOk

`func (o *V1TrailerAssignmentResponse) GetEndMsOk() (int64, bool)`

GetEndMsOk returns a tuple with the EndMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndMs

`func (o *V1TrailerAssignmentResponse) HasEndMs() bool`

HasEndMs returns a boolean if a field has been set.

### SetEndMs

`func (o *V1TrailerAssignmentResponse) SetEndMs(v int64)`

SetEndMs gets a reference to the given int64 and assigns it to the EndMs field.

### GetStartMs

`func (o *V1TrailerAssignmentResponse) GetStartMs() int64`

GetStartMs returns the StartMs field if non-nil, zero value otherwise.

### GetStartMsOk

`func (o *V1TrailerAssignmentResponse) GetStartMsOk() (int64, bool)`

GetStartMsOk returns a tuple with the StartMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartMs

`func (o *V1TrailerAssignmentResponse) HasStartMs() bool`

HasStartMs returns a boolean if a field has been set.

### SetStartMs

`func (o *V1TrailerAssignmentResponse) SetStartMs(v int64)`

SetStartMs gets a reference to the given int64 and assigns it to the StartMs field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


