# Address

Information about an address/geofence. Geofences are either a circle or a polygon.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**list[ContactTinyResponse]**](ContactTinyResponse.md) | An array of all contact mini-objects that are associated with the given address entry. | [optional] 
**id** | **str** | Unique Samsara ID for the address. | 
**latitude** | **float** | Latitude of the address. Either inferred from the formatted address or defined on address creation. | [optional] 
**longitude** | **float** | Longitude of the address. Either inferred from the formatted address or defined on address creation. | [optional] 
**tags** | [**list[TagTinyResponse]**](TagTinyResponse.md) | An array of all tag mini-objects that are associated with the given address entry. | [optional] 
**geofence** | [**AddressGeofenceResponse**](AddressGeofenceResponse.md) |  | [optional] 
**address_types** | **list[str]** | Reporting location type associated with the address (used for ELD reporting purposes). | [optional] 
**formatted_address** | **str** | The full street address for this address/geofence, as it might be recognized by Google Maps. | [optional] 
**name** | **str** | Name of the address. | [optional] 
**notes** | **str** | Notes about the address. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


