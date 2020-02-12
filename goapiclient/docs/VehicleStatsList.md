# VehicleStatsList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | ID of the vehicle. | [optional] 
**Name** | Pointer to **string** | Name of the vehicle. | [optional] 
**EngineStates** | Pointer to [**[]VehicleEngineState**](VehicleEngineState.md) |  | [optional] 
**FuelPercents** | Pointer to [**[]VehicleFuelPercent**](VehicleFuelPercent.md) |  | [optional] 
**ObdOdometerMeters** | Pointer to [**[]VehicleObdOdometerMeters**](VehicleObdOdometerMeters.md) |  | [optional] 
**GpsOdometerMeters** | Pointer to [**[]VehicleGpsOdometerMeters**](VehicleGpsOdometerMeters.md) |  | [optional] 
**ObdEngineSeconds** | Pointer to [**[]VehicleObdEngineSeconds**](VehicleObdEngineSeconds.md) |  | [optional] 
**GpsDistanceMeters** | Pointer to [**[]VehicleGpsDistanceMeters**](VehicleGpsDistanceMeters.md) |  | [optional] 

## Methods

### GetId

`func (o *VehicleStatsList) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *VehicleStatsList) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *VehicleStatsList) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *VehicleStatsList) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetName

`func (o *VehicleStatsList) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *VehicleStatsList) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *VehicleStatsList) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *VehicleStatsList) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetEngineStates

`func (o *VehicleStatsList) GetEngineStates() []VehicleEngineState`

GetEngineStates returns the EngineStates field if non-nil, zero value otherwise.

### GetEngineStatesOk

`func (o *VehicleStatsList) GetEngineStatesOk() ([]VehicleEngineState, bool)`

GetEngineStatesOk returns a tuple with the EngineStates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineStates

`func (o *VehicleStatsList) HasEngineStates() bool`

HasEngineStates returns a boolean if a field has been set.

### SetEngineStates

`func (o *VehicleStatsList) SetEngineStates(v []VehicleEngineState)`

SetEngineStates gets a reference to the given []VehicleEngineState and assigns it to the EngineStates field.

### GetFuelPercents

`func (o *VehicleStatsList) GetFuelPercents() []VehicleFuelPercent`

GetFuelPercents returns the FuelPercents field if non-nil, zero value otherwise.

### GetFuelPercentsOk

`func (o *VehicleStatsList) GetFuelPercentsOk() ([]VehicleFuelPercent, bool)`

GetFuelPercentsOk returns a tuple with the FuelPercents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFuelPercents

`func (o *VehicleStatsList) HasFuelPercents() bool`

HasFuelPercents returns a boolean if a field has been set.

### SetFuelPercents

`func (o *VehicleStatsList) SetFuelPercents(v []VehicleFuelPercent)`

SetFuelPercents gets a reference to the given []VehicleFuelPercent and assigns it to the FuelPercents field.

### GetObdOdometerMeters

`func (o *VehicleStatsList) GetObdOdometerMeters() []VehicleObdOdometerMeters`

GetObdOdometerMeters returns the ObdOdometerMeters field if non-nil, zero value otherwise.

### GetObdOdometerMetersOk

`func (o *VehicleStatsList) GetObdOdometerMetersOk() ([]VehicleObdOdometerMeters, bool)`

GetObdOdometerMetersOk returns a tuple with the ObdOdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdOdometerMeters

`func (o *VehicleStatsList) HasObdOdometerMeters() bool`

HasObdOdometerMeters returns a boolean if a field has been set.

### SetObdOdometerMeters

`func (o *VehicleStatsList) SetObdOdometerMeters(v []VehicleObdOdometerMeters)`

SetObdOdometerMeters gets a reference to the given []VehicleObdOdometerMeters and assigns it to the ObdOdometerMeters field.

### GetGpsOdometerMeters

`func (o *VehicleStatsList) GetGpsOdometerMeters() []VehicleGpsOdometerMeters`

GetGpsOdometerMeters returns the GpsOdometerMeters field if non-nil, zero value otherwise.

### GetGpsOdometerMetersOk

`func (o *VehicleStatsList) GetGpsOdometerMetersOk() ([]VehicleGpsOdometerMeters, bool)`

GetGpsOdometerMetersOk returns a tuple with the GpsOdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGpsOdometerMeters

`func (o *VehicleStatsList) HasGpsOdometerMeters() bool`

HasGpsOdometerMeters returns a boolean if a field has been set.

### SetGpsOdometerMeters

`func (o *VehicleStatsList) SetGpsOdometerMeters(v []VehicleGpsOdometerMeters)`

SetGpsOdometerMeters gets a reference to the given []VehicleGpsOdometerMeters and assigns it to the GpsOdometerMeters field.

### GetObdEngineSeconds

`func (o *VehicleStatsList) GetObdEngineSeconds() []VehicleObdEngineSeconds`

GetObdEngineSeconds returns the ObdEngineSeconds field if non-nil, zero value otherwise.

### GetObdEngineSecondsOk

`func (o *VehicleStatsList) GetObdEngineSecondsOk() ([]VehicleObdEngineSeconds, bool)`

GetObdEngineSecondsOk returns a tuple with the ObdEngineSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdEngineSeconds

`func (o *VehicleStatsList) HasObdEngineSeconds() bool`

HasObdEngineSeconds returns a boolean if a field has been set.

### SetObdEngineSeconds

`func (o *VehicleStatsList) SetObdEngineSeconds(v []VehicleObdEngineSeconds)`

SetObdEngineSeconds gets a reference to the given []VehicleObdEngineSeconds and assigns it to the ObdEngineSeconds field.

### GetGpsDistanceMeters

`func (o *VehicleStatsList) GetGpsDistanceMeters() []VehicleGpsDistanceMeters`

GetGpsDistanceMeters returns the GpsDistanceMeters field if non-nil, zero value otherwise.

### GetGpsDistanceMetersOk

`func (o *VehicleStatsList) GetGpsDistanceMetersOk() ([]VehicleGpsDistanceMeters, bool)`

GetGpsDistanceMetersOk returns a tuple with the GpsDistanceMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGpsDistanceMeters

`func (o *VehicleStatsList) HasGpsDistanceMeters() bool`

HasGpsDistanceMeters returns a boolean if a field has been set.

### SetGpsDistanceMeters

`func (o *VehicleStatsList) SetGpsDistanceMeters(v []VehicleGpsDistanceMeters)`

SetGpsDistanceMeters gets a reference to the given []VehicleGpsDistanceMeters and assigns it to the GpsDistanceMeters field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


