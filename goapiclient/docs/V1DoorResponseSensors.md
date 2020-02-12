# V1DoorResponseSensors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DoorClosed** | Pointer to **bool** | Flag indicating whether the current door is closed or open. | [optional] 
**DoorStatusTime** | Pointer to **string** | The timestamp of reported door status, specified in RFC 3339 time. | [optional] 
**Id** | Pointer to **int64** | ID of the sensor. | [optional] 
**Name** | Pointer to **string** | Name of the sensor. | [optional] 
**TrailerId** | Pointer to **int32** | ID of the trailer associated with the sensor for the data point. If no trailer is connected, this parameter will not be reported. | [optional] 
**VehicleId** | Pointer to **int32** | ID of the vehicle associated with the sensor for the data point. If no vehicle is connected, this parameter will not be reported. | [optional] 

## Methods

### GetDoorClosed

`func (o *V1DoorResponseSensors) GetDoorClosed() bool`

GetDoorClosed returns the DoorClosed field if non-nil, zero value otherwise.

### GetDoorClosedOk

`func (o *V1DoorResponseSensors) GetDoorClosedOk() (bool, bool)`

GetDoorClosedOk returns a tuple with the DoorClosed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDoorClosed

`func (o *V1DoorResponseSensors) HasDoorClosed() bool`

HasDoorClosed returns a boolean if a field has been set.

### SetDoorClosed

`func (o *V1DoorResponseSensors) SetDoorClosed(v bool)`

SetDoorClosed gets a reference to the given bool and assigns it to the DoorClosed field.

### GetDoorStatusTime

`func (o *V1DoorResponseSensors) GetDoorStatusTime() string`

GetDoorStatusTime returns the DoorStatusTime field if non-nil, zero value otherwise.

### GetDoorStatusTimeOk

`func (o *V1DoorResponseSensors) GetDoorStatusTimeOk() (string, bool)`

GetDoorStatusTimeOk returns a tuple with the DoorStatusTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDoorStatusTime

`func (o *V1DoorResponseSensors) HasDoorStatusTime() bool`

HasDoorStatusTime returns a boolean if a field has been set.

### SetDoorStatusTime

`func (o *V1DoorResponseSensors) SetDoorStatusTime(v string)`

SetDoorStatusTime gets a reference to the given string and assigns it to the DoorStatusTime field.

### GetId

`func (o *V1DoorResponseSensors) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1DoorResponseSensors) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1DoorResponseSensors) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1DoorResponseSensors) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetName

`func (o *V1DoorResponseSensors) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *V1DoorResponseSensors) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *V1DoorResponseSensors) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *V1DoorResponseSensors) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetTrailerId

`func (o *V1DoorResponseSensors) GetTrailerId() int32`

GetTrailerId returns the TrailerId field if non-nil, zero value otherwise.

### GetTrailerIdOk

`func (o *V1DoorResponseSensors) GetTrailerIdOk() (int32, bool)`

GetTrailerIdOk returns a tuple with the TrailerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerId

`func (o *V1DoorResponseSensors) HasTrailerId() bool`

HasTrailerId returns a boolean if a field has been set.

### SetTrailerId

`func (o *V1DoorResponseSensors) SetTrailerId(v int32)`

SetTrailerId gets a reference to the given int32 and assigns it to the TrailerId field.

### GetVehicleId

`func (o *V1DoorResponseSensors) GetVehicleId() int32`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1DoorResponseSensors) GetVehicleIdOk() (int32, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1DoorResponseSensors) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1DoorResponseSensors) SetVehicleId(v int32)`

SetVehicleId gets a reference to the given int32 and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


