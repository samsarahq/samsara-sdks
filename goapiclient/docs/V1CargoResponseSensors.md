# V1CargoResponseSensors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CargoEmpty** | Pointer to **bool** | Flag indicating whether the current cargo is empty or loaded. | [optional] 
**CargoStatusTime** | Pointer to **string** | The timestamp of reported cargo status, specified in RFC 3339 time. | [optional] 
**Id** | Pointer to **int64** | ID of the sensor. | [optional] 
**Name** | Pointer to **string** | Name of the sensor. | [optional] 
**TrailerId** | Pointer to **int32** | ID of the trailer associated with the sensor for the data point. If no trailer is connected, this parameter will not be reported. | [optional] 
**VehicleId** | Pointer to **int32** | ID of the vehicle associated with the sensor for the data point. If no vehicle is connected, this parameter will not be reported. | [optional] 

## Methods

### GetCargoEmpty

`func (o *V1CargoResponseSensors) GetCargoEmpty() bool`

GetCargoEmpty returns the CargoEmpty field if non-nil, zero value otherwise.

### GetCargoEmptyOk

`func (o *V1CargoResponseSensors) GetCargoEmptyOk() (bool, bool)`

GetCargoEmptyOk returns a tuple with the CargoEmpty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCargoEmpty

`func (o *V1CargoResponseSensors) HasCargoEmpty() bool`

HasCargoEmpty returns a boolean if a field has been set.

### SetCargoEmpty

`func (o *V1CargoResponseSensors) SetCargoEmpty(v bool)`

SetCargoEmpty gets a reference to the given bool and assigns it to the CargoEmpty field.

### GetCargoStatusTime

`func (o *V1CargoResponseSensors) GetCargoStatusTime() string`

GetCargoStatusTime returns the CargoStatusTime field if non-nil, zero value otherwise.

### GetCargoStatusTimeOk

`func (o *V1CargoResponseSensors) GetCargoStatusTimeOk() (string, bool)`

GetCargoStatusTimeOk returns a tuple with the CargoStatusTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCargoStatusTime

`func (o *V1CargoResponseSensors) HasCargoStatusTime() bool`

HasCargoStatusTime returns a boolean if a field has been set.

### SetCargoStatusTime

`func (o *V1CargoResponseSensors) SetCargoStatusTime(v string)`

SetCargoStatusTime gets a reference to the given string and assigns it to the CargoStatusTime field.

### GetId

`func (o *V1CargoResponseSensors) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1CargoResponseSensors) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1CargoResponseSensors) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1CargoResponseSensors) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetName

`func (o *V1CargoResponseSensors) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *V1CargoResponseSensors) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *V1CargoResponseSensors) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *V1CargoResponseSensors) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetTrailerId

`func (o *V1CargoResponseSensors) GetTrailerId() int32`

GetTrailerId returns the TrailerId field if non-nil, zero value otherwise.

### GetTrailerIdOk

`func (o *V1CargoResponseSensors) GetTrailerIdOk() (int32, bool)`

GetTrailerIdOk returns a tuple with the TrailerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerId

`func (o *V1CargoResponseSensors) HasTrailerId() bool`

HasTrailerId returns a boolean if a field has been set.

### SetTrailerId

`func (o *V1CargoResponseSensors) SetTrailerId(v int32)`

SetTrailerId gets a reference to the given int32 and assigns it to the TrailerId field.

### GetVehicleId

`func (o *V1CargoResponseSensors) GetVehicleId() int32`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1CargoResponseSensors) GetVehicleIdOk() (int32, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1CargoResponseSensors) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1CargoResponseSensors) SetVehicleId(v int32)`

SetVehicleId gets a reference to the given int32 and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


