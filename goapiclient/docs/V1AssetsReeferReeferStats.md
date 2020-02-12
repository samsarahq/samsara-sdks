# V1AssetsReeferReeferStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AmbientAirTemperature** | Pointer to [**[]V1AssetsReeferReeferStatsAmbientAirTemperature**](V1AssetsReefer_reeferStats_ambientAirTemperature.md) | Ambient temperature of the reefer. This is the temperature of the air around the Samsara Asset Gateway. | [optional] 
**DischargeAirTemperature** | Pointer to [**[]V1AssetsReeferReeferStatsDischargeAirTemperature**](V1AssetsReefer_reeferStats_dischargeAirTemperature.md) | Discharge air temperature of the reefer. This is the temperature of the air as it leaves the cooling unit. | [optional] 
**EngineHours** | Pointer to [**[]V1AssetReeferResponseReeferStatsEngineHours**](V1AssetReeferResponse_reeferStats_engineHours.md) | Engine hours of the reefer | [optional] 
**FuelPercentage** | Pointer to [**[]V1AssetReeferResponseReeferStatsFuelPercentage**](V1AssetReeferResponse_reeferStats_fuelPercentage.md) | Fuel percentage of the reefer | [optional] 
**PowerStatus** | Pointer to [**[]V1AssetsReeferReeferStatsPowerStatus**](V1AssetsReefer_reeferStats_powerStatus.md) | Power status of the reefer | [optional] 
**ReeferAlarms** | Pointer to [**[]V1AssetReeferResponseReeferStatsAlarms1**](V1AssetReeferResponse_reeferStats_alarms_1.md) | Reefer alarms | [optional] 
**ReturnAirTemperature** | Pointer to [**[]V1AssetReeferResponseReeferStatsReturnAirTemp**](V1AssetReeferResponse_reeferStats_returnAirTemp.md) | Return air temperature of the reefer. This is the temperature read by the reefer module (Carrier, Thermo King) that shows the temperature of the air as it enters the system. | [optional] 
**SetPoint** | Pointer to [**[]V1AssetReeferResponseReeferStatsSetPoint**](V1AssetReeferResponse_reeferStats_setPoint.md) | Set point temperature of the reefer | [optional] 

## Methods

### GetAmbientAirTemperature

`func (o *V1AssetsReeferReeferStats) GetAmbientAirTemperature() []V1AssetsReeferReeferStatsAmbientAirTemperature`

GetAmbientAirTemperature returns the AmbientAirTemperature field if non-nil, zero value otherwise.

### GetAmbientAirTemperatureOk

`func (o *V1AssetsReeferReeferStats) GetAmbientAirTemperatureOk() ([]V1AssetsReeferReeferStatsAmbientAirTemperature, bool)`

GetAmbientAirTemperatureOk returns a tuple with the AmbientAirTemperature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAmbientAirTemperature

`func (o *V1AssetsReeferReeferStats) HasAmbientAirTemperature() bool`

HasAmbientAirTemperature returns a boolean if a field has been set.

### SetAmbientAirTemperature

`func (o *V1AssetsReeferReeferStats) SetAmbientAirTemperature(v []V1AssetsReeferReeferStatsAmbientAirTemperature)`

SetAmbientAirTemperature gets a reference to the given []V1AssetsReeferReeferStatsAmbientAirTemperature and assigns it to the AmbientAirTemperature field.

### GetDischargeAirTemperature

`func (o *V1AssetsReeferReeferStats) GetDischargeAirTemperature() []V1AssetsReeferReeferStatsDischargeAirTemperature`

GetDischargeAirTemperature returns the DischargeAirTemperature field if non-nil, zero value otherwise.

### GetDischargeAirTemperatureOk

`func (o *V1AssetsReeferReeferStats) GetDischargeAirTemperatureOk() ([]V1AssetsReeferReeferStatsDischargeAirTemperature, bool)`

GetDischargeAirTemperatureOk returns a tuple with the DischargeAirTemperature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDischargeAirTemperature

`func (o *V1AssetsReeferReeferStats) HasDischargeAirTemperature() bool`

HasDischargeAirTemperature returns a boolean if a field has been set.

### SetDischargeAirTemperature

`func (o *V1AssetsReeferReeferStats) SetDischargeAirTemperature(v []V1AssetsReeferReeferStatsDischargeAirTemperature)`

SetDischargeAirTemperature gets a reference to the given []V1AssetsReeferReeferStatsDischargeAirTemperature and assigns it to the DischargeAirTemperature field.

### GetEngineHours

`func (o *V1AssetsReeferReeferStats) GetEngineHours() []V1AssetReeferResponseReeferStatsEngineHours`

GetEngineHours returns the EngineHours field if non-nil, zero value otherwise.

### GetEngineHoursOk

`func (o *V1AssetsReeferReeferStats) GetEngineHoursOk() ([]V1AssetReeferResponseReeferStatsEngineHours, bool)`

GetEngineHoursOk returns a tuple with the EngineHours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEngineHours

`func (o *V1AssetsReeferReeferStats) HasEngineHours() bool`

HasEngineHours returns a boolean if a field has been set.

### SetEngineHours

`func (o *V1AssetsReeferReeferStats) SetEngineHours(v []V1AssetReeferResponseReeferStatsEngineHours)`

SetEngineHours gets a reference to the given []V1AssetReeferResponseReeferStatsEngineHours and assigns it to the EngineHours field.

### GetFuelPercentage

`func (o *V1AssetsReeferReeferStats) GetFuelPercentage() []V1AssetReeferResponseReeferStatsFuelPercentage`

GetFuelPercentage returns the FuelPercentage field if non-nil, zero value otherwise.

### GetFuelPercentageOk

`func (o *V1AssetsReeferReeferStats) GetFuelPercentageOk() ([]V1AssetReeferResponseReeferStatsFuelPercentage, bool)`

GetFuelPercentageOk returns a tuple with the FuelPercentage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFuelPercentage

`func (o *V1AssetsReeferReeferStats) HasFuelPercentage() bool`

HasFuelPercentage returns a boolean if a field has been set.

### SetFuelPercentage

`func (o *V1AssetsReeferReeferStats) SetFuelPercentage(v []V1AssetReeferResponseReeferStatsFuelPercentage)`

SetFuelPercentage gets a reference to the given []V1AssetReeferResponseReeferStatsFuelPercentage and assigns it to the FuelPercentage field.

### GetPowerStatus

`func (o *V1AssetsReeferReeferStats) GetPowerStatus() []V1AssetsReeferReeferStatsPowerStatus`

GetPowerStatus returns the PowerStatus field if non-nil, zero value otherwise.

### GetPowerStatusOk

`func (o *V1AssetsReeferReeferStats) GetPowerStatusOk() ([]V1AssetsReeferReeferStatsPowerStatus, bool)`

GetPowerStatusOk returns a tuple with the PowerStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPowerStatus

`func (o *V1AssetsReeferReeferStats) HasPowerStatus() bool`

HasPowerStatus returns a boolean if a field has been set.

### SetPowerStatus

`func (o *V1AssetsReeferReeferStats) SetPowerStatus(v []V1AssetsReeferReeferStatsPowerStatus)`

SetPowerStatus gets a reference to the given []V1AssetsReeferReeferStatsPowerStatus and assigns it to the PowerStatus field.

### GetReeferAlarms

`func (o *V1AssetsReeferReeferStats) GetReeferAlarms() []V1AssetReeferResponseReeferStatsAlarms1`

GetReeferAlarms returns the ReeferAlarms field if non-nil, zero value otherwise.

### GetReeferAlarmsOk

`func (o *V1AssetsReeferReeferStats) GetReeferAlarmsOk() ([]V1AssetReeferResponseReeferStatsAlarms1, bool)`

GetReeferAlarmsOk returns a tuple with the ReeferAlarms field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasReeferAlarms

`func (o *V1AssetsReeferReeferStats) HasReeferAlarms() bool`

HasReeferAlarms returns a boolean if a field has been set.

### SetReeferAlarms

`func (o *V1AssetsReeferReeferStats) SetReeferAlarms(v []V1AssetReeferResponseReeferStatsAlarms1)`

SetReeferAlarms gets a reference to the given []V1AssetReeferResponseReeferStatsAlarms1 and assigns it to the ReeferAlarms field.

### GetReturnAirTemperature

`func (o *V1AssetsReeferReeferStats) GetReturnAirTemperature() []V1AssetReeferResponseReeferStatsReturnAirTemp`

GetReturnAirTemperature returns the ReturnAirTemperature field if non-nil, zero value otherwise.

### GetReturnAirTemperatureOk

`func (o *V1AssetsReeferReeferStats) GetReturnAirTemperatureOk() ([]V1AssetReeferResponseReeferStatsReturnAirTemp, bool)`

GetReturnAirTemperatureOk returns a tuple with the ReturnAirTemperature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasReturnAirTemperature

`func (o *V1AssetsReeferReeferStats) HasReturnAirTemperature() bool`

HasReturnAirTemperature returns a boolean if a field has been set.

### SetReturnAirTemperature

`func (o *V1AssetsReeferReeferStats) SetReturnAirTemperature(v []V1AssetReeferResponseReeferStatsReturnAirTemp)`

SetReturnAirTemperature gets a reference to the given []V1AssetReeferResponseReeferStatsReturnAirTemp and assigns it to the ReturnAirTemperature field.

### GetSetPoint

`func (o *V1AssetsReeferReeferStats) GetSetPoint() []V1AssetReeferResponseReeferStatsSetPoint`

GetSetPoint returns the SetPoint field if non-nil, zero value otherwise.

### GetSetPointOk

`func (o *V1AssetsReeferReeferStats) GetSetPointOk() ([]V1AssetReeferResponseReeferStatsSetPoint, bool)`

GetSetPointOk returns a tuple with the SetPoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSetPoint

`func (o *V1AssetsReeferReeferStats) HasSetPoint() bool`

HasSetPoint returns a boolean if a field has been set.

### SetSetPoint

`func (o *V1AssetsReeferReeferStats) SetSetPoint(v []V1AssetReeferResponseReeferStatsSetPoint)`

SetSetPoint gets a reference to the given []V1AssetReeferResponseReeferStatsSetPoint and assigns it to the SetPoint field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


