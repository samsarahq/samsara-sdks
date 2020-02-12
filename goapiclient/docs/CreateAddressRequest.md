# CreateAddressRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AddressTypes** | Pointer to **[]string** | Reporting location type associated with the address (used for ELD reporting purposes). | [optional] 
**ContactIds** | Pointer to **[]string** | An array of Contact IDs associated with this Address. | [optional] 
**ExternalIds** | Pointer to **map[string]string** | User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (&#x60;\&quot;\&quot;&#x60;). An external ID can be used as a path parameter to retrieve or update that resource. | [optional] 
**FormattedAddress** | Pointer to **string** | The full street address for this address/geofence, as it might be recognized by Google Maps. | 
**Geofence** | Pointer to [**AddressGeofence**](AddressGeofence.md) |  | 
**Latitude** | Pointer to **float64** | Latitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. | [optional] 
**Longitude** | Pointer to **float64** | Longitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. | [optional] 
**Name** | Pointer to **string** | Name of the address. | 
**Notes** | Pointer to **string** | Notes about the address. | [optional] 
**TagIds** | Pointer to **[]string** | An array of IDs of tags to associate with this address. | [optional] 

## Methods

### GetAddressTypes

`func (o *CreateAddressRequest) GetAddressTypes() []string`

GetAddressTypes returns the AddressTypes field if non-nil, zero value otherwise.

### GetAddressTypesOk

`func (o *CreateAddressRequest) GetAddressTypesOk() ([]string, bool)`

GetAddressTypesOk returns a tuple with the AddressTypes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAddressTypes

`func (o *CreateAddressRequest) HasAddressTypes() bool`

HasAddressTypes returns a boolean if a field has been set.

### SetAddressTypes

`func (o *CreateAddressRequest) SetAddressTypes(v []string)`

SetAddressTypes gets a reference to the given []string and assigns it to the AddressTypes field.

### GetContactIds

`func (o *CreateAddressRequest) GetContactIds() []string`

GetContactIds returns the ContactIds field if non-nil, zero value otherwise.

### GetContactIdsOk

`func (o *CreateAddressRequest) GetContactIdsOk() ([]string, bool)`

GetContactIdsOk returns a tuple with the ContactIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasContactIds

`func (o *CreateAddressRequest) HasContactIds() bool`

HasContactIds returns a boolean if a field has been set.

### SetContactIds

`func (o *CreateAddressRequest) SetContactIds(v []string)`

SetContactIds gets a reference to the given []string and assigns it to the ContactIds field.

### GetExternalIds

`func (o *CreateAddressRequest) GetExternalIds() map[string]string`

GetExternalIds returns the ExternalIds field if non-nil, zero value otherwise.

### GetExternalIdsOk

`func (o *CreateAddressRequest) GetExternalIdsOk() (map[string]string, bool)`

GetExternalIdsOk returns a tuple with the ExternalIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasExternalIds

`func (o *CreateAddressRequest) HasExternalIds() bool`

HasExternalIds returns a boolean if a field has been set.

### SetExternalIds

`func (o *CreateAddressRequest) SetExternalIds(v map[string]string)`

SetExternalIds gets a reference to the given map[string]string and assigns it to the ExternalIds field.

### GetFormattedAddress

`func (o *CreateAddressRequest) GetFormattedAddress() string`

GetFormattedAddress returns the FormattedAddress field if non-nil, zero value otherwise.

### GetFormattedAddressOk

`func (o *CreateAddressRequest) GetFormattedAddressOk() (string, bool)`

GetFormattedAddressOk returns a tuple with the FormattedAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFormattedAddress

`func (o *CreateAddressRequest) HasFormattedAddress() bool`

HasFormattedAddress returns a boolean if a field has been set.

### SetFormattedAddress

`func (o *CreateAddressRequest) SetFormattedAddress(v string)`

SetFormattedAddress gets a reference to the given string and assigns it to the FormattedAddress field.

### GetGeofence

`func (o *CreateAddressRequest) GetGeofence() AddressGeofence`

GetGeofence returns the Geofence field if non-nil, zero value otherwise.

### GetGeofenceOk

`func (o *CreateAddressRequest) GetGeofenceOk() (AddressGeofence, bool)`

GetGeofenceOk returns a tuple with the Geofence field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGeofence

`func (o *CreateAddressRequest) HasGeofence() bool`

HasGeofence returns a boolean if a field has been set.

### SetGeofence

`func (o *CreateAddressRequest) SetGeofence(v AddressGeofence)`

SetGeofence gets a reference to the given AddressGeofence and assigns it to the Geofence field.

### GetLatitude

`func (o *CreateAddressRequest) GetLatitude() float64`

GetLatitude returns the Latitude field if non-nil, zero value otherwise.

### GetLatitudeOk

`func (o *CreateAddressRequest) GetLatitudeOk() (float64, bool)`

GetLatitudeOk returns a tuple with the Latitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLatitude

`func (o *CreateAddressRequest) HasLatitude() bool`

HasLatitude returns a boolean if a field has been set.

### SetLatitude

`func (o *CreateAddressRequest) SetLatitude(v float64)`

SetLatitude gets a reference to the given float64 and assigns it to the Latitude field.

### GetLongitude

`func (o *CreateAddressRequest) GetLongitude() float64`

GetLongitude returns the Longitude field if non-nil, zero value otherwise.

### GetLongitudeOk

`func (o *CreateAddressRequest) GetLongitudeOk() (float64, bool)`

GetLongitudeOk returns a tuple with the Longitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLongitude

`func (o *CreateAddressRequest) HasLongitude() bool`

HasLongitude returns a boolean if a field has been set.

### SetLongitude

`func (o *CreateAddressRequest) SetLongitude(v float64)`

SetLongitude gets a reference to the given float64 and assigns it to the Longitude field.

### GetName

`func (o *CreateAddressRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateAddressRequest) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *CreateAddressRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *CreateAddressRequest) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetNotes

`func (o *CreateAddressRequest) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *CreateAddressRequest) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *CreateAddressRequest) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *CreateAddressRequest) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetTagIds

`func (o *CreateAddressRequest) GetTagIds() []string`

GetTagIds returns the TagIds field if non-nil, zero value otherwise.

### GetTagIdsOk

`func (o *CreateAddressRequest) GetTagIdsOk() ([]string, bool)`

GetTagIdsOk returns a tuple with the TagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTagIds

`func (o *CreateAddressRequest) HasTagIds() bool`

HasTagIds returns a boolean if a field has been set.

### SetTagIds

`func (o *CreateAddressRequest) SetTagIds(v []string)`

SetTagIds gets a reference to the given []string and assigns it to the TagIds field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


