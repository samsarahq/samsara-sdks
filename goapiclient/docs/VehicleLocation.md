# VehicleLocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Heading** | Pointer to **float64** | Heading of the vehicle in degrees. | 
**Latitude** | Pointer to **float64** | GPS latitude represented in degrees | 
**Longitude** | Pointer to **float64** | GPS longitude represented in degrees | 
**ReverseGeo** | Pointer to [**VehicleLocationReverseGeo**](VehicleLocationReverseGeo.md) |  | [optional] 
**Speed** | Pointer to **float64** | GPS speed of the vehicle in miles per hour. | 
**Time** | Pointer to **string** | UTC timestamp in RFC 3339 milliseconds format. | 

## Methods

### GetHeading

`func (o *VehicleLocation) GetHeading() float64`

GetHeading returns the Heading field if non-nil, zero value otherwise.

### GetHeadingOk

`func (o *VehicleLocation) GetHeadingOk() (float64, bool)`

GetHeadingOk returns a tuple with the Heading field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHeading

`func (o *VehicleLocation) HasHeading() bool`

HasHeading returns a boolean if a field has been set.

### SetHeading

`func (o *VehicleLocation) SetHeading(v float64)`

SetHeading gets a reference to the given float64 and assigns it to the Heading field.

### GetLatitude

`func (o *VehicleLocation) GetLatitude() float64`

GetLatitude returns the Latitude field if non-nil, zero value otherwise.

### GetLatitudeOk

`func (o *VehicleLocation) GetLatitudeOk() (float64, bool)`

GetLatitudeOk returns a tuple with the Latitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLatitude

`func (o *VehicleLocation) HasLatitude() bool`

HasLatitude returns a boolean if a field has been set.

### SetLatitude

`func (o *VehicleLocation) SetLatitude(v float64)`

SetLatitude gets a reference to the given float64 and assigns it to the Latitude field.

### GetLongitude

`func (o *VehicleLocation) GetLongitude() float64`

GetLongitude returns the Longitude field if non-nil, zero value otherwise.

### GetLongitudeOk

`func (o *VehicleLocation) GetLongitudeOk() (float64, bool)`

GetLongitudeOk returns a tuple with the Longitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLongitude

`func (o *VehicleLocation) HasLongitude() bool`

HasLongitude returns a boolean if a field has been set.

### SetLongitude

`func (o *VehicleLocation) SetLongitude(v float64)`

SetLongitude gets a reference to the given float64 and assigns it to the Longitude field.

### GetReverseGeo

`func (o *VehicleLocation) GetReverseGeo() VehicleLocationReverseGeo`

GetReverseGeo returns the ReverseGeo field if non-nil, zero value otherwise.

### GetReverseGeoOk

`func (o *VehicleLocation) GetReverseGeoOk() (VehicleLocationReverseGeo, bool)`

GetReverseGeoOk returns a tuple with the ReverseGeo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasReverseGeo

`func (o *VehicleLocation) HasReverseGeo() bool`

HasReverseGeo returns a boolean if a field has been set.

### SetReverseGeo

`func (o *VehicleLocation) SetReverseGeo(v VehicleLocationReverseGeo)`

SetReverseGeo gets a reference to the given VehicleLocationReverseGeo and assigns it to the ReverseGeo field.

### GetSpeed

`func (o *VehicleLocation) GetSpeed() float64`

GetSpeed returns the Speed field if non-nil, zero value otherwise.

### GetSpeedOk

`func (o *VehicleLocation) GetSpeedOk() (float64, bool)`

GetSpeedOk returns a tuple with the Speed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSpeed

`func (o *VehicleLocation) HasSpeed() bool`

HasSpeed returns a boolean if a field has been set.

### SetSpeed

`func (o *VehicleLocation) SetSpeed(v float64)`

SetSpeed gets a reference to the given float64 and assigns it to the Speed field.

### GetTime

`func (o *VehicleLocation) GetTime() string`

GetTime returns the Time field if non-nil, zero value otherwise.

### GetTimeOk

`func (o *VehicleLocation) GetTimeOk() (string, bool)`

GetTimeOk returns a tuple with the Time field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTime

`func (o *VehicleLocation) HasTime() bool`

HasTime returns a boolean if a field has been set.

### SetTime

`func (o *VehicleLocation) SetTime(v string)`

SetTime gets a reference to the given string and assigns it to the Time field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


