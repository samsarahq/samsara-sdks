# V1AssetCurrentLocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Latitude** | Pointer to **float32** | The latitude of the location in degrees. | [optional] 
**Location** | Pointer to **string** | The best effort (street,city,state) for the latitude and longitude. | [optional] 
**Longitude** | Pointer to **float32** | The longitude of the location in degrees. | [optional] 
**SpeedMilesPerHour** | Pointer to **float32** | The speed calculated from GPS that the asset was traveling at in miles per hour. | [optional] 
**TimeMs** | Pointer to **float32** | Time in Unix milliseconds since epoch when the asset was at the location. | [optional] 

## Methods

### GetLatitude

`func (o *V1AssetCurrentLocation) GetLatitude() float32`

GetLatitude returns the Latitude field if non-nil, zero value otherwise.

### GetLatitudeOk

`func (o *V1AssetCurrentLocation) GetLatitudeOk() (float32, bool)`

GetLatitudeOk returns a tuple with the Latitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLatitude

`func (o *V1AssetCurrentLocation) HasLatitude() bool`

HasLatitude returns a boolean if a field has been set.

### SetLatitude

`func (o *V1AssetCurrentLocation) SetLatitude(v float32)`

SetLatitude gets a reference to the given float32 and assigns it to the Latitude field.

### GetLocation

`func (o *V1AssetCurrentLocation) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *V1AssetCurrentLocation) GetLocationOk() (string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocation

`func (o *V1AssetCurrentLocation) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### SetLocation

`func (o *V1AssetCurrentLocation) SetLocation(v string)`

SetLocation gets a reference to the given string and assigns it to the Location field.

### GetLongitude

`func (o *V1AssetCurrentLocation) GetLongitude() float32`

GetLongitude returns the Longitude field if non-nil, zero value otherwise.

### GetLongitudeOk

`func (o *V1AssetCurrentLocation) GetLongitudeOk() (float32, bool)`

GetLongitudeOk returns a tuple with the Longitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLongitude

`func (o *V1AssetCurrentLocation) HasLongitude() bool`

HasLongitude returns a boolean if a field has been set.

### SetLongitude

`func (o *V1AssetCurrentLocation) SetLongitude(v float32)`

SetLongitude gets a reference to the given float32 and assigns it to the Longitude field.

### GetSpeedMilesPerHour

`func (o *V1AssetCurrentLocation) GetSpeedMilesPerHour() float32`

GetSpeedMilesPerHour returns the SpeedMilesPerHour field if non-nil, zero value otherwise.

### GetSpeedMilesPerHourOk

`func (o *V1AssetCurrentLocation) GetSpeedMilesPerHourOk() (float32, bool)`

GetSpeedMilesPerHourOk returns a tuple with the SpeedMilesPerHour field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSpeedMilesPerHour

`func (o *V1AssetCurrentLocation) HasSpeedMilesPerHour() bool`

HasSpeedMilesPerHour returns a boolean if a field has been set.

### SetSpeedMilesPerHour

`func (o *V1AssetCurrentLocation) SetSpeedMilesPerHour(v float32)`

SetSpeedMilesPerHour gets a reference to the given float32 and assigns it to the SpeedMilesPerHour field.

### GetTimeMs

`func (o *V1AssetCurrentLocation) GetTimeMs() float32`

GetTimeMs returns the TimeMs field if non-nil, zero value otherwise.

### GetTimeMsOk

`func (o *V1AssetCurrentLocation) GetTimeMsOk() (float32, bool)`

GetTimeMsOk returns a tuple with the TimeMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTimeMs

`func (o *V1AssetCurrentLocation) HasTimeMs() bool`

HasTimeMs returns a boolean if a field has been set.

### SetTimeMs

`func (o *V1AssetCurrentLocation) SetTimeMs(v float32)`

SetTimeMs gets a reference to the given float32 and assigns it to the TimeMs field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


