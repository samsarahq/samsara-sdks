# Address

An address in the organization's Address Book.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_types** | **list[str]** | Types associated with this address for ELD reporting purposes. | [optional] 
**contacts** | [**list[ContactTinyObject]**](ContactTinyObject.md) | List of contacts associated with this address. | [optional] 
**external_ids** | **dict(str, str)** | User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and **must be alphanumeric** (&#x60;_&#x60;&#39;s, &#x60;-&#x60;&#39;, etc. are not allowed). Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (&#x60;\&quot;\&quot;&#x60;). An external ID can be used as a path parameter to retrieve or update that resource. | [optional] 
**formatted_address** | **str** | Street address of this address. | 
**geofence** | [**AddressGeofence**](AddressGeofence.md) |  | 
**id** | **str** | Unique identifier for the address. | 
**latitude** | **float** | Latitude of the address. Either geocoded from the &#x60;formattedAddress&#x60; or defined on address creation. | 
**longitude** | **float** | Longitude of the address. Either geocoded from the &#x60;formattedAddress&#x60; or defined on address creation. | 
**name** | **str** | Name of the address. | 
**notes** | **str** | Notes about the address. | [optional] 
**tags** | [**list[TagTinyObject]**](TagTinyObject.md) | List of tags this address is associated with. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


