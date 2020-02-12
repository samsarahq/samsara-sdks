# V1HumidityResponseSensors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Humidity** | Pointer to **int32** | Currently reported relative humidity in percent, from 0-100. | [optional] 
**HumidityTime** | Pointer to **string** | The timestamp of reported relative humidity, specified in RFC 3339 time. | [optional] 
**Id** | Pointer to **int64** | ID of the sensor. | [optional] 
**Name** | Pointer to **string** | Name of the sensor. | [optional] 
**TrailerId** | Pointer to **int32** | ID of the trailer associated with the sensor for the data point. If no trailer is connected, this parameter will not be reported. | [optional] 
**VehicleId** | Pointer to **int32** | ID of the vehicle associated with the sensor for the data point. If no vehicle is connected, this parameter will not be reported. | [optional] 

## Methods

### GetHumidity

`func (o *V1HumidityResponseSensors) GetHumidity() int32`

GetHumidity returns the Humidity field if non-nil, zero value otherwise.

### GetHumidityOk

`func (o *V1HumidityResponseSensors) GetHumidityOk() (int32, bool)`

GetHumidityOk returns a tuple with the Humidity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHumidity

`func (o *V1HumidityResponseSensors) HasHumidity() bool`

HasHumidity returns a boolean if a field has been set.

### SetHumidity

`func (o *V1HumidityResponseSensors) SetHumidity(v int32)`

SetHumidity gets a reference to the given int32 and assigns it to the Humidity field.

### GetHumidityTime

`func (o *V1HumidityResponseSensors) GetHumidityTime() string`

GetHumidityTime returns the HumidityTime field if non-nil, zero value otherwise.

### GetHumidityTimeOk

`func (o *V1HumidityResponseSensors) GetHumidityTimeOk() (string, bool)`

GetHumidityTimeOk returns a tuple with the HumidityTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHumidityTime

`func (o *V1HumidityResponseSensors) HasHumidityTime() bool`

HasHumidityTime returns a boolean if a field has been set.

### SetHumidityTime

`func (o *V1HumidityResponseSensors) SetHumidityTime(v string)`

SetHumidityTime gets a reference to the given string and assigns it to the HumidityTime field.

### GetId

`func (o *V1HumidityResponseSensors) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1HumidityResponseSensors) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1HumidityResponseSensors) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1HumidityResponseSensors) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetName

`func (o *V1HumidityResponseSensors) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *V1HumidityResponseSensors) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *V1HumidityResponseSensors) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *V1HumidityResponseSensors) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetTrailerId

`func (o *V1HumidityResponseSensors) GetTrailerId() int32`

GetTrailerId returns the TrailerId field if non-nil, zero value otherwise.

### GetTrailerIdOk

`func (o *V1HumidityResponseSensors) GetTrailerIdOk() (int32, bool)`

GetTrailerIdOk returns a tuple with the TrailerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerId

`func (o *V1HumidityResponseSensors) HasTrailerId() bool`

HasTrailerId returns a boolean if a field has been set.

### SetTrailerId

`func (o *V1HumidityResponseSensors) SetTrailerId(v int32)`

SetTrailerId gets a reference to the given int32 and assigns it to the TrailerId field.

### GetVehicleId

`func (o *V1HumidityResponseSensors) GetVehicleId() int32`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1HumidityResponseSensors) GetVehicleIdOk() (int32, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1HumidityResponseSensors) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1HumidityResponseSensors) SetVehicleId(v int32)`

SetVehicleId gets a reference to the given int32 and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


