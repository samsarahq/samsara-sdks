# V1jobUpdateObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ChangedAtMs** | Pointer to **int64** | Timestamp that this event was updated, represented as Unix milliseconds since epoch. | [optional] 
**JobId** | Pointer to **int64** | ID of the Samsara job. | [optional] 
**JobState** | Pointer to [**V1jobStatus**](V1jobStatus.md) |  | [optional] 
**PrevJobState** | Pointer to [**V1jobStatus**](V1jobStatus.md) |  | [optional] 
**Route** | Pointer to [**V1DispatchRoute**](V1DispatchRoute.md) |  | [optional] 
**RouteId** | Pointer to **int64** | ID of the Samsara dispatch route. | [optional] 

## Methods

### GetChangedAtMs

`func (o *V1jobUpdateObject) GetChangedAtMs() int64`

GetChangedAtMs returns the ChangedAtMs field if non-nil, zero value otherwise.

### GetChangedAtMsOk

`func (o *V1jobUpdateObject) GetChangedAtMsOk() (int64, bool)`

GetChangedAtMsOk returns a tuple with the ChangedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasChangedAtMs

`func (o *V1jobUpdateObject) HasChangedAtMs() bool`

HasChangedAtMs returns a boolean if a field has been set.

### SetChangedAtMs

`func (o *V1jobUpdateObject) SetChangedAtMs(v int64)`

SetChangedAtMs gets a reference to the given int64 and assigns it to the ChangedAtMs field.

### GetJobId

`func (o *V1jobUpdateObject) GetJobId() int64`

GetJobId returns the JobId field if non-nil, zero value otherwise.

### GetJobIdOk

`func (o *V1jobUpdateObject) GetJobIdOk() (int64, bool)`

GetJobIdOk returns a tuple with the JobId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasJobId

`func (o *V1jobUpdateObject) HasJobId() bool`

HasJobId returns a boolean if a field has been set.

### SetJobId

`func (o *V1jobUpdateObject) SetJobId(v int64)`

SetJobId gets a reference to the given int64 and assigns it to the JobId field.

### GetJobState

`func (o *V1jobUpdateObject) GetJobState() V1jobStatus`

GetJobState returns the JobState field if non-nil, zero value otherwise.

### GetJobStateOk

`func (o *V1jobUpdateObject) GetJobStateOk() (V1jobStatus, bool)`

GetJobStateOk returns a tuple with the JobState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasJobState

`func (o *V1jobUpdateObject) HasJobState() bool`

HasJobState returns a boolean if a field has been set.

### SetJobState

`func (o *V1jobUpdateObject) SetJobState(v V1jobStatus)`

SetJobState gets a reference to the given V1jobStatus and assigns it to the JobState field.

### GetPrevJobState

`func (o *V1jobUpdateObject) GetPrevJobState() V1jobStatus`

GetPrevJobState returns the PrevJobState field if non-nil, zero value otherwise.

### GetPrevJobStateOk

`func (o *V1jobUpdateObject) GetPrevJobStateOk() (V1jobStatus, bool)`

GetPrevJobStateOk returns a tuple with the PrevJobState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPrevJobState

`func (o *V1jobUpdateObject) HasPrevJobState() bool`

HasPrevJobState returns a boolean if a field has been set.

### SetPrevJobState

`func (o *V1jobUpdateObject) SetPrevJobState(v V1jobStatus)`

SetPrevJobState gets a reference to the given V1jobStatus and assigns it to the PrevJobState field.

### GetRoute

`func (o *V1jobUpdateObject) GetRoute() V1DispatchRoute`

GetRoute returns the Route field if non-nil, zero value otherwise.

### GetRouteOk

`func (o *V1jobUpdateObject) GetRouteOk() (V1DispatchRoute, bool)`

GetRouteOk returns a tuple with the Route field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRoute

`func (o *V1jobUpdateObject) HasRoute() bool`

HasRoute returns a boolean if a field has been set.

### SetRoute

`func (o *V1jobUpdateObject) SetRoute(v V1DispatchRoute)`

SetRoute gets a reference to the given V1DispatchRoute and assigns it to the Route field.

### GetRouteId

`func (o *V1jobUpdateObject) GetRouteId() int64`

GetRouteId returns the RouteId field if non-nil, zero value otherwise.

### GetRouteIdOk

`func (o *V1jobUpdateObject) GetRouteIdOk() (int64, bool)`

GetRouteIdOk returns a tuple with the RouteId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRouteId

`func (o *V1jobUpdateObject) HasRouteId() bool`

HasRouteId returns a boolean if a field has been set.

### SetRouteId

`func (o *V1jobUpdateObject) SetRouteId(v int64)`

SetRouteId gets a reference to the given int64 and assigns it to the RouteId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


