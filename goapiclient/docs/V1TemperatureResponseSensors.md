# V1TemperatureResponseSensors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AmbientTemperature** | Pointer to **int32** | Currently reported ambient temperature in millidegrees celsius. | [optional] 
**AmbientTemperatureTime** | Pointer to **string** | The timestamp of reported ambient temperature, specified in RFC 3339 time. | [optional] 
**Id** | Pointer to **int64** | ID of the sensor. | [optional] 
**Name** | Pointer to **string** | Name of the sensor. | [optional] 
**ProbeTemperature** | Pointer to **int32** | Currently reported probe temperature in millidegrees celsius. If no probe is connected, this parameter will not be reported. | [optional] 
**ProbeTemperatureTime** | Pointer to **string** | The timestamp of reported probe temperature, specified in RFC 3339 time. | [optional] 
**TrailerId** | Pointer to **int32** | ID of the trailer associated with the sensor for the data point. If no trailer is connected, this parameter will not be reported. | [optional] 
**VehicleId** | Pointer to **int32** | ID of the vehicle associated with the sensor for the data point. If no vehicle is connected, this parameter will not be reported. | [optional] 

## Methods

### GetAmbientTemperature

`func (o *V1TemperatureResponseSensors) GetAmbientTemperature() int32`

GetAmbientTemperature returns the AmbientTemperature field if non-nil, zero value otherwise.

### GetAmbientTemperatureOk

`func (o *V1TemperatureResponseSensors) GetAmbientTemperatureOk() (int32, bool)`

GetAmbientTemperatureOk returns a tuple with the AmbientTemperature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAmbientTemperature

`func (o *V1TemperatureResponseSensors) HasAmbientTemperature() bool`

HasAmbientTemperature returns a boolean if a field has been set.

### SetAmbientTemperature

`func (o *V1TemperatureResponseSensors) SetAmbientTemperature(v int32)`

SetAmbientTemperature gets a reference to the given int32 and assigns it to the AmbientTemperature field.

### GetAmbientTemperatureTime

`func (o *V1TemperatureResponseSensors) GetAmbientTemperatureTime() string`

GetAmbientTemperatureTime returns the AmbientTemperatureTime field if non-nil, zero value otherwise.

### GetAmbientTemperatureTimeOk

`func (o *V1TemperatureResponseSensors) GetAmbientTemperatureTimeOk() (string, bool)`

GetAmbientTemperatureTimeOk returns a tuple with the AmbientTemperatureTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAmbientTemperatureTime

`func (o *V1TemperatureResponseSensors) HasAmbientTemperatureTime() bool`

HasAmbientTemperatureTime returns a boolean if a field has been set.

### SetAmbientTemperatureTime

`func (o *V1TemperatureResponseSensors) SetAmbientTemperatureTime(v string)`

SetAmbientTemperatureTime gets a reference to the given string and assigns it to the AmbientTemperatureTime field.

### GetId

`func (o *V1TemperatureResponseSensors) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1TemperatureResponseSensors) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1TemperatureResponseSensors) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1TemperatureResponseSensors) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetName

`func (o *V1TemperatureResponseSensors) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *V1TemperatureResponseSensors) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *V1TemperatureResponseSensors) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *V1TemperatureResponseSensors) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetProbeTemperature

`func (o *V1TemperatureResponseSensors) GetProbeTemperature() int32`

GetProbeTemperature returns the ProbeTemperature field if non-nil, zero value otherwise.

### GetProbeTemperatureOk

`func (o *V1TemperatureResponseSensors) GetProbeTemperatureOk() (int32, bool)`

GetProbeTemperatureOk returns a tuple with the ProbeTemperature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasProbeTemperature

`func (o *V1TemperatureResponseSensors) HasProbeTemperature() bool`

HasProbeTemperature returns a boolean if a field has been set.

### SetProbeTemperature

`func (o *V1TemperatureResponseSensors) SetProbeTemperature(v int32)`

SetProbeTemperature gets a reference to the given int32 and assigns it to the ProbeTemperature field.

### GetProbeTemperatureTime

`func (o *V1TemperatureResponseSensors) GetProbeTemperatureTime() string`

GetProbeTemperatureTime returns the ProbeTemperatureTime field if non-nil, zero value otherwise.

### GetProbeTemperatureTimeOk

`func (o *V1TemperatureResponseSensors) GetProbeTemperatureTimeOk() (string, bool)`

GetProbeTemperatureTimeOk returns a tuple with the ProbeTemperatureTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasProbeTemperatureTime

`func (o *V1TemperatureResponseSensors) HasProbeTemperatureTime() bool`

HasProbeTemperatureTime returns a boolean if a field has been set.

### SetProbeTemperatureTime

`func (o *V1TemperatureResponseSensors) SetProbeTemperatureTime(v string)`

SetProbeTemperatureTime gets a reference to the given string and assigns it to the ProbeTemperatureTime field.

### GetTrailerId

`func (o *V1TemperatureResponseSensors) GetTrailerId() int32`

GetTrailerId returns the TrailerId field if non-nil, zero value otherwise.

### GetTrailerIdOk

`func (o *V1TemperatureResponseSensors) GetTrailerIdOk() (int32, bool)`

GetTrailerIdOk returns a tuple with the TrailerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerId

`func (o *V1TemperatureResponseSensors) HasTrailerId() bool`

HasTrailerId returns a boolean if a field has been set.

### SetTrailerId

`func (o *V1TemperatureResponseSensors) SetTrailerId(v int32)`

SetTrailerId gets a reference to the given int32 and assigns it to the TrailerId field.

### GetVehicleId

`func (o *V1TemperatureResponseSensors) GetVehicleId() int32`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1TemperatureResponseSensors) GetVehicleIdOk() (int32, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1TemperatureResponseSensors) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1TemperatureResponseSensors) SetVehicleId(v int32)`

SetVehicleId gets a reference to the given int32 and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


