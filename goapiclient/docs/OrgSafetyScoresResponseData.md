# OrgSafetyScoresResponseData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CrashCount** | Pointer to **int64** | Crash count | [optional] 
**DriverId** | Pointer to **int64** | Driver Id | [optional] 
**HarshAccelCount** | Pointer to **int64** | Harsh accel count | [optional] 
**HarshBrakingCount** | Pointer to **int64** | Harsh braking count | [optional] 
**HarshEventIdentifiers** | Pointer to [**[]OrgSafetyScoresResponseHarshEventIdentifiers**](OrgSafetyScoresResponse_harshEventIdentifiers.md) |  | [optional] 
**HarshTurningCount** | Pointer to **int64** | Harsh turning count | [optional] 
**SafetyScore** | Pointer to **int64** | Vehicle/Driver Safety Score | [optional] 
**SafetyScoreRank** | Pointer to **int64** | Vehicle/Driver Safety Rank | [optional] 
**TimeOverSpeedLimitMs** | Pointer to **int64** | Overspeed limit time, specified in milliseconds UNIX time. | [optional] 
**TotalDistanceDrivenMeters** | Pointer to **int64** | Total distance driven meters | [optional] 
**TotalHarshEventCount** | Pointer to **int64** | Total harsh event count | [optional] 
**TotalTimeDrivenMs** | Pointer to **int64** | Total driver time, specified in milliseconds UNIX time. | [optional] 
**VehicleId** | Pointer to **int64** | Vehicle Id | [optional] 

## Methods

### GetCrashCount

`func (o *OrgSafetyScoresResponseData) GetCrashCount() int64`

GetCrashCount returns the CrashCount field if non-nil, zero value otherwise.

### GetCrashCountOk

`func (o *OrgSafetyScoresResponseData) GetCrashCountOk() (int64, bool)`

GetCrashCountOk returns a tuple with the CrashCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCrashCount

`func (o *OrgSafetyScoresResponseData) HasCrashCount() bool`

HasCrashCount returns a boolean if a field has been set.

### SetCrashCount

`func (o *OrgSafetyScoresResponseData) SetCrashCount(v int64)`

SetCrashCount gets a reference to the given int64 and assigns it to the CrashCount field.

### GetDriverId

`func (o *OrgSafetyScoresResponseData) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *OrgSafetyScoresResponseData) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *OrgSafetyScoresResponseData) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *OrgSafetyScoresResponseData) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetHarshAccelCount

`func (o *OrgSafetyScoresResponseData) GetHarshAccelCount() int64`

GetHarshAccelCount returns the HarshAccelCount field if non-nil, zero value otherwise.

### GetHarshAccelCountOk

`func (o *OrgSafetyScoresResponseData) GetHarshAccelCountOk() (int64, bool)`

GetHarshAccelCountOk returns a tuple with the HarshAccelCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshAccelCount

`func (o *OrgSafetyScoresResponseData) HasHarshAccelCount() bool`

HasHarshAccelCount returns a boolean if a field has been set.

### SetHarshAccelCount

`func (o *OrgSafetyScoresResponseData) SetHarshAccelCount(v int64)`

SetHarshAccelCount gets a reference to the given int64 and assigns it to the HarshAccelCount field.

### GetHarshBrakingCount

`func (o *OrgSafetyScoresResponseData) GetHarshBrakingCount() int64`

GetHarshBrakingCount returns the HarshBrakingCount field if non-nil, zero value otherwise.

### GetHarshBrakingCountOk

`func (o *OrgSafetyScoresResponseData) GetHarshBrakingCountOk() (int64, bool)`

GetHarshBrakingCountOk returns a tuple with the HarshBrakingCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshBrakingCount

`func (o *OrgSafetyScoresResponseData) HasHarshBrakingCount() bool`

HasHarshBrakingCount returns a boolean if a field has been set.

### SetHarshBrakingCount

`func (o *OrgSafetyScoresResponseData) SetHarshBrakingCount(v int64)`

SetHarshBrakingCount gets a reference to the given int64 and assigns it to the HarshBrakingCount field.

### GetHarshEventIdentifiers

`func (o *OrgSafetyScoresResponseData) GetHarshEventIdentifiers() []OrgSafetyScoresResponseHarshEventIdentifiers`

GetHarshEventIdentifiers returns the HarshEventIdentifiers field if non-nil, zero value otherwise.

### GetHarshEventIdentifiersOk

`func (o *OrgSafetyScoresResponseData) GetHarshEventIdentifiersOk() ([]OrgSafetyScoresResponseHarshEventIdentifiers, bool)`

GetHarshEventIdentifiersOk returns a tuple with the HarshEventIdentifiers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshEventIdentifiers

`func (o *OrgSafetyScoresResponseData) HasHarshEventIdentifiers() bool`

HasHarshEventIdentifiers returns a boolean if a field has been set.

### SetHarshEventIdentifiers

`func (o *OrgSafetyScoresResponseData) SetHarshEventIdentifiers(v []OrgSafetyScoresResponseHarshEventIdentifiers)`

SetHarshEventIdentifiers gets a reference to the given []OrgSafetyScoresResponseHarshEventIdentifiers and assigns it to the HarshEventIdentifiers field.

### GetHarshTurningCount

`func (o *OrgSafetyScoresResponseData) GetHarshTurningCount() int64`

GetHarshTurningCount returns the HarshTurningCount field if non-nil, zero value otherwise.

### GetHarshTurningCountOk

`func (o *OrgSafetyScoresResponseData) GetHarshTurningCountOk() (int64, bool)`

GetHarshTurningCountOk returns a tuple with the HarshTurningCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshTurningCount

`func (o *OrgSafetyScoresResponseData) HasHarshTurningCount() bool`

HasHarshTurningCount returns a boolean if a field has been set.

### SetHarshTurningCount

`func (o *OrgSafetyScoresResponseData) SetHarshTurningCount(v int64)`

SetHarshTurningCount gets a reference to the given int64 and assigns it to the HarshTurningCount field.

### GetSafetyScore

`func (o *OrgSafetyScoresResponseData) GetSafetyScore() int64`

GetSafetyScore returns the SafetyScore field if non-nil, zero value otherwise.

### GetSafetyScoreOk

`func (o *OrgSafetyScoresResponseData) GetSafetyScoreOk() (int64, bool)`

GetSafetyScoreOk returns a tuple with the SafetyScore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSafetyScore

`func (o *OrgSafetyScoresResponseData) HasSafetyScore() bool`

HasSafetyScore returns a boolean if a field has been set.

### SetSafetyScore

`func (o *OrgSafetyScoresResponseData) SetSafetyScore(v int64)`

SetSafetyScore gets a reference to the given int64 and assigns it to the SafetyScore field.

### GetSafetyScoreRank

`func (o *OrgSafetyScoresResponseData) GetSafetyScoreRank() int64`

GetSafetyScoreRank returns the SafetyScoreRank field if non-nil, zero value otherwise.

### GetSafetyScoreRankOk

`func (o *OrgSafetyScoresResponseData) GetSafetyScoreRankOk() (int64, bool)`

GetSafetyScoreRankOk returns a tuple with the SafetyScoreRank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSafetyScoreRank

`func (o *OrgSafetyScoresResponseData) HasSafetyScoreRank() bool`

HasSafetyScoreRank returns a boolean if a field has been set.

### SetSafetyScoreRank

`func (o *OrgSafetyScoresResponseData) SetSafetyScoreRank(v int64)`

SetSafetyScoreRank gets a reference to the given int64 and assigns it to the SafetyScoreRank field.

### GetTimeOverSpeedLimitMs

`func (o *OrgSafetyScoresResponseData) GetTimeOverSpeedLimitMs() int64`

GetTimeOverSpeedLimitMs returns the TimeOverSpeedLimitMs field if non-nil, zero value otherwise.

### GetTimeOverSpeedLimitMsOk

`func (o *OrgSafetyScoresResponseData) GetTimeOverSpeedLimitMsOk() (int64, bool)`

GetTimeOverSpeedLimitMsOk returns a tuple with the TimeOverSpeedLimitMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTimeOverSpeedLimitMs

`func (o *OrgSafetyScoresResponseData) HasTimeOverSpeedLimitMs() bool`

HasTimeOverSpeedLimitMs returns a boolean if a field has been set.

### SetTimeOverSpeedLimitMs

`func (o *OrgSafetyScoresResponseData) SetTimeOverSpeedLimitMs(v int64)`

SetTimeOverSpeedLimitMs gets a reference to the given int64 and assigns it to the TimeOverSpeedLimitMs field.

### GetTotalDistanceDrivenMeters

`func (o *OrgSafetyScoresResponseData) GetTotalDistanceDrivenMeters() int64`

GetTotalDistanceDrivenMeters returns the TotalDistanceDrivenMeters field if non-nil, zero value otherwise.

### GetTotalDistanceDrivenMetersOk

`func (o *OrgSafetyScoresResponseData) GetTotalDistanceDrivenMetersOk() (int64, bool)`

GetTotalDistanceDrivenMetersOk returns a tuple with the TotalDistanceDrivenMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTotalDistanceDrivenMeters

`func (o *OrgSafetyScoresResponseData) HasTotalDistanceDrivenMeters() bool`

HasTotalDistanceDrivenMeters returns a boolean if a field has been set.

### SetTotalDistanceDrivenMeters

`func (o *OrgSafetyScoresResponseData) SetTotalDistanceDrivenMeters(v int64)`

SetTotalDistanceDrivenMeters gets a reference to the given int64 and assigns it to the TotalDistanceDrivenMeters field.

### GetTotalHarshEventCount

`func (o *OrgSafetyScoresResponseData) GetTotalHarshEventCount() int64`

GetTotalHarshEventCount returns the TotalHarshEventCount field if non-nil, zero value otherwise.

### GetTotalHarshEventCountOk

`func (o *OrgSafetyScoresResponseData) GetTotalHarshEventCountOk() (int64, bool)`

GetTotalHarshEventCountOk returns a tuple with the TotalHarshEventCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTotalHarshEventCount

`func (o *OrgSafetyScoresResponseData) HasTotalHarshEventCount() bool`

HasTotalHarshEventCount returns a boolean if a field has been set.

### SetTotalHarshEventCount

`func (o *OrgSafetyScoresResponseData) SetTotalHarshEventCount(v int64)`

SetTotalHarshEventCount gets a reference to the given int64 and assigns it to the TotalHarshEventCount field.

### GetTotalTimeDrivenMs

`func (o *OrgSafetyScoresResponseData) GetTotalTimeDrivenMs() int64`

GetTotalTimeDrivenMs returns the TotalTimeDrivenMs field if non-nil, zero value otherwise.

### GetTotalTimeDrivenMsOk

`func (o *OrgSafetyScoresResponseData) GetTotalTimeDrivenMsOk() (int64, bool)`

GetTotalTimeDrivenMsOk returns a tuple with the TotalTimeDrivenMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTotalTimeDrivenMs

`func (o *OrgSafetyScoresResponseData) HasTotalTimeDrivenMs() bool`

HasTotalTimeDrivenMs returns a boolean if a field has been set.

### SetTotalTimeDrivenMs

`func (o *OrgSafetyScoresResponseData) SetTotalTimeDrivenMs(v int64)`

SetTotalTimeDrivenMs gets a reference to the given int64 and assigns it to the TotalTimeDrivenMs field.

### GetVehicleId

`func (o *OrgSafetyScoresResponseData) GetVehicleId() int64`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *OrgSafetyScoresResponseData) GetVehicleIdOk() (int64, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *OrgSafetyScoresResponseData) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *OrgSafetyScoresResponseData) SetVehicleId(v int64)`

SetVehicleId gets a reference to the given int64 and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


