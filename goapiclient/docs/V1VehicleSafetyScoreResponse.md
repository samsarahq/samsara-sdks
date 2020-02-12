# V1VehicleSafetyScoreResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CrashCount** | Pointer to **int32** | Crash event count | [optional] 
**HarshAccelCount** | Pointer to **int32** | Harsh acceleration event count | [optional] 
**HarshBrakingCount** | Pointer to **int32** | Harsh braking event count | [optional] 
**HarshEvents** | Pointer to [**[]V1SafetyReportHarshEvent**](V1SafetyReportHarshEvent.md) |  | [optional] 
**HarshTurningCount** | Pointer to **int32** | Harsh turning event count | [optional] 
**SafetyScore** | Pointer to **int32** | Safety Score | [optional] 
**SafetyScoreRank** | Pointer to **string** | Safety Score Rank | [optional] 
**TimeOverSpeedLimitMs** | Pointer to **int32** | Amount of time driven over the speed limit in milliseconds | [optional] 
**TotalDistanceDrivenMeters** | Pointer to **int32** | Total distance driven in meters | [optional] 
**TotalHarshEventCount** | Pointer to **int32** | Total harsh event count | [optional] 
**TotalTimeDrivenMs** | Pointer to **int32** | Amount of time driven in milliseconds | [optional] 
**VehicleId** | Pointer to **int32** | Vehicle ID | [optional] 

## Methods

### GetCrashCount

`func (o *V1VehicleSafetyScoreResponse) GetCrashCount() int32`

GetCrashCount returns the CrashCount field if non-nil, zero value otherwise.

### GetCrashCountOk

`func (o *V1VehicleSafetyScoreResponse) GetCrashCountOk() (int32, bool)`

GetCrashCountOk returns a tuple with the CrashCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCrashCount

`func (o *V1VehicleSafetyScoreResponse) HasCrashCount() bool`

HasCrashCount returns a boolean if a field has been set.

### SetCrashCount

`func (o *V1VehicleSafetyScoreResponse) SetCrashCount(v int32)`

SetCrashCount gets a reference to the given int32 and assigns it to the CrashCount field.

### GetHarshAccelCount

`func (o *V1VehicleSafetyScoreResponse) GetHarshAccelCount() int32`

GetHarshAccelCount returns the HarshAccelCount field if non-nil, zero value otherwise.

### GetHarshAccelCountOk

`func (o *V1VehicleSafetyScoreResponse) GetHarshAccelCountOk() (int32, bool)`

GetHarshAccelCountOk returns a tuple with the HarshAccelCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshAccelCount

`func (o *V1VehicleSafetyScoreResponse) HasHarshAccelCount() bool`

HasHarshAccelCount returns a boolean if a field has been set.

### SetHarshAccelCount

`func (o *V1VehicleSafetyScoreResponse) SetHarshAccelCount(v int32)`

SetHarshAccelCount gets a reference to the given int32 and assigns it to the HarshAccelCount field.

### GetHarshBrakingCount

`func (o *V1VehicleSafetyScoreResponse) GetHarshBrakingCount() int32`

GetHarshBrakingCount returns the HarshBrakingCount field if non-nil, zero value otherwise.

### GetHarshBrakingCountOk

`func (o *V1VehicleSafetyScoreResponse) GetHarshBrakingCountOk() (int32, bool)`

GetHarshBrakingCountOk returns a tuple with the HarshBrakingCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshBrakingCount

`func (o *V1VehicleSafetyScoreResponse) HasHarshBrakingCount() bool`

HasHarshBrakingCount returns a boolean if a field has been set.

### SetHarshBrakingCount

`func (o *V1VehicleSafetyScoreResponse) SetHarshBrakingCount(v int32)`

SetHarshBrakingCount gets a reference to the given int32 and assigns it to the HarshBrakingCount field.

### GetHarshEvents

`func (o *V1VehicleSafetyScoreResponse) GetHarshEvents() []V1SafetyReportHarshEvent`

GetHarshEvents returns the HarshEvents field if non-nil, zero value otherwise.

### GetHarshEventsOk

`func (o *V1VehicleSafetyScoreResponse) GetHarshEventsOk() ([]V1SafetyReportHarshEvent, bool)`

GetHarshEventsOk returns a tuple with the HarshEvents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshEvents

`func (o *V1VehicleSafetyScoreResponse) HasHarshEvents() bool`

HasHarshEvents returns a boolean if a field has been set.

### SetHarshEvents

`func (o *V1VehicleSafetyScoreResponse) SetHarshEvents(v []V1SafetyReportHarshEvent)`

SetHarshEvents gets a reference to the given []V1SafetyReportHarshEvent and assigns it to the HarshEvents field.

### GetHarshTurningCount

`func (o *V1VehicleSafetyScoreResponse) GetHarshTurningCount() int32`

GetHarshTurningCount returns the HarshTurningCount field if non-nil, zero value otherwise.

### GetHarshTurningCountOk

`func (o *V1VehicleSafetyScoreResponse) GetHarshTurningCountOk() (int32, bool)`

GetHarshTurningCountOk returns a tuple with the HarshTurningCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshTurningCount

`func (o *V1VehicleSafetyScoreResponse) HasHarshTurningCount() bool`

HasHarshTurningCount returns a boolean if a field has been set.

### SetHarshTurningCount

`func (o *V1VehicleSafetyScoreResponse) SetHarshTurningCount(v int32)`

SetHarshTurningCount gets a reference to the given int32 and assigns it to the HarshTurningCount field.

### GetSafetyScore

`func (o *V1VehicleSafetyScoreResponse) GetSafetyScore() int32`

GetSafetyScore returns the SafetyScore field if non-nil, zero value otherwise.

### GetSafetyScoreOk

`func (o *V1VehicleSafetyScoreResponse) GetSafetyScoreOk() (int32, bool)`

GetSafetyScoreOk returns a tuple with the SafetyScore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSafetyScore

`func (o *V1VehicleSafetyScoreResponse) HasSafetyScore() bool`

HasSafetyScore returns a boolean if a field has been set.

### SetSafetyScore

`func (o *V1VehicleSafetyScoreResponse) SetSafetyScore(v int32)`

SetSafetyScore gets a reference to the given int32 and assigns it to the SafetyScore field.

### GetSafetyScoreRank

`func (o *V1VehicleSafetyScoreResponse) GetSafetyScoreRank() string`

GetSafetyScoreRank returns the SafetyScoreRank field if non-nil, zero value otherwise.

### GetSafetyScoreRankOk

`func (o *V1VehicleSafetyScoreResponse) GetSafetyScoreRankOk() (string, bool)`

GetSafetyScoreRankOk returns a tuple with the SafetyScoreRank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSafetyScoreRank

`func (o *V1VehicleSafetyScoreResponse) HasSafetyScoreRank() bool`

HasSafetyScoreRank returns a boolean if a field has been set.

### SetSafetyScoreRank

`func (o *V1VehicleSafetyScoreResponse) SetSafetyScoreRank(v string)`

SetSafetyScoreRank gets a reference to the given string and assigns it to the SafetyScoreRank field.

### GetTimeOverSpeedLimitMs

`func (o *V1VehicleSafetyScoreResponse) GetTimeOverSpeedLimitMs() int32`

GetTimeOverSpeedLimitMs returns the TimeOverSpeedLimitMs field if non-nil, zero value otherwise.

### GetTimeOverSpeedLimitMsOk

`func (o *V1VehicleSafetyScoreResponse) GetTimeOverSpeedLimitMsOk() (int32, bool)`

GetTimeOverSpeedLimitMsOk returns a tuple with the TimeOverSpeedLimitMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTimeOverSpeedLimitMs

`func (o *V1VehicleSafetyScoreResponse) HasTimeOverSpeedLimitMs() bool`

HasTimeOverSpeedLimitMs returns a boolean if a field has been set.

### SetTimeOverSpeedLimitMs

`func (o *V1VehicleSafetyScoreResponse) SetTimeOverSpeedLimitMs(v int32)`

SetTimeOverSpeedLimitMs gets a reference to the given int32 and assigns it to the TimeOverSpeedLimitMs field.

### GetTotalDistanceDrivenMeters

`func (o *V1VehicleSafetyScoreResponse) GetTotalDistanceDrivenMeters() int32`

GetTotalDistanceDrivenMeters returns the TotalDistanceDrivenMeters field if non-nil, zero value otherwise.

### GetTotalDistanceDrivenMetersOk

`func (o *V1VehicleSafetyScoreResponse) GetTotalDistanceDrivenMetersOk() (int32, bool)`

GetTotalDistanceDrivenMetersOk returns a tuple with the TotalDistanceDrivenMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTotalDistanceDrivenMeters

`func (o *V1VehicleSafetyScoreResponse) HasTotalDistanceDrivenMeters() bool`

HasTotalDistanceDrivenMeters returns a boolean if a field has been set.

### SetTotalDistanceDrivenMeters

`func (o *V1VehicleSafetyScoreResponse) SetTotalDistanceDrivenMeters(v int32)`

SetTotalDistanceDrivenMeters gets a reference to the given int32 and assigns it to the TotalDistanceDrivenMeters field.

### GetTotalHarshEventCount

`func (o *V1VehicleSafetyScoreResponse) GetTotalHarshEventCount() int32`

GetTotalHarshEventCount returns the TotalHarshEventCount field if non-nil, zero value otherwise.

### GetTotalHarshEventCountOk

`func (o *V1VehicleSafetyScoreResponse) GetTotalHarshEventCountOk() (int32, bool)`

GetTotalHarshEventCountOk returns a tuple with the TotalHarshEventCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTotalHarshEventCount

`func (o *V1VehicleSafetyScoreResponse) HasTotalHarshEventCount() bool`

HasTotalHarshEventCount returns a boolean if a field has been set.

### SetTotalHarshEventCount

`func (o *V1VehicleSafetyScoreResponse) SetTotalHarshEventCount(v int32)`

SetTotalHarshEventCount gets a reference to the given int32 and assigns it to the TotalHarshEventCount field.

### GetTotalTimeDrivenMs

`func (o *V1VehicleSafetyScoreResponse) GetTotalTimeDrivenMs() int32`

GetTotalTimeDrivenMs returns the TotalTimeDrivenMs field if non-nil, zero value otherwise.

### GetTotalTimeDrivenMsOk

`func (o *V1VehicleSafetyScoreResponse) GetTotalTimeDrivenMsOk() (int32, bool)`

GetTotalTimeDrivenMsOk returns a tuple with the TotalTimeDrivenMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTotalTimeDrivenMs

`func (o *V1VehicleSafetyScoreResponse) HasTotalTimeDrivenMs() bool`

HasTotalTimeDrivenMs returns a boolean if a field has been set.

### SetTotalTimeDrivenMs

`func (o *V1VehicleSafetyScoreResponse) SetTotalTimeDrivenMs(v int32)`

SetTotalTimeDrivenMs gets a reference to the given int32 and assigns it to the TotalTimeDrivenMs field.

### GetVehicleId

`func (o *V1VehicleSafetyScoreResponse) GetVehicleId() int32`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1VehicleSafetyScoreResponse) GetVehicleIdOk() (int32, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1VehicleSafetyScoreResponse) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1VehicleSafetyScoreResponse) SetVehicleId(v int32)`

SetVehicleId gets a reference to the given int32 and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


