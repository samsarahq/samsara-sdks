# CreateRouteRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssignedDriverId** | Pointer to **string** | If the route should be assigned to a driver, the ID of that driver. | [optional] 
**AssignedVehicleId** | Pointer to **string** | If the route should be assigned to a vehicle, the ID of that vehicle. | [optional] 
**Name** | Pointer to **string** | Name of the route. | [optional] 
**Notes** | Pointer to **string** | Notes about the route. | [optional] 
**PlannedMeters** | Pointer to **float32** | The number of meters that are planned to be driven during this route. | [optional] 
**RouteStops** | Pointer to [**[]CreateRouteStopRequest**](CreateRouteStopRequest.md) | The route stops in the route. Stops will be ordered by &#x60;scheduledArrivalTime&#x60;. The start location of the route (stop with earliest &#x60;scheduledDepartureTime&#x60;) should not have &#x60;scheduledArrivalTime&#x60; populated. All other stops should &#x60;scheduledArrivalTime&#x60; and may optionally have &#x60;scheduledDepartureTime&#x60; populated. | [optional] 

## Methods

### GetAssignedDriverId

`func (o *CreateRouteRequest) GetAssignedDriverId() string`

GetAssignedDriverId returns the AssignedDriverId field if non-nil, zero value otherwise.

### GetAssignedDriverIdOk

`func (o *CreateRouteRequest) GetAssignedDriverIdOk() (string, bool)`

GetAssignedDriverIdOk returns a tuple with the AssignedDriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAssignedDriverId

`func (o *CreateRouteRequest) HasAssignedDriverId() bool`

HasAssignedDriverId returns a boolean if a field has been set.

### SetAssignedDriverId

`func (o *CreateRouteRequest) SetAssignedDriverId(v string)`

SetAssignedDriverId gets a reference to the given string and assigns it to the AssignedDriverId field.

### GetAssignedVehicleId

`func (o *CreateRouteRequest) GetAssignedVehicleId() string`

GetAssignedVehicleId returns the AssignedVehicleId field if non-nil, zero value otherwise.

### GetAssignedVehicleIdOk

`func (o *CreateRouteRequest) GetAssignedVehicleIdOk() (string, bool)`

GetAssignedVehicleIdOk returns a tuple with the AssignedVehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAssignedVehicleId

`func (o *CreateRouteRequest) HasAssignedVehicleId() bool`

HasAssignedVehicleId returns a boolean if a field has been set.

### SetAssignedVehicleId

`func (o *CreateRouteRequest) SetAssignedVehicleId(v string)`

SetAssignedVehicleId gets a reference to the given string and assigns it to the AssignedVehicleId field.

### GetName

`func (o *CreateRouteRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateRouteRequest) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *CreateRouteRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *CreateRouteRequest) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetNotes

`func (o *CreateRouteRequest) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *CreateRouteRequest) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *CreateRouteRequest) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *CreateRouteRequest) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetPlannedMeters

`func (o *CreateRouteRequest) GetPlannedMeters() float32`

GetPlannedMeters returns the PlannedMeters field if non-nil, zero value otherwise.

### GetPlannedMetersOk

`func (o *CreateRouteRequest) GetPlannedMetersOk() (float32, bool)`

GetPlannedMetersOk returns a tuple with the PlannedMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPlannedMeters

`func (o *CreateRouteRequest) HasPlannedMeters() bool`

HasPlannedMeters returns a boolean if a field has been set.

### SetPlannedMeters

`func (o *CreateRouteRequest) SetPlannedMeters(v float32)`

SetPlannedMeters gets a reference to the given float32 and assigns it to the PlannedMeters field.

### GetRouteStops

`func (o *CreateRouteRequest) GetRouteStops() []CreateRouteStopRequest`

GetRouteStops returns the RouteStops field if non-nil, zero value otherwise.

### GetRouteStopsOk

`func (o *CreateRouteRequest) GetRouteStopsOk() ([]CreateRouteStopRequest, bool)`

GetRouteStopsOk returns a tuple with the RouteStops field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRouteStops

`func (o *CreateRouteRequest) HasRouteStops() bool`

HasRouteStops returns a boolean if a field has been set.

### SetRouteStops

`func (o *CreateRouteRequest) SetRouteStops(v []CreateRouteStopRequest)`

SetRouteStops gets a reference to the given []CreateRouteStopRequest and assigns it to the RouteStops field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


