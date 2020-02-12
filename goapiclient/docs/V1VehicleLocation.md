# V1VehicleLocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DriverId** | Pointer to **int32** | The ID of the driver currently assigned to this vehicle. | [optional] 
**Heading** | Pointer to **float64** | Heading in degrees. | [optional] 
**Id** | Pointer to **int64** | ID of the vehicle. | 
**Latitude** | Pointer to **float64** | Latitude in decimal degrees. | [optional] 
**Location** | Pointer to **string** | Text representation of nearest identifiable location to (latitude, longitude) coordinates. | [optional] 
**Longitude** | Pointer to **float64** | Longitude in decimal degrees. | [optional] 
**Name** | Pointer to **string** | Name of the vehicle. | [optional] 
**OdometerMeters** | Pointer to **int64** | The number of meters reported by the odometer. | [optional] 
**OdometerType** | Pointer to **string** | The source of data for odometerMeters. Will be either GPS or OBD | [optional] 
**OnTrip** | Pointer to **bool** | Whether or not a trip is currently in progress for this vehicle. More information available via /fleet/trips endpoint. | [optional] 
**RouteIds** | Pointer to **[]int64** | A list of currently active route IDs that the vehicle is in. | [optional] 
**Speed** | Pointer to **float64** | Speed in miles per hour. | [optional] 
**Time** | Pointer to **int32** | The time the reported location was logged, reported as a UNIX timestamp in milliseconds. | [optional] 
**Vin** | Pointer to **string** | Vehicle Identification Number (VIN) of the vehicle. | [optional] 

## Methods

### GetDriverId

`func (o *V1VehicleLocation) GetDriverId() int32`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1VehicleLocation) GetDriverIdOk() (int32, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1VehicleLocation) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1VehicleLocation) SetDriverId(v int32)`

SetDriverId gets a reference to the given int32 and assigns it to the DriverId field.

### GetHeading

`func (o *V1VehicleLocation) GetHeading() float64`

GetHeading returns the Heading field if non-nil, zero value otherwise.

### GetHeadingOk

`func (o *V1VehicleLocation) GetHeadingOk() (float64, bool)`

GetHeadingOk returns a tuple with the Heading field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHeading

`func (o *V1VehicleLocation) HasHeading() bool`

HasHeading returns a boolean if a field has been set.

### SetHeading

`func (o *V1VehicleLocation) SetHeading(v float64)`

SetHeading gets a reference to the given float64 and assigns it to the Heading field.

### GetId

`func (o *V1VehicleLocation) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1VehicleLocation) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1VehicleLocation) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1VehicleLocation) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetLatitude

`func (o *V1VehicleLocation) GetLatitude() float64`

GetLatitude returns the Latitude field if non-nil, zero value otherwise.

### GetLatitudeOk

`func (o *V1VehicleLocation) GetLatitudeOk() (float64, bool)`

GetLatitudeOk returns a tuple with the Latitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLatitude

`func (o *V1VehicleLocation) HasLatitude() bool`

HasLatitude returns a boolean if a field has been set.

### SetLatitude

`func (o *V1VehicleLocation) SetLatitude(v float64)`

SetLatitude gets a reference to the given float64 and assigns it to the Latitude field.

### GetLocation

`func (o *V1VehicleLocation) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *V1VehicleLocation) GetLocationOk() (string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocation

`func (o *V1VehicleLocation) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### SetLocation

`func (o *V1VehicleLocation) SetLocation(v string)`

SetLocation gets a reference to the given string and assigns it to the Location field.

### GetLongitude

`func (o *V1VehicleLocation) GetLongitude() float64`

GetLongitude returns the Longitude field if non-nil, zero value otherwise.

### GetLongitudeOk

`func (o *V1VehicleLocation) GetLongitudeOk() (float64, bool)`

GetLongitudeOk returns a tuple with the Longitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLongitude

`func (o *V1VehicleLocation) HasLongitude() bool`

HasLongitude returns a boolean if a field has been set.

### SetLongitude

`func (o *V1VehicleLocation) SetLongitude(v float64)`

SetLongitude gets a reference to the given float64 and assigns it to the Longitude field.

### GetName

`func (o *V1VehicleLocation) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *V1VehicleLocation) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *V1VehicleLocation) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *V1VehicleLocation) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetOdometerMeters

`func (o *V1VehicleLocation) GetOdometerMeters() int64`

GetOdometerMeters returns the OdometerMeters field if non-nil, zero value otherwise.

### GetOdometerMetersOk

`func (o *V1VehicleLocation) GetOdometerMetersOk() (int64, bool)`

GetOdometerMetersOk returns a tuple with the OdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOdometerMeters

`func (o *V1VehicleLocation) HasOdometerMeters() bool`

HasOdometerMeters returns a boolean if a field has been set.

### SetOdometerMeters

`func (o *V1VehicleLocation) SetOdometerMeters(v int64)`

SetOdometerMeters gets a reference to the given int64 and assigns it to the OdometerMeters field.

### GetOdometerType

`func (o *V1VehicleLocation) GetOdometerType() string`

GetOdometerType returns the OdometerType field if non-nil, zero value otherwise.

### GetOdometerTypeOk

`func (o *V1VehicleLocation) GetOdometerTypeOk() (string, bool)`

GetOdometerTypeOk returns a tuple with the OdometerType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOdometerType

`func (o *V1VehicleLocation) HasOdometerType() bool`

HasOdometerType returns a boolean if a field has been set.

### SetOdometerType

`func (o *V1VehicleLocation) SetOdometerType(v string)`

SetOdometerType gets a reference to the given string and assigns it to the OdometerType field.

### GetOnTrip

`func (o *V1VehicleLocation) GetOnTrip() bool`

GetOnTrip returns the OnTrip field if non-nil, zero value otherwise.

### GetOnTripOk

`func (o *V1VehicleLocation) GetOnTripOk() (bool, bool)`

GetOnTripOk returns a tuple with the OnTrip field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOnTrip

`func (o *V1VehicleLocation) HasOnTrip() bool`

HasOnTrip returns a boolean if a field has been set.

### SetOnTrip

`func (o *V1VehicleLocation) SetOnTrip(v bool)`

SetOnTrip gets a reference to the given bool and assigns it to the OnTrip field.

### GetRouteIds

`func (o *V1VehicleLocation) GetRouteIds() []int64`

GetRouteIds returns the RouteIds field if non-nil, zero value otherwise.

### GetRouteIdsOk

`func (o *V1VehicleLocation) GetRouteIdsOk() ([]int64, bool)`

GetRouteIdsOk returns a tuple with the RouteIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRouteIds

`func (o *V1VehicleLocation) HasRouteIds() bool`

HasRouteIds returns a boolean if a field has been set.

### SetRouteIds

`func (o *V1VehicleLocation) SetRouteIds(v []int64)`

SetRouteIds gets a reference to the given []int64 and assigns it to the RouteIds field.

### GetSpeed

`func (o *V1VehicleLocation) GetSpeed() float64`

GetSpeed returns the Speed field if non-nil, zero value otherwise.

### GetSpeedOk

`func (o *V1VehicleLocation) GetSpeedOk() (float64, bool)`

GetSpeedOk returns a tuple with the Speed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSpeed

`func (o *V1VehicleLocation) HasSpeed() bool`

HasSpeed returns a boolean if a field has been set.

### SetSpeed

`func (o *V1VehicleLocation) SetSpeed(v float64)`

SetSpeed gets a reference to the given float64 and assigns it to the Speed field.

### GetTime

`func (o *V1VehicleLocation) GetTime() int32`

GetTime returns the Time field if non-nil, zero value otherwise.

### GetTimeOk

`func (o *V1VehicleLocation) GetTimeOk() (int32, bool)`

GetTimeOk returns a tuple with the Time field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTime

`func (o *V1VehicleLocation) HasTime() bool`

HasTime returns a boolean if a field has been set.

### SetTime

`func (o *V1VehicleLocation) SetTime(v int32)`

SetTime gets a reference to the given int32 and assigns it to the Time field.

### GetVin

`func (o *V1VehicleLocation) GetVin() string`

GetVin returns the Vin field if non-nil, zero value otherwise.

### GetVinOk

`func (o *V1VehicleLocation) GetVinOk() (string, bool)`

GetVinOk returns a tuple with the Vin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVin

`func (o *V1VehicleLocation) HasVin() bool`

HasVin returns a boolean if a field has been set.

### SetVin

`func (o *V1VehicleLocation) SetVin(v string)`

SetVin gets a reference to the given string and assigns it to the Vin field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


