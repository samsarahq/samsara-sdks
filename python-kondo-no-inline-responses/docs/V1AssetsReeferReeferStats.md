# V1AssetsReeferReeferStats

Contains all the state changes of the reefer for the included stat types. Each state change is recorded independently, so the number of records in each array may differ depending on when that stat changed state. Stat types with a continuous value (such as temperature) will be recorded at different rates depending on the reefer, but generally readings have a frequency on the order of seconds.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ambient_air_temperature** | [**list[V1AssetsReeferReeferStatsAmbientAirTemperature]**](V1AssetsReeferReeferStatsAmbientAirTemperature.md) | Ambient temperature of the reefer. This is the temperature of the air around the Samsara Asset Gateway. | [optional] 
**discharge_air_temperature** | [**list[V1AssetsReeferReeferStatsDischargeAirTemperature]**](V1AssetsReeferReeferStatsDischargeAirTemperature.md) | Discharge air temperature of the reefer. This is the temperature of the air as it leaves the cooling unit. | [optional] 
**engine_hours** | [**list[V1AssetReeferResponseReeferStatsEngineHours]**](V1AssetReeferResponseReeferStatsEngineHours.md) | Engine hours of the reefer | [optional] 
**fuel_percentage** | [**list[V1AssetReeferResponseReeferStatsFuelPercentage]**](V1AssetReeferResponseReeferStatsFuelPercentage.md) | Fuel percentage of the reefer | [optional] 
**power_status** | [**list[V1AssetsReeferReeferStatsPowerStatus]**](V1AssetsReeferReeferStatsPowerStatus.md) | Power status of the reefer | [optional] 
**reefer_alarms** | [**list[V1AssetReeferResponseReeferStatsAlarms1]**](V1AssetReeferResponseReeferStatsAlarms1.md) | Reefer alarms | [optional] 
**return_air_temperature** | [**list[V1AssetReeferResponseReeferStatsReturnAirTemp]**](V1AssetReeferResponseReeferStatsReturnAirTemp.md) | Return air temperature of the reefer. This is the temperature read by the reefer module (Carrier, Thermo King) that shows the temperature of the air as it enters the system. | [optional] 
**set_point** | [**list[V1AssetReeferResponseReeferStatsSetPoint]**](V1AssetReeferResponseReeferStatsSetPoint.md) | Set point temperature of the reefer | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


