# CreateRouteStopRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Notes** | Pointer to **string** | Route stop notes. | [optional] 
**ScheduledArrivalTime** | Pointer to **string** | Scheduled arrival time for the route stop in RFC 3339 format. | [optional] 
**ScheduledDepartureTime** | Pointer to **string** | Scheduled departure time for the route stop in RFC 3339 format. | [optional] 
**StopLocation** | Pointer to [**RouteLocation**](RouteLocation.md) |  | [optional] 

## Methods

### GetNotes

`func (o *CreateRouteStopRequest) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *CreateRouteStopRequest) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *CreateRouteStopRequest) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *CreateRouteStopRequest) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetScheduledArrivalTime

`func (o *CreateRouteStopRequest) GetScheduledArrivalTime() string`

GetScheduledArrivalTime returns the ScheduledArrivalTime field if non-nil, zero value otherwise.

### GetScheduledArrivalTimeOk

`func (o *CreateRouteStopRequest) GetScheduledArrivalTimeOk() (string, bool)`

GetScheduledArrivalTimeOk returns a tuple with the ScheduledArrivalTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledArrivalTime

`func (o *CreateRouteStopRequest) HasScheduledArrivalTime() bool`

HasScheduledArrivalTime returns a boolean if a field has been set.

### SetScheduledArrivalTime

`func (o *CreateRouteStopRequest) SetScheduledArrivalTime(v string)`

SetScheduledArrivalTime gets a reference to the given string and assigns it to the ScheduledArrivalTime field.

### GetScheduledDepartureTime

`func (o *CreateRouteStopRequest) GetScheduledDepartureTime() string`

GetScheduledDepartureTime returns the ScheduledDepartureTime field if non-nil, zero value otherwise.

### GetScheduledDepartureTimeOk

`func (o *CreateRouteStopRequest) GetScheduledDepartureTimeOk() (string, bool)`

GetScheduledDepartureTimeOk returns a tuple with the ScheduledDepartureTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledDepartureTime

`func (o *CreateRouteStopRequest) HasScheduledDepartureTime() bool`

HasScheduledDepartureTime returns a boolean if a field has been set.

### SetScheduledDepartureTime

`func (o *CreateRouteStopRequest) SetScheduledDepartureTime(v string)`

SetScheduledDepartureTime gets a reference to the given string and assigns it to the ScheduledDepartureTime field.

### GetStopLocation

`func (o *CreateRouteStopRequest) GetStopLocation() RouteLocation`

GetStopLocation returns the StopLocation field if non-nil, zero value otherwise.

### GetStopLocationOk

`func (o *CreateRouteStopRequest) GetStopLocationOk() (RouteLocation, bool)`

GetStopLocationOk returns a tuple with the StopLocation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStopLocation

`func (o *CreateRouteStopRequest) HasStopLocation() bool`

HasStopLocation returns a boolean if a field has been set.

### SetStopLocation

`func (o *CreateRouteStopRequest) SetStopLocation(v RouteLocation)`

SetStopLocation gets a reference to the given RouteLocation and assigns it to the StopLocation field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


