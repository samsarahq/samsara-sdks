# Address

An Address object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_types** | **list[str]** | Reporting location type associated with the address (used for ELD reporting purposes). | [optional] 
**contacts** | [**list[ContactTinyResponse]**](ContactTinyResponse.md) | An array of all contact mini-objects that are associated with the given address entry. | [optional] 
**external_ids** | **dict(str, str)** | User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (&#x60;\&quot;\&quot;&#x60;). An external ID can be used as a path parameter to retrieve or update that resource. | [optional] 
**formatted_address** | **str** | The full street address for this address/geofence, as it might be recognized by Google Maps. | 
**geofence** | [**AddressGeofence**](AddressGeofence.md) |  | 
**id** | **str** | ID of the Address. | 
**latitude** | **float** | Latitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. | [optional] 
**longitude** | **float** | Longitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. | [optional] 
**name** | **str** | Name of the address. | 
**notes** | **str** | Notes about the address. | [optional] 
**tags** | [**list[TagTinyResponse]**](TagTinyResponse.md) | An array of all tag mini-objects that are associated with the given address entry. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


