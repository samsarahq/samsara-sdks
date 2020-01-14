# AddressPatch

Information about an address/geofence. Geofences are either a circle or a polygon.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_ids** | **list[str]** | An array of IDs of contacts to associate with this address. | [optional] 
**latitude** | **float** | Optional latitude field to override the geocoded latitude from the formatted address. | [optional] 
**longitude** | **float** | Optional longitude field to override the geocoded longitude from the formatted address. | [optional] 
**tag_ids** | **list[str]** | An array of IDs of tags to associate with this address. | [optional] 
**geofence** | [**AddressGeofenceRequest**](AddressGeofenceRequest.md) |  | [optional] 
**address_types** | **list[str]** | Reporting location type associated with the address (used for ELD reporting purposes). | [optional] 
**formatted_address** | **str** | The full street address for this address/geofence, as it might be recognized by Google Maps. | [optional] 
**name** | **str** | Name of the address. | [optional] 
**notes** | **str** | Notes about the address. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


