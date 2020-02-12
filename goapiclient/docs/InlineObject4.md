# InlineObject4

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InspectionType** | Pointer to **string** | Only type &#39;mechanic&#39; is currently accepted. | 
**MechanicNotes** | Pointer to **string** | Any notes from the mechanic. | [optional] 
**OdometerMiles** | Pointer to **int32** | The current odometer of the vehicle. | [optional] 
**PreviousDefectsCorrected** | Pointer to **bool** | Whether any previous defects were corrected. If this vehicle or trailer was previously marked unsafe, and this DVIR marks it as safe, either previousDefectsCorrected or previousDefectsIgnored must be true. | [optional] 
**PreviousDefectsIgnored** | Pointer to **bool** | Whether any previous defects were ignored. If this vehicle or trailer was previously marked unsafe, and this DVIR marks it as safe, either previousDefectsCorrected or previousDefectsIgnored must be true. | [optional] 
**ResolvedDefectIds** | Pointer to **[]int64** | List of defect IDs to resolve.  The defects must be associated with the provided vehicle or trailer. | [optional] 
**Safe** | Pointer to **string** | Whether or not this vehicle or trailer is safe to drive. | 
**TrailerId** | Pointer to **int32** | Id of trailer being inspected. Either vehicleId or trailerId must be provided. | [optional] 
**UserEmail** | Pointer to **string** | The Samsara login email for the person creating the DVIR. The email must correspond to a Samsara user&#39;s email. | 
**VehicleId** | Pointer to **int32** | Id of vehicle being inspected. Either vehicleId or trailerId must be provided. | [optional] 

## Methods

### GetInspectionType

`func (o *InlineObject4) GetInspectionType() string`

GetInspectionType returns the InspectionType field if non-nil, zero value otherwise.

### GetInspectionTypeOk

`func (o *InlineObject4) GetInspectionTypeOk() (string, bool)`

GetInspectionTypeOk returns a tuple with the InspectionType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasInspectionType

`func (o *InlineObject4) HasInspectionType() bool`

HasInspectionType returns a boolean if a field has been set.

### SetInspectionType

`func (o *InlineObject4) SetInspectionType(v string)`

SetInspectionType gets a reference to the given string and assigns it to the InspectionType field.

### GetMechanicNotes

`func (o *InlineObject4) GetMechanicNotes() string`

GetMechanicNotes returns the MechanicNotes field if non-nil, zero value otherwise.

### GetMechanicNotesOk

`func (o *InlineObject4) GetMechanicNotesOk() (string, bool)`

GetMechanicNotesOk returns a tuple with the MechanicNotes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMechanicNotes

`func (o *InlineObject4) HasMechanicNotes() bool`

HasMechanicNotes returns a boolean if a field has been set.

### SetMechanicNotes

`func (o *InlineObject4) SetMechanicNotes(v string)`

SetMechanicNotes gets a reference to the given string and assigns it to the MechanicNotes field.

### GetOdometerMiles

`func (o *InlineObject4) GetOdometerMiles() int32`

GetOdometerMiles returns the OdometerMiles field if non-nil, zero value otherwise.

### GetOdometerMilesOk

`func (o *InlineObject4) GetOdometerMilesOk() (int32, bool)`

GetOdometerMilesOk returns a tuple with the OdometerMiles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOdometerMiles

`func (o *InlineObject4) HasOdometerMiles() bool`

HasOdometerMiles returns a boolean if a field has been set.

### SetOdometerMiles

`func (o *InlineObject4) SetOdometerMiles(v int32)`

SetOdometerMiles gets a reference to the given int32 and assigns it to the OdometerMiles field.

### GetPreviousDefectsCorrected

`func (o *InlineObject4) GetPreviousDefectsCorrected() bool`

GetPreviousDefectsCorrected returns the PreviousDefectsCorrected field if non-nil, zero value otherwise.

### GetPreviousDefectsCorrectedOk

`func (o *InlineObject4) GetPreviousDefectsCorrectedOk() (bool, bool)`

GetPreviousDefectsCorrectedOk returns a tuple with the PreviousDefectsCorrected field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPreviousDefectsCorrected

`func (o *InlineObject4) HasPreviousDefectsCorrected() bool`

HasPreviousDefectsCorrected returns a boolean if a field has been set.

### SetPreviousDefectsCorrected

`func (o *InlineObject4) SetPreviousDefectsCorrected(v bool)`

SetPreviousDefectsCorrected gets a reference to the given bool and assigns it to the PreviousDefectsCorrected field.

### GetPreviousDefectsIgnored

`func (o *InlineObject4) GetPreviousDefectsIgnored() bool`

GetPreviousDefectsIgnored returns the PreviousDefectsIgnored field if non-nil, zero value otherwise.

### GetPreviousDefectsIgnoredOk

`func (o *InlineObject4) GetPreviousDefectsIgnoredOk() (bool, bool)`

GetPreviousDefectsIgnoredOk returns a tuple with the PreviousDefectsIgnored field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPreviousDefectsIgnored

`func (o *InlineObject4) HasPreviousDefectsIgnored() bool`

HasPreviousDefectsIgnored returns a boolean if a field has been set.

### SetPreviousDefectsIgnored

`func (o *InlineObject4) SetPreviousDefectsIgnored(v bool)`

SetPreviousDefectsIgnored gets a reference to the given bool and assigns it to the PreviousDefectsIgnored field.

### GetResolvedDefectIds

`func (o *InlineObject4) GetResolvedDefectIds() []int64`

GetResolvedDefectIds returns the ResolvedDefectIds field if non-nil, zero value otherwise.

### GetResolvedDefectIdsOk

`func (o *InlineObject4) GetResolvedDefectIdsOk() ([]int64, bool)`

GetResolvedDefectIdsOk returns a tuple with the ResolvedDefectIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasResolvedDefectIds

`func (o *InlineObject4) HasResolvedDefectIds() bool`

HasResolvedDefectIds returns a boolean if a field has been set.

### SetResolvedDefectIds

`func (o *InlineObject4) SetResolvedDefectIds(v []int64)`

SetResolvedDefectIds gets a reference to the given []int64 and assigns it to the ResolvedDefectIds field.

### GetSafe

`func (o *InlineObject4) GetSafe() string`

GetSafe returns the Safe field if non-nil, zero value otherwise.

### GetSafeOk

`func (o *InlineObject4) GetSafeOk() (string, bool)`

GetSafeOk returns a tuple with the Safe field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSafe

`func (o *InlineObject4) HasSafe() bool`

HasSafe returns a boolean if a field has been set.

### SetSafe

`func (o *InlineObject4) SetSafe(v string)`

SetSafe gets a reference to the given string and assigns it to the Safe field.

### GetTrailerId

`func (o *InlineObject4) GetTrailerId() int32`

GetTrailerId returns the TrailerId field if non-nil, zero value otherwise.

### GetTrailerIdOk

`func (o *InlineObject4) GetTrailerIdOk() (int32, bool)`

GetTrailerIdOk returns a tuple with the TrailerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerId

`func (o *InlineObject4) HasTrailerId() bool`

HasTrailerId returns a boolean if a field has been set.

### SetTrailerId

`func (o *InlineObject4) SetTrailerId(v int32)`

SetTrailerId gets a reference to the given int32 and assigns it to the TrailerId field.

### GetUserEmail

`func (o *InlineObject4) GetUserEmail() string`

GetUserEmail returns the UserEmail field if non-nil, zero value otherwise.

### GetUserEmailOk

`func (o *InlineObject4) GetUserEmailOk() (string, bool)`

GetUserEmailOk returns a tuple with the UserEmail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasUserEmail

`func (o *InlineObject4) HasUserEmail() bool`

HasUserEmail returns a boolean if a field has been set.

### SetUserEmail

`func (o *InlineObject4) SetUserEmail(v string)`

SetUserEmail gets a reference to the given string and assigns it to the UserEmail field.

### GetVehicleId

`func (o *InlineObject4) GetVehicleId() int32`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *InlineObject4) GetVehicleIdOk() (int32, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *InlineObject4) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *InlineObject4) SetVehicleId(v int32)`

SetVehicleId gets a reference to the given int32 and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


