# V1DvirBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthorSignature** | Pointer to [**V1DvirBaseAuthorSignature**](V1DvirBase_authorSignature.md) |  | [optional] 
**DefectsCorrected** | Pointer to **bool** | Signifies if the defects on the vehicle corrected after the DVIR is done. | [optional] 
**DefectsNeedNotBeCorrected** | Pointer to **bool** | Signifies if the defects on this vehicle can be ignored. | [optional] 
**Id** | Pointer to **int64** | The id of this DVIR record. | [optional] 
**InspectionType** | Pointer to **string** | Inspection type of the DVIR. | [optional] 
**MechanicNotes** | Pointer to **string** | The mechanics notes on the DVIR. | [optional] 
**MechanicOrAgentSignature** | Pointer to [**V1DvirBaseMechanicOrAgentSignature**](V1DvirBase_mechanicOrAgentSignature.md) |  | [optional] 
**NextDriverSignature** | Pointer to [**V1DvirBaseNextDriverSignature**](V1DvirBase_nextDriverSignature.md) |  | [optional] 
**OdometerMiles** | Pointer to **int64** | The odometer reading in miles for the vehicle when the DVIR was done. | [optional] 
**StartedAtMs** | Pointer to **int64** | Timestamp when driver began filling out this DVIR, in UNIX milliseconds. | [optional] 
**TimeMs** | Pointer to **int64** | Timestamp of when this DVIR was signed &amp; completed, in UNIX milliseconds. | [optional] 
**TrailerDefects** | Pointer to [**[]V1DvirDefectBase**](V1DvirDefectBase.md) | Defects registered for the trailer which was part of the DVIR. | [optional] 
**TrailerId** | Pointer to **int32** | The id of the trailer which was part of the DVIR. | [optional] 
**TrailerName** | Pointer to **string** | The name of the trailer which was part of the DVIR. | [optional] 
**Vehicle** | Pointer to [**V1DvirBaseVehicle**](V1DvirBase_vehicle.md) |  | [optional] 
**VehicleCondition** | Pointer to **string** | The condition of vechile on which DVIR was done. | [optional] 
**VehicleDefects** | Pointer to [**[]V1DvirDefectBase**](V1DvirDefectBase.md) | Defects registered for the vehicle which was part of the DVIR. | [optional] 

## Methods

### GetAuthorSignature

`func (o *V1DvirBase) GetAuthorSignature() V1DvirBaseAuthorSignature`

GetAuthorSignature returns the AuthorSignature field if non-nil, zero value otherwise.

### GetAuthorSignatureOk

`func (o *V1DvirBase) GetAuthorSignatureOk() (V1DvirBaseAuthorSignature, bool)`

GetAuthorSignatureOk returns a tuple with the AuthorSignature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuthorSignature

`func (o *V1DvirBase) HasAuthorSignature() bool`

HasAuthorSignature returns a boolean if a field has been set.

### SetAuthorSignature

`func (o *V1DvirBase) SetAuthorSignature(v V1DvirBaseAuthorSignature)`

SetAuthorSignature gets a reference to the given V1DvirBaseAuthorSignature and assigns it to the AuthorSignature field.

### GetDefectsCorrected

`func (o *V1DvirBase) GetDefectsCorrected() bool`

GetDefectsCorrected returns the DefectsCorrected field if non-nil, zero value otherwise.

### GetDefectsCorrectedOk

`func (o *V1DvirBase) GetDefectsCorrectedOk() (bool, bool)`

GetDefectsCorrectedOk returns a tuple with the DefectsCorrected field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDefectsCorrected

`func (o *V1DvirBase) HasDefectsCorrected() bool`

HasDefectsCorrected returns a boolean if a field has been set.

### SetDefectsCorrected

`func (o *V1DvirBase) SetDefectsCorrected(v bool)`

SetDefectsCorrected gets a reference to the given bool and assigns it to the DefectsCorrected field.

### GetDefectsNeedNotBeCorrected

`func (o *V1DvirBase) GetDefectsNeedNotBeCorrected() bool`

GetDefectsNeedNotBeCorrected returns the DefectsNeedNotBeCorrected field if non-nil, zero value otherwise.

### GetDefectsNeedNotBeCorrectedOk

`func (o *V1DvirBase) GetDefectsNeedNotBeCorrectedOk() (bool, bool)`

GetDefectsNeedNotBeCorrectedOk returns a tuple with the DefectsNeedNotBeCorrected field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDefectsNeedNotBeCorrected

`func (o *V1DvirBase) HasDefectsNeedNotBeCorrected() bool`

HasDefectsNeedNotBeCorrected returns a boolean if a field has been set.

### SetDefectsNeedNotBeCorrected

`func (o *V1DvirBase) SetDefectsNeedNotBeCorrected(v bool)`

SetDefectsNeedNotBeCorrected gets a reference to the given bool and assigns it to the DefectsNeedNotBeCorrected field.

### GetId

`func (o *V1DvirBase) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1DvirBase) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1DvirBase) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1DvirBase) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetInspectionType

`func (o *V1DvirBase) GetInspectionType() string`

GetInspectionType returns the InspectionType field if non-nil, zero value otherwise.

### GetInspectionTypeOk

`func (o *V1DvirBase) GetInspectionTypeOk() (string, bool)`

GetInspectionTypeOk returns a tuple with the InspectionType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasInspectionType

`func (o *V1DvirBase) HasInspectionType() bool`

HasInspectionType returns a boolean if a field has been set.

### SetInspectionType

`func (o *V1DvirBase) SetInspectionType(v string)`

SetInspectionType gets a reference to the given string and assigns it to the InspectionType field.

### GetMechanicNotes

`func (o *V1DvirBase) GetMechanicNotes() string`

GetMechanicNotes returns the MechanicNotes field if non-nil, zero value otherwise.

### GetMechanicNotesOk

`func (o *V1DvirBase) GetMechanicNotesOk() (string, bool)`

GetMechanicNotesOk returns a tuple with the MechanicNotes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMechanicNotes

`func (o *V1DvirBase) HasMechanicNotes() bool`

HasMechanicNotes returns a boolean if a field has been set.

### SetMechanicNotes

`func (o *V1DvirBase) SetMechanicNotes(v string)`

SetMechanicNotes gets a reference to the given string and assigns it to the MechanicNotes field.

### GetMechanicOrAgentSignature

`func (o *V1DvirBase) GetMechanicOrAgentSignature() V1DvirBaseMechanicOrAgentSignature`

GetMechanicOrAgentSignature returns the MechanicOrAgentSignature field if non-nil, zero value otherwise.

### GetMechanicOrAgentSignatureOk

`func (o *V1DvirBase) GetMechanicOrAgentSignatureOk() (V1DvirBaseMechanicOrAgentSignature, bool)`

GetMechanicOrAgentSignatureOk returns a tuple with the MechanicOrAgentSignature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMechanicOrAgentSignature

`func (o *V1DvirBase) HasMechanicOrAgentSignature() bool`

HasMechanicOrAgentSignature returns a boolean if a field has been set.

### SetMechanicOrAgentSignature

`func (o *V1DvirBase) SetMechanicOrAgentSignature(v V1DvirBaseMechanicOrAgentSignature)`

SetMechanicOrAgentSignature gets a reference to the given V1DvirBaseMechanicOrAgentSignature and assigns it to the MechanicOrAgentSignature field.

### GetNextDriverSignature

`func (o *V1DvirBase) GetNextDriverSignature() V1DvirBaseNextDriverSignature`

GetNextDriverSignature returns the NextDriverSignature field if non-nil, zero value otherwise.

### GetNextDriverSignatureOk

`func (o *V1DvirBase) GetNextDriverSignatureOk() (V1DvirBaseNextDriverSignature, bool)`

GetNextDriverSignatureOk returns a tuple with the NextDriverSignature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNextDriverSignature

`func (o *V1DvirBase) HasNextDriverSignature() bool`

HasNextDriverSignature returns a boolean if a field has been set.

### SetNextDriverSignature

`func (o *V1DvirBase) SetNextDriverSignature(v V1DvirBaseNextDriverSignature)`

SetNextDriverSignature gets a reference to the given V1DvirBaseNextDriverSignature and assigns it to the NextDriverSignature field.

### GetOdometerMiles

`func (o *V1DvirBase) GetOdometerMiles() int64`

GetOdometerMiles returns the OdometerMiles field if non-nil, zero value otherwise.

### GetOdometerMilesOk

`func (o *V1DvirBase) GetOdometerMilesOk() (int64, bool)`

GetOdometerMilesOk returns a tuple with the OdometerMiles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOdometerMiles

`func (o *V1DvirBase) HasOdometerMiles() bool`

HasOdometerMiles returns a boolean if a field has been set.

### SetOdometerMiles

`func (o *V1DvirBase) SetOdometerMiles(v int64)`

SetOdometerMiles gets a reference to the given int64 and assigns it to the OdometerMiles field.

### GetStartedAtMs

`func (o *V1DvirBase) GetStartedAtMs() int64`

GetStartedAtMs returns the StartedAtMs field if non-nil, zero value otherwise.

### GetStartedAtMsOk

`func (o *V1DvirBase) GetStartedAtMsOk() (int64, bool)`

GetStartedAtMsOk returns a tuple with the StartedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartedAtMs

`func (o *V1DvirBase) HasStartedAtMs() bool`

HasStartedAtMs returns a boolean if a field has been set.

### SetStartedAtMs

`func (o *V1DvirBase) SetStartedAtMs(v int64)`

SetStartedAtMs gets a reference to the given int64 and assigns it to the StartedAtMs field.

### GetTimeMs

`func (o *V1DvirBase) GetTimeMs() int64`

GetTimeMs returns the TimeMs field if non-nil, zero value otherwise.

### GetTimeMsOk

`func (o *V1DvirBase) GetTimeMsOk() (int64, bool)`

GetTimeMsOk returns a tuple with the TimeMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTimeMs

`func (o *V1DvirBase) HasTimeMs() bool`

HasTimeMs returns a boolean if a field has been set.

### SetTimeMs

`func (o *V1DvirBase) SetTimeMs(v int64)`

SetTimeMs gets a reference to the given int64 and assigns it to the TimeMs field.

### GetTrailerDefects

`func (o *V1DvirBase) GetTrailerDefects() []V1DvirDefectBase`

GetTrailerDefects returns the TrailerDefects field if non-nil, zero value otherwise.

### GetTrailerDefectsOk

`func (o *V1DvirBase) GetTrailerDefectsOk() ([]V1DvirDefectBase, bool)`

GetTrailerDefectsOk returns a tuple with the TrailerDefects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerDefects

`func (o *V1DvirBase) HasTrailerDefects() bool`

HasTrailerDefects returns a boolean if a field has been set.

### SetTrailerDefects

`func (o *V1DvirBase) SetTrailerDefects(v []V1DvirDefectBase)`

SetTrailerDefects gets a reference to the given []V1DvirDefectBase and assigns it to the TrailerDefects field.

### GetTrailerId

`func (o *V1DvirBase) GetTrailerId() int32`

GetTrailerId returns the TrailerId field if non-nil, zero value otherwise.

### GetTrailerIdOk

`func (o *V1DvirBase) GetTrailerIdOk() (int32, bool)`

GetTrailerIdOk returns a tuple with the TrailerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerId

`func (o *V1DvirBase) HasTrailerId() bool`

HasTrailerId returns a boolean if a field has been set.

### SetTrailerId

`func (o *V1DvirBase) SetTrailerId(v int32)`

SetTrailerId gets a reference to the given int32 and assigns it to the TrailerId field.

### GetTrailerName

`func (o *V1DvirBase) GetTrailerName() string`

GetTrailerName returns the TrailerName field if non-nil, zero value otherwise.

### GetTrailerNameOk

`func (o *V1DvirBase) GetTrailerNameOk() (string, bool)`

GetTrailerNameOk returns a tuple with the TrailerName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerName

`func (o *V1DvirBase) HasTrailerName() bool`

HasTrailerName returns a boolean if a field has been set.

### SetTrailerName

`func (o *V1DvirBase) SetTrailerName(v string)`

SetTrailerName gets a reference to the given string and assigns it to the TrailerName field.

### GetVehicle

`func (o *V1DvirBase) GetVehicle() V1DvirBaseVehicle`

GetVehicle returns the Vehicle field if non-nil, zero value otherwise.

### GetVehicleOk

`func (o *V1DvirBase) GetVehicleOk() (V1DvirBaseVehicle, bool)`

GetVehicleOk returns a tuple with the Vehicle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicle

`func (o *V1DvirBase) HasVehicle() bool`

HasVehicle returns a boolean if a field has been set.

### SetVehicle

`func (o *V1DvirBase) SetVehicle(v V1DvirBaseVehicle)`

SetVehicle gets a reference to the given V1DvirBaseVehicle and assigns it to the Vehicle field.

### GetVehicleCondition

`func (o *V1DvirBase) GetVehicleCondition() string`

GetVehicleCondition returns the VehicleCondition field if non-nil, zero value otherwise.

### GetVehicleConditionOk

`func (o *V1DvirBase) GetVehicleConditionOk() (string, bool)`

GetVehicleConditionOk returns a tuple with the VehicleCondition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleCondition

`func (o *V1DvirBase) HasVehicleCondition() bool`

HasVehicleCondition returns a boolean if a field has been set.

### SetVehicleCondition

`func (o *V1DvirBase) SetVehicleCondition(v string)`

SetVehicleCondition gets a reference to the given string and assigns it to the VehicleCondition field.

### GetVehicleDefects

`func (o *V1DvirBase) GetVehicleDefects() []V1DvirDefectBase`

GetVehicleDefects returns the VehicleDefects field if non-nil, zero value otherwise.

### GetVehicleDefectsOk

`func (o *V1DvirBase) GetVehicleDefectsOk() ([]V1DvirDefectBase, bool)`

GetVehicleDefectsOk returns a tuple with the VehicleDefects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleDefects

`func (o *V1DvirBase) HasVehicleDefects() bool`

HasVehicleDefects returns a boolean if a field has been set.

### SetVehicleDefects

`func (o *V1DvirBase) SetVehicleDefects(v []V1DvirDefectBase)`

SetVehicleDefects gets a reference to the given []V1DvirDefectBase and assigns it to the VehicleDefects field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


