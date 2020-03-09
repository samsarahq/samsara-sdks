# Dvir

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthorSignature** | Pointer to [**DvirAuthorSignature**](DvirAuthorSignature.md) |  | [optional] 
**EndTime** | Pointer to [**time.Time**](time.Time.md) | Time when driver signed and completed this DVIR. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**Id** | Pointer to **string** | Unique Samsara ID for the DVIR. | 
**LicensePlate** | Pointer to **string** | The license plate of this vehicle. | [optional] 
**Location** | Pointer to **string** | Optional string if your jurisdiction requires a location of the DVIR. | [optional] 
**MechanicNotes** | Pointer to **string** | The mechanics notes on the DVIR. | [optional] 
**OdometerMeters** | Pointer to **int32** | The odometer reading in meters. | [optional] 
**SafetyStatus** | Pointer to **string** | The condition of vehicle on which DVIR was done. | [optional] [default to SAFETY_STATUS_UNSAFE]
**SecondSignature** | Pointer to [**DvirSecondSignature**](DvirSecondSignature.md) |  | [optional] 
**StartTime** | Pointer to [**time.Time**](time.Time.md) | Time when driver began filling out this DVIR. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**ThirdSignature** | Pointer to [**DvirThirdSignature**](DvirThirdSignature.md) |  | [optional] 
**Trailer** | Pointer to [**DvirTrailer**](DvirTrailer.md) |  | [optional] 
**TrailerDefects** | Pointer to [**[]DvirTrailerDefectsItems**](dvirTrailerDefectsItems.md) | Defects registered for the trailer which was part of the DVIR. | [optional] 
**TrailerName** | Pointer to **string** | The name of the trailer the DVIR was submitted for.  Only included for tractor+trailer DVIRs. | [optional] 
**Type** | Pointer to **string** | Inspection type of the DVIR. | [optional] [default to TYPE_UNSPECIFIED]
**Vehicle** | Pointer to [**DvirVehicle**](DvirVehicle.md) |  | [optional] 
**VehicleDefects** | Pointer to [**[]DvirTrailerDefectsItems**](dvirTrailerDefectsItems.md) | Defects registered for the vehicle which was part of the DVIR. | [optional] 

## Methods

### GetAuthorSignature

`func (o *Dvir) GetAuthorSignature() DvirAuthorSignature`

GetAuthorSignature returns the AuthorSignature field if non-nil, zero value otherwise.

### GetAuthorSignatureOk

`func (o *Dvir) GetAuthorSignatureOk() (DvirAuthorSignature, bool)`

GetAuthorSignatureOk returns a tuple with the AuthorSignature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAuthorSignature

`func (o *Dvir) HasAuthorSignature() bool`

HasAuthorSignature returns a boolean if a field has been set.

### SetAuthorSignature

`func (o *Dvir) SetAuthorSignature(v DvirAuthorSignature)`

SetAuthorSignature gets a reference to the given DvirAuthorSignature and assigns it to the AuthorSignature field.

### GetEndTime

`func (o *Dvir) GetEndTime() time.Time`

GetEndTime returns the EndTime field if non-nil, zero value otherwise.

### GetEndTimeOk

`func (o *Dvir) GetEndTimeOk() (time.Time, bool)`

GetEndTimeOk returns a tuple with the EndTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndTime

`func (o *Dvir) HasEndTime() bool`

HasEndTime returns a boolean if a field has been set.

### SetEndTime

`func (o *Dvir) SetEndTime(v time.Time)`

SetEndTime gets a reference to the given time.Time and assigns it to the EndTime field.

### GetId

`func (o *Dvir) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Dvir) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *Dvir) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *Dvir) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetLicensePlate

`func (o *Dvir) GetLicensePlate() string`

GetLicensePlate returns the LicensePlate field if non-nil, zero value otherwise.

### GetLicensePlateOk

`func (o *Dvir) GetLicensePlateOk() (string, bool)`

GetLicensePlateOk returns a tuple with the LicensePlate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLicensePlate

`func (o *Dvir) HasLicensePlate() bool`

HasLicensePlate returns a boolean if a field has been set.

### SetLicensePlate

`func (o *Dvir) SetLicensePlate(v string)`

SetLicensePlate gets a reference to the given string and assigns it to the LicensePlate field.

### GetLocation

`func (o *Dvir) GetLocation() string`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *Dvir) GetLocationOk() (string, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocation

`func (o *Dvir) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### SetLocation

`func (o *Dvir) SetLocation(v string)`

SetLocation gets a reference to the given string and assigns it to the Location field.

### GetMechanicNotes

`func (o *Dvir) GetMechanicNotes() string`

GetMechanicNotes returns the MechanicNotes field if non-nil, zero value otherwise.

### GetMechanicNotesOk

`func (o *Dvir) GetMechanicNotesOk() (string, bool)`

GetMechanicNotesOk returns a tuple with the MechanicNotes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMechanicNotes

`func (o *Dvir) HasMechanicNotes() bool`

HasMechanicNotes returns a boolean if a field has been set.

### SetMechanicNotes

`func (o *Dvir) SetMechanicNotes(v string)`

SetMechanicNotes gets a reference to the given string and assigns it to the MechanicNotes field.

### GetOdometerMeters

`func (o *Dvir) GetOdometerMeters() int32`

GetOdometerMeters returns the OdometerMeters field if non-nil, zero value otherwise.

### GetOdometerMetersOk

`func (o *Dvir) GetOdometerMetersOk() (int32, bool)`

GetOdometerMetersOk returns a tuple with the OdometerMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOdometerMeters

`func (o *Dvir) HasOdometerMeters() bool`

HasOdometerMeters returns a boolean if a field has been set.

### SetOdometerMeters

`func (o *Dvir) SetOdometerMeters(v int32)`

SetOdometerMeters gets a reference to the given int32 and assigns it to the OdometerMeters field.

### GetSafetyStatus

`func (o *Dvir) GetSafetyStatus() string`

GetSafetyStatus returns the SafetyStatus field if non-nil, zero value otherwise.

### GetSafetyStatusOk

`func (o *Dvir) GetSafetyStatusOk() (string, bool)`

GetSafetyStatusOk returns a tuple with the SafetyStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSafetyStatus

`func (o *Dvir) HasSafetyStatus() bool`

HasSafetyStatus returns a boolean if a field has been set.

### SetSafetyStatus

`func (o *Dvir) SetSafetyStatus(v string)`

SetSafetyStatus gets a reference to the given string and assigns it to the SafetyStatus field.

### GetSecondSignature

`func (o *Dvir) GetSecondSignature() DvirSecondSignature`

GetSecondSignature returns the SecondSignature field if non-nil, zero value otherwise.

### GetSecondSignatureOk

`func (o *Dvir) GetSecondSignatureOk() (DvirSecondSignature, bool)`

GetSecondSignatureOk returns a tuple with the SecondSignature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSecondSignature

`func (o *Dvir) HasSecondSignature() bool`

HasSecondSignature returns a boolean if a field has been set.

### SetSecondSignature

`func (o *Dvir) SetSecondSignature(v DvirSecondSignature)`

SetSecondSignature gets a reference to the given DvirSecondSignature and assigns it to the SecondSignature field.

### GetStartTime

`func (o *Dvir) GetStartTime() time.Time`

GetStartTime returns the StartTime field if non-nil, zero value otherwise.

### GetStartTimeOk

`func (o *Dvir) GetStartTimeOk() (time.Time, bool)`

GetStartTimeOk returns a tuple with the StartTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartTime

`func (o *Dvir) HasStartTime() bool`

HasStartTime returns a boolean if a field has been set.

### SetStartTime

`func (o *Dvir) SetStartTime(v time.Time)`

SetStartTime gets a reference to the given time.Time and assigns it to the StartTime field.

### GetThirdSignature

`func (o *Dvir) GetThirdSignature() DvirThirdSignature`

GetThirdSignature returns the ThirdSignature field if non-nil, zero value otherwise.

### GetThirdSignatureOk

`func (o *Dvir) GetThirdSignatureOk() (DvirThirdSignature, bool)`

GetThirdSignatureOk returns a tuple with the ThirdSignature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasThirdSignature

`func (o *Dvir) HasThirdSignature() bool`

HasThirdSignature returns a boolean if a field has been set.

### SetThirdSignature

`func (o *Dvir) SetThirdSignature(v DvirThirdSignature)`

SetThirdSignature gets a reference to the given DvirThirdSignature and assigns it to the ThirdSignature field.

### GetTrailer

`func (o *Dvir) GetTrailer() DvirTrailer`

GetTrailer returns the Trailer field if non-nil, zero value otherwise.

### GetTrailerOk

`func (o *Dvir) GetTrailerOk() (DvirTrailer, bool)`

GetTrailerOk returns a tuple with the Trailer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailer

`func (o *Dvir) HasTrailer() bool`

HasTrailer returns a boolean if a field has been set.

### SetTrailer

`func (o *Dvir) SetTrailer(v DvirTrailer)`

SetTrailer gets a reference to the given DvirTrailer and assigns it to the Trailer field.

### GetTrailerDefects

`func (o *Dvir) GetTrailerDefects() []DvirTrailerDefectsItems`

GetTrailerDefects returns the TrailerDefects field if non-nil, zero value otherwise.

### GetTrailerDefectsOk

`func (o *Dvir) GetTrailerDefectsOk() ([]DvirTrailerDefectsItems, bool)`

GetTrailerDefectsOk returns a tuple with the TrailerDefects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerDefects

`func (o *Dvir) HasTrailerDefects() bool`

HasTrailerDefects returns a boolean if a field has been set.

### SetTrailerDefects

`func (o *Dvir) SetTrailerDefects(v []DvirTrailerDefectsItems)`

SetTrailerDefects gets a reference to the given []DvirTrailerDefectsItems and assigns it to the TrailerDefects field.

### GetTrailerName

`func (o *Dvir) GetTrailerName() string`

GetTrailerName returns the TrailerName field if non-nil, zero value otherwise.

### GetTrailerNameOk

`func (o *Dvir) GetTrailerNameOk() (string, bool)`

GetTrailerNameOk returns a tuple with the TrailerName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerName

`func (o *Dvir) HasTrailerName() bool`

HasTrailerName returns a boolean if a field has been set.

### SetTrailerName

`func (o *Dvir) SetTrailerName(v string)`

SetTrailerName gets a reference to the given string and assigns it to the TrailerName field.

### GetType

`func (o *Dvir) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Dvir) GetTypeOk() (string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasType

`func (o *Dvir) HasType() bool`

HasType returns a boolean if a field has been set.

### SetType

`func (o *Dvir) SetType(v string)`

SetType gets a reference to the given string and assigns it to the Type field.

### GetVehicle

`func (o *Dvir) GetVehicle() DvirVehicle`

GetVehicle returns the Vehicle field if non-nil, zero value otherwise.

### GetVehicleOk

`func (o *Dvir) GetVehicleOk() (DvirVehicle, bool)`

GetVehicleOk returns a tuple with the Vehicle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicle

`func (o *Dvir) HasVehicle() bool`

HasVehicle returns a boolean if a field has been set.

### SetVehicle

`func (o *Dvir) SetVehicle(v DvirVehicle)`

SetVehicle gets a reference to the given DvirVehicle and assigns it to the Vehicle field.

### GetVehicleDefects

`func (o *Dvir) GetVehicleDefects() []DvirTrailerDefectsItems`

GetVehicleDefects returns the VehicleDefects field if non-nil, zero value otherwise.

### GetVehicleDefectsOk

`func (o *Dvir) GetVehicleDefectsOk() ([]DvirTrailerDefectsItems, bool)`

GetVehicleDefectsOk returns a tuple with the VehicleDefects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleDefects

`func (o *Dvir) HasVehicleDefects() bool`

HasVehicleDefects returns a boolean if a field has been set.

### SetVehicleDefects

`func (o *Dvir) SetVehicleDefects(v []DvirTrailerDefectsItems)`

SetVehicleDefects gets a reference to the given []DvirTrailerDefectsItems and assigns it to the VehicleDefects field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


