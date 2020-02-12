# VehicleStatsSnapshotResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | ID of the vehicle. | [optional] 
**Name** | Pointer to **string** | Name of the vehicle. | [optional] 
**EngineState** | Pointer to [**VehicleEngineState**](VehicleEngineState.md) |  | [optional] 
**FuelPercent** | Pointer to [**VehicleFuelPercent**](VehicleFuelPercent.md) |  | [optional] 
**GpsDistanceMeters** | Pointer to [**VehicleGpsDistanceMeters**](VehicleGpsDistanceMeters.md) |  | [optional] 
**GpsOdometerMeters** | Pointer to [**VehicleGpsOdometerMeters**](VehicleGpsOdometerMeters.md) |  | [optional] 
**ObdEngineSeconds** | Pointer to [**VehicleObdEngineSeconds**](VehicleObdEngineSeconds.md) |  | [optional] 
**ObdOdometerMeters** | Pointer to [**VehicleObdOdometerMeters**](VehicleObdOdometerMeters.md) |  | [optional] 

## Methods

### GetId

`func (o *VehicleStatsSnapshotResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *VehicleStatsSnapshotResponse) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *VehicleStatsSnapshotResponse) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *VehicleStatsSnapshotResponse) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetName

`func (o *VehicleStatsSnapshotResponse) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *VehicleStatsSnapshotResponse) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *VehicleStatsSnapshotResponse) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *VehicleStatsSnapshotResponse) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetEngineState

`func (o *VehicleStatsSnapshotResponse) GetEngineState() VehicleEngineState`

GetEngineState returns the EngineState field if non-nil, zero value otherwise.

### GetEngineStateOk

`func (o *VehicleStatsSnapshotResponse) GetEngineStateOk() (VehicleEngineState, bool)`

GetEngineStateOk returns a tuple with the EngineState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineState

`func (o *VehicleStatsSnapshotResponse) HasEngineState() bool`

HasEngineState returns a boolean if a field has been set.

### SetEngineState

`func (o *VehicleStatsSnapshotResponse) SetEngineState(v VehicleEngineState)`

SetEngineState gets a reference to the given VehicleEngineState and assigns it to the EngineState field.

### GetFuelPercent

`func (o *VehicleStatsSnapshotResponse) GetFuelPercent() VehicleFuelPercent`

GetFuelPercent returns the FuelPercent field if non-nil, zero value otherwise.

### GetFuelPercentOk

`func (o *VehicleStatsSnapshotResponse) GetFuelPercentOk() (VehicleFuelPercent, bool)`

GetFuelPercentOk returns a tuple with the FuelPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFuelPercent

`func (o *VehicleStatsSnapshotResponse) HasFuelPercent() bool`

HasFuelPercent returns a boolean if a field has been set.

### SetFuelPercent

`func (o *VehicleStatsSnapshotResponse) SetFuelPercent(v VehicleFuelPercent)`

SetFuelPercent gets a reference to the given VehicleFuelPercent and assigns it to the FuelPercent field.

### GetGpsDistanceMeters

`func (o *VehicleStatsSnapshotResponse) GetGpsDistanceMeters() VehicleGpsDistanceMeters`

GetGpsDistanceMeters returns the GpsDistanceMeters field if non-nil, zero value otherwise.

### GetGpsDistanceMetersOk

`func (o *VehicleStatsSnapshotResponse) GetGpsDistanceMetersOk() (VehicleGpsDistanceMeters, bool)`

GetGpsDistanceMetersOk returns a tuple with the GpsDistanceMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGpsDistanceMeters

`func (o *VehicleStatsSnapshotResponse) HasGpsDistanceMeters() bool`

HasGpsDistanceMeters returns a boolean if a field has been set.

### SetGpsDistanceMeters

`func (o *VehicleStatsSnapshotResponse) SetGpsDistanceMeters(v VehicleGpsDistanceMeters)`

SetGpsDistanceMeters gets a reference to the given VehicleGpsDistanceMeters and assigns it to the GpsDistanceMeters field.

### GetGpsOdometerMeters

`func (o *VehicleStatsSnapshotResponse) GetGpsOdometerMeters() VehicleGpsOdometerMeters`

GetGpsOdometerMeters returns the GpsOdometerMeters field if non-nil, zero value otherwise.

### GetGpsOdometerMetersOk

`func (o *VehicleStatsSnapshotResponse) GetGpsOdometerMetersOk() (VehicleGpsOdometerMeters, bool)`

GetGpsOdometerMetersOk returns a tuple with the GpsOdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGpsOdometerMeters

`func (o *VehicleStatsSnapshotResponse) HasGpsOdometerMeters() bool`

HasGpsOdometerMeters returns a boolean if a field has been set.

### SetGpsOdometerMeters

`func (o *VehicleStatsSnapshotResponse) SetGpsOdometerMeters(v VehicleGpsOdometerMeters)`

SetGpsOdometerMeters gets a reference to the given VehicleGpsOdometerMeters and assigns it to the GpsOdometerMeters field.

### GetObdEngineSeconds

`func (o *VehicleStatsSnapshotResponse) GetObdEngineSeconds() VehicleObdEngineSeconds`

GetObdEngineSeconds returns the ObdEngineSeconds field if non-nil, zero value otherwise.

### GetObdEngineSecondsOk

`func (o *VehicleStatsSnapshotResponse) GetObdEngineSecondsOk() (VehicleObdEngineSeconds, bool)`

GetObdEngineSecondsOk returns a tuple with the ObdEngineSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdEngineSeconds

`func (o *VehicleStatsSnapshotResponse) HasObdEngineSeconds() bool`

HasObdEngineSeconds returns a boolean if a field has been set.

### SetObdEngineSeconds

`func (o *VehicleStatsSnapshotResponse) SetObdEngineSeconds(v VehicleObdEngineSeconds)`

SetObdEngineSeconds gets a reference to the given VehicleObdEngineSeconds and assigns it to the ObdEngineSeconds field.

### GetObdOdometerMeters

`func (o *VehicleStatsSnapshotResponse) GetObdOdometerMeters() VehicleObdOdometerMeters`

GetObdOdometerMeters returns the ObdOdometerMeters field if non-nil, zero value otherwise.

### GetObdOdometerMetersOk

`func (o *VehicleStatsSnapshotResponse) GetObdOdometerMetersOk() (VehicleObdOdometerMeters, bool)`

GetObdOdometerMetersOk returns a tuple with the ObdOdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdOdometerMeters

`func (o *VehicleStatsSnapshotResponse) HasObdOdometerMeters() bool`

HasObdOdometerMeters returns a boolean if a field has been set.

### SetObdOdometerMeters

`func (o *VehicleStatsSnapshotResponse) SetObdOdometerMeters(v VehicleObdOdometerMeters)`

SetObdOdometerMeters gets a reference to the given VehicleObdOdometerMeters and assigns it to the ObdOdometerMeters field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


