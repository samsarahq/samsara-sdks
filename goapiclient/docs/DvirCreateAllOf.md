# DvirCreateAllOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthorId** | Pointer to **string** | Samsara user ID of the mechanic creating the DVIR. | 
**LicensePlate** | Pointer to **string** | The license plate of this vehicle. | [optional] 
**Location** | Pointer to **string** | Optional string if your jurisdiction requires a location of the DVIR. | [optional] 
**MechanicNotes** | Pointer to **string** | Any notes from the mechanic. | [optional] 
**OdometerMeters** | Pointer to **int32** | The current odometer of the vehicle. | [optional] 
**ResolvedDefectIds** | Pointer to **[]string** | Array of ids for defects being resolved with this DVIR. | [optional] 
**SafetyStatus** | Pointer to **string** | Whether or not this vehicle or trailer is safe to drive. | 
**TrailerId** | Pointer to **string** | Id of trailer being inspected. Either vehicleId or trailerId must be provided. | [optional] 
**Type** | Pointer to **string** | Only type &#39;mechanic&#39; is currently accepted. | 
**VehicleId** | Pointer to **string** | Id of vehicle being inspected. Either vehicleId or trailerId must be provided. | [optional] 

## Methods

### GetAuthorId

`func (o *DvirCreateAllOf) GetAuthorId() string`

GetAuthorId returns the AuthorId field if non-nil, zero value otherwise.

### GetAuthorIdOk

`func (o *DvirCreateAllOf) GetAuthorIdOk() (string, bool)`

GetAuthorIdOk returns a tuple with the AuthorId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuthorId

`func (o *DvirCreateAllOf) HasAuthorId() bool`

HasAuthorId returns a boolean if a field has been set.

### SetAuthorId

`func (o *DvirCreateAllOf) SetAuthorId(v string)`

SetAuthorId gets a reference to the given string and assigns it to the AuthorId field.

### GetLicensePlate

`func (o *DvirCreateAllOf) GetLicensePlate() string`

GetLicensePlate returns the LicensePlate field if non-nil, zero value otherwise.

### GetLicensePlateOk

`func (o *DvirCreateAllOf) GetLicensePlateOk() (string, bool)`

GetLicensePlateOk returns a tuple with the LicensePlate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLicensePlate

`func (o *DvirCreateAllOf) HasLicensePlate() bool`

HasLicensePlate returns a boolean if a field has been set.

### SetLicensePlate

`func (o *DvirCreateAllOf) SetLicensePlate(v string)`

SetLicensePlate gets a reference to the given string and assigns it to the LicensePlate field.

### GetLocation

`func (o *DvirCreateAllOf) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *DvirCreateAllOf) GetLocationOk() (string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocation

`func (o *DvirCreateAllOf) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### SetLocation

`func (o *DvirCreateAllOf) SetLocation(v string)`

SetLocation gets a reference to the given string and assigns it to the Location field.

### GetMechanicNotes

`func (o *DvirCreateAllOf) GetMechanicNotes() string`

GetMechanicNotes returns the MechanicNotes field if non-nil, zero value otherwise.

### GetMechanicNotesOk

`func (o *DvirCreateAllOf) GetMechanicNotesOk() (string, bool)`

GetMechanicNotesOk returns a tuple with the MechanicNotes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMechanicNotes

`func (o *DvirCreateAllOf) HasMechanicNotes() bool`

HasMechanicNotes returns a boolean if a field has been set.

### SetMechanicNotes

`func (o *DvirCreateAllOf) SetMechanicNotes(v string)`

SetMechanicNotes gets a reference to the given string and assigns it to the MechanicNotes field.

### GetOdometerMeters

`func (o *DvirCreateAllOf) GetOdometerMeters() int32`

GetOdometerMeters returns the OdometerMeters field if non-nil, zero value otherwise.

### GetOdometerMetersOk

`func (o *DvirCreateAllOf) GetOdometerMetersOk() (int32, bool)`

GetOdometerMetersOk returns a tuple with the OdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOdometerMeters

`func (o *DvirCreateAllOf) HasOdometerMeters() bool`

HasOdometerMeters returns a boolean if a field has been set.

### SetOdometerMeters

`func (o *DvirCreateAllOf) SetOdometerMeters(v int32)`

SetOdometerMeters gets a reference to the given int32 and assigns it to the OdometerMeters field.

### GetResolvedDefectIds

`func (o *DvirCreateAllOf) GetResolvedDefectIds() []string`

GetResolvedDefectIds returns the ResolvedDefectIds field if non-nil, zero value otherwise.

### GetResolvedDefectIdsOk

`func (o *DvirCreateAllOf) GetResolvedDefectIdsOk() ([]string, bool)`

GetResolvedDefectIdsOk returns a tuple with the ResolvedDefectIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasResolvedDefectIds

`func (o *DvirCreateAllOf) HasResolvedDefectIds() bool`

HasResolvedDefectIds returns a boolean if a field has been set.

### SetResolvedDefectIds

`func (o *DvirCreateAllOf) SetResolvedDefectIds(v []string)`

SetResolvedDefectIds gets a reference to the given []string and assigns it to the ResolvedDefectIds field.

### GetSafetyStatus

`func (o *DvirCreateAllOf) GetSafetyStatus() string`

GetSafetyStatus returns the SafetyStatus field if non-nil, zero value otherwise.

### GetSafetyStatusOk

`func (o *DvirCreateAllOf) GetSafetyStatusOk() (string, bool)`

GetSafetyStatusOk returns a tuple with the SafetyStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSafetyStatus

`func (o *DvirCreateAllOf) HasSafetyStatus() bool`

HasSafetyStatus returns a boolean if a field has been set.

### SetSafetyStatus

`func (o *DvirCreateAllOf) SetSafetyStatus(v string)`

SetSafetyStatus gets a reference to the given string and assigns it to the SafetyStatus field.

### GetTrailerId

`func (o *DvirCreateAllOf) GetTrailerId() string`

GetTrailerId returns the TrailerId field if non-nil, zero value otherwise.

### GetTrailerIdOk

`func (o *DvirCreateAllOf) GetTrailerIdOk() (string, bool)`

GetTrailerIdOk returns a tuple with the TrailerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerId

`func (o *DvirCreateAllOf) HasTrailerId() bool`

HasTrailerId returns a boolean if a field has been set.

### SetTrailerId

`func (o *DvirCreateAllOf) SetTrailerId(v string)`

SetTrailerId gets a reference to the given string and assigns it to the TrailerId field.

### GetType

`func (o *DvirCreateAllOf) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *DvirCreateAllOf) GetTypeOk() (string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasType

`func (o *DvirCreateAllOf) HasType() bool`

HasType returns a boolean if a field has been set.

### SetType

`func (o *DvirCreateAllOf) SetType(v string)`

SetType gets a reference to the given string and assigns it to the Type field.

### GetVehicleId

`func (o *DvirCreateAllOf) GetVehicleId() string`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *DvirCreateAllOf) GetVehicleIdOk() (string, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *DvirCreateAllOf) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *DvirCreateAllOf) SetVehicleId(v string)`

SetVehicleId gets a reference to the given string and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


