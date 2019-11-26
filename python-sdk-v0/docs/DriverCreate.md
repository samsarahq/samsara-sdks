# DriverCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_settings** | **object** | Carrier for a given driver. If the driver&#x27;s carrier differs from the general organization&#x27;s carrier settings, the override value is used. Updating this value only updates the override setting for this driver. | [optional] 
**current_vehicle_id** | **str** | ID of vehicle that driver is currently assigned to. | [optional] 
**eld_adverse_weather_exemption_enabled** | **bool** | Flag indicating this driver may use Adverse Weather exemptions in ELD logs. | [optional] [default to False]
**eld_big_day_exemption_enabled** | **bool** | Flag indicating this driver may use Big Day exemption in ELD logs. | [optional] [default to False]
**eld_day_start_hour** | **int** | &#x60;0&#x60; indicating midnight-to-midnight ELD driving hours, &#x60;12&#x60; to indicate noon-to-noon driving hours. | [optional] 
**eld_exempt** | **bool** | Flag indicating this driver is exempt from the Electronic Logging Mandate. | [optional] [default to False]
**eld_exempt_reason** | **str** | Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt). | [optional] 
**eld_pc_enabled** | **bool** | Flag indicating this driver may select the Personal Conveyance duty status in ELD logs. | [optional] [default to False]
**eld_ym_enabled** | **bool** | Flag indicating this driver may select the Yard Move duty status in ELD logs. | [optional] [default to False]
**external_ids** | [**ExternalIds**](ExternalIds.md) |  | [optional] 
**license_number** | **str** | Driver&#x27;s state issued license number. The combination of this number and &#x60;licenseState&#x60; must be unique. | [optional] 
**license_state** | **str** | Abbreviation of state that issued driver&#x27;s license. | [optional] 
**locale** | **str** | Locale override (uncommon). These are specified by ISO 3166-2 country codes for supported locales. | [optional] 
**name** | **str** | Driver&#x27;s name. | 
**notes** | **str** | Notes about the driver. | [optional] 
**password** | **str** | Password that the driver can use to login to the Samsara driver app. | 
**phone** | **str** | Phone number of the driver. | [optional] 
**static_assigned_vehicle_id** | **str** | ID of vehicle that the driver is permanently assigned to. (uncommon). | [optional] 
**tag_ids** | **list[str]** | IDs of tags the driver is associated with. | [optional] 
**timezone** | **str** | Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs. | [optional] 
**username** | **str** | Driver&#x27;s login username into the driver app. The username may not contain spaces or the &#x27;@&#x27; symbol. The username must be unique. | 
**vehicle_group_tag_id** | **str** | Tag ID which determines which vehicles a driver will see when selecting vehicles. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

