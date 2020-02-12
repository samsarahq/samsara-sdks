# V1HosLogsSummaryResponseDrivers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CurrentDutyStatusCode** | Pointer to **string** | The Hours of Service status type. | [optional] 
**CycleRemaining** | Pointer to **int64** | The amount of remaining cycle time (in ms). | [optional] 
**CycleTomorrow** | Pointer to **int64** | The amount of cycle time (in ms) available tomorrow. | [optional] 
**DriveMsToday** | Pointer to **float32** | The amount of driving time today (in ms). | [optional] 
**DriverId** | Pointer to **int64** | ID of the driver. | [optional] 
**DriverName** | Pointer to **string** | Name of the driver. | [optional] 
**DrivingInViolationCycle** | Pointer to **int64** | The amount of driving time in violation in this cycle (in ms). | [optional] 
**DrivingInViolationToday** | Pointer to **int64** | The amount of driving time in violation today (in ms). | [optional] 
**OnDutyMsToday** | Pointer to **float32** | The amount of on duty time today (in ms). | [optional] 
**PendingDriveMsToday** | Pointer to **float32** | The amount of driving time today for pending logs (in ms). | [optional] 
**PendingOnDutyMsToday** | Pointer to **float32** | The amount of on duty time today for pending logs (in ms). | [optional] 
**ShiftDriveRemaining** | Pointer to **int64** | The amount of remaining shift drive time (in ms). | [optional] 
**ShiftRemaining** | Pointer to **int64** | The amount of remaining shift time (in ms). | [optional] 
**TimeInCurrentStatus** | Pointer to **int64** | The amount of time (in ms) that the driver has been in the current &#x60;dutyStatus&#x60;. | [optional] 
**TimeUntilBreak** | Pointer to **int64** | The amount of time (in ms) remaining until the driver cannot drive without a rest break. | [optional] 
**VehicleName** | Pointer to **string** | Name of the vehicle. | [optional] 

## Methods

### GetCurrentDutyStatusCode

`func (o *V1HosLogsSummaryResponseDrivers) GetCurrentDutyStatusCode() string`

GetCurrentDutyStatusCode returns the CurrentDutyStatusCode field if non-nil, zero value otherwise.

### GetCurrentDutyStatusCodeOk

`func (o *V1HosLogsSummaryResponseDrivers) GetCurrentDutyStatusCodeOk() (string, bool)`

GetCurrentDutyStatusCodeOk returns a tuple with the CurrentDutyStatusCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCurrentDutyStatusCode

`func (o *V1HosLogsSummaryResponseDrivers) HasCurrentDutyStatusCode() bool`

HasCurrentDutyStatusCode returns a boolean if a field has been set.

### SetCurrentDutyStatusCode

`func (o *V1HosLogsSummaryResponseDrivers) SetCurrentDutyStatusCode(v string)`

SetCurrentDutyStatusCode gets a reference to the given string and assigns it to the CurrentDutyStatusCode field.

### GetCycleRemaining

`func (o *V1HosLogsSummaryResponseDrivers) GetCycleRemaining() int64`

GetCycleRemaining returns the CycleRemaining field if non-nil, zero value otherwise.

### GetCycleRemainingOk

`func (o *V1HosLogsSummaryResponseDrivers) GetCycleRemainingOk() (int64, bool)`

GetCycleRemainingOk returns a tuple with the CycleRemaining field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCycleRemaining

`func (o *V1HosLogsSummaryResponseDrivers) HasCycleRemaining() bool`

HasCycleRemaining returns a boolean if a field has been set.

### SetCycleRemaining

`func (o *V1HosLogsSummaryResponseDrivers) SetCycleRemaining(v int64)`

SetCycleRemaining gets a reference to the given int64 and assigns it to the CycleRemaining field.

### GetCycleTomorrow

`func (o *V1HosLogsSummaryResponseDrivers) GetCycleTomorrow() int64`

GetCycleTomorrow returns the CycleTomorrow field if non-nil, zero value otherwise.

### GetCycleTomorrowOk

`func (o *V1HosLogsSummaryResponseDrivers) GetCycleTomorrowOk() (int64, bool)`

GetCycleTomorrowOk returns a tuple with the CycleTomorrow field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCycleTomorrow

`func (o *V1HosLogsSummaryResponseDrivers) HasCycleTomorrow() bool`

HasCycleTomorrow returns a boolean if a field has been set.

### SetCycleTomorrow

`func (o *V1HosLogsSummaryResponseDrivers) SetCycleTomorrow(v int64)`

SetCycleTomorrow gets a reference to the given int64 and assigns it to the CycleTomorrow field.

### GetDriveMsToday

`func (o *V1HosLogsSummaryResponseDrivers) GetDriveMsToday() float32`

GetDriveMsToday returns the DriveMsToday field if non-nil, zero value otherwise.

### GetDriveMsTodayOk

`func (o *V1HosLogsSummaryResponseDrivers) GetDriveMsTodayOk() (float32, bool)`

GetDriveMsTodayOk returns a tuple with the DriveMsToday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriveMsToday

`func (o *V1HosLogsSummaryResponseDrivers) HasDriveMsToday() bool`

HasDriveMsToday returns a boolean if a field has been set.

### SetDriveMsToday

`func (o *V1HosLogsSummaryResponseDrivers) SetDriveMsToday(v float32)`

SetDriveMsToday gets a reference to the given float32 and assigns it to the DriveMsToday field.

### GetDriverId

`func (o *V1HosLogsSummaryResponseDrivers) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1HosLogsSummaryResponseDrivers) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1HosLogsSummaryResponseDrivers) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1HosLogsSummaryResponseDrivers) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetDriverName

`func (o *V1HosLogsSummaryResponseDrivers) GetDriverName() string`

GetDriverName returns the DriverName field if non-nil, zero value otherwise.

### GetDriverNameOk

`func (o *V1HosLogsSummaryResponseDrivers) GetDriverNameOk() (string, bool)`

GetDriverNameOk returns a tuple with the DriverName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverName

`func (o *V1HosLogsSummaryResponseDrivers) HasDriverName() bool`

HasDriverName returns a boolean if a field has been set.

### SetDriverName

`func (o *V1HosLogsSummaryResponseDrivers) SetDriverName(v string)`

SetDriverName gets a reference to the given string and assigns it to the DriverName field.

### GetDrivingInViolationCycle

`func (o *V1HosLogsSummaryResponseDrivers) GetDrivingInViolationCycle() int64`

GetDrivingInViolationCycle returns the DrivingInViolationCycle field if non-nil, zero value otherwise.

### GetDrivingInViolationCycleOk

`func (o *V1HosLogsSummaryResponseDrivers) GetDrivingInViolationCycleOk() (int64, bool)`

GetDrivingInViolationCycleOk returns a tuple with the DrivingInViolationCycle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDrivingInViolationCycle

`func (o *V1HosLogsSummaryResponseDrivers) HasDrivingInViolationCycle() bool`

HasDrivingInViolationCycle returns a boolean if a field has been set.

### SetDrivingInViolationCycle

`func (o *V1HosLogsSummaryResponseDrivers) SetDrivingInViolationCycle(v int64)`

SetDrivingInViolationCycle gets a reference to the given int64 and assigns it to the DrivingInViolationCycle field.

### GetDrivingInViolationToday

`func (o *V1HosLogsSummaryResponseDrivers) GetDrivingInViolationToday() int64`

GetDrivingInViolationToday returns the DrivingInViolationToday field if non-nil, zero value otherwise.

### GetDrivingInViolationTodayOk

`func (o *V1HosLogsSummaryResponseDrivers) GetDrivingInViolationTodayOk() (int64, bool)`

GetDrivingInViolationTodayOk returns a tuple with the DrivingInViolationToday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDrivingInViolationToday

`func (o *V1HosLogsSummaryResponseDrivers) HasDrivingInViolationToday() bool`

HasDrivingInViolationToday returns a boolean if a field has been set.

### SetDrivingInViolationToday

`func (o *V1HosLogsSummaryResponseDrivers) SetDrivingInViolationToday(v int64)`

SetDrivingInViolationToday gets a reference to the given int64 and assigns it to the DrivingInViolationToday field.

### GetOnDutyMsToday

`func (o *V1HosLogsSummaryResponseDrivers) GetOnDutyMsToday() float32`

GetOnDutyMsToday returns the OnDutyMsToday field if non-nil, zero value otherwise.

### GetOnDutyMsTodayOk

`func (o *V1HosLogsSummaryResponseDrivers) GetOnDutyMsTodayOk() (float32, bool)`

GetOnDutyMsTodayOk returns a tuple with the OnDutyMsToday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOnDutyMsToday

`func (o *V1HosLogsSummaryResponseDrivers) HasOnDutyMsToday() bool`

HasOnDutyMsToday returns a boolean if a field has been set.

### SetOnDutyMsToday

`func (o *V1HosLogsSummaryResponseDrivers) SetOnDutyMsToday(v float32)`

SetOnDutyMsToday gets a reference to the given float32 and assigns it to the OnDutyMsToday field.

### GetPendingDriveMsToday

`func (o *V1HosLogsSummaryResponseDrivers) GetPendingDriveMsToday() float32`

GetPendingDriveMsToday returns the PendingDriveMsToday field if non-nil, zero value otherwise.

### GetPendingDriveMsTodayOk

`func (o *V1HosLogsSummaryResponseDrivers) GetPendingDriveMsTodayOk() (float32, bool)`

GetPendingDriveMsTodayOk returns a tuple with the PendingDriveMsToday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPendingDriveMsToday

`func (o *V1HosLogsSummaryResponseDrivers) HasPendingDriveMsToday() bool`

HasPendingDriveMsToday returns a boolean if a field has been set.

### SetPendingDriveMsToday

`func (o *V1HosLogsSummaryResponseDrivers) SetPendingDriveMsToday(v float32)`

SetPendingDriveMsToday gets a reference to the given float32 and assigns it to the PendingDriveMsToday field.

### GetPendingOnDutyMsToday

`func (o *V1HosLogsSummaryResponseDrivers) GetPendingOnDutyMsToday() float32`

GetPendingOnDutyMsToday returns the PendingOnDutyMsToday field if non-nil, zero value otherwise.

### GetPendingOnDutyMsTodayOk

`func (o *V1HosLogsSummaryResponseDrivers) GetPendingOnDutyMsTodayOk() (float32, bool)`

GetPendingOnDutyMsTodayOk returns a tuple with the PendingOnDutyMsToday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPendingOnDutyMsToday

`func (o *V1HosLogsSummaryResponseDrivers) HasPendingOnDutyMsToday() bool`

HasPendingOnDutyMsToday returns a boolean if a field has been set.

### SetPendingOnDutyMsToday

`func (o *V1HosLogsSummaryResponseDrivers) SetPendingOnDutyMsToday(v float32)`

SetPendingOnDutyMsToday gets a reference to the given float32 and assigns it to the PendingOnDutyMsToday field.

### GetShiftDriveRemaining

`func (o *V1HosLogsSummaryResponseDrivers) GetShiftDriveRemaining() int64`

GetShiftDriveRemaining returns the ShiftDriveRemaining field if non-nil, zero value otherwise.

### GetShiftDriveRemainingOk

`func (o *V1HosLogsSummaryResponseDrivers) GetShiftDriveRemainingOk() (int64, bool)`

GetShiftDriveRemainingOk returns a tuple with the ShiftDriveRemaining field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasShiftDriveRemaining

`func (o *V1HosLogsSummaryResponseDrivers) HasShiftDriveRemaining() bool`

HasShiftDriveRemaining returns a boolean if a field has been set.

### SetShiftDriveRemaining

`func (o *V1HosLogsSummaryResponseDrivers) SetShiftDriveRemaining(v int64)`

SetShiftDriveRemaining gets a reference to the given int64 and assigns it to the ShiftDriveRemaining field.

### GetShiftRemaining

`func (o *V1HosLogsSummaryResponseDrivers) GetShiftRemaining() int64`

GetShiftRemaining returns the ShiftRemaining field if non-nil, zero value otherwise.

### GetShiftRemainingOk

`func (o *V1HosLogsSummaryResponseDrivers) GetShiftRemainingOk() (int64, bool)`

GetShiftRemainingOk returns a tuple with the ShiftRemaining field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasShiftRemaining

`func (o *V1HosLogsSummaryResponseDrivers) HasShiftRemaining() bool`

HasShiftRemaining returns a boolean if a field has been set.

### SetShiftRemaining

`func (o *V1HosLogsSummaryResponseDrivers) SetShiftRemaining(v int64)`

SetShiftRemaining gets a reference to the given int64 and assigns it to the ShiftRemaining field.

### GetTimeInCurrentStatus

`func (o *V1HosLogsSummaryResponseDrivers) GetTimeInCurrentStatus() int64`

GetTimeInCurrentStatus returns the TimeInCurrentStatus field if non-nil, zero value otherwise.

### GetTimeInCurrentStatusOk

`func (o *V1HosLogsSummaryResponseDrivers) GetTimeInCurrentStatusOk() (int64, bool)`

GetTimeInCurrentStatusOk returns a tuple with the TimeInCurrentStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTimeInCurrentStatus

`func (o *V1HosLogsSummaryResponseDrivers) HasTimeInCurrentStatus() bool`

HasTimeInCurrentStatus returns a boolean if a field has been set.

### SetTimeInCurrentStatus

`func (o *V1HosLogsSummaryResponseDrivers) SetTimeInCurrentStatus(v int64)`

SetTimeInCurrentStatus gets a reference to the given int64 and assigns it to the TimeInCurrentStatus field.

### GetTimeUntilBreak

`func (o *V1HosLogsSummaryResponseDrivers) GetTimeUntilBreak() int64`

GetTimeUntilBreak returns the TimeUntilBreak field if non-nil, zero value otherwise.

### GetTimeUntilBreakOk

`func (o *V1HosLogsSummaryResponseDrivers) GetTimeUntilBreakOk() (int64, bool)`

GetTimeUntilBreakOk returns a tuple with the TimeUntilBreak field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTimeUntilBreak

`func (o *V1HosLogsSummaryResponseDrivers) HasTimeUntilBreak() bool`

HasTimeUntilBreak returns a boolean if a field has been set.

### SetTimeUntilBreak

`func (o *V1HosLogsSummaryResponseDrivers) SetTimeUntilBreak(v int64)`

SetTimeUntilBreak gets a reference to the given int64 and assigns it to the TimeUntilBreak field.

### GetVehicleName

`func (o *V1HosLogsSummaryResponseDrivers) GetVehicleName() string`

GetVehicleName returns the VehicleName field if non-nil, zero value otherwise.

### GetVehicleNameOk

`func (o *V1HosLogsSummaryResponseDrivers) GetVehicleNameOk() (string, bool)`

GetVehicleNameOk returns a tuple with the VehicleName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleName

`func (o *V1HosLogsSummaryResponseDrivers) HasVehicleName() bool`

HasVehicleName returns a boolean if a field has been set.

### SetVehicleName

`func (o *V1HosLogsSummaryResponseDrivers) SetVehicleName(v string)`

SetVehicleName gets a reference to the given string and assigns it to the VehicleName field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


