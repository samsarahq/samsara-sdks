# VehicleResponse

The vehicle object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aux_input_type1** | **str** | The type of aux input that this vehicle has connected to port 1. Setting to \&quot;none\&quot; will remove the configured aux input. | [optional] 
**aux_input_type2** | **str** | The type of aux input that this vehicle has connected to port 2. Setting to \&quot;none\&quot; will remove the configured aux input. | [optional] 
**external_ids** | **dict(str, str)** | User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (&#x60;\&quot;\&quot;&#x60;). An external ID can be used as a path parameter to retrieve or update that resource. | [optional] 
**harsh_acceleration_setting_type** | **str** | Enumeration of the harsh acceleration setting types. This setting influences the acceleration sensitivity from which a harsh event is triggered. If set to &#x60;off&#x60;, then no acceleration based harsh events are triggered for the vehicle. | [optional] 
**id** | **str** | Unique Samsara ID for the vehicle. | 
**license_plate** | **str** | The license plate of this vehicle. | [optional] 
**make** | **str** | Vehicle&#39;s manufacturing make. | [optional] 
**model** | **str** | Vehicle&#39;s manufacturing model. | [optional] 
**name** | **str** | Name of the vehicle. | [optional] 
**notes** | **str** | Notes about a vehicle. Samsara supports a maximum of 255 chars. | [optional] 
**static_assigned_driver** | [**VehicleListResponseStaticAssignedDriver**](VehicleListResponseStaticAssignedDriver.md) |  | [optional] 
**tags** | [**list[AddressAllOfTags]**](AddressAllOfTags.md) | An array of all tag mini-objects that are associated with the given vehicle. | [optional] 
**vin** | **str** | A vehicle identification number. | [optional] 
**year** | **str** | Vehicle&#39;s manufacturing year. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


