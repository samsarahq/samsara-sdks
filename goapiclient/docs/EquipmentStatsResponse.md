# EquipmentStatsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | ID of the equipment. | 
**Name** | Pointer to **string** | Name of the equipment. | [optional] 
**EngineRpm** | Pointer to [**[]EquipmentEngineRpm**](EquipmentEngineRpm.md) |  | [optional] 
**EngineSeconds** | Pointer to [**[]EquipmentEngineSeconds**](EquipmentEngineSeconds.md) |  | [optional] 
**EngineStates** | Pointer to [**[]EquipmentEngineState**](EquipmentEngineState.md) |  | [optional] 
**FuelPercents** | Pointer to [**[]EquipmentFuelPercent**](EquipmentFuelPercent.md) |  | [optional] 
**GatewayEngineSeconds** | Pointer to [**[]EquipmentGatewayEngineSeconds**](EquipmentGatewayEngineSeconds.md) |  | [optional] 
**GatewayEngineStates** | Pointer to [**[]EquipmentGatewayEngineState**](EquipmentGatewayEngineState.md) |  | [optional] 
**GpsOdometerMeters** | Pointer to [**[]EquipmentGpsOdometerMeters**](EquipmentGpsOdometerMeters.md) |  | [optional] 
**ObdEngineSeconds** | Pointer to [**[]EquipmentObdEngineSeconds**](EquipmentObdEngineSeconds.md) |  | [optional] 
**ObdEngineStates** | Pointer to [**[]EquipmentObdEngineState**](EquipmentObdEngineState.md) |  | [optional] 

## Methods

### GetId

`func (o *EquipmentStatsResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *EquipmentStatsResponse) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *EquipmentStatsResponse) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *EquipmentStatsResponse) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetName

`func (o *EquipmentStatsResponse) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *EquipmentStatsResponse) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *EquipmentStatsResponse) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *EquipmentStatsResponse) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetEngineRpm

`func (o *EquipmentStatsResponse) GetEngineRpm() []EquipmentEngineRpm`

GetEngineRpm returns the EngineRpm field if non-nil, zero value otherwise.

### GetEngineRpmOk

`func (o *EquipmentStatsResponse) GetEngineRpmOk() ([]EquipmentEngineRpm, bool)`

GetEngineRpmOk returns a tuple with the EngineRpm field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineRpm

`func (o *EquipmentStatsResponse) HasEngineRpm() bool`

HasEngineRpm returns a boolean if a field has been set.

### SetEngineRpm

`func (o *EquipmentStatsResponse) SetEngineRpm(v []EquipmentEngineRpm)`

SetEngineRpm gets a reference to the given []EquipmentEngineRpm and assigns it to the EngineRpm field.

### GetEngineSeconds

`func (o *EquipmentStatsResponse) GetEngineSeconds() []EquipmentEngineSeconds`

GetEngineSeconds returns the EngineSeconds field if non-nil, zero value otherwise.

### GetEngineSecondsOk

`func (o *EquipmentStatsResponse) GetEngineSecondsOk() ([]EquipmentEngineSeconds, bool)`

GetEngineSecondsOk returns a tuple with the EngineSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineSeconds

`func (o *EquipmentStatsResponse) HasEngineSeconds() bool`

HasEngineSeconds returns a boolean if a field has been set.

### SetEngineSeconds

`func (o *EquipmentStatsResponse) SetEngineSeconds(v []EquipmentEngineSeconds)`

SetEngineSeconds gets a reference to the given []EquipmentEngineSeconds and assigns it to the EngineSeconds field.

### GetEngineStates

`func (o *EquipmentStatsResponse) GetEngineStates() []EquipmentEngineState`

GetEngineStates returns the EngineStates field if non-nil, zero value otherwise.

### GetEngineStatesOk

`func (o *EquipmentStatsResponse) GetEngineStatesOk() ([]EquipmentEngineState, bool)`

GetEngineStatesOk returns a tuple with the EngineStates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineStates

`func (o *EquipmentStatsResponse) HasEngineStates() bool`

HasEngineStates returns a boolean if a field has been set.

### SetEngineStates

`func (o *EquipmentStatsResponse) SetEngineStates(v []EquipmentEngineState)`

SetEngineStates gets a reference to the given []EquipmentEngineState and assigns it to the EngineStates field.

### GetFuelPercents

`func (o *EquipmentStatsResponse) GetFuelPercents() []EquipmentFuelPercent`

GetFuelPercents returns the FuelPercents field if non-nil, zero value otherwise.

### GetFuelPercentsOk

`func (o *EquipmentStatsResponse) GetFuelPercentsOk() ([]EquipmentFuelPercent, bool)`

GetFuelPercentsOk returns a tuple with the FuelPercents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFuelPercents

`func (o *EquipmentStatsResponse) HasFuelPercents() bool`

HasFuelPercents returns a boolean if a field has been set.

### SetFuelPercents

`func (o *EquipmentStatsResponse) SetFuelPercents(v []EquipmentFuelPercent)`

SetFuelPercents gets a reference to the given []EquipmentFuelPercent and assigns it to the FuelPercents field.

### GetGatewayEngineSeconds

`func (o *EquipmentStatsResponse) GetGatewayEngineSeconds() []EquipmentGatewayEngineSeconds`

GetGatewayEngineSeconds returns the GatewayEngineSeconds field if non-nil, zero value otherwise.

### GetGatewayEngineSecondsOk

`func (o *EquipmentStatsResponse) GetGatewayEngineSecondsOk() ([]EquipmentGatewayEngineSeconds, bool)`

GetGatewayEngineSecondsOk returns a tuple with the GatewayEngineSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGatewayEngineSeconds

`func (o *EquipmentStatsResponse) HasGatewayEngineSeconds() bool`

HasGatewayEngineSeconds returns a boolean if a field has been set.

### SetGatewayEngineSeconds

`func (o *EquipmentStatsResponse) SetGatewayEngineSeconds(v []EquipmentGatewayEngineSeconds)`

SetGatewayEngineSeconds gets a reference to the given []EquipmentGatewayEngineSeconds and assigns it to the GatewayEngineSeconds field.

### GetGatewayEngineStates

`func (o *EquipmentStatsResponse) GetGatewayEngineStates() []EquipmentGatewayEngineState`

GetGatewayEngineStates returns the GatewayEngineStates field if non-nil, zero value otherwise.

### GetGatewayEngineStatesOk

`func (o *EquipmentStatsResponse) GetGatewayEngineStatesOk() ([]EquipmentGatewayEngineState, bool)`

GetGatewayEngineStatesOk returns a tuple with the GatewayEngineStates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGatewayEngineStates

`func (o *EquipmentStatsResponse) HasGatewayEngineStates() bool`

HasGatewayEngineStates returns a boolean if a field has been set.

### SetGatewayEngineStates

`func (o *EquipmentStatsResponse) SetGatewayEngineStates(v []EquipmentGatewayEngineState)`

SetGatewayEngineStates gets a reference to the given []EquipmentGatewayEngineState and assigns it to the GatewayEngineStates field.

### GetGpsOdometerMeters

`func (o *EquipmentStatsResponse) GetGpsOdometerMeters() []EquipmentGpsOdometerMeters`

GetGpsOdometerMeters returns the GpsOdometerMeters field if non-nil, zero value otherwise.

### GetGpsOdometerMetersOk

`func (o *EquipmentStatsResponse) GetGpsOdometerMetersOk() ([]EquipmentGpsOdometerMeters, bool)`

GetGpsOdometerMetersOk returns a tuple with the GpsOdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGpsOdometerMeters

`func (o *EquipmentStatsResponse) HasGpsOdometerMeters() bool`

HasGpsOdometerMeters returns a boolean if a field has been set.

### SetGpsOdometerMeters

`func (o *EquipmentStatsResponse) SetGpsOdometerMeters(v []EquipmentGpsOdometerMeters)`

SetGpsOdometerMeters gets a reference to the given []EquipmentGpsOdometerMeters and assigns it to the GpsOdometerMeters field.

### GetObdEngineSeconds

`func (o *EquipmentStatsResponse) GetObdEngineSeconds() []EquipmentObdEngineSeconds`

GetObdEngineSeconds returns the ObdEngineSeconds field if non-nil, zero value otherwise.

### GetObdEngineSecondsOk

`func (o *EquipmentStatsResponse) GetObdEngineSecondsOk() ([]EquipmentObdEngineSeconds, bool)`

GetObdEngineSecondsOk returns a tuple with the ObdEngineSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdEngineSeconds

`func (o *EquipmentStatsResponse) HasObdEngineSeconds() bool`

HasObdEngineSeconds returns a boolean if a field has been set.

### SetObdEngineSeconds

`func (o *EquipmentStatsResponse) SetObdEngineSeconds(v []EquipmentObdEngineSeconds)`

SetObdEngineSeconds gets a reference to the given []EquipmentObdEngineSeconds and assigns it to the ObdEngineSeconds field.

### GetObdEngineStates

`func (o *EquipmentStatsResponse) GetObdEngineStates() []EquipmentObdEngineState`

GetObdEngineStates returns the ObdEngineStates field if non-nil, zero value otherwise.

### GetObdEngineStatesOk

`func (o *EquipmentStatsResponse) GetObdEngineStatesOk() ([]EquipmentObdEngineState, bool)`

GetObdEngineStatesOk returns a tuple with the ObdEngineStates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdEngineStates

`func (o *EquipmentStatsResponse) HasObdEngineStates() bool`

HasObdEngineStates returns a boolean if a field has been set.

### SetObdEngineStates

`func (o *EquipmentStatsResponse) SetObdEngineStates(v []EquipmentObdEngineState)`

SetObdEngineStates gets a reference to the given []EquipmentObdEngineState and assigns it to the ObdEngineStates field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


