# RouteLocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FormattedAddress** | Pointer to **string** | The location address. | [optional] 
**Id** | Pointer to **string** | Unique address identifier. If this field is provided, the other fields in this object will be filled from the associated address. | [optional] 
**Latitude** | Pointer to **float64** | The latitude of the address in decimal degrees. | [optional] 
**Longitude** | Pointer to **float64** | The longitude of the address in decimal degrees. | [optional] 
**Name** | Pointer to **string** | The location address name. | [optional] 

## Methods

### GetFormattedAddress

`func (o *RouteLocation) GetFormattedAddress() string`

GetFormattedAddress returns the FormattedAddress field if non-nil, zero value otherwise.

### GetFormattedAddressOk

`func (o *RouteLocation) GetFormattedAddressOk() (string, bool)`

GetFormattedAddressOk returns a tuple with the FormattedAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFormattedAddress

`func (o *RouteLocation) HasFormattedAddress() bool`

HasFormattedAddress returns a boolean if a field has been set.

### SetFormattedAddress

`func (o *RouteLocation) SetFormattedAddress(v string)`

SetFormattedAddress gets a reference to the given string and assigns it to the FormattedAddress field.

### GetId

`func (o *RouteLocation) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *RouteLocation) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *RouteLocation) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *RouteLocation) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetLatitude

`func (o *RouteLocation) GetLatitude() float64`

GetLatitude returns the Latitude field if non-nil, zero value otherwise.

### GetLatitudeOk

`func (o *RouteLocation) GetLatitudeOk() (float64, bool)`

GetLatitudeOk returns a tuple with the Latitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLatitude

`func (o *RouteLocation) HasLatitude() bool`

HasLatitude returns a boolean if a field has been set.

### SetLatitude

`func (o *RouteLocation) SetLatitude(v float64)`

SetLatitude gets a reference to the given float64 and assigns it to the Latitude field.

### GetLongitude

`func (o *RouteLocation) GetLongitude() float64`

GetLongitude returns the Longitude field if non-nil, zero value otherwise.

### GetLongitudeOk

`func (o *RouteLocation) GetLongitudeOk() (float64, bool)`

GetLongitudeOk returns a tuple with the Longitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLongitude

`func (o *RouteLocation) HasLongitude() bool`

HasLongitude returns a boolean if a field has been set.

### SetLongitude

`func (o *RouteLocation) SetLongitude(v float64)`

SetLongitude gets a reference to the given float64 and assigns it to the Longitude field.

### GetName

`func (o *RouteLocation) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RouteLocation) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *RouteLocation) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *RouteLocation) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


