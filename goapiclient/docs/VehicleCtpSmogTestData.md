# VehicleCtpSmogTestData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CommProtocol** | Pointer to **string** | CAN bus communication protocol as detected by the vehicle gateway. | [optional] 
**DeviceFirmware** | Pointer to **string** | CTP firmware version as reported by the vehicle gateway. | [optional] 
**DlcPinVoltageMilliVolts** | Pointer to **int32** | Positive battery voltage as detected by the vehicle gateway reported in millivolts. | [optional] 
**DlcPinVoltageMilliVoltsValid** | Pointer to **bool** | Indicates DlcPinVoltageMilliVolts was successfully read from the CAN bus. | [optional] 
**LinkId** | Pointer to **string** | Device serial number. | [optional] 
**RemoteObdTestRecords** | Pointer to [**[]RemoteObdTestRecords**](RemoteObdTestRecords.md) | Contains all of the specific OBD data collected for a single ECU present on a vehicle. There can can be multiple ECUs on a vehicle. | [optional] 
**TestDateTime** | Pointer to **string** | UTC timestamp in RFC 3339 milliseconds format. | [optional] 

## Methods

### GetCommProtocol

`func (o *VehicleCtpSmogTestData) GetCommProtocol() string`

GetCommProtocol returns the CommProtocol field if non-nil, zero value otherwise.

### GetCommProtocolOk

`func (o *VehicleCtpSmogTestData) GetCommProtocolOk() (string, bool)`

GetCommProtocolOk returns a tuple with the CommProtocol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCommProtocol

`func (o *VehicleCtpSmogTestData) HasCommProtocol() bool`

HasCommProtocol returns a boolean if a field has been set.

### SetCommProtocol

`func (o *VehicleCtpSmogTestData) SetCommProtocol(v string)`

SetCommProtocol gets a reference to the given string and assigns it to the CommProtocol field.

### GetDeviceFirmware

`func (o *VehicleCtpSmogTestData) GetDeviceFirmware() string`

GetDeviceFirmware returns the DeviceFirmware field if non-nil, zero value otherwise.

### GetDeviceFirmwareOk

`func (o *VehicleCtpSmogTestData) GetDeviceFirmwareOk() (string, bool)`

GetDeviceFirmwareOk returns a tuple with the DeviceFirmware field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDeviceFirmware

`func (o *VehicleCtpSmogTestData) HasDeviceFirmware() bool`

HasDeviceFirmware returns a boolean if a field has been set.

### SetDeviceFirmware

`func (o *VehicleCtpSmogTestData) SetDeviceFirmware(v string)`

SetDeviceFirmware gets a reference to the given string and assigns it to the DeviceFirmware field.

### GetDlcPinVoltageMilliVolts

`func (o *VehicleCtpSmogTestData) GetDlcPinVoltageMilliVolts() int32`

GetDlcPinVoltageMilliVolts returns the DlcPinVoltageMilliVolts field if non-nil, zero value otherwise.

### GetDlcPinVoltageMilliVoltsOk

`func (o *VehicleCtpSmogTestData) GetDlcPinVoltageMilliVoltsOk() (int32, bool)`

GetDlcPinVoltageMilliVoltsOk returns a tuple with the DlcPinVoltageMilliVolts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDlcPinVoltageMilliVolts

`func (o *VehicleCtpSmogTestData) HasDlcPinVoltageMilliVolts() bool`

HasDlcPinVoltageMilliVolts returns a boolean if a field has been set.

### SetDlcPinVoltageMilliVolts

`func (o *VehicleCtpSmogTestData) SetDlcPinVoltageMilliVolts(v int32)`

SetDlcPinVoltageMilliVolts gets a reference to the given int32 and assigns it to the DlcPinVoltageMilliVolts field.

### GetDlcPinVoltageMilliVoltsValid

`func (o *VehicleCtpSmogTestData) GetDlcPinVoltageMilliVoltsValid() bool`

GetDlcPinVoltageMilliVoltsValid returns the DlcPinVoltageMilliVoltsValid field if non-nil, zero value otherwise.

### GetDlcPinVoltageMilliVoltsValidOk

`func (o *VehicleCtpSmogTestData) GetDlcPinVoltageMilliVoltsValidOk() (bool, bool)`

GetDlcPinVoltageMilliVoltsValidOk returns a tuple with the DlcPinVoltageMilliVoltsValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDlcPinVoltageMilliVoltsValid

`func (o *VehicleCtpSmogTestData) HasDlcPinVoltageMilliVoltsValid() bool`

HasDlcPinVoltageMilliVoltsValid returns a boolean if a field has been set.

### SetDlcPinVoltageMilliVoltsValid

`func (o *VehicleCtpSmogTestData) SetDlcPinVoltageMilliVoltsValid(v bool)`

SetDlcPinVoltageMilliVoltsValid gets a reference to the given bool and assigns it to the DlcPinVoltageMilliVoltsValid field.

### GetLinkId

`func (o *VehicleCtpSmogTestData) GetLinkId() string`

GetLinkId returns the LinkId field if non-nil, zero value otherwise.

### GetLinkIdOk

`func (o *VehicleCtpSmogTestData) GetLinkIdOk() (string, bool)`

GetLinkIdOk returns a tuple with the LinkId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLinkId

`func (o *VehicleCtpSmogTestData) HasLinkId() bool`

HasLinkId returns a boolean if a field has been set.

### SetLinkId

`func (o *VehicleCtpSmogTestData) SetLinkId(v string)`

SetLinkId gets a reference to the given string and assigns it to the LinkId field.

### GetRemoteObdTestRecords

`func (o *VehicleCtpSmogTestData) GetRemoteObdTestRecords() []RemoteObdTestRecords`

GetRemoteObdTestRecords returns the RemoteObdTestRecords field if non-nil, zero value otherwise.

### GetRemoteObdTestRecordsOk

`func (o *VehicleCtpSmogTestData) GetRemoteObdTestRecordsOk() ([]RemoteObdTestRecords, bool)`

GetRemoteObdTestRecordsOk returns a tuple with the RemoteObdTestRecords field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRemoteObdTestRecords

`func (o *VehicleCtpSmogTestData) HasRemoteObdTestRecords() bool`

HasRemoteObdTestRecords returns a boolean if a field has been set.

### SetRemoteObdTestRecords

`func (o *VehicleCtpSmogTestData) SetRemoteObdTestRecords(v []RemoteObdTestRecords)`

SetRemoteObdTestRecords gets a reference to the given []RemoteObdTestRecords and assigns it to the RemoteObdTestRecords field.

### GetTestDateTime

`func (o *VehicleCtpSmogTestData) GetTestDateTime() string`

GetTestDateTime returns the TestDateTime field if non-nil, zero value otherwise.

### GetTestDateTimeOk

`func (o *VehicleCtpSmogTestData) GetTestDateTimeOk() (string, bool)`

GetTestDateTimeOk returns a tuple with the TestDateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTestDateTime

`func (o *VehicleCtpSmogTestData) HasTestDateTime() bool`

HasTestDateTime returns a boolean if a field has been set.

### SetTestDateTime

`func (o *VehicleCtpSmogTestData) SetTestDateTime(v string)`

SetTestDateTime gets a reference to the given string and assigns it to the TestDateTime field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


