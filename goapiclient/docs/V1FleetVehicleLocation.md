# V1FleetVehicleLocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Latitude** | Pointer to **float64** | The latitude of the location in degrees. | [optional] 
**Location** | Pointer to **string** | The best effort (street,city,state) for the latitude and longitude. | [optional] 
**Longitude** | Pointer to **float64** | The longitude of the location in degrees. | [optional] 
**SpeedMilesPerHour** | Pointer to **float64** | The speed calculated from GPS that the asset was traveling at in miles per hour. | [optional] 
**TimeMs** | Pointer to **float32** | Time in Unix milliseconds since epoch when the asset was at the location. | [optional] 

## Methods

### GetLatitude

`func (o *V1FleetVehicleLocation) GetLatitude() float64`

GetLatitude returns the Latitude field if non-nil, zero value otherwise.

### GetLatitudeOk

`func (o *V1FleetVehicleLocation) GetLatitudeOk() (float64, bool)`

GetLatitudeOk returns a tuple with the Latitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLatitude

`func (o *V1FleetVehicleLocation) HasLatitude() bool`

HasLatitude returns a boolean if a field has been set.

### SetLatitude

`func (o *V1FleetVehicleLocation) SetLatitude(v float64)`

SetLatitude gets a reference to the given float64 and assigns it to the Latitude field.

### GetLocation

`func (o *V1FleetVehicleLocation) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *V1FleetVehicleLocation) GetLocationOk() (string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocation

`func (o *V1FleetVehicleLocation) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### SetLocation

`func (o *V1FleetVehicleLocation) SetLocation(v string)`

SetLocation gets a reference to the given string and assigns it to the Location field.

### GetLongitude

`func (o *V1FleetVehicleLocation) GetLongitude() float64`

GetLongitude returns the Longitude field if non-nil, zero value otherwise.

### GetLongitudeOk

`func (o *V1FleetVehicleLocation) GetLongitudeOk() (float64, bool)`

GetLongitudeOk returns a tuple with the Longitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLongitude

`func (o *V1FleetVehicleLocation) HasLongitude() bool`

HasLongitude returns a boolean if a field has been set.

### SetLongitude

`func (o *V1FleetVehicleLocation) SetLongitude(v float64)`

SetLongitude gets a reference to the given float64 and assigns it to the Longitude field.

### GetSpeedMilesPerHour

`func (o *V1FleetVehicleLocation) GetSpeedMilesPerHour() float64`

GetSpeedMilesPerHour returns the SpeedMilesPerHour field if non-nil, zero value otherwise.

### GetSpeedMilesPerHourOk

`func (o *V1FleetVehicleLocation) GetSpeedMilesPerHourOk() (float64, bool)`

GetSpeedMilesPerHourOk returns a tuple with the SpeedMilesPerHour field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSpeedMilesPerHour

`func (o *V1FleetVehicleLocation) HasSpeedMilesPerHour() bool`

HasSpeedMilesPerHour returns a boolean if a field has been set.

### SetSpeedMilesPerHour

`func (o *V1FleetVehicleLocation) SetSpeedMilesPerHour(v float64)`

SetSpeedMilesPerHour gets a reference to the given float64 and assigns it to the SpeedMilesPerHour field.

### GetTimeMs

`func (o *V1FleetVehicleLocation) GetTimeMs() float32`

GetTimeMs returns the TimeMs field if non-nil, zero value otherwise.

### GetTimeMsOk

`func (o *V1FleetVehicleLocation) GetTimeMsOk() (float32, bool)`

GetTimeMsOk returns a tuple with the TimeMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTimeMs

`func (o *V1FleetVehicleLocation) HasTimeMs() bool`

HasTimeMs returns a boolean if a field has been set.

### SetTimeMs

`func (o *V1FleetVehicleLocation) SetTimeMs(v float32)`

SetTimeMs gets a reference to the given float32 and assigns it to the TimeMs field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


