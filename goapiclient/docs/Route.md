# Route

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ActualEndTime** | Pointer to **string** | Actual end time, if it exists, for the route in RFC 3339 format. | [optional] 
**ActualStartTime** | Pointer to **string** | Actual start time, if it exists, for the route in RFC 3339 format. | [optional] 
**AssignedDriver** | Pointer to [**DriverTinyResponse**](driverTinyResponse.md) |  | [optional] 
**AssignedVehicle** | Pointer to [**VehicleTinyResponse**](vehicleTinyResponse.md) |  | [optional] 
**Driver** | Pointer to [**DriverTinyResponse**](driverTinyResponse.md) |  | [optional] 
**Id** | Pointer to **string** | Unique identifier for the route. | [optional] 
**Name** | Pointer to **string** | Name of the route. | [optional] 
**Notes** | Pointer to **string** | Route notes. | [optional] 
**OdometerEndMeters** | Pointer to **float32** | The odometer reading of the assignedVehicle or associated vehicle object at the end of the route. | [optional] 
**OdometerStartMeters** | Pointer to **float32** | The odometer reading of the assignedVehicle or associated vehicle object at the start of the route. | [optional] 
**PlannedMeters** | Pointer to **float32** | Total planned distance in meters for the route. | [optional] 
**RouteStops** | Pointer to [**[]RouteStop**](RouteStop.md) | The route stops in the route. | [optional] 
**ScheduledEndTime** | Pointer to **string** | Scheduled end time for the route in RFC 3339 format. | [optional] 
**ScheduledStartTime** | Pointer to **string** | Scheduled start time for the route in RFC 3339 format. | [optional] 
**StartLocation** | Pointer to [**RouteLocation**](RouteLocation.md) |  | [optional] 
**State** | Pointer to **string** | The current state of the route. | [optional] 
**Vehicle** | Pointer to [**VehicleTinyResponse**](vehicleTinyResponse.md) |  | [optional] 

## Methods

### GetActualEndTime

`func (o *Route) GetActualEndTime() string`

GetActualEndTime returns the ActualEndTime field if non-nil, zero value otherwise.

### GetActualEndTimeOk

`func (o *Route) GetActualEndTimeOk() (string, bool)`

GetActualEndTimeOk returns a tuple with the ActualEndTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasActualEndTime

`func (o *Route) HasActualEndTime() bool`

HasActualEndTime returns a boolean if a field has been set.

### SetActualEndTime

`func (o *Route) SetActualEndTime(v string)`

SetActualEndTime gets a reference to the given string and assigns it to the ActualEndTime field.

### GetActualStartTime

`func (o *Route) GetActualStartTime() string`

GetActualStartTime returns the ActualStartTime field if non-nil, zero value otherwise.

### GetActualStartTimeOk

`func (o *Route) GetActualStartTimeOk() (string, bool)`

GetActualStartTimeOk returns a tuple with the ActualStartTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasActualStartTime

`func (o *Route) HasActualStartTime() bool`

HasActualStartTime returns a boolean if a field has been set.

### SetActualStartTime

`func (o *Route) SetActualStartTime(v string)`

SetActualStartTime gets a reference to the given string and assigns it to the ActualStartTime field.

### GetAssignedDriver

`func (o *Route) GetAssignedDriver() DriverTinyResponse`

GetAssignedDriver returns the AssignedDriver field if non-nil, zero value otherwise.

### GetAssignedDriverOk

`func (o *Route) GetAssignedDriverOk() (DriverTinyResponse, bool)`

GetAssignedDriverOk returns a tuple with the AssignedDriver field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAssignedDriver

`func (o *Route) HasAssignedDriver() bool`

HasAssignedDriver returns a boolean if a field has been set.

### SetAssignedDriver

`func (o *Route) SetAssignedDriver(v DriverTinyResponse)`

SetAssignedDriver gets a reference to the given DriverTinyResponse and assigns it to the AssignedDriver field.

### GetAssignedVehicle

`func (o *Route) GetAssignedVehicle() VehicleTinyResponse`

GetAssignedVehicle returns the AssignedVehicle field if non-nil, zero value otherwise.

### GetAssignedVehicleOk

`func (o *Route) GetAssignedVehicleOk() (VehicleTinyResponse, bool)`

GetAssignedVehicleOk returns a tuple with the AssignedVehicle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAssignedVehicle

`func (o *Route) HasAssignedVehicle() bool`

HasAssignedVehicle returns a boolean if a field has been set.

### SetAssignedVehicle

`func (o *Route) SetAssignedVehicle(v VehicleTinyResponse)`

SetAssignedVehicle gets a reference to the given VehicleTinyResponse and assigns it to the AssignedVehicle field.

### GetDriver

`func (o *Route) GetDriver() DriverTinyResponse`

GetDriver returns the Driver field if non-nil, zero value otherwise.

### GetDriverOk

`func (o *Route) GetDriverOk() (DriverTinyResponse, bool)`

GetDriverOk returns a tuple with the Driver field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriver

`func (o *Route) HasDriver() bool`

HasDriver returns a boolean if a field has been set.

### SetDriver

`func (o *Route) SetDriver(v DriverTinyResponse)`

SetDriver gets a reference to the given DriverTinyResponse and assigns it to the Driver field.

### GetId

`func (o *Route) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Route) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *Route) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *Route) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetName

`func (o *Route) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Route) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *Route) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *Route) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetNotes

`func (o *Route) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *Route) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *Route) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *Route) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetOdometerEndMeters

`func (o *Route) GetOdometerEndMeters() float32`

GetOdometerEndMeters returns the OdometerEndMeters field if non-nil, zero value otherwise.

### GetOdometerEndMetersOk

`func (o *Route) GetOdometerEndMetersOk() (float32, bool)`

GetOdometerEndMetersOk returns a tuple with the OdometerEndMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOdometerEndMeters

`func (o *Route) HasOdometerEndMeters() bool`

HasOdometerEndMeters returns a boolean if a field has been set.

### SetOdometerEndMeters

`func (o *Route) SetOdometerEndMeters(v float32)`

SetOdometerEndMeters gets a reference to the given float32 and assigns it to the OdometerEndMeters field.

### GetOdometerStartMeters

`func (o *Route) GetOdometerStartMeters() float32`

GetOdometerStartMeters returns the OdometerStartMeters field if non-nil, zero value otherwise.

### GetOdometerStartMetersOk

`func (o *Route) GetOdometerStartMetersOk() (float32, bool)`

GetOdometerStartMetersOk returns a tuple with the OdometerStartMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOdometerStartMeters

`func (o *Route) HasOdometerStartMeters() bool`

HasOdometerStartMeters returns a boolean if a field has been set.

### SetOdometerStartMeters

`func (o *Route) SetOdometerStartMeters(v float32)`

SetOdometerStartMeters gets a reference to the given float32 and assigns it to the OdometerStartMeters field.

### GetPlannedMeters

`func (o *Route) GetPlannedMeters() float32`

GetPlannedMeters returns the PlannedMeters field if non-nil, zero value otherwise.

### GetPlannedMetersOk

`func (o *Route) GetPlannedMetersOk() (float32, bool)`

GetPlannedMetersOk returns a tuple with the PlannedMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPlannedMeters

`func (o *Route) HasPlannedMeters() bool`

HasPlannedMeters returns a boolean if a field has been set.

### SetPlannedMeters

`func (o *Route) SetPlannedMeters(v float32)`

SetPlannedMeters gets a reference to the given float32 and assigns it to the PlannedMeters field.

### GetRouteStops

`func (o *Route) GetRouteStops() []RouteStop`

GetRouteStops returns the RouteStops field if non-nil, zero value otherwise.

### GetRouteStopsOk

`func (o *Route) GetRouteStopsOk() ([]RouteStop, bool)`

GetRouteStopsOk returns a tuple with the RouteStops field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRouteStops

`func (o *Route) HasRouteStops() bool`

HasRouteStops returns a boolean if a field has been set.

### SetRouteStops

`func (o *Route) SetRouteStops(v []RouteStop)`

SetRouteStops gets a reference to the given []RouteStop and assigns it to the RouteStops field.

### GetScheduledEndTime

`func (o *Route) GetScheduledEndTime() string`

GetScheduledEndTime returns the ScheduledEndTime field if non-nil, zero value otherwise.

### GetScheduledEndTimeOk

`func (o *Route) GetScheduledEndTimeOk() (string, bool)`

GetScheduledEndTimeOk returns a tuple with the ScheduledEndTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledEndTime

`func (o *Route) HasScheduledEndTime() bool`

HasScheduledEndTime returns a boolean if a field has been set.

### SetScheduledEndTime

`func (o *Route) SetScheduledEndTime(v string)`

SetScheduledEndTime gets a reference to the given string and assigns it to the ScheduledEndTime field.

### GetScheduledStartTime

`func (o *Route) GetScheduledStartTime() string`

GetScheduledStartTime returns the ScheduledStartTime field if non-nil, zero value otherwise.

### GetScheduledStartTimeOk

`func (o *Route) GetScheduledStartTimeOk() (string, bool)`

GetScheduledStartTimeOk returns a tuple with the ScheduledStartTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledStartTime

`func (o *Route) HasScheduledStartTime() bool`

HasScheduledStartTime returns a boolean if a field has been set.

### SetScheduledStartTime

`func (o *Route) SetScheduledStartTime(v string)`

SetScheduledStartTime gets a reference to the given string and assigns it to the ScheduledStartTime field.

### GetStartLocation

`func (o *Route) GetStartLocation() RouteLocation`

GetStartLocation returns the StartLocation field if non-nil, zero value otherwise.

### GetStartLocationOk

`func (o *Route) GetStartLocationOk() (RouteLocation, bool)`

GetStartLocationOk returns a tuple with the StartLocation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartLocation

`func (o *Route) HasStartLocation() bool`

HasStartLocation returns a boolean if a field has been set.

### SetStartLocation

`func (o *Route) SetStartLocation(v RouteLocation)`

SetStartLocation gets a reference to the given RouteLocation and assigns it to the StartLocation field.

### GetState

`func (o *Route) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *Route) GetStateOk() (string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasState

`func (o *Route) HasState() bool`

HasState returns a boolean if a field has been set.

### SetState

`func (o *Route) SetState(v string)`

SetState gets a reference to the given string and assigns it to the State field.

### GetVehicle

`func (o *Route) GetVehicle() VehicleTinyResponse`

GetVehicle returns the Vehicle field if non-nil, zero value otherwise.

### GetVehicleOk

`func (o *Route) GetVehicleOk() (VehicleTinyResponse, bool)`

GetVehicleOk returns a tuple with the Vehicle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicle

`func (o *Route) HasVehicle() bool`

HasVehicle returns a boolean if a field has been set.

### SetVehicle

`func (o *Route) SetVehicle(v VehicleTinyResponse)`

SetVehicle gets a reference to the given VehicleTinyResponse and assigns it to the Vehicle field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


