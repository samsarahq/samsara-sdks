# EquipmentStatsSnapshotResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | ID of the equipment. | 
**Name** | Pointer to **string** | Name of the equipment. | [optional] 
**EngineRpm** | Pointer to [**EquipmentEngineRpm**](EquipmentEngineRpm.md) |  | [optional] 
**EngineSeconds** | Pointer to [**EquipmentEngineSeconds**](EquipmentEngineSeconds.md) |  | [optional] 
**EngineState** | Pointer to [**EquipmentEngineState**](EquipmentEngineState.md) |  | [optional] 
**FuelPercent** | Pointer to [**EquipmentFuelPercent**](EquipmentFuelPercent.md) |  | [optional] 
**GatewayEngineSeconds** | Pointer to [**EquipmentGatewayEngineSeconds**](EquipmentGatewayEngineSeconds.md) |  | [optional] 
**GatewayEngineState** | Pointer to [**EquipmentGatewayEngineState**](EquipmentGatewayEngineState.md) |  | [optional] 
**GpsOdometerMeters** | Pointer to [**EquipmentGpsOdometerMeters**](EquipmentGpsOdometerMeters.md) |  | [optional] 
**ObdEngineSeconds** | Pointer to [**EquipmentObdEngineSeconds**](EquipmentObdEngineSeconds.md) |  | [optional] 
**ObdEngineState** | Pointer to [**EquipmentObdEngineState**](EquipmentObdEngineState.md) |  | [optional] 

## Methods

### GetId

`func (o *EquipmentStatsSnapshotResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *EquipmentStatsSnapshotResponse) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *EquipmentStatsSnapshotResponse) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *EquipmentStatsSnapshotResponse) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetName

`func (o *EquipmentStatsSnapshotResponse) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *EquipmentStatsSnapshotResponse) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *EquipmentStatsSnapshotResponse) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *EquipmentStatsSnapshotResponse) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetEngineRpm

`func (o *EquipmentStatsSnapshotResponse) GetEngineRpm() EquipmentEngineRpm`

GetEngineRpm returns the EngineRpm field if non-nil, zero value otherwise.

### GetEngineRpmOk

`func (o *EquipmentStatsSnapshotResponse) GetEngineRpmOk() (EquipmentEngineRpm, bool)`

GetEngineRpmOk returns a tuple with the EngineRpm field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineRpm

`func (o *EquipmentStatsSnapshotResponse) HasEngineRpm() bool`

HasEngineRpm returns a boolean if a field has been set.

### SetEngineRpm

`func (o *EquipmentStatsSnapshotResponse) SetEngineRpm(v EquipmentEngineRpm)`

SetEngineRpm gets a reference to the given EquipmentEngineRpm and assigns it to the EngineRpm field.

### GetEngineSeconds

`func (o *EquipmentStatsSnapshotResponse) GetEngineSeconds() EquipmentEngineSeconds`

GetEngineSeconds returns the EngineSeconds field if non-nil, zero value otherwise.

### GetEngineSecondsOk

`func (o *EquipmentStatsSnapshotResponse) GetEngineSecondsOk() (EquipmentEngineSeconds, bool)`

GetEngineSecondsOk returns a tuple with the EngineSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineSeconds

`func (o *EquipmentStatsSnapshotResponse) HasEngineSeconds() bool`

HasEngineSeconds returns a boolean if a field has been set.

### SetEngineSeconds

`func (o *EquipmentStatsSnapshotResponse) SetEngineSeconds(v EquipmentEngineSeconds)`

SetEngineSeconds gets a reference to the given EquipmentEngineSeconds and assigns it to the EngineSeconds field.

### GetEngineState

`func (o *EquipmentStatsSnapshotResponse) GetEngineState() EquipmentEngineState`

GetEngineState returns the EngineState field if non-nil, zero value otherwise.

### GetEngineStateOk

`func (o *EquipmentStatsSnapshotResponse) GetEngineStateOk() (EquipmentEngineState, bool)`

GetEngineStateOk returns a tuple with the EngineState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineState

`func (o *EquipmentStatsSnapshotResponse) HasEngineState() bool`

HasEngineState returns a boolean if a field has been set.

### SetEngineState

`func (o *EquipmentStatsSnapshotResponse) SetEngineState(v EquipmentEngineState)`

SetEngineState gets a reference to the given EquipmentEngineState and assigns it to the EngineState field.

### GetFuelPercent

`func (o *EquipmentStatsSnapshotResponse) GetFuelPercent() EquipmentFuelPercent`

GetFuelPercent returns the FuelPercent field if non-nil, zero value otherwise.

### GetFuelPercentOk

`func (o *EquipmentStatsSnapshotResponse) GetFuelPercentOk() (EquipmentFuelPercent, bool)`

GetFuelPercentOk returns a tuple with the FuelPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFuelPercent

`func (o *EquipmentStatsSnapshotResponse) HasFuelPercent() bool`

HasFuelPercent returns a boolean if a field has been set.

### SetFuelPercent

`func (o *EquipmentStatsSnapshotResponse) SetFuelPercent(v EquipmentFuelPercent)`

SetFuelPercent gets a reference to the given EquipmentFuelPercent and assigns it to the FuelPercent field.

### GetGatewayEngineSeconds

`func (o *EquipmentStatsSnapshotResponse) GetGatewayEngineSeconds() EquipmentGatewayEngineSeconds`

GetGatewayEngineSeconds returns the GatewayEngineSeconds field if non-nil, zero value otherwise.

### GetGatewayEngineSecondsOk

`func (o *EquipmentStatsSnapshotResponse) GetGatewayEngineSecondsOk() (EquipmentGatewayEngineSeconds, bool)`

GetGatewayEngineSecondsOk returns a tuple with the GatewayEngineSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGatewayEngineSeconds

`func (o *EquipmentStatsSnapshotResponse) HasGatewayEngineSeconds() bool`

HasGatewayEngineSeconds returns a boolean if a field has been set.

### SetGatewayEngineSeconds

`func (o *EquipmentStatsSnapshotResponse) SetGatewayEngineSeconds(v EquipmentGatewayEngineSeconds)`

SetGatewayEngineSeconds gets a reference to the given EquipmentGatewayEngineSeconds and assigns it to the GatewayEngineSeconds field.

### GetGatewayEngineState

`func (o *EquipmentStatsSnapshotResponse) GetGatewayEngineState() EquipmentGatewayEngineState`

GetGatewayEngineState returns the GatewayEngineState field if non-nil, zero value otherwise.

### GetGatewayEngineStateOk

`func (o *EquipmentStatsSnapshotResponse) GetGatewayEngineStateOk() (EquipmentGatewayEngineState, bool)`

GetGatewayEngineStateOk returns a tuple with the GatewayEngineState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGatewayEngineState

`func (o *EquipmentStatsSnapshotResponse) HasGatewayEngineState() bool`

HasGatewayEngineState returns a boolean if a field has been set.

### SetGatewayEngineState

`func (o *EquipmentStatsSnapshotResponse) SetGatewayEngineState(v EquipmentGatewayEngineState)`

SetGatewayEngineState gets a reference to the given EquipmentGatewayEngineState and assigns it to the GatewayEngineState field.

### GetGpsOdometerMeters

`func (o *EquipmentStatsSnapshotResponse) GetGpsOdometerMeters() EquipmentGpsOdometerMeters`

GetGpsOdometerMeters returns the GpsOdometerMeters field if non-nil, zero value otherwise.

### GetGpsOdometerMetersOk

`func (o *EquipmentStatsSnapshotResponse) GetGpsOdometerMetersOk() (EquipmentGpsOdometerMeters, bool)`

GetGpsOdometerMetersOk returns a tuple with the GpsOdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGpsOdometerMeters

`func (o *EquipmentStatsSnapshotResponse) HasGpsOdometerMeters() bool`

HasGpsOdometerMeters returns a boolean if a field has been set.

### SetGpsOdometerMeters

`func (o *EquipmentStatsSnapshotResponse) SetGpsOdometerMeters(v EquipmentGpsOdometerMeters)`

SetGpsOdometerMeters gets a reference to the given EquipmentGpsOdometerMeters and assigns it to the GpsOdometerMeters field.

### GetObdEngineSeconds

`func (o *EquipmentStatsSnapshotResponse) GetObdEngineSeconds() EquipmentObdEngineSeconds`

GetObdEngineSeconds returns the ObdEngineSeconds field if non-nil, zero value otherwise.

### GetObdEngineSecondsOk

`func (o *EquipmentStatsSnapshotResponse) GetObdEngineSecondsOk() (EquipmentObdEngineSeconds, bool)`

GetObdEngineSecondsOk returns a tuple with the ObdEngineSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdEngineSeconds

`func (o *EquipmentStatsSnapshotResponse) HasObdEngineSeconds() bool`

HasObdEngineSeconds returns a boolean if a field has been set.

### SetObdEngineSeconds

`func (o *EquipmentStatsSnapshotResponse) SetObdEngineSeconds(v EquipmentObdEngineSeconds)`

SetObdEngineSeconds gets a reference to the given EquipmentObdEngineSeconds and assigns it to the ObdEngineSeconds field.

### GetObdEngineState

`func (o *EquipmentStatsSnapshotResponse) GetObdEngineState() EquipmentObdEngineState`

GetObdEngineState returns the ObdEngineState field if non-nil, zero value otherwise.

### GetObdEngineStateOk

`func (o *EquipmentStatsSnapshotResponse) GetObdEngineStateOk() (EquipmentObdEngineState, bool)`

GetObdEngineStateOk returns a tuple with the ObdEngineState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdEngineState

`func (o *EquipmentStatsSnapshotResponse) HasObdEngineState() bool`

HasObdEngineState returns a boolean if a field has been set.

### SetObdEngineState

`func (o *EquipmentStatsSnapshotResponse) SetObdEngineState(v EquipmentObdEngineState)`

SetObdEngineState gets a reference to the given EquipmentObdEngineState and assigns it to the ObdEngineState field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


