# VehicleStatsCtpSmogTestData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CommProtocol** | Pointer to **string** | CAN bus communication protocol as detected by the vehicle gateway. | [optional] 
**DeviceFirmware** | Pointer to **string** | CTP firmware version as reported by the vehicle gateway. | [optional] 
**DlcPinVoltageMilliVolts** | Pointer to **int32** | Positive battery voltage as detected by the vehicle gateway reported in millivolts. | [optional] 
**DlcPinVoltageMilliVoltsValid** | Pointer to **bool** | Indicates DlcPinVoltageMilliVolts was successfully read from the CAN bus. | [optional] 
**LinkId** | Pointer to **int32** | Device serial number. | [optional] 
**RemoteObdTestRecords** | Pointer to [**[]RemoteObdTestRecordType**](RemoteObdTestRecordType.md) | Contains all of the specific OBD data collected for a single ECU present on a vehicle. There can can be multiple ECUs on a vehicle. | [optional] 
**TestDateTime** | Pointer to [**time.Time**](time.Time.md) | UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 

## Methods

### GetCommProtocol

`func (o *VehicleStatsCtpSmogTestData) GetCommProtocol() string`

GetCommProtocol returns the CommProtocol field if non-nil, zero value otherwise.

### GetCommProtocolOk

`func (o *VehicleStatsCtpSmogTestData) GetCommProtocolOk() (string, bool)`

GetCommProtocolOk returns a tuple with the CommProtocol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCommProtocol

`func (o *VehicleStatsCtpSmogTestData) HasCommProtocol() bool`

HasCommProtocol returns a boolean if a field has been set.

### SetCommProtocol

`func (o *VehicleStatsCtpSmogTestData) SetCommProtocol(v string)`

SetCommProtocol gets a reference to the given string and assigns it to the CommProtocol field.

### GetDeviceFirmware

`func (o *VehicleStatsCtpSmogTestData) GetDeviceFirmware() string`

GetDeviceFirmware returns the DeviceFirmware field if non-nil, zero value otherwise.

### GetDeviceFirmwareOk

`func (o *VehicleStatsCtpSmogTestData) GetDeviceFirmwareOk() (string, bool)`

GetDeviceFirmwareOk returns a tuple with the DeviceFirmware field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDeviceFirmware

`func (o *VehicleStatsCtpSmogTestData) HasDeviceFirmware() bool`

HasDeviceFirmware returns a boolean if a field has been set.

### SetDeviceFirmware

`func (o *VehicleStatsCtpSmogTestData) SetDeviceFirmware(v string)`

SetDeviceFirmware gets a reference to the given string and assigns it to the DeviceFirmware field.

### GetDlcPinVoltageMilliVolts

`func (o *VehicleStatsCtpSmogTestData) GetDlcPinVoltageMilliVolts() int32`

GetDlcPinVoltageMilliVolts returns the DlcPinVoltageMilliVolts field if non-nil, zero value otherwise.

### GetDlcPinVoltageMilliVoltsOk

`func (o *VehicleStatsCtpSmogTestData) GetDlcPinVoltageMilliVoltsOk() (int32, bool)`

GetDlcPinVoltageMilliVoltsOk returns a tuple with the DlcPinVoltageMilliVolts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDlcPinVoltageMilliVolts

`func (o *VehicleStatsCtpSmogTestData) HasDlcPinVoltageMilliVolts() bool`

HasDlcPinVoltageMilliVolts returns a boolean if a field has been set.

### SetDlcPinVoltageMilliVolts

`func (o *VehicleStatsCtpSmogTestData) SetDlcPinVoltageMilliVolts(v int32)`

SetDlcPinVoltageMilliVolts gets a reference to the given int32 and assigns it to the DlcPinVoltageMilliVolts field.

### GetDlcPinVoltageMilliVoltsValid

`func (o *VehicleStatsCtpSmogTestData) GetDlcPinVoltageMilliVoltsValid() bool`

GetDlcPinVoltageMilliVoltsValid returns the DlcPinVoltageMilliVoltsValid field if non-nil, zero value otherwise.

### GetDlcPinVoltageMilliVoltsValidOk

`func (o *VehicleStatsCtpSmogTestData) GetDlcPinVoltageMilliVoltsValidOk() (bool, bool)`

GetDlcPinVoltageMilliVoltsValidOk returns a tuple with the DlcPinVoltageMilliVoltsValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDlcPinVoltageMilliVoltsValid

`func (o *VehicleStatsCtpSmogTestData) HasDlcPinVoltageMilliVoltsValid() bool`

HasDlcPinVoltageMilliVoltsValid returns a boolean if a field has been set.

### SetDlcPinVoltageMilliVoltsValid

`func (o *VehicleStatsCtpSmogTestData) SetDlcPinVoltageMilliVoltsValid(v bool)`

SetDlcPinVoltageMilliVoltsValid gets a reference to the given bool and assigns it to the DlcPinVoltageMilliVoltsValid field.

### GetLinkId

`func (o *VehicleStatsCtpSmogTestData) GetLinkId() int32`

GetLinkId returns the LinkId field if non-nil, zero value otherwise.

### GetLinkIdOk

`func (o *VehicleStatsCtpSmogTestData) GetLinkIdOk() (int32, bool)`

GetLinkIdOk returns a tuple with the LinkId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLinkId

`func (o *VehicleStatsCtpSmogTestData) HasLinkId() bool`

HasLinkId returns a boolean if a field has been set.

### SetLinkId

`func (o *VehicleStatsCtpSmogTestData) SetLinkId(v int32)`

SetLinkId gets a reference to the given int32 and assigns it to the LinkId field.

### GetRemoteObdTestRecords

`func (o *VehicleStatsCtpSmogTestData) GetRemoteObdTestRecords() []RemoteObdTestRecordType`

GetRemoteObdTestRecords returns the RemoteObdTestRecords field if non-nil, zero value otherwise.

### GetRemoteObdTestRecordsOk

`func (o *VehicleStatsCtpSmogTestData) GetRemoteObdTestRecordsOk() ([]RemoteObdTestRecordType, bool)`

GetRemoteObdTestRecordsOk returns a tuple with the RemoteObdTestRecords field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRemoteObdTestRecords

`func (o *VehicleStatsCtpSmogTestData) HasRemoteObdTestRecords() bool`

HasRemoteObdTestRecords returns a boolean if a field has been set.

### SetRemoteObdTestRecords

`func (o *VehicleStatsCtpSmogTestData) SetRemoteObdTestRecords(v []RemoteObdTestRecordType)`

SetRemoteObdTestRecords gets a reference to the given []RemoteObdTestRecordType and assigns it to the RemoteObdTestRecords field.

### GetTestDateTime

`func (o *VehicleStatsCtpSmogTestData) GetTestDateTime() time.Time`

GetTestDateTime returns the TestDateTime field if non-nil, zero value otherwise.

### GetTestDateTimeOk

`func (o *VehicleStatsCtpSmogTestData) GetTestDateTimeOk() (time.Time, bool)`

GetTestDateTimeOk returns a tuple with the TestDateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTestDateTime

`func (o *VehicleStatsCtpSmogTestData) HasTestDateTime() bool`

HasTestDateTime returns a boolean if a field has been set.

### SetTestDateTime

`func (o *VehicleStatsCtpSmogTestData) SetTestDateTime(v time.Time)`

SetTestDateTime gets a reference to the given time.Time and assigns it to the TestDateTime field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


