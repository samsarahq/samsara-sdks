# V1HosLogsResponseLogs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CodriverIds** | Pointer to **[]float32** |  | [optional] 
**DriverId** | Pointer to **int64** | ID of the driver. | [optional] 
**GroupId** | Pointer to **int64** | Deprecated. | [optional] 
**HosStatusType** | Pointer to **string** | The Hours of Service status type. One of &#x60;OFF_DUTY&#x60;, &#x60;SLEEPER_BED&#x60;, &#x60;DRIVING&#x60;, &#x60;ON_DUTY&#x60;, &#x60;YARD_MOVE&#x60;, &#x60;PERSONAL_CONVEYANCE&#x60;. | [optional] 
**LocCity** | Pointer to **string** | City in which the log was recorded. | [optional] 
**LocLat** | Pointer to **float32** | Latitude at which the log was recorded. | [optional] 
**LocLng** | Pointer to **float32** | Longitude at which the log was recorded. | [optional] 
**LocName** | Pointer to **string** | Name of location at which the log was recorded. | [optional] 
**LocState** | Pointer to **string** | State in which the log was recorded. | [optional] 
**LogStartMs** | Pointer to **int64** | The time at which the log/HOS status started in UNIX milliseconds. | [optional] 
**Remark** | Pointer to **string** | Remark associated with the log entry. | [optional] 
**VehicleId** | Pointer to **int64** | ID of the vehicle. | [optional] 

## Methods

### GetCodriverIds

`func (o *V1HosLogsResponseLogs) GetCodriverIds() []float32`

GetCodriverIds returns the CodriverIds field if non-nil, zero value otherwise.

### GetCodriverIdsOk

`func (o *V1HosLogsResponseLogs) GetCodriverIdsOk() ([]float32, bool)`

GetCodriverIdsOk returns a tuple with the CodriverIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCodriverIds

`func (o *V1HosLogsResponseLogs) HasCodriverIds() bool`

HasCodriverIds returns a boolean if a field has been set.

### SetCodriverIds

`func (o *V1HosLogsResponseLogs) SetCodriverIds(v []float32)`

SetCodriverIds gets a reference to the given []float32 and assigns it to the CodriverIds field.

### GetDriverId

`func (o *V1HosLogsResponseLogs) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1HosLogsResponseLogs) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1HosLogsResponseLogs) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1HosLogsResponseLogs) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetGroupId

`func (o *V1HosLogsResponseLogs) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *V1HosLogsResponseLogs) GetGroupIdOk() (int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGroupId

`func (o *V1HosLogsResponseLogs) HasGroupId() bool`

HasGroupId returns a boolean if a field has been set.

### SetGroupId

`func (o *V1HosLogsResponseLogs) SetGroupId(v int64)`

SetGroupId gets a reference to the given int64 and assigns it to the GroupId field.

### GetHosStatusType

`func (o *V1HosLogsResponseLogs) GetHosStatusType() string`

GetHosStatusType returns the HosStatusType field if non-nil, zero value otherwise.

### GetHosStatusTypeOk

`func (o *V1HosLogsResponseLogs) GetHosStatusTypeOk() (string, bool)`

GetHosStatusTypeOk returns a tuple with the HosStatusType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHosStatusType

`func (o *V1HosLogsResponseLogs) HasHosStatusType() bool`

HasHosStatusType returns a boolean if a field has been set.

### SetHosStatusType

`func (o *V1HosLogsResponseLogs) SetHosStatusType(v string)`

SetHosStatusType gets a reference to the given string and assigns it to the HosStatusType field.

### GetLocCity

`func (o *V1HosLogsResponseLogs) GetLocCity() string`

GetLocCity returns the LocCity field if non-nil, zero value otherwise.

### GetLocCityOk

`func (o *V1HosLogsResponseLogs) GetLocCityOk() (string, bool)`

GetLocCityOk returns a tuple with the LocCity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocCity

`func (o *V1HosLogsResponseLogs) HasLocCity() bool`

HasLocCity returns a boolean if a field has been set.

### SetLocCity

`func (o *V1HosLogsResponseLogs) SetLocCity(v string)`

SetLocCity gets a reference to the given string and assigns it to the LocCity field.

### GetLocLat

`func (o *V1HosLogsResponseLogs) GetLocLat() float32`

GetLocLat returns the LocLat field if non-nil, zero value otherwise.

### GetLocLatOk

`func (o *V1HosLogsResponseLogs) GetLocLatOk() (float32, bool)`

GetLocLatOk returns a tuple with the LocLat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocLat

`func (o *V1HosLogsResponseLogs) HasLocLat() bool`

HasLocLat returns a boolean if a field has been set.

### SetLocLat

`func (o *V1HosLogsResponseLogs) SetLocLat(v float32)`

SetLocLat gets a reference to the given float32 and assigns it to the LocLat field.

### GetLocLng

`func (o *V1HosLogsResponseLogs) GetLocLng() float32`

GetLocLng returns the LocLng field if non-nil, zero value otherwise.

### GetLocLngOk

`func (o *V1HosLogsResponseLogs) GetLocLngOk() (float32, bool)`

GetLocLngOk returns a tuple with the LocLng field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocLng

`func (o *V1HosLogsResponseLogs) HasLocLng() bool`

HasLocLng returns a boolean if a field has been set.

### SetLocLng

`func (o *V1HosLogsResponseLogs) SetLocLng(v float32)`

SetLocLng gets a reference to the given float32 and assigns it to the LocLng field.

### GetLocName

`func (o *V1HosLogsResponseLogs) GetLocName() string`

GetLocName returns the LocName field if non-nil, zero value otherwise.

### GetLocNameOk

`func (o *V1HosLogsResponseLogs) GetLocNameOk() (string, bool)`

GetLocNameOk returns a tuple with the LocName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocName

`func (o *V1HosLogsResponseLogs) HasLocName() bool`

HasLocName returns a boolean if a field has been set.

### SetLocName

`func (o *V1HosLogsResponseLogs) SetLocName(v string)`

SetLocName gets a reference to the given string and assigns it to the LocName field.

### GetLocState

`func (o *V1HosLogsResponseLogs) GetLocState() string`

GetLocState returns the LocState field if non-nil, zero value otherwise.

### GetLocStateOk

`func (o *V1HosLogsResponseLogs) GetLocStateOk() (string, bool)`

GetLocStateOk returns a tuple with the LocState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocState

`func (o *V1HosLogsResponseLogs) HasLocState() bool`

HasLocState returns a boolean if a field has been set.

### SetLocState

`func (o *V1HosLogsResponseLogs) SetLocState(v string)`

SetLocState gets a reference to the given string and assigns it to the LocState field.

### GetLogStartMs

`func (o *V1HosLogsResponseLogs) GetLogStartMs() int64`

GetLogStartMs returns the LogStartMs field if non-nil, zero value otherwise.

### GetLogStartMsOk

`func (o *V1HosLogsResponseLogs) GetLogStartMsOk() (int64, bool)`

GetLogStartMsOk returns a tuple with the LogStartMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLogStartMs

`func (o *V1HosLogsResponseLogs) HasLogStartMs() bool`

HasLogStartMs returns a boolean if a field has been set.

### SetLogStartMs

`func (o *V1HosLogsResponseLogs) SetLogStartMs(v int64)`

SetLogStartMs gets a reference to the given int64 and assigns it to the LogStartMs field.

### GetRemark

`func (o *V1HosLogsResponseLogs) GetRemark() string`

GetRemark returns the Remark field if non-nil, zero value otherwise.

### GetRemarkOk

`func (o *V1HosLogsResponseLogs) GetRemarkOk() (string, bool)`

GetRemarkOk returns a tuple with the Remark field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRemark

`func (o *V1HosLogsResponseLogs) HasRemark() bool`

HasRemark returns a boolean if a field has been set.

### SetRemark

`func (o *V1HosLogsResponseLogs) SetRemark(v string)`

SetRemark gets a reference to the given string and assigns it to the Remark field.

### GetVehicleId

`func (o *V1HosLogsResponseLogs) GetVehicleId() int64`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1HosLogsResponseLogs) GetVehicleIdOk() (int64, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1HosLogsResponseLogs) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1HosLogsResponseLogs) SetVehicleId(v int64)`

SetVehicleId gets a reference to the given int64 and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


