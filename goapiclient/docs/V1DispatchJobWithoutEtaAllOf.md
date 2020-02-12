# V1DispatchJobWithoutEtaAllOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ArrivedAtMs** | Pointer to **int64** | The time at which the driver arrived at the job destination. | [optional] 
**CompletedAtMs** | Pointer to **int64** | The time at which the job was marked complete (e.g. started driving to the next destination). | [optional] 
**DispatchRouteId** | Pointer to **int64** | ID of the route that this job belongs to. | 
**Documents** | Pointer to [**[]V1DispatchJobDocumentInfo**](V1DispatchJobDocumentInfo.md) | Document submissions associated with this job. | [optional] 
**DriverId** | Pointer to **int64** | ID of the driver assigned to the dispatch job. | [optional] 
**EnRouteAtMs** | Pointer to **int64** | The time at which the assigned driver started fulfilling the job (e.g. started driving to the destination). | [optional] 
**FleetViewerUrl** | Pointer to **string** | Fleet viewer url of the dispatch job. | [optional] 
**GroupId** | Pointer to **int64** | Deprecated. | [optional] 
**Id** | Pointer to **int64** | ID of the Samsara dispatch job. | 
**JobState** | Pointer to [**V1jobStatus**](V1jobStatus.md) |  | 
**SkippedAtMs** | Pointer to **int64** | The time at which the job was marked skipped. | [optional] 
**VehicleId** | Pointer to **int64** | ID of the vehicle used for the dispatch job. | [optional] 

## Methods

### GetArrivedAtMs

`func (o *V1DispatchJobWithoutEtaAllOf) GetArrivedAtMs() int64`

GetArrivedAtMs returns the ArrivedAtMs field if non-nil, zero value otherwise.

### GetArrivedAtMsOk

`func (o *V1DispatchJobWithoutEtaAllOf) GetArrivedAtMsOk() (int64, bool)`

GetArrivedAtMsOk returns a tuple with the ArrivedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasArrivedAtMs

`func (o *V1DispatchJobWithoutEtaAllOf) HasArrivedAtMs() bool`

HasArrivedAtMs returns a boolean if a field has been set.

### SetArrivedAtMs

`func (o *V1DispatchJobWithoutEtaAllOf) SetArrivedAtMs(v int64)`

SetArrivedAtMs gets a reference to the given int64 and assigns it to the ArrivedAtMs field.

### GetCompletedAtMs

`func (o *V1DispatchJobWithoutEtaAllOf) GetCompletedAtMs() int64`

GetCompletedAtMs returns the CompletedAtMs field if non-nil, zero value otherwise.

### GetCompletedAtMsOk

`func (o *V1DispatchJobWithoutEtaAllOf) GetCompletedAtMsOk() (int64, bool)`

GetCompletedAtMsOk returns a tuple with the CompletedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCompletedAtMs

`func (o *V1DispatchJobWithoutEtaAllOf) HasCompletedAtMs() bool`

HasCompletedAtMs returns a boolean if a field has been set.

### SetCompletedAtMs

`func (o *V1DispatchJobWithoutEtaAllOf) SetCompletedAtMs(v int64)`

SetCompletedAtMs gets a reference to the given int64 and assigns it to the CompletedAtMs field.

### GetDispatchRouteId

`func (o *V1DispatchJobWithoutEtaAllOf) GetDispatchRouteId() int64`

GetDispatchRouteId returns the DispatchRouteId field if non-nil, zero value otherwise.

### GetDispatchRouteIdOk

`func (o *V1DispatchJobWithoutEtaAllOf) GetDispatchRouteIdOk() (int64, bool)`

GetDispatchRouteIdOk returns a tuple with the DispatchRouteId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDispatchRouteId

`func (o *V1DispatchJobWithoutEtaAllOf) HasDispatchRouteId() bool`

HasDispatchRouteId returns a boolean if a field has been set.

### SetDispatchRouteId

`func (o *V1DispatchJobWithoutEtaAllOf) SetDispatchRouteId(v int64)`

SetDispatchRouteId gets a reference to the given int64 and assigns it to the DispatchRouteId field.

### GetDocuments

`func (o *V1DispatchJobWithoutEtaAllOf) GetDocuments() []V1DispatchJobDocumentInfo`

GetDocuments returns the Documents field if non-nil, zero value otherwise.

### GetDocumentsOk

`func (o *V1DispatchJobWithoutEtaAllOf) GetDocumentsOk() ([]V1DispatchJobDocumentInfo, bool)`

GetDocumentsOk returns a tuple with the Documents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDocuments

`func (o *V1DispatchJobWithoutEtaAllOf) HasDocuments() bool`

HasDocuments returns a boolean if a field has been set.

### SetDocuments

`func (o *V1DispatchJobWithoutEtaAllOf) SetDocuments(v []V1DispatchJobDocumentInfo)`

SetDocuments gets a reference to the given []V1DispatchJobDocumentInfo and assigns it to the Documents field.

### GetDriverId

`func (o *V1DispatchJobWithoutEtaAllOf) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1DispatchJobWithoutEtaAllOf) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1DispatchJobWithoutEtaAllOf) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1DispatchJobWithoutEtaAllOf) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetEnRouteAtMs

`func (o *V1DispatchJobWithoutEtaAllOf) GetEnRouteAtMs() int64`

GetEnRouteAtMs returns the EnRouteAtMs field if non-nil, zero value otherwise.

### GetEnRouteAtMsOk

`func (o *V1DispatchJobWithoutEtaAllOf) GetEnRouteAtMsOk() (int64, bool)`

GetEnRouteAtMsOk returns a tuple with the EnRouteAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEnRouteAtMs

`func (o *V1DispatchJobWithoutEtaAllOf) HasEnRouteAtMs() bool`

HasEnRouteAtMs returns a boolean if a field has been set.

### SetEnRouteAtMs

`func (o *V1DispatchJobWithoutEtaAllOf) SetEnRouteAtMs(v int64)`

SetEnRouteAtMs gets a reference to the given int64 and assigns it to the EnRouteAtMs field.

### GetFleetViewerUrl

`func (o *V1DispatchJobWithoutEtaAllOf) GetFleetViewerUrl() string`

GetFleetViewerUrl returns the FleetViewerUrl field if non-nil, zero value otherwise.

### GetFleetViewerUrlOk

`func (o *V1DispatchJobWithoutEtaAllOf) GetFleetViewerUrlOk() (string, bool)`

GetFleetViewerUrlOk returns a tuple with the FleetViewerUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFleetViewerUrl

`func (o *V1DispatchJobWithoutEtaAllOf) HasFleetViewerUrl() bool`

HasFleetViewerUrl returns a boolean if a field has been set.

### SetFleetViewerUrl

`func (o *V1DispatchJobWithoutEtaAllOf) SetFleetViewerUrl(v string)`

SetFleetViewerUrl gets a reference to the given string and assigns it to the FleetViewerUrl field.

### GetGroupId

`func (o *V1DispatchJobWithoutEtaAllOf) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *V1DispatchJobWithoutEtaAllOf) GetGroupIdOk() (int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGroupId

`func (o *V1DispatchJobWithoutEtaAllOf) HasGroupId() bool`

HasGroupId returns a boolean if a field has been set.

### SetGroupId

`func (o *V1DispatchJobWithoutEtaAllOf) SetGroupId(v int64)`

SetGroupId gets a reference to the given int64 and assigns it to the GroupId field.

### GetId

`func (o *V1DispatchJobWithoutEtaAllOf) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1DispatchJobWithoutEtaAllOf) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1DispatchJobWithoutEtaAllOf) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1DispatchJobWithoutEtaAllOf) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetJobState

`func (o *V1DispatchJobWithoutEtaAllOf) GetJobState() V1jobStatus`

GetJobState returns the JobState field if non-nil, zero value otherwise.

### GetJobStateOk

`func (o *V1DispatchJobWithoutEtaAllOf) GetJobStateOk() (V1jobStatus, bool)`

GetJobStateOk returns a tuple with the JobState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasJobState

`func (o *V1DispatchJobWithoutEtaAllOf) HasJobState() bool`

HasJobState returns a boolean if a field has been set.

### SetJobState

`func (o *V1DispatchJobWithoutEtaAllOf) SetJobState(v V1jobStatus)`

SetJobState gets a reference to the given V1jobStatus and assigns it to the JobState field.

### GetSkippedAtMs

`func (o *V1DispatchJobWithoutEtaAllOf) GetSkippedAtMs() int64`

GetSkippedAtMs returns the SkippedAtMs field if non-nil, zero value otherwise.

### GetSkippedAtMsOk

`func (o *V1DispatchJobWithoutEtaAllOf) GetSkippedAtMsOk() (int64, bool)`

GetSkippedAtMsOk returns a tuple with the SkippedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSkippedAtMs

`func (o *V1DispatchJobWithoutEtaAllOf) HasSkippedAtMs() bool`

HasSkippedAtMs returns a boolean if a field has been set.

### SetSkippedAtMs

`func (o *V1DispatchJobWithoutEtaAllOf) SetSkippedAtMs(v int64)`

SetSkippedAtMs gets a reference to the given int64 and assigns it to the SkippedAtMs field.

### GetVehicleId

`func (o *V1DispatchJobWithoutEtaAllOf) GetVehicleId() int64`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1DispatchJobWithoutEtaAllOf) GetVehicleIdOk() (int64, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1DispatchJobWithoutEtaAllOf) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1DispatchJobWithoutEtaAllOf) SetVehicleId(v int64)`

SetVehicleId gets a reference to the given int64 and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


