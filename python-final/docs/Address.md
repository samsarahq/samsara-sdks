# Address

Information about an address/geofence. Geofences are either a circle or a polygon.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geofence** | **object** | The geofence that defines this address and its bounds. This can either be a circle, or a polygon | [optional] 
**address_types** | **list[str]** | Reporting location type associated with the address (used for ELD reporting purposes). | [optional] 
**formatted_address** | **str** | The full street address for this address/geofence, as it might be recognized by Google Maps. | [optional] 
**name** | **str** | Name of the address. | [optional] 
**notes** | **str** | Notes about the address. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


