# V1DispatchRouteCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DispatchJobs** | Pointer to [**[]V1DispatchJobCreate**](V1DispatchJobCreate.md) | The dispatch jobs to create for this route. | 
**DriverId** | Pointer to **int64** | ID of the driver assigned to the dispatch route. Note that driver_id and vehicle_id are mutually exclusive. If neither is specified, then the route is unassigned. | [optional] 
**Name** | Pointer to **string** | Descriptive name of this route. | 
**Notes** | Pointer to **string** | Notes regarding the details of this route; maximum of 2000 characters; newline characters (&#39;\\n&#39;)can be used for formatting. | [optional] 
**ScheduledEndMs** | Pointer to **int64** | The time in Unix epoch milliseconds that the last job in the route is scheduled to end. | [optional] 
**ScheduledMeters** | Pointer to **int64** | The distance expected to be traveled for this route in meters. | [optional] 
**ScheduledStartMs** | Pointer to **int64** | The time in Unix epoch milliseconds that the route is scheduled to start. | 
**StartLocationAddress** | Pointer to **string** | The address of the route&#39;s starting location, as it would be recognized if provided to maps.google.com. Optional if a valid start location address ID is provided. | [optional] 
**StartLocationAddressId** | Pointer to **int64** | ID of the start location associated with an address book entry. Optional if valid values are provided for start location address and latitude/longitude. If a valid start location address ID is provided, address/latitude/longitude will be used from the address book entry. Name of the address book entry will only be used if the start location name is not provided. | [optional] 
**StartLocationLat** | Pointer to **float64** | Latitude of the start location in decimal degrees. Optional if a valid start location address ID is provided. | [optional] 
**StartLocationLng** | Pointer to **float64** | Longitude of the start location in decimal degrees. Optional if a valid start location address ID is provided. | [optional] 
**StartLocationName** | Pointer to **string** | The name of the route&#39;s starting location. If provided, it will take precedence over the name of the address book entry. | [optional] 
**TrailerId** | Pointer to **int64** | ID of the trailer assigned to the dispatch route. Note that trailers can only be assigned to routes that have a Vehicle or Driver assigned to them. | [optional] 
**VehicleId** | Pointer to **int64** | ID of the vehicle assigned to the dispatch route. Note that vehicle_id and driver_id are mutually exclusive. If neither is specified, then the route is unassigned. | [optional] 

## Methods

### GetDispatchJobs

`func (o *V1DispatchRouteCreate) GetDispatchJobs() []V1DispatchJobCreate`

GetDispatchJobs returns the DispatchJobs field if non-nil, zero value otherwise.

### GetDispatchJobsOk

`func (o *V1DispatchRouteCreate) GetDispatchJobsOk() ([]V1DispatchJobCreate, bool)`

GetDispatchJobsOk returns a tuple with the DispatchJobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDispatchJobs

`func (o *V1DispatchRouteCreate) HasDispatchJobs() bool`

HasDispatchJobs returns a boolean if a field has been set.

### SetDispatchJobs

`func (o *V1DispatchRouteCreate) SetDispatchJobs(v []V1DispatchJobCreate)`

SetDispatchJobs gets a reference to the given []V1DispatchJobCreate and assigns it to the DispatchJobs field.

### GetDriverId

`func (o *V1DispatchRouteCreate) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1DispatchRouteCreate) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1DispatchRouteCreate) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1DispatchRouteCreate) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetName

`func (o *V1DispatchRouteCreate) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *V1DispatchRouteCreate) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *V1DispatchRouteCreate) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *V1DispatchRouteCreate) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetNotes

`func (o *V1DispatchRouteCreate) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *V1DispatchRouteCreate) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *V1DispatchRouteCreate) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *V1DispatchRouteCreate) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetScheduledEndMs

`func (o *V1DispatchRouteCreate) GetScheduledEndMs() int64`

GetScheduledEndMs returns the ScheduledEndMs field if non-nil, zero value otherwise.

### GetScheduledEndMsOk

`func (o *V1DispatchRouteCreate) GetScheduledEndMsOk() (int64, bool)`

GetScheduledEndMsOk returns a tuple with the ScheduledEndMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledEndMs

`func (o *V1DispatchRouteCreate) HasScheduledEndMs() bool`

HasScheduledEndMs returns a boolean if a field has been set.

### SetScheduledEndMs

`func (o *V1DispatchRouteCreate) SetScheduledEndMs(v int64)`

SetScheduledEndMs gets a reference to the given int64 and assigns it to the ScheduledEndMs field.

### GetScheduledMeters

`func (o *V1DispatchRouteCreate) GetScheduledMeters() int64`

GetScheduledMeters returns the ScheduledMeters field if non-nil, zero value otherwise.

### GetScheduledMetersOk

`func (o *V1DispatchRouteCreate) GetScheduledMetersOk() (int64, bool)`

GetScheduledMetersOk returns a tuple with the ScheduledMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledMeters

`func (o *V1DispatchRouteCreate) HasScheduledMeters() bool`

HasScheduledMeters returns a boolean if a field has been set.

### SetScheduledMeters

`func (o *V1DispatchRouteCreate) SetScheduledMeters(v int64)`

SetScheduledMeters gets a reference to the given int64 and assigns it to the ScheduledMeters field.

### GetScheduledStartMs

`func (o *V1DispatchRouteCreate) GetScheduledStartMs() int64`

GetScheduledStartMs returns the ScheduledStartMs field if non-nil, zero value otherwise.

### GetScheduledStartMsOk

`func (o *V1DispatchRouteCreate) GetScheduledStartMsOk() (int64, bool)`

GetScheduledStartMsOk returns a tuple with the ScheduledStartMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledStartMs

`func (o *V1DispatchRouteCreate) HasScheduledStartMs() bool`

HasScheduledStartMs returns a boolean if a field has been set.

### SetScheduledStartMs

`func (o *V1DispatchRouteCreate) SetScheduledStartMs(v int64)`

SetScheduledStartMs gets a reference to the given int64 and assigns it to the ScheduledStartMs field.

### GetStartLocationAddress

`func (o *V1DispatchRouteCreate) GetStartLocationAddress() string`

GetStartLocationAddress returns the StartLocationAddress field if non-nil, zero value otherwise.

### GetStartLocationAddressOk

`func (o *V1DispatchRouteCreate) GetStartLocationAddressOk() (string, bool)`

GetStartLocationAddressOk returns a tuple with the StartLocationAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartLocationAddress

`func (o *V1DispatchRouteCreate) HasStartLocationAddress() bool`

HasStartLocationAddress returns a boolean if a field has been set.

### SetStartLocationAddress

`func (o *V1DispatchRouteCreate) SetStartLocationAddress(v string)`

SetStartLocationAddress gets a reference to the given string and assigns it to the StartLocationAddress field.

### GetStartLocationAddressId

`func (o *V1DispatchRouteCreate) GetStartLocationAddressId() int64`

GetStartLocationAddressId returns the StartLocationAddressId field if non-nil, zero value otherwise.

### GetStartLocationAddressIdOk

`func (o *V1DispatchRouteCreate) GetStartLocationAddressIdOk() (int64, bool)`

GetStartLocationAddressIdOk returns a tuple with the StartLocationAddressId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartLocationAddressId

`func (o *V1DispatchRouteCreate) HasStartLocationAddressId() bool`

HasStartLocationAddressId returns a boolean if a field has been set.

### SetStartLocationAddressId

`func (o *V1DispatchRouteCreate) SetStartLocationAddressId(v int64)`

SetStartLocationAddressId gets a reference to the given int64 and assigns it to the StartLocationAddressId field.

### GetStartLocationLat

`func (o *V1DispatchRouteCreate) GetStartLocationLat() float64`

GetStartLocationLat returns the StartLocationLat field if non-nil, zero value otherwise.

### GetStartLocationLatOk

`func (o *V1DispatchRouteCreate) GetStartLocationLatOk() (float64, bool)`

GetStartLocationLatOk returns a tuple with the StartLocationLat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartLocationLat

`func (o *V1DispatchRouteCreate) HasStartLocationLat() bool`

HasStartLocationLat returns a boolean if a field has been set.

### SetStartLocationLat

`func (o *V1DispatchRouteCreate) SetStartLocationLat(v float64)`

SetStartLocationLat gets a reference to the given float64 and assigns it to the StartLocationLat field.

### GetStartLocationLng

`func (o *V1DispatchRouteCreate) GetStartLocationLng() float64`

GetStartLocationLng returns the StartLocationLng field if non-nil, zero value otherwise.

### GetStartLocationLngOk

`func (o *V1DispatchRouteCreate) GetStartLocationLngOk() (float64, bool)`

GetStartLocationLngOk returns a tuple with the StartLocationLng field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartLocationLng

`func (o *V1DispatchRouteCreate) HasStartLocationLng() bool`

HasStartLocationLng returns a boolean if a field has been set.

### SetStartLocationLng

`func (o *V1DispatchRouteCreate) SetStartLocationLng(v float64)`

SetStartLocationLng gets a reference to the given float64 and assigns it to the StartLocationLng field.

### GetStartLocationName

`func (o *V1DispatchRouteCreate) GetStartLocationName() string`

GetStartLocationName returns the StartLocationName field if non-nil, zero value otherwise.

### GetStartLocationNameOk

`func (o *V1DispatchRouteCreate) GetStartLocationNameOk() (string, bool)`

GetStartLocationNameOk returns a tuple with the StartLocationName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartLocationName

`func (o *V1DispatchRouteCreate) HasStartLocationName() bool`

HasStartLocationName returns a boolean if a field has been set.

### SetStartLocationName

`func (o *V1DispatchRouteCreate) SetStartLocationName(v string)`

SetStartLocationName gets a reference to the given string and assigns it to the StartLocationName field.

### GetTrailerId

`func (o *V1DispatchRouteCreate) GetTrailerId() int64`

GetTrailerId returns the TrailerId field if non-nil, zero value otherwise.

### GetTrailerIdOk

`func (o *V1DispatchRouteCreate) GetTrailerIdOk() (int64, bool)`

GetTrailerIdOk returns a tuple with the TrailerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerId

`func (o *V1DispatchRouteCreate) HasTrailerId() bool`

HasTrailerId returns a boolean if a field has been set.

### SetTrailerId

`func (o *V1DispatchRouteCreate) SetTrailerId(v int64)`

SetTrailerId gets a reference to the given int64 and assigns it to the TrailerId field.

### GetVehicleId

`func (o *V1DispatchRouteCreate) GetVehicleId() int64`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1DispatchRouteCreate) GetVehicleIdOk() (int64, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1DispatchRouteCreate) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1DispatchRouteCreate) SetVehicleId(v int64)`

SetVehicleId gets a reference to the given int64 and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


