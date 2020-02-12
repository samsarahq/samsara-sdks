# V1DriverSafetyScoreResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CrashCount** | Pointer to **int32** | Crash event count | [optional] 
**DriverId** | Pointer to **int32** | Driver ID | [optional] 
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

## Methods

### GetCrashCount

`func (o *V1DriverSafetyScoreResponse) GetCrashCount() int32`

GetCrashCount returns the CrashCount field if non-nil, zero value otherwise.

### GetCrashCountOk

`func (o *V1DriverSafetyScoreResponse) GetCrashCountOk() (int32, bool)`

GetCrashCountOk returns a tuple with the CrashCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCrashCount

`func (o *V1DriverSafetyScoreResponse) HasCrashCount() bool`

HasCrashCount returns a boolean if a field has been set.

### SetCrashCount

`func (o *V1DriverSafetyScoreResponse) SetCrashCount(v int32)`

SetCrashCount gets a reference to the given int32 and assigns it to the CrashCount field.

### GetDriverId

`func (o *V1DriverSafetyScoreResponse) GetDriverId() int32`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1DriverSafetyScoreResponse) GetDriverIdOk() (int32, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1DriverSafetyScoreResponse) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1DriverSafetyScoreResponse) SetDriverId(v int32)`

SetDriverId gets a reference to the given int32 and assigns it to the DriverId field.

### GetHarshAccelCount

`func (o *V1DriverSafetyScoreResponse) GetHarshAccelCount() int32`

GetHarshAccelCount returns the HarshAccelCount field if non-nil, zero value otherwise.

### GetHarshAccelCountOk

`func (o *V1DriverSafetyScoreResponse) GetHarshAccelCountOk() (int32, bool)`

GetHarshAccelCountOk returns a tuple with the HarshAccelCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshAccelCount

`func (o *V1DriverSafetyScoreResponse) HasHarshAccelCount() bool`

HasHarshAccelCount returns a boolean if a field has been set.

### SetHarshAccelCount

`func (o *V1DriverSafetyScoreResponse) SetHarshAccelCount(v int32)`

SetHarshAccelCount gets a reference to the given int32 and assigns it to the HarshAccelCount field.

### GetHarshBrakingCount

`func (o *V1DriverSafetyScoreResponse) GetHarshBrakingCount() int32`

GetHarshBrakingCount returns the HarshBrakingCount field if non-nil, zero value otherwise.

### GetHarshBrakingCountOk

`func (o *V1DriverSafetyScoreResponse) GetHarshBrakingCountOk() (int32, bool)`

GetHarshBrakingCountOk returns a tuple with the HarshBrakingCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshBrakingCount

`func (o *V1DriverSafetyScoreResponse) HasHarshBrakingCount() bool`

HasHarshBrakingCount returns a boolean if a field has been set.

### SetHarshBrakingCount

`func (o *V1DriverSafetyScoreResponse) SetHarshBrakingCount(v int32)`

SetHarshBrakingCount gets a reference to the given int32 and assigns it to the HarshBrakingCount field.

### GetHarshEvents

`func (o *V1DriverSafetyScoreResponse) GetHarshEvents() []V1SafetyReportHarshEvent`

GetHarshEvents returns the HarshEvents field if non-nil, zero value otherwise.

### GetHarshEventsOk

`func (o *V1DriverSafetyScoreResponse) GetHarshEventsOk() ([]V1SafetyReportHarshEvent, bool)`

GetHarshEventsOk returns a tuple with the HarshEvents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshEvents

`func (o *V1DriverSafetyScoreResponse) HasHarshEvents() bool`

HasHarshEvents returns a boolean if a field has been set.

### SetHarshEvents

`func (o *V1DriverSafetyScoreResponse) SetHarshEvents(v []V1SafetyReportHarshEvent)`

SetHarshEvents gets a reference to the given []V1SafetyReportHarshEvent and assigns it to the HarshEvents field.

### GetHarshTurningCount

`func (o *V1DriverSafetyScoreResponse) GetHarshTurningCount() int32`

GetHarshTurningCount returns the HarshTurningCount field if non-nil, zero value otherwise.

### GetHarshTurningCountOk

`func (o *V1DriverSafetyScoreResponse) GetHarshTurningCountOk() (int32, bool)`

GetHarshTurningCountOk returns a tuple with the HarshTurningCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshTurningCount

`func (o *V1DriverSafetyScoreResponse) HasHarshTurningCount() bool`

HasHarshTurningCount returns a boolean if a field has been set.

### SetHarshTurningCount

`func (o *V1DriverSafetyScoreResponse) SetHarshTurningCount(v int32)`

SetHarshTurningCount gets a reference to the given int32 and assigns it to the HarshTurningCount field.

### GetSafetyScore

`func (o *V1DriverSafetyScoreResponse) GetSafetyScore() int32`

GetSafetyScore returns the SafetyScore field if non-nil, zero value otherwise.

### GetSafetyScoreOk

`func (o *V1DriverSafetyScoreResponse) GetSafetyScoreOk() (int32, bool)`

GetSafetyScoreOk returns a tuple with the SafetyScore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSafetyScore

`func (o *V1DriverSafetyScoreResponse) HasSafetyScore() bool`

HasSafetyScore returns a boolean if a field has been set.

### SetSafetyScore

`func (o *V1DriverSafetyScoreResponse) SetSafetyScore(v int32)`

SetSafetyScore gets a reference to the given int32 and assigns it to the SafetyScore field.

### GetSafetyScoreRank

`func (o *V1DriverSafetyScoreResponse) GetSafetyScoreRank() string`

GetSafetyScoreRank returns the SafetyScoreRank field if non-nil, zero value otherwise.

### GetSafetyScoreRankOk

`func (o *V1DriverSafetyScoreResponse) GetSafetyScoreRankOk() (string, bool)`

GetSafetyScoreRankOk returns a tuple with the SafetyScoreRank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSafetyScoreRank

`func (o *V1DriverSafetyScoreResponse) HasSafetyScoreRank() bool`

HasSafetyScoreRank returns a boolean if a field has been set.

### SetSafetyScoreRank

`func (o *V1DriverSafetyScoreResponse) SetSafetyScoreRank(v string)`

SetSafetyScoreRank gets a reference to the given string and assigns it to the SafetyScoreRank field.

### GetTimeOverSpeedLimitMs

`func (o *V1DriverSafetyScoreResponse) GetTimeOverSpeedLimitMs() int32`

GetTimeOverSpeedLimitMs returns the TimeOverSpeedLimitMs field if non-nil, zero value otherwise.

### GetTimeOverSpeedLimitMsOk

`func (o *V1DriverSafetyScoreResponse) GetTimeOverSpeedLimitMsOk() (int32, bool)`

GetTimeOverSpeedLimitMsOk returns a tuple with the TimeOverSpeedLimitMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTimeOverSpeedLimitMs

`func (o *V1DriverSafetyScoreResponse) HasTimeOverSpeedLimitMs() bool`

HasTimeOverSpeedLimitMs returns a boolean if a field has been set.

### SetTimeOverSpeedLimitMs

`func (o *V1DriverSafetyScoreResponse) SetTimeOverSpeedLimitMs(v int32)`

SetTimeOverSpeedLimitMs gets a reference to the given int32 and assigns it to the TimeOverSpeedLimitMs field.

### GetTotalDistanceDrivenMeters

`func (o *V1DriverSafetyScoreResponse) GetTotalDistanceDrivenMeters() int32`

GetTotalDistanceDrivenMeters returns the TotalDistanceDrivenMeters field if non-nil, zero value otherwise.

### GetTotalDistanceDrivenMetersOk

`func (o *V1DriverSafetyScoreResponse) GetTotalDistanceDrivenMetersOk() (int32, bool)`

GetTotalDistanceDrivenMetersOk returns a tuple with the TotalDistanceDrivenMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTotalDistanceDrivenMeters

`func (o *V1DriverSafetyScoreResponse) HasTotalDistanceDrivenMeters() bool`

HasTotalDistanceDrivenMeters returns a boolean if a field has been set.

### SetTotalDistanceDrivenMeters

`func (o *V1DriverSafetyScoreResponse) SetTotalDistanceDrivenMeters(v int32)`

SetTotalDistanceDrivenMeters gets a reference to the given int32 and assigns it to the TotalDistanceDrivenMeters field.

### GetTotalHarshEventCount

`func (o *V1DriverSafetyScoreResponse) GetTotalHarshEventCount() int32`

GetTotalHarshEventCount returns the TotalHarshEventCount field if non-nil, zero value otherwise.

### GetTotalHarshEventCountOk

`func (o *V1DriverSafetyScoreResponse) GetTotalHarshEventCountOk() (int32, bool)`

GetTotalHarshEventCountOk returns a tuple with the TotalHarshEventCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTotalHarshEventCount

`func (o *V1DriverSafetyScoreResponse) HasTotalHarshEventCount() bool`

HasTotalHarshEventCount returns a boolean if a field has been set.

### SetTotalHarshEventCount

`func (o *V1DriverSafetyScoreResponse) SetTotalHarshEventCount(v int32)`

SetTotalHarshEventCount gets a reference to the given int32 and assigns it to the TotalHarshEventCount field.

### GetTotalTimeDrivenMs

`func (o *V1DriverSafetyScoreResponse) GetTotalTimeDrivenMs() int32`

GetTotalTimeDrivenMs returns the TotalTimeDrivenMs field if non-nil, zero value otherwise.

### GetTotalTimeDrivenMsOk

`func (o *V1DriverSafetyScoreResponse) GetTotalTimeDrivenMsOk() (int32, bool)`

GetTotalTimeDrivenMsOk returns a tuple with the TotalTimeDrivenMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTotalTimeDrivenMs

`func (o *V1DriverSafetyScoreResponse) HasTotalTimeDrivenMs() bool`

HasTotalTimeDrivenMs returns a boolean if a field has been set.

### SetTotalTimeDrivenMs

`func (o *V1DriverSafetyScoreResponse) SetTotalTimeDrivenMs(v int32)`

SetTotalTimeDrivenMs gets a reference to the given int32 and assigns it to the TotalTimeDrivenMs field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


