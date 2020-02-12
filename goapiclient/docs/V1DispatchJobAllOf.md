# V1DispatchJobAllOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ArrivedAtMs** | Pointer to **int64** | The time at which the driver arrived at the job destination. | [optional] 
**CompletedAtMs** | Pointer to **int64** | The time at which the job was marked complete (e.g. started driving to the next destination). | [optional] 
**DispatchRouteId** | Pointer to **int64** | ID of the route that this job belongs to. | 
**Documents** | Pointer to [**[]V1DispatchJobDocumentInfo**](V1DispatchJobDocumentInfo.md) | Document submissions associated with this job. | [optional] 
**DriverId** | Pointer to **int64** | ID of the driver assigned to the dispatch job. | [optional] 
**EnRouteAtMs** | Pointer to **int64** | The time at which the assigned driver started fulfilling the job (e.g. started driving to the destination). | [optional] 
**EstimatedArrivalMs** | Pointer to **int64** | The time at which the assigned driver is estimated to arrive at the job destination. Only valid for en-route jobs. | [optional] 
**FleetViewerUrl** | Pointer to **string** | Fleet viewer url of the dispatch job. | [optional] 
**GroupId** | Pointer to **int64** | Deprecated. | [optional] 
**Id** | Pointer to **int64** | ID of the Samsara dispatch job. | 
**JobState** | Pointer to [**V1jobStatus**](V1jobStatus.md) |  | 
**SkippedAtMs** | Pointer to **int64** | The time at which the job was marked skipped. | [optional] 
**VehicleId** | Pointer to **int64** | ID of the vehicle used for the dispatch job. | [optional] 

## Methods

### GetArrivedAtMs

`func (o *V1DispatchJobAllOf) GetArrivedAtMs() int64`

GetArrivedAtMs returns the ArrivedAtMs field if non-nil, zero value otherwise.

### GetArrivedAtMsOk

`func (o *V1DispatchJobAllOf) GetArrivedAtMsOk() (int64, bool)`

GetArrivedAtMsOk returns a tuple with the ArrivedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasArrivedAtMs

`func (o *V1DispatchJobAllOf) HasArrivedAtMs() bool`

HasArrivedAtMs returns a boolean if a field has been set.

### SetArrivedAtMs

`func (o *V1DispatchJobAllOf) SetArrivedAtMs(v int64)`

SetArrivedAtMs gets a reference to the given int64 and assigns it to the ArrivedAtMs field.

### GetCompletedAtMs

`func (o *V1DispatchJobAllOf) GetCompletedAtMs() int64`

GetCompletedAtMs returns the CompletedAtMs field if non-nil, zero value otherwise.

### GetCompletedAtMsOk

`func (o *V1DispatchJobAllOf) GetCompletedAtMsOk() (int64, bool)`

GetCompletedAtMsOk returns a tuple with the CompletedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCompletedAtMs

`func (o *V1DispatchJobAllOf) HasCompletedAtMs() bool`

HasCompletedAtMs returns a boolean if a field has been set.

### SetCompletedAtMs

`func (o *V1DispatchJobAllOf) SetCompletedAtMs(v int64)`

SetCompletedAtMs gets a reference to the given int64 and assigns it to the CompletedAtMs field.

### GetDispatchRouteId

`func (o *V1DispatchJobAllOf) GetDispatchRouteId() int64`

GetDispatchRouteId returns the DispatchRouteId field if non-nil, zero value otherwise.

### GetDispatchRouteIdOk

`func (o *V1DispatchJobAllOf) GetDispatchRouteIdOk() (int64, bool)`

GetDispatchRouteIdOk returns a tuple with the DispatchRouteId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDispatchRouteId

`func (o *V1DispatchJobAllOf) HasDispatchRouteId() bool`

HasDispatchRouteId returns a boolean if a field has been set.

### SetDispatchRouteId

`func (o *V1DispatchJobAllOf) SetDispatchRouteId(v int64)`

SetDispatchRouteId gets a reference to the given int64 and assigns it to the DispatchRouteId field.

### GetDocuments

`func (o *V1DispatchJobAllOf) GetDocuments() []V1DispatchJobDocumentInfo`

GetDocuments returns the Documents field if non-nil, zero value otherwise.

### GetDocumentsOk

`func (o *V1DispatchJobAllOf) GetDocumentsOk() ([]V1DispatchJobDocumentInfo, bool)`

GetDocumentsOk returns a tuple with the Documents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDocuments

`func (o *V1DispatchJobAllOf) HasDocuments() bool`

HasDocuments returns a boolean if a field has been set.

### SetDocuments

`func (o *V1DispatchJobAllOf) SetDocuments(v []V1DispatchJobDocumentInfo)`

SetDocuments gets a reference to the given []V1DispatchJobDocumentInfo and assigns it to the Documents field.

### GetDriverId

`func (o *V1DispatchJobAllOf) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1DispatchJobAllOf) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1DispatchJobAllOf) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1DispatchJobAllOf) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetEnRouteAtMs

`func (o *V1DispatchJobAllOf) GetEnRouteAtMs() int64`

GetEnRouteAtMs returns the EnRouteAtMs field if non-nil, zero value otherwise.

### GetEnRouteAtMsOk

`func (o *V1DispatchJobAllOf) GetEnRouteAtMsOk() (int64, bool)`

GetEnRouteAtMsOk returns a tuple with the EnRouteAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEnRouteAtMs

`func (o *V1DispatchJobAllOf) HasEnRouteAtMs() bool`

HasEnRouteAtMs returns a boolean if a field has been set.

### SetEnRouteAtMs

`func (o *V1DispatchJobAllOf) SetEnRouteAtMs(v int64)`

SetEnRouteAtMs gets a reference to the given int64 and assigns it to the EnRouteAtMs field.

### GetEstimatedArrivalMs

`func (o *V1DispatchJobAllOf) GetEstimatedArrivalMs() int64`

GetEstimatedArrivalMs returns the EstimatedArrivalMs field if non-nil, zero value otherwise.

### GetEstimatedArrivalMsOk

`func (o *V1DispatchJobAllOf) GetEstimatedArrivalMsOk() (int64, bool)`

GetEstimatedArrivalMsOk returns a tuple with the EstimatedArrivalMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEstimatedArrivalMs

`func (o *V1DispatchJobAllOf) HasEstimatedArrivalMs() bool`

HasEstimatedArrivalMs returns a boolean if a field has been set.

### SetEstimatedArrivalMs

`func (o *V1DispatchJobAllOf) SetEstimatedArrivalMs(v int64)`

SetEstimatedArrivalMs gets a reference to the given int64 and assigns it to the EstimatedArrivalMs field.

### GetFleetViewerUrl

`func (o *V1DispatchJobAllOf) GetFleetViewerUrl() string`

GetFleetViewerUrl returns the FleetViewerUrl field if non-nil, zero value otherwise.

### GetFleetViewerUrlOk

`func (o *V1DispatchJobAllOf) GetFleetViewerUrlOk() (string, bool)`

GetFleetViewerUrlOk returns a tuple with the FleetViewerUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFleetViewerUrl

`func (o *V1DispatchJobAllOf) HasFleetViewerUrl() bool`

HasFleetViewerUrl returns a boolean if a field has been set.

### SetFleetViewerUrl

`func (o *V1DispatchJobAllOf) SetFleetViewerUrl(v string)`

SetFleetViewerUrl gets a reference to the given string and assigns it to the FleetViewerUrl field.

### GetGroupId

`func (o *V1DispatchJobAllOf) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *V1DispatchJobAllOf) GetGroupIdOk() (int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGroupId

`func (o *V1DispatchJobAllOf) HasGroupId() bool`

HasGroupId returns a boolean if a field has been set.

### SetGroupId

`func (o *V1DispatchJobAllOf) SetGroupId(v int64)`

SetGroupId gets a reference to the given int64 and assigns it to the GroupId field.

### GetId

`func (o *V1DispatchJobAllOf) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1DispatchJobAllOf) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1DispatchJobAllOf) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1DispatchJobAllOf) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetJobState

`func (o *V1DispatchJobAllOf) GetJobState() V1jobStatus`

GetJobState returns the JobState field if non-nil, zero value otherwise.

### GetJobStateOk

`func (o *V1DispatchJobAllOf) GetJobStateOk() (V1jobStatus, bool)`

GetJobStateOk returns a tuple with the JobState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasJobState

`func (o *V1DispatchJobAllOf) HasJobState() bool`

HasJobState returns a boolean if a field has been set.

### SetJobState

`func (o *V1DispatchJobAllOf) SetJobState(v V1jobStatus)`

SetJobState gets a reference to the given V1jobStatus and assigns it to the JobState field.

### GetSkippedAtMs

`func (o *V1DispatchJobAllOf) GetSkippedAtMs() int64`

GetSkippedAtMs returns the SkippedAtMs field if non-nil, zero value otherwise.

### GetSkippedAtMsOk

`func (o *V1DispatchJobAllOf) GetSkippedAtMsOk() (int64, bool)`

GetSkippedAtMsOk returns a tuple with the SkippedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSkippedAtMs

`func (o *V1DispatchJobAllOf) HasSkippedAtMs() bool`

HasSkippedAtMs returns a boolean if a field has been set.

### SetSkippedAtMs

`func (o *V1DispatchJobAllOf) SetSkippedAtMs(v int64)`

SetSkippedAtMs gets a reference to the given int64 and assigns it to the SkippedAtMs field.

### GetVehicleId

`func (o *V1DispatchJobAllOf) GetVehicleId() int64`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1DispatchJobAllOf) GetVehicleIdOk() (int64, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1DispatchJobAllOf) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1DispatchJobAllOf) SetVehicleId(v int64)`

SetVehicleId gets a reference to the given int64 and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


