# VehicleStatsResponseData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EngineState** | Pointer to [**VehicleStatsEngineState**](VehicleStatsEngineState.md) |  | [optional] 
**FuelPercent** | Pointer to [**VehicleStatsFuelPercent**](VehicleStatsFuelPercent.md) |  | [optional] 
**GpsDistanceMeters** | Pointer to [**VehicleStatsGpsDistanceMeters**](VehicleStatsGpsDistanceMeters.md) |  | [optional] 
**GpsOdometerMeters** | Pointer to [**VehicleStatsGpsOdometerMeters**](VehicleStatsGpsOdometerMeters.md) |  | [optional] 
**Id** | Pointer to **string** | The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed. | 
**Name** | Pointer to **string** | The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time. | 
**ObdEngineSeconds** | Pointer to [**VehicleStatsObdEngineSeconds**](VehicleStatsObdEngineSeconds.md) |  | [optional] 
**ObdOdometerMeters** | Pointer to [**VehicleStatsObdOdometerMeters**](VehicleStatsObdOdometerMeters.md) |  | [optional] 

## Methods

### GetEngineState

`func (o *VehicleStatsResponseData) GetEngineState() VehicleStatsEngineState`

GetEngineState returns the EngineState field if non-nil, zero value otherwise.

### GetEngineStateOk

`func (o *VehicleStatsResponseData) GetEngineStateOk() (VehicleStatsEngineState, bool)`

GetEngineStateOk returns a tuple with the EngineState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineState

`func (o *VehicleStatsResponseData) HasEngineState() bool`

HasEngineState returns a boolean if a field has been set.

### SetEngineState

`func (o *VehicleStatsResponseData) SetEngineState(v VehicleStatsEngineState)`

SetEngineState gets a reference to the given VehicleStatsEngineState and assigns it to the EngineState field.

### GetFuelPercent

`func (o *VehicleStatsResponseData) GetFuelPercent() VehicleStatsFuelPercent`

GetFuelPercent returns the FuelPercent field if non-nil, zero value otherwise.

### GetFuelPercentOk

`func (o *VehicleStatsResponseData) GetFuelPercentOk() (VehicleStatsFuelPercent, bool)`

GetFuelPercentOk returns a tuple with the FuelPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFuelPercent

`func (o *VehicleStatsResponseData) HasFuelPercent() bool`

HasFuelPercent returns a boolean if a field has been set.

### SetFuelPercent

`func (o *VehicleStatsResponseData) SetFuelPercent(v VehicleStatsFuelPercent)`

SetFuelPercent gets a reference to the given VehicleStatsFuelPercent and assigns it to the FuelPercent field.

### GetGpsDistanceMeters

`func (o *VehicleStatsResponseData) GetGpsDistanceMeters() VehicleStatsGpsDistanceMeters`

GetGpsDistanceMeters returns the GpsDistanceMeters field if non-nil, zero value otherwise.

### GetGpsDistanceMetersOk

`func (o *VehicleStatsResponseData) GetGpsDistanceMetersOk() (VehicleStatsGpsDistanceMeters, bool)`

GetGpsDistanceMetersOk returns a tuple with the GpsDistanceMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGpsDistanceMeters

`func (o *VehicleStatsResponseData) HasGpsDistanceMeters() bool`

HasGpsDistanceMeters returns a boolean if a field has been set.

### SetGpsDistanceMeters

`func (o *VehicleStatsResponseData) SetGpsDistanceMeters(v VehicleStatsGpsDistanceMeters)`

SetGpsDistanceMeters gets a reference to the given VehicleStatsGpsDistanceMeters and assigns it to the GpsDistanceMeters field.

### GetGpsOdometerMeters

`func (o *VehicleStatsResponseData) GetGpsOdometerMeters() VehicleStatsGpsOdometerMeters`

GetGpsOdometerMeters returns the GpsOdometerMeters field if non-nil, zero value otherwise.

### GetGpsOdometerMetersOk

`func (o *VehicleStatsResponseData) GetGpsOdometerMetersOk() (VehicleStatsGpsOdometerMeters, bool)`

GetGpsOdometerMetersOk returns a tuple with the GpsOdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGpsOdometerMeters

`func (o *VehicleStatsResponseData) HasGpsOdometerMeters() bool`

HasGpsOdometerMeters returns a boolean if a field has been set.

### SetGpsOdometerMeters

`func (o *VehicleStatsResponseData) SetGpsOdometerMeters(v VehicleStatsGpsOdometerMeters)`

SetGpsOdometerMeters gets a reference to the given VehicleStatsGpsOdometerMeters and assigns it to the GpsOdometerMeters field.

### GetId

`func (o *VehicleStatsResponseData) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *VehicleStatsResponseData) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *VehicleStatsResponseData) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *VehicleStatsResponseData) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetName

`func (o *VehicleStatsResponseData) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *VehicleStatsResponseData) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *VehicleStatsResponseData) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *VehicleStatsResponseData) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetObdEngineSeconds

`func (o *VehicleStatsResponseData) GetObdEngineSeconds() VehicleStatsObdEngineSeconds`

GetObdEngineSeconds returns the ObdEngineSeconds field if non-nil, zero value otherwise.

### GetObdEngineSecondsOk

`func (o *VehicleStatsResponseData) GetObdEngineSecondsOk() (VehicleStatsObdEngineSeconds, bool)`

GetObdEngineSecondsOk returns a tuple with the ObdEngineSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdEngineSeconds

`func (o *VehicleStatsResponseData) HasObdEngineSeconds() bool`

HasObdEngineSeconds returns a boolean if a field has been set.

### SetObdEngineSeconds

`func (o *VehicleStatsResponseData) SetObdEngineSeconds(v VehicleStatsObdEngineSeconds)`

SetObdEngineSeconds gets a reference to the given VehicleStatsObdEngineSeconds and assigns it to the ObdEngineSeconds field.

### GetObdOdometerMeters

`func (o *VehicleStatsResponseData) GetObdOdometerMeters() VehicleStatsObdOdometerMeters`

GetObdOdometerMeters returns the ObdOdometerMeters field if non-nil, zero value otherwise.

### GetObdOdometerMetersOk

`func (o *VehicleStatsResponseData) GetObdOdometerMetersOk() (VehicleStatsObdOdometerMeters, bool)`

GetObdOdometerMetersOk returns a tuple with the ObdOdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdOdometerMeters

`func (o *VehicleStatsResponseData) HasObdOdometerMeters() bool`

HasObdOdometerMeters returns a boolean if a field has been set.

### SetObdOdometerMeters

`func (o *VehicleStatsResponseData) SetObdOdometerMeters(v VehicleStatsObdOdometerMeters)`

SetObdOdometerMeters gets a reference to the given VehicleStatsObdOdometerMeters and assigns it to the ObdOdometerMeters field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


