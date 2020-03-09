# VehicleStatsListResponseData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CtpSmogTestData** | Pointer to [**[]VehicleStatsCtpSmogTestData**](VehicleStatsCtpSmogTestData.md) | Required data for one CTP smog test. | [optional] 
**EngineStates** | Pointer to [**[]VehicleStatsEngineState**](VehicleStatsEngineState.md) | A list of engine state events for the given vehicle. | [optional] 
**FuelPercent** | Pointer to [**[]VehicleStatsFuelPercent**](VehicleStatsFuelPercent.md) | A list of fuel percentage readings for the given vehicle. | [optional] 
**GpsDistanceMeters** | Pointer to [**[]VehicleStatsGpsDistanceMeters**](VehicleStatsGpsDistanceMeters.md) | A list of GPS distance events for the given vehicle. | [optional] 
**GpsOdometerMeters** | Pointer to [**[]VehicleStatsGpsOdometerMeters**](VehicleStatsGpsOdometerMeters.md) | A list of GPS odometer events for the given vehicle. | [optional] 
**Id** | Pointer to **string** | The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed. | 
**Name** | Pointer to **string** | The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time. | 
**ObdEngineSeconds** | Pointer to [**[]VehicleStatsObdEngineSeconds**](VehicleStatsObdEngineSeconds.md) | A list of OBD engine seconds readings for the given vehicle. | [optional] 
**ObdOdometerMeters** | Pointer to [**[]VehicleStatsObdOdometerMeters**](VehicleStatsObdOdometerMeters.md) | A list of OBD odometer readings for the given vehicle. | [optional] 

## Methods

### GetCtpSmogTestData

`func (o *VehicleStatsListResponseData) GetCtpSmogTestData() []VehicleStatsCtpSmogTestData`

GetCtpSmogTestData returns the CtpSmogTestData field if non-nil, zero value otherwise.

### GetCtpSmogTestDataOk

`func (o *VehicleStatsListResponseData) GetCtpSmogTestDataOk() ([]VehicleStatsCtpSmogTestData, bool)`

GetCtpSmogTestDataOk returns a tuple with the CtpSmogTestData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCtpSmogTestData

`func (o *VehicleStatsListResponseData) HasCtpSmogTestData() bool`

HasCtpSmogTestData returns a boolean if a field has been set.

### SetCtpSmogTestData

`func (o *VehicleStatsListResponseData) SetCtpSmogTestData(v []VehicleStatsCtpSmogTestData)`

SetCtpSmogTestData gets a reference to the given []VehicleStatsCtpSmogTestData and assigns it to the CtpSmogTestData field.

### GetEngineStates

`func (o *VehicleStatsListResponseData) GetEngineStates() []VehicleStatsEngineState`

GetEngineStates returns the EngineStates field if non-nil, zero value otherwise.

### GetEngineStatesOk

`func (o *VehicleStatsListResponseData) GetEngineStatesOk() ([]VehicleStatsEngineState, bool)`

GetEngineStatesOk returns a tuple with the EngineStates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineStates

`func (o *VehicleStatsListResponseData) HasEngineStates() bool`

HasEngineStates returns a boolean if a field has been set.

### SetEngineStates

`func (o *VehicleStatsListResponseData) SetEngineStates(v []VehicleStatsEngineState)`

SetEngineStates gets a reference to the given []VehicleStatsEngineState and assigns it to the EngineStates field.

### GetFuelPercent

`func (o *VehicleStatsListResponseData) GetFuelPercent() []VehicleStatsFuelPercent`

GetFuelPercent returns the FuelPercent field if non-nil, zero value otherwise.

### GetFuelPercentOk

`func (o *VehicleStatsListResponseData) GetFuelPercentOk() ([]VehicleStatsFuelPercent, bool)`

GetFuelPercentOk returns a tuple with the FuelPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFuelPercent

`func (o *VehicleStatsListResponseData) HasFuelPercent() bool`

HasFuelPercent returns a boolean if a field has been set.

### SetFuelPercent

`func (o *VehicleStatsListResponseData) SetFuelPercent(v []VehicleStatsFuelPercent)`

SetFuelPercent gets a reference to the given []VehicleStatsFuelPercent and assigns it to the FuelPercent field.

### GetGpsDistanceMeters

`func (o *VehicleStatsListResponseData) GetGpsDistanceMeters() []VehicleStatsGpsDistanceMeters`

GetGpsDistanceMeters returns the GpsDistanceMeters field if non-nil, zero value otherwise.

### GetGpsDistanceMetersOk

`func (o *VehicleStatsListResponseData) GetGpsDistanceMetersOk() ([]VehicleStatsGpsDistanceMeters, bool)`

GetGpsDistanceMetersOk returns a tuple with the GpsDistanceMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGpsDistanceMeters

`func (o *VehicleStatsListResponseData) HasGpsDistanceMeters() bool`

HasGpsDistanceMeters returns a boolean if a field has been set.

### SetGpsDistanceMeters

`func (o *VehicleStatsListResponseData) SetGpsDistanceMeters(v []VehicleStatsGpsDistanceMeters)`

SetGpsDistanceMeters gets a reference to the given []VehicleStatsGpsDistanceMeters and assigns it to the GpsDistanceMeters field.

### GetGpsOdometerMeters

`func (o *VehicleStatsListResponseData) GetGpsOdometerMeters() []VehicleStatsGpsOdometerMeters`

GetGpsOdometerMeters returns the GpsOdometerMeters field if non-nil, zero value otherwise.

### GetGpsOdometerMetersOk

`func (o *VehicleStatsListResponseData) GetGpsOdometerMetersOk() ([]VehicleStatsGpsOdometerMeters, bool)`

GetGpsOdometerMetersOk returns a tuple with the GpsOdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGpsOdometerMeters

`func (o *VehicleStatsListResponseData) HasGpsOdometerMeters() bool`

HasGpsOdometerMeters returns a boolean if a field has been set.

### SetGpsOdometerMeters

`func (o *VehicleStatsListResponseData) SetGpsOdometerMeters(v []VehicleStatsGpsOdometerMeters)`

SetGpsOdometerMeters gets a reference to the given []VehicleStatsGpsOdometerMeters and assigns it to the GpsOdometerMeters field.

### GetId

`func (o *VehicleStatsListResponseData) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *VehicleStatsListResponseData) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *VehicleStatsListResponseData) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *VehicleStatsListResponseData) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetName

`func (o *VehicleStatsListResponseData) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *VehicleStatsListResponseData) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *VehicleStatsListResponseData) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *VehicleStatsListResponseData) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetObdEngineSeconds

`func (o *VehicleStatsListResponseData) GetObdEngineSeconds() []VehicleStatsObdEngineSeconds`

GetObdEngineSeconds returns the ObdEngineSeconds field if non-nil, zero value otherwise.

### GetObdEngineSecondsOk

`func (o *VehicleStatsListResponseData) GetObdEngineSecondsOk() ([]VehicleStatsObdEngineSeconds, bool)`

GetObdEngineSecondsOk returns a tuple with the ObdEngineSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdEngineSeconds

`func (o *VehicleStatsListResponseData) HasObdEngineSeconds() bool`

HasObdEngineSeconds returns a boolean if a field has been set.

### SetObdEngineSeconds

`func (o *VehicleStatsListResponseData) SetObdEngineSeconds(v []VehicleStatsObdEngineSeconds)`

SetObdEngineSeconds gets a reference to the given []VehicleStatsObdEngineSeconds and assigns it to the ObdEngineSeconds field.

### GetObdOdometerMeters

`func (o *VehicleStatsListResponseData) GetObdOdometerMeters() []VehicleStatsObdOdometerMeters`

GetObdOdometerMeters returns the ObdOdometerMeters field if non-nil, zero value otherwise.

### GetObdOdometerMetersOk

`func (o *VehicleStatsListResponseData) GetObdOdometerMetersOk() ([]VehicleStatsObdOdometerMeters, bool)`

GetObdOdometerMetersOk returns a tuple with the ObdOdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdOdometerMeters

`func (o *VehicleStatsListResponseData) HasObdOdometerMeters() bool`

HasObdOdometerMeters returns a boolean if a field has been set.

### SetObdOdometerMeters

`func (o *VehicleStatsListResponseData) SetObdOdometerMeters(v []VehicleStatsObdOdometerMeters)`

SetObdOdometerMeters gets a reference to the given []VehicleStatsObdOdometerMeters and assigns it to the ObdOdometerMeters field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


