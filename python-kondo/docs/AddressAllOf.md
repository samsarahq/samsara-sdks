# AddressAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**list[ContactTinyResponse]**](ContactTinyResponse.md) | An array of all contact mini-objects that are associated with the given address entry. | [optional] 
**external_ids** | **dict(str, str)** | User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (&#x60;\&quot;\&quot;&#x60;). An external ID can be used as a path parameter to retrieve or update that resource. | [optional] 
**id** | **str** | Unique Samsara ID for the address. | [optional] 
**latitude** | **float** | Latitude of the address. Either inferred from the formatted address or defined on address creation. | [optional] 
**longitude** | **float** | Longitude of the address. Either inferred from the formatted address or defined on address creation. | [optional] 
**tags** | [**list[TagTinyResponse]**](TagTinyResponse.md) | An array of all tag mini-objects that are associated with the given address entry. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


