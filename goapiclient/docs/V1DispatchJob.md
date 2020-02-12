# V1DispatchJob

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
**DestinationAddress** | Pointer to **string** | The address of the job destination, as it would be recognized if provided to maps.google.com. Optional if a valid destination address ID is provided. | [optional] 
**DestinationAddressId** | Pointer to **int64** | ID of the job destination associated with an address book entry. Optional if valid values are provided for destination address and latitude/longitude. If a valid destination address ID is provided, address/latitude/longitude will be used from the address book entry. Name of the address book entry will only be used if the destination name is not provided. | [optional] 
**DestinationLat** | Pointer to **float64** | Latitude of the destination in decimal degrees. Optional if a valid destination address ID is provided. | [optional] 
**DestinationLng** | Pointer to **float64** | Longitude of the destination in decimal degrees. Optional if a valid destination address ID is provided. | [optional] 
**DestinationName** | Pointer to **string** | The name of the job destination. If provided, it will take precedence over the name of the address book entry. | [optional] 
**Notes** | Pointer to **string** | Notes regarding the details of this job, maximum of 2000 characters; newline characters (&#39;\\n&#39;)can be used for formatting. | [optional] 
**ScheduledArrivalTimeMs** | Pointer to **int64** | The time at which the assigned driver is scheduled to arrive at the job destination. | 
**ScheduledDepartureTimeMs** | Pointer to **int64** | The time at which the assigned driver is scheduled to depart from the job destination. | [optional] 

## Methods

### GetArrivedAtMs

`func (o *V1DispatchJob) GetArrivedAtMs() int64`

GetArrivedAtMs returns the ArrivedAtMs field if non-nil, zero value otherwise.

### GetArrivedAtMsOk

`func (o *V1DispatchJob) GetArrivedAtMsOk() (int64, bool)`

GetArrivedAtMsOk returns a tuple with the ArrivedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasArrivedAtMs

`func (o *V1DispatchJob) HasArrivedAtMs() bool`

HasArrivedAtMs returns a boolean if a field has been set.

### SetArrivedAtMs

`func (o *V1DispatchJob) SetArrivedAtMs(v int64)`

SetArrivedAtMs gets a reference to the given int64 and assigns it to the ArrivedAtMs field.

### GetCompletedAtMs

`func (o *V1DispatchJob) GetCompletedAtMs() int64`

GetCompletedAtMs returns the CompletedAtMs field if non-nil, zero value otherwise.

### GetCompletedAtMsOk

`func (o *V1DispatchJob) GetCompletedAtMsOk() (int64, bool)`

GetCompletedAtMsOk returns a tuple with the CompletedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCompletedAtMs

`func (o *V1DispatchJob) HasCompletedAtMs() bool`

HasCompletedAtMs returns a boolean if a field has been set.

### SetCompletedAtMs

`func (o *V1DispatchJob) SetCompletedAtMs(v int64)`

SetCompletedAtMs gets a reference to the given int64 and assigns it to the CompletedAtMs field.

### GetDispatchRouteId

`func (o *V1DispatchJob) GetDispatchRouteId() int64`

GetDispatchRouteId returns the DispatchRouteId field if non-nil, zero value otherwise.

### GetDispatchRouteIdOk

`func (o *V1DispatchJob) GetDispatchRouteIdOk() (int64, bool)`

GetDispatchRouteIdOk returns a tuple with the DispatchRouteId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDispatchRouteId

`func (o *V1DispatchJob) HasDispatchRouteId() bool`

HasDispatchRouteId returns a boolean if a field has been set.

### SetDispatchRouteId

`func (o *V1DispatchJob) SetDispatchRouteId(v int64)`

SetDispatchRouteId gets a reference to the given int64 and assigns it to the DispatchRouteId field.

### GetDocuments

`func (o *V1DispatchJob) GetDocuments() []V1DispatchJobDocumentInfo`

GetDocuments returns the Documents field if non-nil, zero value otherwise.

### GetDocumentsOk

`func (o *V1DispatchJob) GetDocumentsOk() ([]V1DispatchJobDocumentInfo, bool)`

GetDocumentsOk returns a tuple with the Documents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDocuments

`func (o *V1DispatchJob) HasDocuments() bool`

HasDocuments returns a boolean if a field has been set.

### SetDocuments

`func (o *V1DispatchJob) SetDocuments(v []V1DispatchJobDocumentInfo)`

SetDocuments gets a reference to the given []V1DispatchJobDocumentInfo and assigns it to the Documents field.

### GetDriverId

`func (o *V1DispatchJob) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1DispatchJob) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1DispatchJob) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1DispatchJob) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetEnRouteAtMs

`func (o *V1DispatchJob) GetEnRouteAtMs() int64`

GetEnRouteAtMs returns the EnRouteAtMs field if non-nil, zero value otherwise.

### GetEnRouteAtMsOk

`func (o *V1DispatchJob) GetEnRouteAtMsOk() (int64, bool)`

GetEnRouteAtMsOk returns a tuple with the EnRouteAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEnRouteAtMs

`func (o *V1DispatchJob) HasEnRouteAtMs() bool`

HasEnRouteAtMs returns a boolean if a field has been set.

### SetEnRouteAtMs

`func (o *V1DispatchJob) SetEnRouteAtMs(v int64)`

SetEnRouteAtMs gets a reference to the given int64 and assigns it to the EnRouteAtMs field.

### GetEstimatedArrivalMs

`func (o *V1DispatchJob) GetEstimatedArrivalMs() int64`

GetEstimatedArrivalMs returns the EstimatedArrivalMs field if non-nil, zero value otherwise.

### GetEstimatedArrivalMsOk

`func (o *V1DispatchJob) GetEstimatedArrivalMsOk() (int64, bool)`

GetEstimatedArrivalMsOk returns a tuple with the EstimatedArrivalMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEstimatedArrivalMs

`func (o *V1DispatchJob) HasEstimatedArrivalMs() bool`

HasEstimatedArrivalMs returns a boolean if a field has been set.

### SetEstimatedArrivalMs

`func (o *V1DispatchJob) SetEstimatedArrivalMs(v int64)`

SetEstimatedArrivalMs gets a reference to the given int64 and assigns it to the EstimatedArrivalMs field.

### GetFleetViewerUrl

`func (o *V1DispatchJob) GetFleetViewerUrl() string`

GetFleetViewerUrl returns the FleetViewerUrl field if non-nil, zero value otherwise.

### GetFleetViewerUrlOk

`func (o *V1DispatchJob) GetFleetViewerUrlOk() (string, bool)`

GetFleetViewerUrlOk returns a tuple with the FleetViewerUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFleetViewerUrl

`func (o *V1DispatchJob) HasFleetViewerUrl() bool`

HasFleetViewerUrl returns a boolean if a field has been set.

### SetFleetViewerUrl

`func (o *V1DispatchJob) SetFleetViewerUrl(v string)`

SetFleetViewerUrl gets a reference to the given string and assigns it to the FleetViewerUrl field.

### GetGroupId

`func (o *V1DispatchJob) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *V1DispatchJob) GetGroupIdOk() (int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGroupId

`func (o *V1DispatchJob) HasGroupId() bool`

HasGroupId returns a boolean if a field has been set.

### SetGroupId

`func (o *V1DispatchJob) SetGroupId(v int64)`

SetGroupId gets a reference to the given int64 and assigns it to the GroupId field.

### GetId

`func (o *V1DispatchJob) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1DispatchJob) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1DispatchJob) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1DispatchJob) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetJobState

`func (o *V1DispatchJob) GetJobState() V1jobStatus`

GetJobState returns the JobState field if non-nil, zero value otherwise.

### GetJobStateOk

`func (o *V1DispatchJob) GetJobStateOk() (V1jobStatus, bool)`

GetJobStateOk returns a tuple with the JobState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasJobState

`func (o *V1DispatchJob) HasJobState() bool`

HasJobState returns a boolean if a field has been set.

### SetJobState

`func (o *V1DispatchJob) SetJobState(v V1jobStatus)`

SetJobState gets a reference to the given V1jobStatus and assigns it to the JobState field.

### GetSkippedAtMs

`func (o *V1DispatchJob) GetSkippedAtMs() int64`

GetSkippedAtMs returns the SkippedAtMs field if non-nil, zero value otherwise.

### GetSkippedAtMsOk

`func (o *V1DispatchJob) GetSkippedAtMsOk() (int64, bool)`

GetSkippedAtMsOk returns a tuple with the SkippedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSkippedAtMs

`func (o *V1DispatchJob) HasSkippedAtMs() bool`

HasSkippedAtMs returns a boolean if a field has been set.

### SetSkippedAtMs

`func (o *V1DispatchJob) SetSkippedAtMs(v int64)`

SetSkippedAtMs gets a reference to the given int64 and assigns it to the SkippedAtMs field.

### GetVehicleId

`func (o *V1DispatchJob) GetVehicleId() int64`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1DispatchJob) GetVehicleIdOk() (int64, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1DispatchJob) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1DispatchJob) SetVehicleId(v int64)`

SetVehicleId gets a reference to the given int64 and assigns it to the VehicleId field.

### GetDestinationAddress

`func (o *V1DispatchJob) GetDestinationAddress() string`

GetDestinationAddress returns the DestinationAddress field if non-nil, zero value otherwise.

### GetDestinationAddressOk

`func (o *V1DispatchJob) GetDestinationAddressOk() (string, bool)`

GetDestinationAddressOk returns a tuple with the DestinationAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationAddress

`func (o *V1DispatchJob) HasDestinationAddress() bool`

HasDestinationAddress returns a boolean if a field has been set.

### SetDestinationAddress

`func (o *V1DispatchJob) SetDestinationAddress(v string)`

SetDestinationAddress gets a reference to the given string and assigns it to the DestinationAddress field.

### GetDestinationAddressId

`func (o *V1DispatchJob) GetDestinationAddressId() int64`

GetDestinationAddressId returns the DestinationAddressId field if non-nil, zero value otherwise.

### GetDestinationAddressIdOk

`func (o *V1DispatchJob) GetDestinationAddressIdOk() (int64, bool)`

GetDestinationAddressIdOk returns a tuple with the DestinationAddressId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationAddressId

`func (o *V1DispatchJob) HasDestinationAddressId() bool`

HasDestinationAddressId returns a boolean if a field has been set.

### SetDestinationAddressId

`func (o *V1DispatchJob) SetDestinationAddressId(v int64)`

SetDestinationAddressId gets a reference to the given int64 and assigns it to the DestinationAddressId field.

### GetDestinationLat

`func (o *V1DispatchJob) GetDestinationLat() float64`

GetDestinationLat returns the DestinationLat field if non-nil, zero value otherwise.

### GetDestinationLatOk

`func (o *V1DispatchJob) GetDestinationLatOk() (float64, bool)`

GetDestinationLatOk returns a tuple with the DestinationLat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationLat

`func (o *V1DispatchJob) HasDestinationLat() bool`

HasDestinationLat returns a boolean if a field has been set.

### SetDestinationLat

`func (o *V1DispatchJob) SetDestinationLat(v float64)`

SetDestinationLat gets a reference to the given float64 and assigns it to the DestinationLat field.

### GetDestinationLng

`func (o *V1DispatchJob) GetDestinationLng() float64`

GetDestinationLng returns the DestinationLng field if non-nil, zero value otherwise.

### GetDestinationLngOk

`func (o *V1DispatchJob) GetDestinationLngOk() (float64, bool)`

GetDestinationLngOk returns a tuple with the DestinationLng field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationLng

`func (o *V1DispatchJob) HasDestinationLng() bool`

HasDestinationLng returns a boolean if a field has been set.

### SetDestinationLng

`func (o *V1DispatchJob) SetDestinationLng(v float64)`

SetDestinationLng gets a reference to the given float64 and assigns it to the DestinationLng field.

### GetDestinationName

`func (o *V1DispatchJob) GetDestinationName() string`

GetDestinationName returns the DestinationName field if non-nil, zero value otherwise.

### GetDestinationNameOk

`func (o *V1DispatchJob) GetDestinationNameOk() (string, bool)`

GetDestinationNameOk returns a tuple with the DestinationName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationName

`func (o *V1DispatchJob) HasDestinationName() bool`

HasDestinationName returns a boolean if a field has been set.

### SetDestinationName

`func (o *V1DispatchJob) SetDestinationName(v string)`

SetDestinationName gets a reference to the given string and assigns it to the DestinationName field.

### GetNotes

`func (o *V1DispatchJob) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *V1DispatchJob) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *V1DispatchJob) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *V1DispatchJob) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetScheduledArrivalTimeMs

`func (o *V1DispatchJob) GetScheduledArrivalTimeMs() int64`

GetScheduledArrivalTimeMs returns the ScheduledArrivalTimeMs field if non-nil, zero value otherwise.

### GetScheduledArrivalTimeMsOk

`func (o *V1DispatchJob) GetScheduledArrivalTimeMsOk() (int64, bool)`

GetScheduledArrivalTimeMsOk returns a tuple with the ScheduledArrivalTimeMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledArrivalTimeMs

`func (o *V1DispatchJob) HasScheduledArrivalTimeMs() bool`

HasScheduledArrivalTimeMs returns a boolean if a field has been set.

### SetScheduledArrivalTimeMs

`func (o *V1DispatchJob) SetScheduledArrivalTimeMs(v int64)`

SetScheduledArrivalTimeMs gets a reference to the given int64 and assigns it to the ScheduledArrivalTimeMs field.

### GetScheduledDepartureTimeMs

`func (o *V1DispatchJob) GetScheduledDepartureTimeMs() int64`

GetScheduledDepartureTimeMs returns the ScheduledDepartureTimeMs field if non-nil, zero value otherwise.

### GetScheduledDepartureTimeMsOk

`func (o *V1DispatchJob) GetScheduledDepartureTimeMsOk() (int64, bool)`

GetScheduledDepartureTimeMsOk returns a tuple with the ScheduledDepartureTimeMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledDepartureTimeMs

`func (o *V1DispatchJob) HasScheduledDepartureTimeMs() bool`

HasScheduledDepartureTimeMs returns a boolean if a field has been set.

### SetScheduledDepartureTimeMs

`func (o *V1DispatchJob) SetScheduledDepartureTimeMs(v int64)`

SetScheduledDepartureTimeMs gets a reference to the given int64 and assigns it to the ScheduledDepartureTimeMs field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


