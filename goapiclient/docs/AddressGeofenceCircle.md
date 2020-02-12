# AddressGeofenceCircle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Latitude** | Pointer to **float64** | Latitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. | [optional] 
**Longitude** | Pointer to **float64** | Longitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. | [optional] 
**RadiusMeters** | Pointer to **int64** | The radius of the circular geofence in meters. | 

## Methods

### GetLatitude

`func (o *AddressGeofenceCircle) GetLatitude() float64`

GetLatitude returns the Latitude field if non-nil, zero value otherwise.

### GetLatitudeOk

`func (o *AddressGeofenceCircle) GetLatitudeOk() (float64, bool)`

GetLatitudeOk returns a tuple with the Latitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLatitude

`func (o *AddressGeofenceCircle) HasLatitude() bool`

HasLatitude returns a boolean if a field has been set.

### SetLatitude

`func (o *AddressGeofenceCircle) SetLatitude(v float64)`

SetLatitude gets a reference to the given float64 and assigns it to the Latitude field.

### GetLongitude

`func (o *AddressGeofenceCircle) GetLongitude() float64`

GetLongitude returns the Longitude field if non-nil, zero value otherwise.

### GetLongitudeOk

`func (o *AddressGeofenceCircle) GetLongitudeOk() (float64, bool)`

GetLongitudeOk returns a tuple with the Longitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLongitude

`func (o *AddressGeofenceCircle) HasLongitude() bool`

HasLongitude returns a boolean if a field has been set.

### SetLongitude

`func (o *AddressGeofenceCircle) SetLongitude(v float64)`

SetLongitude gets a reference to the given float64 and assigns it to the Longitude field.

### GetRadiusMeters

`func (o *AddressGeofenceCircle) GetRadiusMeters() int64`

GetRadiusMeters returns the RadiusMeters field if non-nil, zero value otherwise.

### GetRadiusMetersOk

`func (o *AddressGeofenceCircle) GetRadiusMetersOk() (int64, bool)`

GetRadiusMetersOk returns a tuple with the RadiusMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRadiusMeters

`func (o *AddressGeofenceCircle) HasRadiusMeters() bool`

HasRadiusMeters returns a boolean if a field has been set.

### SetRadiusMeters

`func (o *AddressGeofenceCircle) SetRadiusMeters(v int64)`

SetRadiusMeters gets a reference to the given int64 and assigns it to the RadiusMeters field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


