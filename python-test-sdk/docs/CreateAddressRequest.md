# CreateAddressRequest

A create Address request body.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_ids** | **list[str]** | An array of IDs of contacts to associate with this address. | [optional] 
**external_ids** | **dict(str, str)** | User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (&#x60;\&quot;\&quot;&#x60;). An external ID can be used as a path parameter to retrieve or update that resource. | [optional] 
**formatted_address** | **str** | The full street address for this address/geofence, as it might be recognized by Google Maps. | 
**geofence** | [**AddressGeofence**](AddressGeofence.md) |  | 
**latitude** | **float** | Latitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. | [optional] 
**longitude** | **float** | Longitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. | [optional] 
**name** | **str** | Name of the address. | 
**notes** | **str** | Notes about the address. | [optional] 
**tag_ids** | **list[str]** | An array of IDs of tags to associate with this address. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


