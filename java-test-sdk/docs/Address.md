

# Address

An Address object.
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressTypes** | [**List&lt;AddressTypesEnum&gt;**](#List&lt;AddressTypesEnum&gt;) | Reporting location type associated with the address (used for ELD reporting purposes). |  [optional]
**contacts** | [**List&lt;ContactTinyResponse&gt;**](ContactTinyResponse.md) | An array of all contact mini-objects that are associated with the given address entry. |  [optional]
**externalIds** | **Map&lt;String, String&gt;** | User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (&#x60;\&quot;\&quot;&#x60;). An external ID can be used as a path parameter to retrieve or update that resource. |  [optional]
**formattedAddress** | **String** | The full street address for this address/geofence, as it might be recognized by Google Maps. | 
**geofence** | [**AddressGeofence**](AddressGeofence.md) |  | 
**id** | **String** | ID of the Address. | 
**latitude** | **Double** | Latitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. |  [optional]
**longitude** | **Double** | Longitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. |  [optional]
**name** | **String** | Name of the address. | 
**notes** | **String** | Notes about the address. |  [optional]
**tags** | [**List&lt;TagTinyResponse&gt;**](TagTinyResponse.md) | An array of all tag mini-objects that are associated with the given address entry. |  [optional]



## Enum: List&lt;AddressTypesEnum&gt;

Name | Value
---- | -----
YARD | &quot;yard&quot;
SHORTHAUL | &quot;shortHaul&quot;



