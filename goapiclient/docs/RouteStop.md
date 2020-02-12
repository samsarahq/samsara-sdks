# RouteStop

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ActualArrivalTime** | Pointer to **string** | Actual arrival time, if it exists, for the route stop in RFC 3339 format. | [optional] 
**ActualDepartureTime** | Pointer to **string** | Actual departure time, if it exists, for the route stop in RFC 3339 format. | [optional] 
**Documents** | Pointer to [**[]RouteStopDocuments**](RouteStop_documents.md) | The documents associated with the stop. | [optional] 
**Id** | Pointer to **string** | Unique identifier for the route stop. | [optional] 
**LiveShareUrl** | Pointer to **string** | The live share URL for the stop. | [optional] 
**Notes** | Pointer to **string** | Route stop notes. | [optional] 
**ScheduledArrivalTime** | Pointer to **string** | Scheduled arrival time for the route stop in RFC 3339 format. | [optional] 
**ScheduledDepartureTime** | Pointer to **string** | Scheduled departure time for the route stop in RFC 3339 format. | [optional] 
**SkippedTime** | Pointer to **string** | Skipped time, if it exists, for the route stop in RFC 3339 format. | [optional] 
**State** | Pointer to **string** | The current state of the route stop. | [optional] 
**StopLocation** | Pointer to [**RouteLocation**](RouteLocation.md) |  | [optional] 

## Methods

### GetActualArrivalTime

`func (o *RouteStop) GetActualArrivalTime() string`

GetActualArrivalTime returns the ActualArrivalTime field if non-nil, zero value otherwise.

### GetActualArrivalTimeOk

`func (o *RouteStop) GetActualArrivalTimeOk() (string, bool)`

GetActualArrivalTimeOk returns a tuple with the ActualArrivalTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasActualArrivalTime

`func (o *RouteStop) HasActualArrivalTime() bool`

HasActualArrivalTime returns a boolean if a field has been set.

### SetActualArrivalTime

`func (o *RouteStop) SetActualArrivalTime(v string)`

SetActualArrivalTime gets a reference to the given string and assigns it to the ActualArrivalTime field.

### GetActualDepartureTime

`func (o *RouteStop) GetActualDepartureTime() string`

GetActualDepartureTime returns the ActualDepartureTime field if non-nil, zero value otherwise.

### GetActualDepartureTimeOk

`func (o *RouteStop) GetActualDepartureTimeOk() (string, bool)`

GetActualDepartureTimeOk returns a tuple with the ActualDepartureTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasActualDepartureTime

`func (o *RouteStop) HasActualDepartureTime() bool`

HasActualDepartureTime returns a boolean if a field has been set.

### SetActualDepartureTime

`func (o *RouteStop) SetActualDepartureTime(v string)`

SetActualDepartureTime gets a reference to the given string and assigns it to the ActualDepartureTime field.

### GetDocuments

`func (o *RouteStop) GetDocuments() []RouteStopDocuments`

GetDocuments returns the Documents field if non-nil, zero value otherwise.

### GetDocumentsOk

`func (o *RouteStop) GetDocumentsOk() ([]RouteStopDocuments, bool)`

GetDocumentsOk returns a tuple with the Documents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDocuments

`func (o *RouteStop) HasDocuments() bool`

HasDocuments returns a boolean if a field has been set.

### SetDocuments

`func (o *RouteStop) SetDocuments(v []RouteStopDocuments)`

SetDocuments gets a reference to the given []RouteStopDocuments and assigns it to the Documents field.

### GetId

`func (o *RouteStop) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *RouteStop) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *RouteStop) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *RouteStop) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetLiveShareUrl

`func (o *RouteStop) GetLiveShareUrl() string`

GetLiveShareUrl returns the LiveShareUrl field if non-nil, zero value otherwise.

### GetLiveShareUrlOk

`func (o *RouteStop) GetLiveShareUrlOk() (string, bool)`

GetLiveShareUrlOk returns a tuple with the LiveShareUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLiveShareUrl

`func (o *RouteStop) HasLiveShareUrl() bool`

HasLiveShareUrl returns a boolean if a field has been set.

### SetLiveShareUrl

`func (o *RouteStop) SetLiveShareUrl(v string)`

SetLiveShareUrl gets a reference to the given string and assigns it to the LiveShareUrl field.

### GetNotes

`func (o *RouteStop) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *RouteStop) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *RouteStop) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *RouteStop) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetScheduledArrivalTime

`func (o *RouteStop) GetScheduledArrivalTime() string`

GetScheduledArrivalTime returns the ScheduledArrivalTime field if non-nil, zero value otherwise.

### GetScheduledArrivalTimeOk

`func (o *RouteStop) GetScheduledArrivalTimeOk() (string, bool)`

GetScheduledArrivalTimeOk returns a tuple with the ScheduledArrivalTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledArrivalTime

`func (o *RouteStop) HasScheduledArrivalTime() bool`

HasScheduledArrivalTime returns a boolean if a field has been set.

### SetScheduledArrivalTime

`func (o *RouteStop) SetScheduledArrivalTime(v string)`

SetScheduledArrivalTime gets a reference to the given string and assigns it to the ScheduledArrivalTime field.

### GetScheduledDepartureTime

`func (o *RouteStop) GetScheduledDepartureTime() string`

GetScheduledDepartureTime returns the ScheduledDepartureTime field if non-nil, zero value otherwise.

### GetScheduledDepartureTimeOk

`func (o *RouteStop) GetScheduledDepartureTimeOk() (string, bool)`

GetScheduledDepartureTimeOk returns a tuple with the ScheduledDepartureTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledDepartureTime

`func (o *RouteStop) HasScheduledDepartureTime() bool`

HasScheduledDepartureTime returns a boolean if a field has been set.

### SetScheduledDepartureTime

`func (o *RouteStop) SetScheduledDepartureTime(v string)`

SetScheduledDepartureTime gets a reference to the given string and assigns it to the ScheduledDepartureTime field.

### GetSkippedTime

`func (o *RouteStop) GetSkippedTime() string`

GetSkippedTime returns the SkippedTime field if non-nil, zero value otherwise.

### GetSkippedTimeOk

`func (o *RouteStop) GetSkippedTimeOk() (string, bool)`

GetSkippedTimeOk returns a tuple with the SkippedTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSkippedTime

`func (o *RouteStop) HasSkippedTime() bool`

HasSkippedTime returns a boolean if a field has been set.

### SetSkippedTime

`func (o *RouteStop) SetSkippedTime(v string)`

SetSkippedTime gets a reference to the given string and assigns it to the SkippedTime field.

### GetState

`func (o *RouteStop) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *RouteStop) GetStateOk() (string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasState

`func (o *RouteStop) HasState() bool`

HasState returns a boolean if a field has been set.

### SetState

`func (o *RouteStop) SetState(v string)`

SetState gets a reference to the given string and assigns it to the State field.

### GetStopLocation

`func (o *RouteStop) GetStopLocation() RouteLocation`

GetStopLocation returns the StopLocation field if non-nil, zero value otherwise.

### GetStopLocationOk

`func (o *RouteStop) GetStopLocationOk() (RouteLocation, bool)`

GetStopLocationOk returns a tuple with the StopLocation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStopLocation

`func (o *RouteStop) HasStopLocation() bool`

HasStopLocation returns a boolean if a field has been set.

### SetStopLocation

`func (o *RouteStop) SetStopLocation(v RouteLocation)`

SetStopLocation gets a reference to the given RouteLocation and assigns it to the StopLocation field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


