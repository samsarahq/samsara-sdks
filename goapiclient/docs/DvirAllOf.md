# DvirAllOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthorSignature** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 
**EndTime** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 
**Id** | Pointer to **string** | Unique Samsara ID for the DVIR. | 
**LicensePlate** | Pointer to **string** | The license plate of this vehicle. | [optional] 
**Location** | Pointer to **string** | Optional string if your jurisdiction requires a location of the DVIR. | [optional] 
**MechanicNotes** | Pointer to **string** | The mechanics notes on the DVIR. | [optional] 
**OdometerMeters** | Pointer to **int32** | The odometer reading in meters. | [optional] 
**SafetyStatus** | Pointer to **string** | The condition of vechile on which DVIR was done. | [optional] [default to SAFETY_STATUS_UNSAFE]
**SecondSignature** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 
**StartTime** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 
**ThirdSignature** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 
**Trailer** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 
**TrailerDefects** | Pointer to [**[]DvirAllOf0TrailerDefectsItems**](dvirAllOf0TrailerDefectsItems.md) | Defects registered for the trailer which was part of the DVIR. | [optional] 
**TrailerName** | Pointer to **string** | The name of the trailer the DVIR was submitted for.  Only included for tractor+trailer DVIRs. | [optional] 
**Type** | Pointer to **string** | Inspection type of the DVIR. | [optional] [default to TYPE_UNSPECIFIED]
**Vehicle** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 
**VehicleDefects** | Pointer to [**[]DvirAllOf0TrailerDefectsItems**](dvirAllOf0TrailerDefectsItems.md) | Defects registered for the vehicle which was part of the DVIR. | [optional] 

## Methods

### GetAuthorSignature

`func (o *DvirAllOf) GetAuthorSignature() map[string]interface{}`

GetAuthorSignature returns the AuthorSignature field if non-nil, zero value otherwise.

### GetAuthorSignatureOk

`func (o *DvirAllOf) GetAuthorSignatureOk() (map[string]interface{}, bool)`

GetAuthorSignatureOk returns a tuple with the AuthorSignature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuthorSignature

`func (o *DvirAllOf) HasAuthorSignature() bool`

HasAuthorSignature returns a boolean if a field has been set.

### SetAuthorSignature

`func (o *DvirAllOf) SetAuthorSignature(v map[string]interface{})`

SetAuthorSignature gets a reference to the given map[string]interface{} and assigns it to the AuthorSignature field.

### GetEndTime

`func (o *DvirAllOf) GetEndTime() map[string]interface{}`

GetEndTime returns the EndTime field if non-nil, zero value otherwise.

### GetEndTimeOk

`func (o *DvirAllOf) GetEndTimeOk() (map[string]interface{}, bool)`

GetEndTimeOk returns a tuple with the EndTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndTime

`func (o *DvirAllOf) HasEndTime() bool`

HasEndTime returns a boolean if a field has been set.

### SetEndTime

`func (o *DvirAllOf) SetEndTime(v map[string]interface{})`

SetEndTime gets a reference to the given map[string]interface{} and assigns it to the EndTime field.

### GetId

`func (o *DvirAllOf) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DvirAllOf) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *DvirAllOf) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *DvirAllOf) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetLicensePlate

`func (o *DvirAllOf) GetLicensePlate() string`

GetLicensePlate returns the LicensePlate field if non-nil, zero value otherwise.

### GetLicensePlateOk

`func (o *DvirAllOf) GetLicensePlateOk() (string, bool)`

GetLicensePlateOk returns a tuple with the LicensePlate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLicensePlate

`func (o *DvirAllOf) HasLicensePlate() bool`

HasLicensePlate returns a boolean if a field has been set.

### SetLicensePlate

`func (o *DvirAllOf) SetLicensePlate(v string)`

SetLicensePlate gets a reference to the given string and assigns it to the LicensePlate field.

### GetLocation

`func (o *DvirAllOf) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *DvirAllOf) GetLocationOk() (string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocation

`func (o *DvirAllOf) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### SetLocation

`func (o *DvirAllOf) SetLocation(v string)`

SetLocation gets a reference to the given string and assigns it to the Location field.

### GetMechanicNotes

`func (o *DvirAllOf) GetMechanicNotes() string`

GetMechanicNotes returns the MechanicNotes field if non-nil, zero value otherwise.

### GetMechanicNotesOk

`func (o *DvirAllOf) GetMechanicNotesOk() (string, bool)`

GetMechanicNotesOk returns a tuple with the MechanicNotes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMechanicNotes

`func (o *DvirAllOf) HasMechanicNotes() bool`

HasMechanicNotes returns a boolean if a field has been set.

### SetMechanicNotes

`func (o *DvirAllOf) SetMechanicNotes(v string)`

SetMechanicNotes gets a reference to the given string and assigns it to the MechanicNotes field.

### GetOdometerMeters

`func (o *DvirAllOf) GetOdometerMeters() int32`

GetOdometerMeters returns the OdometerMeters field if non-nil, zero value otherwise.

### GetOdometerMetersOk

`func (o *DvirAllOf) GetOdometerMetersOk() (int32, bool)`

GetOdometerMetersOk returns a tuple with the OdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOdometerMeters

`func (o *DvirAllOf) HasOdometerMeters() bool`

HasOdometerMeters returns a boolean if a field has been set.

### SetOdometerMeters

`func (o *DvirAllOf) SetOdometerMeters(v int32)`

SetOdometerMeters gets a reference to the given int32 and assigns it to the OdometerMeters field.

### GetSafetyStatus

`func (o *DvirAllOf) GetSafetyStatus() string`

GetSafetyStatus returns the SafetyStatus field if non-nil, zero value otherwise.

### GetSafetyStatusOk

`func (o *DvirAllOf) GetSafetyStatusOk() (string, bool)`

GetSafetyStatusOk returns a tuple with the SafetyStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSafetyStatus

`func (o *DvirAllOf) HasSafetyStatus() bool`

HasSafetyStatus returns a boolean if a field has been set.

### SetSafetyStatus

`func (o *DvirAllOf) SetSafetyStatus(v string)`

SetSafetyStatus gets a reference to the given string and assigns it to the SafetyStatus field.

### GetSecondSignature

`func (o *DvirAllOf) GetSecondSignature() map[string]interface{}`

GetSecondSignature returns the SecondSignature field if non-nil, zero value otherwise.

### GetSecondSignatureOk

`func (o *DvirAllOf) GetSecondSignatureOk() (map[string]interface{}, bool)`

GetSecondSignatureOk returns a tuple with the SecondSignature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSecondSignature

`func (o *DvirAllOf) HasSecondSignature() bool`

HasSecondSignature returns a boolean if a field has been set.

### SetSecondSignature

`func (o *DvirAllOf) SetSecondSignature(v map[string]interface{})`

SetSecondSignature gets a reference to the given map[string]interface{} and assigns it to the SecondSignature field.

### GetStartTime

`func (o *DvirAllOf) GetStartTime() map[string]interface{}`

GetStartTime returns the StartTime field if non-nil, zero value otherwise.

### GetStartTimeOk

`func (o *DvirAllOf) GetStartTimeOk() (map[string]interface{}, bool)`

GetStartTimeOk returns a tuple with the StartTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartTime

`func (o *DvirAllOf) HasStartTime() bool`

HasStartTime returns a boolean if a field has been set.

### SetStartTime

`func (o *DvirAllOf) SetStartTime(v map[string]interface{})`

SetStartTime gets a reference to the given map[string]interface{} and assigns it to the StartTime field.

### GetThirdSignature

`func (o *DvirAllOf) GetThirdSignature() map[string]interface{}`

GetThirdSignature returns the ThirdSignature field if non-nil, zero value otherwise.

### GetThirdSignatureOk

`func (o *DvirAllOf) GetThirdSignatureOk() (map[string]interface{}, bool)`

GetThirdSignatureOk returns a tuple with the ThirdSignature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasThirdSignature

`func (o *DvirAllOf) HasThirdSignature() bool`

HasThirdSignature returns a boolean if a field has been set.

### SetThirdSignature

`func (o *DvirAllOf) SetThirdSignature(v map[string]interface{})`

SetThirdSignature gets a reference to the given map[string]interface{} and assigns it to the ThirdSignature field.

### GetTrailer

`func (o *DvirAllOf) GetTrailer() map[string]interface{}`

GetTrailer returns the Trailer field if non-nil, zero value otherwise.

### GetTrailerOk

`func (o *DvirAllOf) GetTrailerOk() (map[string]interface{}, bool)`

GetTrailerOk returns a tuple with the Trailer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailer

`func (o *DvirAllOf) HasTrailer() bool`

HasTrailer returns a boolean if a field has been set.

### SetTrailer

`func (o *DvirAllOf) SetTrailer(v map[string]interface{})`

SetTrailer gets a reference to the given map[string]interface{} and assigns it to the Trailer field.

### GetTrailerDefects

`func (o *DvirAllOf) GetTrailerDefects() []DvirAllOf0TrailerDefectsItems`

GetTrailerDefects returns the TrailerDefects field if non-nil, zero value otherwise.

### GetTrailerDefectsOk

`func (o *DvirAllOf) GetTrailerDefectsOk() ([]DvirAllOf0TrailerDefectsItems, bool)`

GetTrailerDefectsOk returns a tuple with the TrailerDefects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerDefects

`func (o *DvirAllOf) HasTrailerDefects() bool`

HasTrailerDefects returns a boolean if a field has been set.

### SetTrailerDefects

`func (o *DvirAllOf) SetTrailerDefects(v []DvirAllOf0TrailerDefectsItems)`

SetTrailerDefects gets a reference to the given []DvirAllOf0TrailerDefectsItems and assigns it to the TrailerDefects field.

### GetTrailerName

`func (o *DvirAllOf) GetTrailerName() string`

GetTrailerName returns the TrailerName field if non-nil, zero value otherwise.

### GetTrailerNameOk

`func (o *DvirAllOf) GetTrailerNameOk() (string, bool)`

GetTrailerNameOk returns a tuple with the TrailerName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerName

`func (o *DvirAllOf) HasTrailerName() bool`

HasTrailerName returns a boolean if a field has been set.

### SetTrailerName

`func (o *DvirAllOf) SetTrailerName(v string)`

SetTrailerName gets a reference to the given string and assigns it to the TrailerName field.

### GetType

`func (o *DvirAllOf) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *DvirAllOf) GetTypeOk() (string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasType

`func (o *DvirAllOf) HasType() bool`

HasType returns a boolean if a field has been set.

### SetType

`func (o *DvirAllOf) SetType(v string)`

SetType gets a reference to the given string and assigns it to the Type field.

### GetVehicle

`func (o *DvirAllOf) GetVehicle() map[string]interface{}`

GetVehicle returns the Vehicle field if non-nil, zero value otherwise.

### GetVehicleOk

`func (o *DvirAllOf) GetVehicleOk() (map[string]interface{}, bool)`

GetVehicleOk returns a tuple with the Vehicle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicle

`func (o *DvirAllOf) HasVehicle() bool`

HasVehicle returns a boolean if a field has been set.

### SetVehicle

`func (o *DvirAllOf) SetVehicle(v map[string]interface{})`

SetVehicle gets a reference to the given map[string]interface{} and assigns it to the Vehicle field.

### GetVehicleDefects

`func (o *DvirAllOf) GetVehicleDefects() []DvirAllOf0TrailerDefectsItems`

GetVehicleDefects returns the VehicleDefects field if non-nil, zero value otherwise.

### GetVehicleDefectsOk

`func (o *DvirAllOf) GetVehicleDefectsOk() ([]DvirAllOf0TrailerDefectsItems, bool)`

GetVehicleDefectsOk returns a tuple with the VehicleDefects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleDefects

`func (o *DvirAllOf) HasVehicleDefects() bool`

HasVehicleDefects returns a boolean if a field has been set.

### SetVehicleDefects

`func (o *DvirAllOf) SetVehicleDefects(v []DvirAllOf0TrailerDefectsItems)`

SetVehicleDefects gets a reference to the given []DvirAllOf0TrailerDefectsItems and assigns it to the VehicleDefects field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


