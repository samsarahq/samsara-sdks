# Address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AddressTypes** | Pointer to **[]string** | Reporting location type associated with the address (used for ELD reporting purposes). | [optional] 
**Contacts** | Pointer to [**[]ContactTinyResponse**](contactTinyResponse.md) | An array Contact mini-objects that are associated the Address. | [optional] 
**ExternalIds** | Pointer to **map[string]string** | User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (&#x60;\&quot;\&quot;&#x60;). An external ID can be used as a path parameter to retrieve or update that resource. | [optional] 
**FormattedAddress** | Pointer to **string** | The full street address for this address/geofence, as it might be recognized by Google Maps. | 
**Geofence** | Pointer to [**AddressGeofence**](AddressGeofence.md) |  | 
**Id** | Pointer to **string** | ID of the Address. | 
**Latitude** | Pointer to **float64** | Latitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. | [optional] 
**Longitude** | Pointer to **float64** | Longitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. | [optional] 
**Name** | Pointer to **string** | Name of the address. | 
**Notes** | Pointer to **string** | Notes about the address. | [optional] 
**Tags** | Pointer to [**[]TagTinyResponse**](tagTinyResponse.md) | An array of all tag mini-objects that are associated with the given address entry. | [optional] 

## Methods

### GetAddressTypes

`func (o *Address) GetAddressTypes() []string`

GetAddressTypes returns the AddressTypes field if non-nil, zero value otherwise.

### GetAddressTypesOk

`func (o *Address) GetAddressTypesOk() ([]string, bool)`

GetAddressTypesOk returns a tuple with the AddressTypes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAddressTypes

`func (o *Address) HasAddressTypes() bool`

HasAddressTypes returns a boolean if a field has been set.

### SetAddressTypes

`func (o *Address) SetAddressTypes(v []string)`

SetAddressTypes gets a reference to the given []string and assigns it to the AddressTypes field.

### GetContacts

`func (o *Address) GetContacts() []ContactTinyResponse`

GetContacts returns the Contacts field if non-nil, zero value otherwise.

### GetContactsOk

`func (o *Address) GetContactsOk() ([]ContactTinyResponse, bool)`

GetContactsOk returns a tuple with the Contacts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasContacts

`func (o *Address) HasContacts() bool`

HasContacts returns a boolean if a field has been set.

### SetContacts

`func (o *Address) SetContacts(v []ContactTinyResponse)`

SetContacts gets a reference to the given []ContactTinyResponse and assigns it to the Contacts field.

### GetExternalIds

`func (o *Address) GetExternalIds() map[string]string`

GetExternalIds returns the ExternalIds field if non-nil, zero value otherwise.

### GetExternalIdsOk

`func (o *Address) GetExternalIdsOk() (map[string]string, bool)`

GetExternalIdsOk returns a tuple with the ExternalIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasExternalIds

`func (o *Address) HasExternalIds() bool`

HasExternalIds returns a boolean if a field has been set.

### SetExternalIds

`func (o *Address) SetExternalIds(v map[string]string)`

SetExternalIds gets a reference to the given map[string]string and assigns it to the ExternalIds field.

### GetFormattedAddress

`func (o *Address) GetFormattedAddress() string`

GetFormattedAddress returns the FormattedAddress field if non-nil, zero value otherwise.

### GetFormattedAddressOk

`func (o *Address) GetFormattedAddressOk() (string, bool)`

GetFormattedAddressOk returns a tuple with the FormattedAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFormattedAddress

`func (o *Address) HasFormattedAddress() bool`

HasFormattedAddress returns a boolean if a field has been set.

### SetFormattedAddress

`func (o *Address) SetFormattedAddress(v string)`

SetFormattedAddress gets a reference to the given string and assigns it to the FormattedAddress field.

### GetGeofence

`func (o *Address) GetGeofence() AddressGeofence`

GetGeofence returns the Geofence field if non-nil, zero value otherwise.

### GetGeofenceOk

`func (o *Address) GetGeofenceOk() (AddressGeofence, bool)`

GetGeofenceOk returns a tuple with the Geofence field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGeofence

`func (o *Address) HasGeofence() bool`

HasGeofence returns a boolean if a field has been set.

### SetGeofence

`func (o *Address) SetGeofence(v AddressGeofence)`

SetGeofence gets a reference to the given AddressGeofence and assigns it to the Geofence field.

### GetId

`func (o *Address) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Address) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *Address) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *Address) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetLatitude

`func (o *Address) GetLatitude() float64`

GetLatitude returns the Latitude field if non-nil, zero value otherwise.

### GetLatitudeOk

`func (o *Address) GetLatitudeOk() (float64, bool)`

GetLatitudeOk returns a tuple with the Latitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLatitude

`func (o *Address) HasLatitude() bool`

HasLatitude returns a boolean if a field has been set.

### SetLatitude

`func (o *Address) SetLatitude(v float64)`

SetLatitude gets a reference to the given float64 and assigns it to the Latitude field.

### GetLongitude

`func (o *Address) GetLongitude() float64`

GetLongitude returns the Longitude field if non-nil, zero value otherwise.

### GetLongitudeOk

`func (o *Address) GetLongitudeOk() (float64, bool)`

GetLongitudeOk returns a tuple with the Longitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLongitude

`func (o *Address) HasLongitude() bool`

HasLongitude returns a boolean if a field has been set.

### SetLongitude

`func (o *Address) SetLongitude(v float64)`

SetLongitude gets a reference to the given float64 and assigns it to the Longitude field.

### GetName

`func (o *Address) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Address) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *Address) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *Address) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetNotes

`func (o *Address) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *Address) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *Address) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *Address) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetTags

`func (o *Address) GetTags() []TagTinyResponse`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *Address) GetTagsOk() ([]TagTinyResponse, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTags

`func (o *Address) HasTags() bool`

HasTags returns a boolean if a field has been set.

### SetTags

`func (o *Address) SetTags(v []TagTinyResponse)`

SetTags gets a reference to the given []TagTinyResponse and assigns it to the Tags field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


