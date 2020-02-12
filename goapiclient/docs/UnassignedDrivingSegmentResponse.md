# UnassignedDrivingSegmentResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Annotation** | Pointer to **string** | Annotation for the driving segment. | [optional] 
**CreatedAtTime** | Pointer to [**time.Time**](time.Time.md) | The time that the server created the driving segment, specified in RFC 3339 format. | [optional] 
**Driver** | Pointer to [**DriverTinyResponse**](driverTinyResponse.md) |  | [optional] 
**EndTime** | Pointer to [**time.Time**](time.Time.md) | End time of the driving segment, specified in RFC 3339 format. | [optional] 
**Id** | Pointer to **string** | Unique identifier for the unassigned driving segment. | [optional] 
**StartTime** | Pointer to [**time.Time**](time.Time.md) | Start time of the driving segment, specified in RFC 3339 format. | [optional] 
**Status** | Pointer to **string** | Status of assignment for this segment. | [optional] 
**Vehicle** | Pointer to [**VehicleTinyResponse**](vehicleTinyResponse.md) |  | [optional] 

## Methods

### GetAnnotation

`func (o *UnassignedDrivingSegmentResponse) GetAnnotation() string`

GetAnnotation returns the Annotation field if non-nil, zero value otherwise.

### GetAnnotationOk

`func (o *UnassignedDrivingSegmentResponse) GetAnnotationOk() (string, bool)`

GetAnnotationOk returns a tuple with the Annotation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAnnotation

`func (o *UnassignedDrivingSegmentResponse) HasAnnotation() bool`

HasAnnotation returns a boolean if a field has been set.

### SetAnnotation

`func (o *UnassignedDrivingSegmentResponse) SetAnnotation(v string)`

SetAnnotation gets a reference to the given string and assigns it to the Annotation field.

### GetCreatedAtTime

`func (o *UnassignedDrivingSegmentResponse) GetCreatedAtTime() time.Time`

GetCreatedAtTime returns the CreatedAtTime field if non-nil, zero value otherwise.

### GetCreatedAtTimeOk

`func (o *UnassignedDrivingSegmentResponse) GetCreatedAtTimeOk() (time.Time, bool)`

GetCreatedAtTimeOk returns a tuple with the CreatedAtTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCreatedAtTime

`func (o *UnassignedDrivingSegmentResponse) HasCreatedAtTime() bool`

HasCreatedAtTime returns a boolean if a field has been set.

### SetCreatedAtTime

`func (o *UnassignedDrivingSegmentResponse) SetCreatedAtTime(v time.Time)`

SetCreatedAtTime gets a reference to the given time.Time and assigns it to the CreatedAtTime field.

### GetDriver

`func (o *UnassignedDrivingSegmentResponse) GetDriver() DriverTinyResponse`

GetDriver returns the Driver field if non-nil, zero value otherwise.

### GetDriverOk

`func (o *UnassignedDrivingSegmentResponse) GetDriverOk() (DriverTinyResponse, bool)`

GetDriverOk returns a tuple with the Driver field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriver

`func (o *UnassignedDrivingSegmentResponse) HasDriver() bool`

HasDriver returns a boolean if a field has been set.

### SetDriver

`func (o *UnassignedDrivingSegmentResponse) SetDriver(v DriverTinyResponse)`

SetDriver gets a reference to the given DriverTinyResponse and assigns it to the Driver field.

### GetEndTime

`func (o *UnassignedDrivingSegmentResponse) GetEndTime() time.Time`

GetEndTime returns the EndTime field if non-nil, zero value otherwise.

### GetEndTimeOk

`func (o *UnassignedDrivingSegmentResponse) GetEndTimeOk() (time.Time, bool)`

GetEndTimeOk returns a tuple with the EndTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndTime

`func (o *UnassignedDrivingSegmentResponse) HasEndTime() bool`

HasEndTime returns a boolean if a field has been set.

### SetEndTime

`func (o *UnassignedDrivingSegmentResponse) SetEndTime(v time.Time)`

SetEndTime gets a reference to the given time.Time and assigns it to the EndTime field.

### GetId

`func (o *UnassignedDrivingSegmentResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UnassignedDrivingSegmentResponse) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *UnassignedDrivingSegmentResponse) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *UnassignedDrivingSegmentResponse) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetStartTime

`func (o *UnassignedDrivingSegmentResponse) GetStartTime() time.Time`

GetStartTime returns the StartTime field if non-nil, zero value otherwise.

### GetStartTimeOk

`func (o *UnassignedDrivingSegmentResponse) GetStartTimeOk() (time.Time, bool)`

GetStartTimeOk returns a tuple with the StartTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartTime

`func (o *UnassignedDrivingSegmentResponse) HasStartTime() bool`

HasStartTime returns a boolean if a field has been set.

### SetStartTime

`func (o *UnassignedDrivingSegmentResponse) SetStartTime(v time.Time)`

SetStartTime gets a reference to the given time.Time and assigns it to the StartTime field.

### GetStatus

`func (o *UnassignedDrivingSegmentResponse) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *UnassignedDrivingSegmentResponse) GetStatusOk() (string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStatus

`func (o *UnassignedDrivingSegmentResponse) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### SetStatus

`func (o *UnassignedDrivingSegmentResponse) SetStatus(v string)`

SetStatus gets a reference to the given string and assigns it to the Status field.

### GetVehicle

`func (o *UnassignedDrivingSegmentResponse) GetVehicle() VehicleTinyResponse`

GetVehicle returns the Vehicle field if non-nil, zero value otherwise.

### GetVehicleOk

`func (o *UnassignedDrivingSegmentResponse) GetVehicleOk() (VehicleTinyResponse, bool)`

GetVehicleOk returns a tuple with the Vehicle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicle

`func (o *UnassignedDrivingSegmentResponse) HasVehicle() bool`

HasVehicle returns a boolean if a field has been set.

### SetVehicle

`func (o *UnassignedDrivingSegmentResponse) SetVehicle(v VehicleTinyResponse)`

SetVehicle gets a reference to the given VehicleTinyResponse and assigns it to the Vehicle field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


