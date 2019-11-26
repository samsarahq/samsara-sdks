# VehicleResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aux_input_type1** | **str** | The type of aux input that this vehicle has connected to port 1. Setting to \&quot;none\&quot; will remove the configured aux input. | [optional] 
**aux_input_type2** | **str** | The type of aux input that this vehicle has connected to port 2. Setting to \&quot;none\&quot; will remove the configured aux input. | [optional] 
**external_ids** | [**ExternalIds**](ExternalIds.md) |  | [optional] 
**harsh_acceleration_setting_type** | **str** | Enumeration of the harsh acceleration setting types. This setting influences the acceleration sensitivity from which a harsh event is triggered. If set to &#x60;off&#x60;, then no acceleration based harsh events are triggered for the vehicle. | [optional] 
**id** | **str** | Unique Samsara ID for the vehicle. | 
**license_plate** | **str** | The license plate of this vehicle. | [optional] 
**make** | **str** | Vehicle&#x27;s manufacturing make. | [optional] 
**model** | **str** | Vehicle&#x27;s manufacturing model. | [optional] 
**name** | **str** | Name of the vehicle. | [optional] 
**notes** | **str** | Notes about a vehicle. Samsara supports a maximum of 255 chars. | [optional] 
**static_assigned_driver** | [**DriverTinyResponse**](DriverTinyResponse.md) |  | [optional] 
**tags** | [**list[TagTinyResponse]**](TagTinyResponse.md) | An array of all tag mini-objects that are associated with the given vehicle. | [optional] 
**vin** | **str** | A vehicle identification number. | [optional] 
**year** | **str** | Vehicle&#x27;s manufacturing year. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

