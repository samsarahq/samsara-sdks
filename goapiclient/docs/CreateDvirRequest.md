# CreateDvirRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthorId** | Pointer to **string** | Samsara user ID of the mechanic creating the DVIR. | 
**LicensePlate** | Pointer to **string** | The license plate of this vehicle. | [optional] 
**Location** | Pointer to **string** | Optional string if your jurisdiction requires a location of the DVIR. | [optional] 
**MechanicNotes** | Pointer to **string** | The mechanics notes on the DVIR. | [optional] 
**OdometerMeters** | Pointer to **int32** | The odometer reading in meters. | [optional] 
**ResolvedDefectIds** | Pointer to **[]string** | Array of ids for defects being resolved with this DVIR. | [optional] 
**SafetyStatus** | Pointer to **string** | Whether or not this vehicle or trailer is safe to drive. | 
**TrailerId** | Pointer to **string** | Id of trailer being inspected. Either vehicleId or trailerId must be provided. | [optional] 
**Type** | Pointer to **string** | Only type &#39;mechanic&#39; is currently accepted. | 
**VehicleId** | Pointer to **string** | Id of vehicle being inspected. Either vehicleId or trailerId must be provided. | [optional] 

## Methods

### GetAuthorId

`func (o *CreateDvirRequest) GetAuthorId() string`

GetAuthorId returns the AuthorId field if non-nil, zero value otherwise.

### GetAuthorIdOk

`func (o *CreateDvirRequest) GetAuthorIdOk() (string, bool)`

GetAuthorIdOk returns a tuple with the AuthorId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuthorId

`func (o *CreateDvirRequest) HasAuthorId() bool`

HasAuthorId returns a boolean if a field has been set.

### SetAuthorId

`func (o *CreateDvirRequest) SetAuthorId(v string)`

SetAuthorId gets a reference to the given string and assigns it to the AuthorId field.

### GetLicensePlate

`func (o *CreateDvirRequest) GetLicensePlate() string`

GetLicensePlate returns the LicensePlate field if non-nil, zero value otherwise.

### GetLicensePlateOk

`func (o *CreateDvirRequest) GetLicensePlateOk() (string, bool)`

GetLicensePlateOk returns a tuple with the LicensePlate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLicensePlate

`func (o *CreateDvirRequest) HasLicensePlate() bool`

HasLicensePlate returns a boolean if a field has been set.

### SetLicensePlate

`func (o *CreateDvirRequest) SetLicensePlate(v string)`

SetLicensePlate gets a reference to the given string and assigns it to the LicensePlate field.

### GetLocation

`func (o *CreateDvirRequest) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *CreateDvirRequest) GetLocationOk() (string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocation

`func (o *CreateDvirRequest) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### SetLocation

`func (o *CreateDvirRequest) SetLocation(v string)`

SetLocation gets a reference to the given string and assigns it to the Location field.

### GetMechanicNotes

`func (o *CreateDvirRequest) GetMechanicNotes() string`

GetMechanicNotes returns the MechanicNotes field if non-nil, zero value otherwise.

### GetMechanicNotesOk

`func (o *CreateDvirRequest) GetMechanicNotesOk() (string, bool)`

GetMechanicNotesOk returns a tuple with the MechanicNotes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMechanicNotes

`func (o *CreateDvirRequest) HasMechanicNotes() bool`

HasMechanicNotes returns a boolean if a field has been set.

### SetMechanicNotes

`func (o *CreateDvirRequest) SetMechanicNotes(v string)`

SetMechanicNotes gets a reference to the given string and assigns it to the MechanicNotes field.

### GetOdometerMeters

`func (o *CreateDvirRequest) GetOdometerMeters() int32`

GetOdometerMeters returns the OdometerMeters field if non-nil, zero value otherwise.

### GetOdometerMetersOk

`func (o *CreateDvirRequest) GetOdometerMetersOk() (int32, bool)`

GetOdometerMetersOk returns a tuple with the OdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOdometerMeters

`func (o *CreateDvirRequest) HasOdometerMeters() bool`

HasOdometerMeters returns a boolean if a field has been set.

### SetOdometerMeters

`func (o *CreateDvirRequest) SetOdometerMeters(v int32)`

SetOdometerMeters gets a reference to the given int32 and assigns it to the OdometerMeters field.

### GetResolvedDefectIds

`func (o *CreateDvirRequest) GetResolvedDefectIds() []string`

GetResolvedDefectIds returns the ResolvedDefectIds field if non-nil, zero value otherwise.

### GetResolvedDefectIdsOk

`func (o *CreateDvirRequest) GetResolvedDefectIdsOk() ([]string, bool)`

GetResolvedDefectIdsOk returns a tuple with the ResolvedDefectIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasResolvedDefectIds

`func (o *CreateDvirRequest) HasResolvedDefectIds() bool`

HasResolvedDefectIds returns a boolean if a field has been set.

### SetResolvedDefectIds

`func (o *CreateDvirRequest) SetResolvedDefectIds(v []string)`

SetResolvedDefectIds gets a reference to the given []string and assigns it to the ResolvedDefectIds field.

### GetSafetyStatus

`func (o *CreateDvirRequest) GetSafetyStatus() string`

GetSafetyStatus returns the SafetyStatus field if non-nil, zero value otherwise.

### GetSafetyStatusOk

`func (o *CreateDvirRequest) GetSafetyStatusOk() (string, bool)`

GetSafetyStatusOk returns a tuple with the SafetyStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSafetyStatus

`func (o *CreateDvirRequest) HasSafetyStatus() bool`

HasSafetyStatus returns a boolean if a field has been set.

### SetSafetyStatus

`func (o *CreateDvirRequest) SetSafetyStatus(v string)`

SetSafetyStatus gets a reference to the given string and assigns it to the SafetyStatus field.

### GetTrailerId

`func (o *CreateDvirRequest) GetTrailerId() string`

GetTrailerId returns the TrailerId field if non-nil, zero value otherwise.

### GetTrailerIdOk

`func (o *CreateDvirRequest) GetTrailerIdOk() (string, bool)`

GetTrailerIdOk returns a tuple with the TrailerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerId

`func (o *CreateDvirRequest) HasTrailerId() bool`

HasTrailerId returns a boolean if a field has been set.

### SetTrailerId

`func (o *CreateDvirRequest) SetTrailerId(v string)`

SetTrailerId gets a reference to the given string and assigns it to the TrailerId field.

### GetType

`func (o *CreateDvirRequest) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *CreateDvirRequest) GetTypeOk() (string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasType

`func (o *CreateDvirRequest) HasType() bool`

HasType returns a boolean if a field has been set.

### SetType

`func (o *CreateDvirRequest) SetType(v string)`

SetType gets a reference to the given string and assigns it to the Type field.

### GetVehicleId

`func (o *CreateDvirRequest) GetVehicleId() string`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *CreateDvirRequest) GetVehicleIdOk() (string, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *CreateDvirRequest) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *CreateDvirRequest) SetVehicleId(v string)`

SetVehicleId gets a reference to the given string and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


