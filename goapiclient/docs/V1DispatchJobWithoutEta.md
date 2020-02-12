# V1DispatchJobWithoutEta

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

`func (o *V1DispatchJobWithoutEta) GetArrivedAtMs() int64`

GetArrivedAtMs returns the ArrivedAtMs field if non-nil, zero value otherwise.

### GetArrivedAtMsOk

`func (o *V1DispatchJobWithoutEta) GetArrivedAtMsOk() (int64, bool)`

GetArrivedAtMsOk returns a tuple with the ArrivedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasArrivedAtMs

`func (o *V1DispatchJobWithoutEta) HasArrivedAtMs() bool`

HasArrivedAtMs returns a boolean if a field has been set.

### SetArrivedAtMs

`func (o *V1DispatchJobWithoutEta) SetArrivedAtMs(v int64)`

SetArrivedAtMs gets a reference to the given int64 and assigns it to the ArrivedAtMs field.

### GetCompletedAtMs

`func (o *V1DispatchJobWithoutEta) GetCompletedAtMs() int64`

GetCompletedAtMs returns the CompletedAtMs field if non-nil, zero value otherwise.

### GetCompletedAtMsOk

`func (o *V1DispatchJobWithoutEta) GetCompletedAtMsOk() (int64, bool)`

GetCompletedAtMsOk returns a tuple with the CompletedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCompletedAtMs

`func (o *V1DispatchJobWithoutEta) HasCompletedAtMs() bool`

HasCompletedAtMs returns a boolean if a field has been set.

### SetCompletedAtMs

`func (o *V1DispatchJobWithoutEta) SetCompletedAtMs(v int64)`

SetCompletedAtMs gets a reference to the given int64 and assigns it to the CompletedAtMs field.

### GetDispatchRouteId

`func (o *V1DispatchJobWithoutEta) GetDispatchRouteId() int64`

GetDispatchRouteId returns the DispatchRouteId field if non-nil, zero value otherwise.

### GetDispatchRouteIdOk

`func (o *V1DispatchJobWithoutEta) GetDispatchRouteIdOk() (int64, bool)`

GetDispatchRouteIdOk returns a tuple with the DispatchRouteId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDispatchRouteId

`func (o *V1DispatchJobWithoutEta) HasDispatchRouteId() bool`

HasDispatchRouteId returns a boolean if a field has been set.

### SetDispatchRouteId

`func (o *V1DispatchJobWithoutEta) SetDispatchRouteId(v int64)`

SetDispatchRouteId gets a reference to the given int64 and assigns it to the DispatchRouteId field.

### GetDocuments

`func (o *V1DispatchJobWithoutEta) GetDocuments() []V1DispatchJobDocumentInfo`

GetDocuments returns the Documents field if non-nil, zero value otherwise.

### GetDocumentsOk

`func (o *V1DispatchJobWithoutEta) GetDocumentsOk() ([]V1DispatchJobDocumentInfo, bool)`

GetDocumentsOk returns a tuple with the Documents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDocuments

`func (o *V1DispatchJobWithoutEta) HasDocuments() bool`

HasDocuments returns a boolean if a field has been set.

### SetDocuments

`func (o *V1DispatchJobWithoutEta) SetDocuments(v []V1DispatchJobDocumentInfo)`

SetDocuments gets a reference to the given []V1DispatchJobDocumentInfo and assigns it to the Documents field.

### GetDriverId

`func (o *V1DispatchJobWithoutEta) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1DispatchJobWithoutEta) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1DispatchJobWithoutEta) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1DispatchJobWithoutEta) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetEnRouteAtMs

`func (o *V1DispatchJobWithoutEta) GetEnRouteAtMs() int64`

GetEnRouteAtMs returns the EnRouteAtMs field if non-nil, zero value otherwise.

### GetEnRouteAtMsOk

`func (o *V1DispatchJobWithoutEta) GetEnRouteAtMsOk() (int64, bool)`

GetEnRouteAtMsOk returns a tuple with the EnRouteAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEnRouteAtMs

`func (o *V1DispatchJobWithoutEta) HasEnRouteAtMs() bool`

HasEnRouteAtMs returns a boolean if a field has been set.

### SetEnRouteAtMs

`func (o *V1DispatchJobWithoutEta) SetEnRouteAtMs(v int64)`

SetEnRouteAtMs gets a reference to the given int64 and assigns it to the EnRouteAtMs field.

### GetFleetViewerUrl

`func (o *V1DispatchJobWithoutEta) GetFleetViewerUrl() string`

GetFleetViewerUrl returns the FleetViewerUrl field if non-nil, zero value otherwise.

### GetFleetViewerUrlOk

`func (o *V1DispatchJobWithoutEta) GetFleetViewerUrlOk() (string, bool)`

GetFleetViewerUrlOk returns a tuple with the FleetViewerUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFleetViewerUrl

`func (o *V1DispatchJobWithoutEta) HasFleetViewerUrl() bool`

HasFleetViewerUrl returns a boolean if a field has been set.

### SetFleetViewerUrl

`func (o *V1DispatchJobWithoutEta) SetFleetViewerUrl(v string)`

SetFleetViewerUrl gets a reference to the given string and assigns it to the FleetViewerUrl field.

### GetGroupId

`func (o *V1DispatchJobWithoutEta) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *V1DispatchJobWithoutEta) GetGroupIdOk() (int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGroupId

`func (o *V1DispatchJobWithoutEta) HasGroupId() bool`

HasGroupId returns a boolean if a field has been set.

### SetGroupId

`func (o *V1DispatchJobWithoutEta) SetGroupId(v int64)`

SetGroupId gets a reference to the given int64 and assigns it to the GroupId field.

### GetId

`func (o *V1DispatchJobWithoutEta) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1DispatchJobWithoutEta) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1DispatchJobWithoutEta) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1DispatchJobWithoutEta) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetJobState

`func (o *V1DispatchJobWithoutEta) GetJobState() V1jobStatus`

GetJobState returns the JobState field if non-nil, zero value otherwise.

### GetJobStateOk

`func (o *V1DispatchJobWithoutEta) GetJobStateOk() (V1jobStatus, bool)`

GetJobStateOk returns a tuple with the JobState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasJobState

`func (o *V1DispatchJobWithoutEta) HasJobState() bool`

HasJobState returns a boolean if a field has been set.

### SetJobState

`func (o *V1DispatchJobWithoutEta) SetJobState(v V1jobStatus)`

SetJobState gets a reference to the given V1jobStatus and assigns it to the JobState field.

### GetSkippedAtMs

`func (o *V1DispatchJobWithoutEta) GetSkippedAtMs() int64`

GetSkippedAtMs returns the SkippedAtMs field if non-nil, zero value otherwise.

### GetSkippedAtMsOk

`func (o *V1DispatchJobWithoutEta) GetSkippedAtMsOk() (int64, bool)`

GetSkippedAtMsOk returns a tuple with the SkippedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSkippedAtMs

`func (o *V1DispatchJobWithoutEta) HasSkippedAtMs() bool`

HasSkippedAtMs returns a boolean if a field has been set.

### SetSkippedAtMs

`func (o *V1DispatchJobWithoutEta) SetSkippedAtMs(v int64)`

SetSkippedAtMs gets a reference to the given int64 and assigns it to the SkippedAtMs field.

### GetVehicleId

`func (o *V1DispatchJobWithoutEta) GetVehicleId() int64`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1DispatchJobWithoutEta) GetVehicleIdOk() (int64, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1DispatchJobWithoutEta) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1DispatchJobWithoutEta) SetVehicleId(v int64)`

SetVehicleId gets a reference to the given int64 and assigns it to the VehicleId field.

### GetDestinationAddress

`func (o *V1DispatchJobWithoutEta) GetDestinationAddress() string`

GetDestinationAddress returns the DestinationAddress field if non-nil, zero value otherwise.

### GetDestinationAddressOk

`func (o *V1DispatchJobWithoutEta) GetDestinationAddressOk() (string, bool)`

GetDestinationAddressOk returns a tuple with the DestinationAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationAddress

`func (o *V1DispatchJobWithoutEta) HasDestinationAddress() bool`

HasDestinationAddress returns a boolean if a field has been set.

### SetDestinationAddress

`func (o *V1DispatchJobWithoutEta) SetDestinationAddress(v string)`

SetDestinationAddress gets a reference to the given string and assigns it to the DestinationAddress field.

### GetDestinationAddressId

`func (o *V1DispatchJobWithoutEta) GetDestinationAddressId() int64`

GetDestinationAddressId returns the DestinationAddressId field if non-nil, zero value otherwise.

### GetDestinationAddressIdOk

`func (o *V1DispatchJobWithoutEta) GetDestinationAddressIdOk() (int64, bool)`

GetDestinationAddressIdOk returns a tuple with the DestinationAddressId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationAddressId

`func (o *V1DispatchJobWithoutEta) HasDestinationAddressId() bool`

HasDestinationAddressId returns a boolean if a field has been set.

### SetDestinationAddressId

`func (o *V1DispatchJobWithoutEta) SetDestinationAddressId(v int64)`

SetDestinationAddressId gets a reference to the given int64 and assigns it to the DestinationAddressId field.

### GetDestinationLat

`func (o *V1DispatchJobWithoutEta) GetDestinationLat() float64`

GetDestinationLat returns the DestinationLat field if non-nil, zero value otherwise.

### GetDestinationLatOk

`func (o *V1DispatchJobWithoutEta) GetDestinationLatOk() (float64, bool)`

GetDestinationLatOk returns a tuple with the DestinationLat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationLat

`func (o *V1DispatchJobWithoutEta) HasDestinationLat() bool`

HasDestinationLat returns a boolean if a field has been set.

### SetDestinationLat

`func (o *V1DispatchJobWithoutEta) SetDestinationLat(v float64)`

SetDestinationLat gets a reference to the given float64 and assigns it to the DestinationLat field.

### GetDestinationLng

`func (o *V1DispatchJobWithoutEta) GetDestinationLng() float64`

GetDestinationLng returns the DestinationLng field if non-nil, zero value otherwise.

### GetDestinationLngOk

`func (o *V1DispatchJobWithoutEta) GetDestinationLngOk() (float64, bool)`

GetDestinationLngOk returns a tuple with the DestinationLng field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationLng

`func (o *V1DispatchJobWithoutEta) HasDestinationLng() bool`

HasDestinationLng returns a boolean if a field has been set.

### SetDestinationLng

`func (o *V1DispatchJobWithoutEta) SetDestinationLng(v float64)`

SetDestinationLng gets a reference to the given float64 and assigns it to the DestinationLng field.

### GetDestinationName

`func (o *V1DispatchJobWithoutEta) GetDestinationName() string`

GetDestinationName returns the DestinationName field if non-nil, zero value otherwise.

### GetDestinationNameOk

`func (o *V1DispatchJobWithoutEta) GetDestinationNameOk() (string, bool)`

GetDestinationNameOk returns a tuple with the DestinationName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationName

`func (o *V1DispatchJobWithoutEta) HasDestinationName() bool`

HasDestinationName returns a boolean if a field has been set.

### SetDestinationName

`func (o *V1DispatchJobWithoutEta) SetDestinationName(v string)`

SetDestinationName gets a reference to the given string and assigns it to the DestinationName field.

### GetNotes

`func (o *V1DispatchJobWithoutEta) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *V1DispatchJobWithoutEta) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *V1DispatchJobWithoutEta) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *V1DispatchJobWithoutEta) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetScheduledArrivalTimeMs

`func (o *V1DispatchJobWithoutEta) GetScheduledArrivalTimeMs() int64`

GetScheduledArrivalTimeMs returns the ScheduledArrivalTimeMs field if non-nil, zero value otherwise.

### GetScheduledArrivalTimeMsOk

`func (o *V1DispatchJobWithoutEta) GetScheduledArrivalTimeMsOk() (int64, bool)`

GetScheduledArrivalTimeMsOk returns a tuple with the ScheduledArrivalTimeMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledArrivalTimeMs

`func (o *V1DispatchJobWithoutEta) HasScheduledArrivalTimeMs() bool`

HasScheduledArrivalTimeMs returns a boolean if a field has been set.

### SetScheduledArrivalTimeMs

`func (o *V1DispatchJobWithoutEta) SetScheduledArrivalTimeMs(v int64)`

SetScheduledArrivalTimeMs gets a reference to the given int64 and assigns it to the ScheduledArrivalTimeMs field.

### GetScheduledDepartureTimeMs

`func (o *V1DispatchJobWithoutEta) GetScheduledDepartureTimeMs() int64`

GetScheduledDepartureTimeMs returns the ScheduledDepartureTimeMs field if non-nil, zero value otherwise.

### GetScheduledDepartureTimeMsOk

`func (o *V1DispatchJobWithoutEta) GetScheduledDepartureTimeMsOk() (int64, bool)`

GetScheduledDepartureTimeMsOk returns a tuple with the ScheduledDepartureTimeMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledDepartureTimeMs

`func (o *V1DispatchJobWithoutEta) HasScheduledDepartureTimeMs() bool`

HasScheduledDepartureTimeMs returns a boolean if a field has been set.

### SetScheduledDepartureTimeMs

`func (o *V1DispatchJobWithoutEta) SetScheduledDepartureTimeMs(v int64)`

SetScheduledDepartureTimeMs gets a reference to the given int64 and assigns it to the ScheduledDepartureTimeMs field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


