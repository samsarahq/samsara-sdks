# DriverUpdate

Driver that should be updated.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_vehicle_id** | **str** | ID of vehicle that driver is currently assigned to. | [optional] 
**password** | **str** | Password that the driver can use to login to the Samsara driver app. | [optional] 
**static_assigned_vehicle_id** | **str** | ID of vehicle assigned to the driver for static vehicle assignments. (uncommon). | [optional] 
**tag_ids** | **list[str]** | IDs of tags the driver is associated with. | [optional] 
**vehicle_group_tag_id** | **str** | Tag ID which determines which vehicles a driver will see when selecting vehicles. | [optional] 
**carrier_settings** | [**DriverBaseCarrierSettings**](DriverBaseCarrierSettings.md) |  | [optional] 
**eld_adverse_weather_exemption_enabled** | **bool** | Flag indicating this driver may use Adverse Weather exemptions in ELD logs. | [optional] 
**eld_big_day_exemption_enabled** | **bool** | Flag indicating this driver may use Big Day exemption in ELD logs. | [optional] 
**eld_day_start_hour** | **int** | &#x60;0&#x60; indicating midnight-to-midnight ELD driving hours, &#x60;12&#x60; to indicate noon-to-noon driving hours. | [optional] 
**eld_exempt** | **bool** | Flag indicating this driver is exempt from the Electronic Logging Mandate. | [optional] 
**eld_exempt_reason** | **str** | Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt). | [optional] 
**eld_pc_enabled** | **bool** | Flag indicating this driver may select the Personal Conveyance duty status in ELD logs. | [optional] [default to False]
**eld_ym_enabled** | **bool** | Flag indicating this driver may select the Yard Move duty status in ELD logs. | [optional] [default to False]
**external_ids** | **dict(str, str)** | User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (&#x60;\&quot;\&quot;&#x60;). An external ID can be used as a path parameter to retrieve or update that resource. | [optional] 
**is_deactivated** | **bool** | A boolean that indicates whether or not this driver is deactivated. | [optional] 
**license_number** | **str** | Driver&#39;s state issued license number. The combination of this number and &#x60;licenseState&#x60; must be unique. | [optional] 
**license_state** | **str** | Abbreviation of state that issued driver&#39;s license. | [optional] 
**locale** | **str** | Locale override (uncommon). | [optional] 
**name** | **str** | Driver&#39;s name. | [optional] 
**notes** | **str** | Notes about the driver. | [optional] 
**phone** | **str** | Driver&#39;s phone number. | [optional] 
**tachograph_card_number** | **str** | Driver&#39;s assigned tachograph card number (Europe specific) | [optional] 
**timezone** | **str** | Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs. | [optional] 
**username** | **str** | Driver&#39;s login username into the driver app. The username may not contain spaces or the &#39;@&#39; symbol. The username must be unique. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


