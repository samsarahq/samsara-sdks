# RemoteObdTestRecordType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CalCvn** | Pointer to **string** | Calibration Verification Number as read from the CAN bus. | [optional] 
**CalCvnValid** | Pointer to **bool** | Indicates CalCvnCount was successfully read from the CAN bus. | [optional] 
**CalId** | Pointer to **string** | Calibration ID as read from the CAN bus. | [optional] 
**CalIdValid** | Pointer to **bool** | Indicates CalId was successfully read from the CAN bus. | [optional] 
**Catalyst** | Pointer to **string** | OBD Monitor Status - Catalyst or NMHC Catalyst as read from the CAN bus. | [optional] 
**Comprehensive** | Pointer to **string** | OBD Monitor Status - Comprehensive as read from the CAN bus. | [optional] 
**CompressionIgnitionMonitorSupported** | Pointer to **string** | Compression ignition monitor supported as read from the CAN bus. | [optional] 
**CompressionIgnitionMonitorSupportedValid** | Pointer to **bool** | Indicates CompressionIgnitionMonitorSupported was successfully read from the CAN bus. | [optional] 
**DistanceTraveledSinceCodesCleared** | Pointer to **int32** | Distance Traveled Since Codes Cleared as read from the CAN bus. | [optional] 
**DistanceTraveledSinceCodesClearedValid** | Pointer to **bool** | Indicates DistanceTraveledSinceCodesCleared was successfully read from the CAN bus. | [optional] 
**DistanceTraveledWithMilOn** | Pointer to **int32** | Distance Traveled With MIL On as read from the CAN bus. | [optional] 
**DistanceTraveledWithMilOnValid** | Pointer to **bool** | Indicates DistanceTraveledWithMilOn was successfully read from the CAN bus. | [optional] 
**DtcCount** | Pointer to **int32** | Number of emissions related DTCs read from the CAN bus. | [optional] 
**Egr** | Pointer to **string** | OBD Monitor Status - EGR/VVT as read from the CAN bus. | [optional] 
**EmissionRelatedDtcs** | Pointer to **string** | Emission related DTCs as read from the CAN bus, separated by pipe characters. | [optional] 
**EmissionRelatedDtcsValid** | Pointer to **bool** | Indicates EmissionRelatedDtcs was successfully read from the CAN bus. | [optional] 
**EvapSystem** | Pointer to **string** | OBD Monitor Status - Evaporative System or ISO/SAE Reserved as read from the CAN bus. | [optional] 
**Fuel** | Pointer to **string** | OBD Monitor Status - Fuel as read from the CAN bus. | [optional] 
**HeatedCatalyst** | Pointer to **string** | OBD Monitor Status - Heated Catalyst or NOx/SCR aftertreatment as read from the CAN bus. | [optional] 
**HeatedO2Sensor** | Pointer to **string** | OBD Monitor Status - Oxygen Sensor Heater or PM Filter as read from the CAN bus. | [optional] 
**IsoSaeReserved** | Pointer to **string** | OBD Monitor Status - ISO/SAE Reserved as read from the CAN bus. | [optional] 
**Mil** | Pointer to **string** | Malfunction indicator lamp status as read from the CAN bus. | [optional] 
**MilValid** | Pointer to **bool** | Indicates Mil was successfully read from the CAN bus. | [optional] 
**MinutesSinceCodesCleared** | Pointer to **int32** | Minutes Since Codes Cleared as read from the CAN bus. | [optional] 
**MinutesSinceCodesClearedValid** | Pointer to **bool** | Indicates MinutesSinceCodesCleared was successfully read from the CAN bus. | [optional] 
**MinutesSinceMil** | Pointer to **int32** | Minutes Since MIL On as read from the CAN bus. | [optional] 
**MinutesSinceMilValid** | Pointer to **bool** | Indicates MinutesSinceMil was successfully read from the CAN bus. | [optional] 
**Misfire** | Pointer to **string** | OBD Monitor Status - Misfire as read from the CAN bus. | [optional] 
**NotReadyCount** | Pointer to **int32** | Number of OBD Monitor Statuses reporting &#39;Supported and not ready&#39;. | [optional] 
**O2Sensor** | Pointer to **string** | OBD Monitor Status - Oxygen Sensor or Exhaust Gas Sensor as read from the CAN bus. | [optional] 
**ObdMonitorStatusValid** | Pointer to **bool** | Indicates Obd Monitor Statuses were successfully read from the CAN bus. | [optional] 
**ObdVin** | Pointer to **string** | Vehicle identification number as read from the CAN bus. | [optional] 
**ObdVinValid** | Pointer to **bool** | Indicates ObdVin was successfully read from the CAN bus. | [optional] 
**PcmId** | Pointer to **string** | ECU Address for the ECU that was read from the CAN bus. | [optional] 
**PendingDtcCount** | Pointer to **int32** | Number of pending DTCs read from the CAN bus. | [optional] 
**PendingDtcs** | Pointer to **string** | Pending DTCs as read from the CAN bus, separated by pipe characters. | [optional] 
**PendingDtcsValid** | Pointer to **bool** | Indicates PendingDtcs was successfully read from the CAN bus. | [optional] 
**PermanentDtcCount** | Pointer to **int32** | Number of permanent DTCs read from the CAN bus. | [optional] 
**PermanentDtcs** | Pointer to **string** | Permanent DTCs as read from the CAN bus, separated by pipe characters. | [optional] 
**PermanentDtcsValid** | Pointer to **bool** | Indicates PermanentDtcs was successfully read from the CAN bus. | [optional] 
**PidCount** | Pointer to **int32** | PidCount is a count of all PIDs supported for this control module as read from the CAN bus | [optional] 
**PidCountValid** | Pointer to **bool** | Indicates PidCount was successfully read from the CAN bus. | [optional] 
**Rpm** | Pointer to **int32** | Revolutions per minute as read from the CAN bus. | [optional] 
**RpmValid** | Pointer to **bool** | Indicates Rpm was successfully read from the CAN bus. | [optional] 
**SecondaryAir** | Pointer to **string** | OBD Monitor Status - Secondary Air System or Boost Pressure System as read from the CAN bus. | [optional] 
**WarmupsSinceCodesCleared** | Pointer to **int32** | Warmups Since Codes Cleared as read from the CAN bus. | [optional] 
**WarmupsSinceCodesClearedValid** | Pointer to **bool** | Indicates WarmupsSinceCodesCleared was successfully read from the CAN bus. | [optional] 

## Methods

### GetCalCvn

`func (o *RemoteObdTestRecordType) GetCalCvn() string`

GetCalCvn returns the CalCvn field if non-nil, zero value otherwise.

### GetCalCvnOk

`func (o *RemoteObdTestRecordType) GetCalCvnOk() (string, bool)`

GetCalCvnOk returns a tuple with the CalCvn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCalCvn

`func (o *RemoteObdTestRecordType) HasCalCvn() bool`

HasCalCvn returns a boolean if a field has been set.

### SetCalCvn

`func (o *RemoteObdTestRecordType) SetCalCvn(v string)`

SetCalCvn gets a reference to the given string and assigns it to the CalCvn field.

### GetCalCvnValid

`func (o *RemoteObdTestRecordType) GetCalCvnValid() bool`

GetCalCvnValid returns the CalCvnValid field if non-nil, zero value otherwise.

### GetCalCvnValidOk

`func (o *RemoteObdTestRecordType) GetCalCvnValidOk() (bool, bool)`

GetCalCvnValidOk returns a tuple with the CalCvnValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCalCvnValid

`func (o *RemoteObdTestRecordType) HasCalCvnValid() bool`

HasCalCvnValid returns a boolean if a field has been set.

### SetCalCvnValid

`func (o *RemoteObdTestRecordType) SetCalCvnValid(v bool)`

SetCalCvnValid gets a reference to the given bool and assigns it to the CalCvnValid field.

### GetCalId

`func (o *RemoteObdTestRecordType) GetCalId() string`

GetCalId returns the CalId field if non-nil, zero value otherwise.

### GetCalIdOk

`func (o *RemoteObdTestRecordType) GetCalIdOk() (string, bool)`

GetCalIdOk returns a tuple with the CalId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCalId

`func (o *RemoteObdTestRecordType) HasCalId() bool`

HasCalId returns a boolean if a field has been set.

### SetCalId

`func (o *RemoteObdTestRecordType) SetCalId(v string)`

SetCalId gets a reference to the given string and assigns it to the CalId field.

### GetCalIdValid

`func (o *RemoteObdTestRecordType) GetCalIdValid() bool`

GetCalIdValid returns the CalIdValid field if non-nil, zero value otherwise.

### GetCalIdValidOk

`func (o *RemoteObdTestRecordType) GetCalIdValidOk() (bool, bool)`

GetCalIdValidOk returns a tuple with the CalIdValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCalIdValid

`func (o *RemoteObdTestRecordType) HasCalIdValid() bool`

HasCalIdValid returns a boolean if a field has been set.

### SetCalIdValid

`func (o *RemoteObdTestRecordType) SetCalIdValid(v bool)`

SetCalIdValid gets a reference to the given bool and assigns it to the CalIdValid field.

### GetCatalyst

`func (o *RemoteObdTestRecordType) GetCatalyst() string`

GetCatalyst returns the Catalyst field if non-nil, zero value otherwise.

### GetCatalystOk

`func (o *RemoteObdTestRecordType) GetCatalystOk() (string, bool)`

GetCatalystOk returns a tuple with the Catalyst field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCatalyst

`func (o *RemoteObdTestRecordType) HasCatalyst() bool`

HasCatalyst returns a boolean if a field has been set.

### SetCatalyst

`func (o *RemoteObdTestRecordType) SetCatalyst(v string)`

SetCatalyst gets a reference to the given string and assigns it to the Catalyst field.

### GetComprehensive

`func (o *RemoteObdTestRecordType) GetComprehensive() string`

GetComprehensive returns the Comprehensive field if non-nil, zero value otherwise.

### GetComprehensiveOk

`func (o *RemoteObdTestRecordType) GetComprehensiveOk() (string, bool)`

GetComprehensiveOk returns a tuple with the Comprehensive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasComprehensive

`func (o *RemoteObdTestRecordType) HasComprehensive() bool`

HasComprehensive returns a boolean if a field has been set.

### SetComprehensive

`func (o *RemoteObdTestRecordType) SetComprehensive(v string)`

SetComprehensive gets a reference to the given string and assigns it to the Comprehensive field.

### GetCompressionIgnitionMonitorSupported

`func (o *RemoteObdTestRecordType) GetCompressionIgnitionMonitorSupported() string`

GetCompressionIgnitionMonitorSupported returns the CompressionIgnitionMonitorSupported field if non-nil, zero value otherwise.

### GetCompressionIgnitionMonitorSupportedOk

`func (o *RemoteObdTestRecordType) GetCompressionIgnitionMonitorSupportedOk() (string, bool)`

GetCompressionIgnitionMonitorSupportedOk returns a tuple with the CompressionIgnitionMonitorSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCompressionIgnitionMonitorSupported

`func (o *RemoteObdTestRecordType) HasCompressionIgnitionMonitorSupported() bool`

HasCompressionIgnitionMonitorSupported returns a boolean if a field has been set.

### SetCompressionIgnitionMonitorSupported

`func (o *RemoteObdTestRecordType) SetCompressionIgnitionMonitorSupported(v string)`

SetCompressionIgnitionMonitorSupported gets a reference to the given string and assigns it to the CompressionIgnitionMonitorSupported field.

### GetCompressionIgnitionMonitorSupportedValid

`func (o *RemoteObdTestRecordType) GetCompressionIgnitionMonitorSupportedValid() bool`

GetCompressionIgnitionMonitorSupportedValid returns the CompressionIgnitionMonitorSupportedValid field if non-nil, zero value otherwise.

### GetCompressionIgnitionMonitorSupportedValidOk

`func (o *RemoteObdTestRecordType) GetCompressionIgnitionMonitorSupportedValidOk() (bool, bool)`

GetCompressionIgnitionMonitorSupportedValidOk returns a tuple with the CompressionIgnitionMonitorSupportedValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCompressionIgnitionMonitorSupportedValid

`func (o *RemoteObdTestRecordType) HasCompressionIgnitionMonitorSupportedValid() bool`

HasCompressionIgnitionMonitorSupportedValid returns a boolean if a field has been set.

### SetCompressionIgnitionMonitorSupportedValid

`func (o *RemoteObdTestRecordType) SetCompressionIgnitionMonitorSupportedValid(v bool)`

SetCompressionIgnitionMonitorSupportedValid gets a reference to the given bool and assigns it to the CompressionIgnitionMonitorSupportedValid field.

### GetDistanceTraveledSinceCodesCleared

`func (o *RemoteObdTestRecordType) GetDistanceTraveledSinceCodesCleared() int32`

GetDistanceTraveledSinceCodesCleared returns the DistanceTraveledSinceCodesCleared field if non-nil, zero value otherwise.

### GetDistanceTraveledSinceCodesClearedOk

`func (o *RemoteObdTestRecordType) GetDistanceTraveledSinceCodesClearedOk() (int32, bool)`

GetDistanceTraveledSinceCodesClearedOk returns a tuple with the DistanceTraveledSinceCodesCleared field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDistanceTraveledSinceCodesCleared

`func (o *RemoteObdTestRecordType) HasDistanceTraveledSinceCodesCleared() bool`

HasDistanceTraveledSinceCodesCleared returns a boolean if a field has been set.

### SetDistanceTraveledSinceCodesCleared

`func (o *RemoteObdTestRecordType) SetDistanceTraveledSinceCodesCleared(v int32)`

SetDistanceTraveledSinceCodesCleared gets a reference to the given int32 and assigns it to the DistanceTraveledSinceCodesCleared field.

### GetDistanceTraveledSinceCodesClearedValid

`func (o *RemoteObdTestRecordType) GetDistanceTraveledSinceCodesClearedValid() bool`

GetDistanceTraveledSinceCodesClearedValid returns the DistanceTraveledSinceCodesClearedValid field if non-nil, zero value otherwise.

### GetDistanceTraveledSinceCodesClearedValidOk

`func (o *RemoteObdTestRecordType) GetDistanceTraveledSinceCodesClearedValidOk() (bool, bool)`

GetDistanceTraveledSinceCodesClearedValidOk returns a tuple with the DistanceTraveledSinceCodesClearedValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDistanceTraveledSinceCodesClearedValid

`func (o *RemoteObdTestRecordType) HasDistanceTraveledSinceCodesClearedValid() bool`

HasDistanceTraveledSinceCodesClearedValid returns a boolean if a field has been set.

### SetDistanceTraveledSinceCodesClearedValid

`func (o *RemoteObdTestRecordType) SetDistanceTraveledSinceCodesClearedValid(v bool)`

SetDistanceTraveledSinceCodesClearedValid gets a reference to the given bool and assigns it to the DistanceTraveledSinceCodesClearedValid field.

### GetDistanceTraveledWithMilOn

`func (o *RemoteObdTestRecordType) GetDistanceTraveledWithMilOn() int32`

GetDistanceTraveledWithMilOn returns the DistanceTraveledWithMilOn field if non-nil, zero value otherwise.

### GetDistanceTraveledWithMilOnOk

`func (o *RemoteObdTestRecordType) GetDistanceTraveledWithMilOnOk() (int32, bool)`

GetDistanceTraveledWithMilOnOk returns a tuple with the DistanceTraveledWithMilOn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDistanceTraveledWithMilOn

`func (o *RemoteObdTestRecordType) HasDistanceTraveledWithMilOn() bool`

HasDistanceTraveledWithMilOn returns a boolean if a field has been set.

### SetDistanceTraveledWithMilOn

`func (o *RemoteObdTestRecordType) SetDistanceTraveledWithMilOn(v int32)`

SetDistanceTraveledWithMilOn gets a reference to the given int32 and assigns it to the DistanceTraveledWithMilOn field.

### GetDistanceTraveledWithMilOnValid

`func (o *RemoteObdTestRecordType) GetDistanceTraveledWithMilOnValid() bool`

GetDistanceTraveledWithMilOnValid returns the DistanceTraveledWithMilOnValid field if non-nil, zero value otherwise.

### GetDistanceTraveledWithMilOnValidOk

`func (o *RemoteObdTestRecordType) GetDistanceTraveledWithMilOnValidOk() (bool, bool)`

GetDistanceTraveledWithMilOnValidOk returns a tuple with the DistanceTraveledWithMilOnValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDistanceTraveledWithMilOnValid

`func (o *RemoteObdTestRecordType) HasDistanceTraveledWithMilOnValid() bool`

HasDistanceTraveledWithMilOnValid returns a boolean if a field has been set.

### SetDistanceTraveledWithMilOnValid

`func (o *RemoteObdTestRecordType) SetDistanceTraveledWithMilOnValid(v bool)`

SetDistanceTraveledWithMilOnValid gets a reference to the given bool and assigns it to the DistanceTraveledWithMilOnValid field.

### GetDtcCount

`func (o *RemoteObdTestRecordType) GetDtcCount() int32`

GetDtcCount returns the DtcCount field if non-nil, zero value otherwise.

### GetDtcCountOk

`func (o *RemoteObdTestRecordType) GetDtcCountOk() (int32, bool)`

GetDtcCountOk returns a tuple with the DtcCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDtcCount

`func (o *RemoteObdTestRecordType) HasDtcCount() bool`

HasDtcCount returns a boolean if a field has been set.

### SetDtcCount

`func (o *RemoteObdTestRecordType) SetDtcCount(v int32)`

SetDtcCount gets a reference to the given int32 and assigns it to the DtcCount field.

### GetEgr

`func (o *RemoteObdTestRecordType) GetEgr() string`

GetEgr returns the Egr field if non-nil, zero value otherwise.

### GetEgrOk

`func (o *RemoteObdTestRecordType) GetEgrOk() (string, bool)`

GetEgrOk returns a tuple with the Egr field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEgr

`func (o *RemoteObdTestRecordType) HasEgr() bool`

HasEgr returns a boolean if a field has been set.

### SetEgr

`func (o *RemoteObdTestRecordType) SetEgr(v string)`

SetEgr gets a reference to the given string and assigns it to the Egr field.

### GetEmissionRelatedDtcs

`func (o *RemoteObdTestRecordType) GetEmissionRelatedDtcs() string`

GetEmissionRelatedDtcs returns the EmissionRelatedDtcs field if non-nil, zero value otherwise.

### GetEmissionRelatedDtcsOk

`func (o *RemoteObdTestRecordType) GetEmissionRelatedDtcsOk() (string, bool)`

GetEmissionRelatedDtcsOk returns a tuple with the EmissionRelatedDtcs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEmissionRelatedDtcs

`func (o *RemoteObdTestRecordType) HasEmissionRelatedDtcs() bool`

HasEmissionRelatedDtcs returns a boolean if a field has been set.

### SetEmissionRelatedDtcs

`func (o *RemoteObdTestRecordType) SetEmissionRelatedDtcs(v string)`

SetEmissionRelatedDtcs gets a reference to the given string and assigns it to the EmissionRelatedDtcs field.

### GetEmissionRelatedDtcsValid

`func (o *RemoteObdTestRecordType) GetEmissionRelatedDtcsValid() bool`

GetEmissionRelatedDtcsValid returns the EmissionRelatedDtcsValid field if non-nil, zero value otherwise.

### GetEmissionRelatedDtcsValidOk

`func (o *RemoteObdTestRecordType) GetEmissionRelatedDtcsValidOk() (bool, bool)`

GetEmissionRelatedDtcsValidOk returns a tuple with the EmissionRelatedDtcsValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEmissionRelatedDtcsValid

`func (o *RemoteObdTestRecordType) HasEmissionRelatedDtcsValid() bool`

HasEmissionRelatedDtcsValid returns a boolean if a field has been set.

### SetEmissionRelatedDtcsValid

`func (o *RemoteObdTestRecordType) SetEmissionRelatedDtcsValid(v bool)`

SetEmissionRelatedDtcsValid gets a reference to the given bool and assigns it to the EmissionRelatedDtcsValid field.

### GetEvapSystem

`func (o *RemoteObdTestRecordType) GetEvapSystem() string`

GetEvapSystem returns the EvapSystem field if non-nil, zero value otherwise.

### GetEvapSystemOk

`func (o *RemoteObdTestRecordType) GetEvapSystemOk() (string, bool)`

GetEvapSystemOk returns a tuple with the EvapSystem field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEvapSystem

`func (o *RemoteObdTestRecordType) HasEvapSystem() bool`

HasEvapSystem returns a boolean if a field has been set.

### SetEvapSystem

`func (o *RemoteObdTestRecordType) SetEvapSystem(v string)`

SetEvapSystem gets a reference to the given string and assigns it to the EvapSystem field.

### GetFuel

`func (o *RemoteObdTestRecordType) GetFuel() string`

GetFuel returns the Fuel field if non-nil, zero value otherwise.

### GetFuelOk

`func (o *RemoteObdTestRecordType) GetFuelOk() (string, bool)`

GetFuelOk returns a tuple with the Fuel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFuel

`func (o *RemoteObdTestRecordType) HasFuel() bool`

HasFuel returns a boolean if a field has been set.

### SetFuel

`func (o *RemoteObdTestRecordType) SetFuel(v string)`

SetFuel gets a reference to the given string and assigns it to the Fuel field.

### GetHeatedCatalyst

`func (o *RemoteObdTestRecordType) GetHeatedCatalyst() string`

GetHeatedCatalyst returns the HeatedCatalyst field if non-nil, zero value otherwise.

### GetHeatedCatalystOk

`func (o *RemoteObdTestRecordType) GetHeatedCatalystOk() (string, bool)`

GetHeatedCatalystOk returns a tuple with the HeatedCatalyst field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHeatedCatalyst

`func (o *RemoteObdTestRecordType) HasHeatedCatalyst() bool`

HasHeatedCatalyst returns a boolean if a field has been set.

### SetHeatedCatalyst

`func (o *RemoteObdTestRecordType) SetHeatedCatalyst(v string)`

SetHeatedCatalyst gets a reference to the given string and assigns it to the HeatedCatalyst field.

### GetHeatedO2Sensor

`func (o *RemoteObdTestRecordType) GetHeatedO2Sensor() string`

GetHeatedO2Sensor returns the HeatedO2Sensor field if non-nil, zero value otherwise.

### GetHeatedO2SensorOk

`func (o *RemoteObdTestRecordType) GetHeatedO2SensorOk() (string, bool)`

GetHeatedO2SensorOk returns a tuple with the HeatedO2Sensor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHeatedO2Sensor

`func (o *RemoteObdTestRecordType) HasHeatedO2Sensor() bool`

HasHeatedO2Sensor returns a boolean if a field has been set.

### SetHeatedO2Sensor

`func (o *RemoteObdTestRecordType) SetHeatedO2Sensor(v string)`

SetHeatedO2Sensor gets a reference to the given string and assigns it to the HeatedO2Sensor field.

### GetIsoSaeReserved

`func (o *RemoteObdTestRecordType) GetIsoSaeReserved() string`

GetIsoSaeReserved returns the IsoSaeReserved field if non-nil, zero value otherwise.

### GetIsoSaeReservedOk

`func (o *RemoteObdTestRecordType) GetIsoSaeReservedOk() (string, bool)`

GetIsoSaeReservedOk returns a tuple with the IsoSaeReserved field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasIsoSaeReserved

`func (o *RemoteObdTestRecordType) HasIsoSaeReserved() bool`

HasIsoSaeReserved returns a boolean if a field has been set.

### SetIsoSaeReserved

`func (o *RemoteObdTestRecordType) SetIsoSaeReserved(v string)`

SetIsoSaeReserved gets a reference to the given string and assigns it to the IsoSaeReserved field.

### GetMil

`func (o *RemoteObdTestRecordType) GetMil() string`

GetMil returns the Mil field if non-nil, zero value otherwise.

### GetMilOk

`func (o *RemoteObdTestRecordType) GetMilOk() (string, bool)`

GetMilOk returns a tuple with the Mil field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMil

`func (o *RemoteObdTestRecordType) HasMil() bool`

HasMil returns a boolean if a field has been set.

### SetMil

`func (o *RemoteObdTestRecordType) SetMil(v string)`

SetMil gets a reference to the given string and assigns it to the Mil field.

### GetMilValid

`func (o *RemoteObdTestRecordType) GetMilValid() bool`

GetMilValid returns the MilValid field if non-nil, zero value otherwise.

### GetMilValidOk

`func (o *RemoteObdTestRecordType) GetMilValidOk() (bool, bool)`

GetMilValidOk returns a tuple with the MilValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMilValid

`func (o *RemoteObdTestRecordType) HasMilValid() bool`

HasMilValid returns a boolean if a field has been set.

### SetMilValid

`func (o *RemoteObdTestRecordType) SetMilValid(v bool)`

SetMilValid gets a reference to the given bool and assigns it to the MilValid field.

### GetMinutesSinceCodesCleared

`func (o *RemoteObdTestRecordType) GetMinutesSinceCodesCleared() int32`

GetMinutesSinceCodesCleared returns the MinutesSinceCodesCleared field if non-nil, zero value otherwise.

### GetMinutesSinceCodesClearedOk

`func (o *RemoteObdTestRecordType) GetMinutesSinceCodesClearedOk() (int32, bool)`

GetMinutesSinceCodesClearedOk returns a tuple with the MinutesSinceCodesCleared field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMinutesSinceCodesCleared

`func (o *RemoteObdTestRecordType) HasMinutesSinceCodesCleared() bool`

HasMinutesSinceCodesCleared returns a boolean if a field has been set.

### SetMinutesSinceCodesCleared

`func (o *RemoteObdTestRecordType) SetMinutesSinceCodesCleared(v int32)`

SetMinutesSinceCodesCleared gets a reference to the given int32 and assigns it to the MinutesSinceCodesCleared field.

### GetMinutesSinceCodesClearedValid

`func (o *RemoteObdTestRecordType) GetMinutesSinceCodesClearedValid() bool`

GetMinutesSinceCodesClearedValid returns the MinutesSinceCodesClearedValid field if non-nil, zero value otherwise.

### GetMinutesSinceCodesClearedValidOk

`func (o *RemoteObdTestRecordType) GetMinutesSinceCodesClearedValidOk() (bool, bool)`

GetMinutesSinceCodesClearedValidOk returns a tuple with the MinutesSinceCodesClearedValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMinutesSinceCodesClearedValid

`func (o *RemoteObdTestRecordType) HasMinutesSinceCodesClearedValid() bool`

HasMinutesSinceCodesClearedValid returns a boolean if a field has been set.

### SetMinutesSinceCodesClearedValid

`func (o *RemoteObdTestRecordType) SetMinutesSinceCodesClearedValid(v bool)`

SetMinutesSinceCodesClearedValid gets a reference to the given bool and assigns it to the MinutesSinceCodesClearedValid field.

### GetMinutesSinceMil

`func (o *RemoteObdTestRecordType) GetMinutesSinceMil() int32`

GetMinutesSinceMil returns the MinutesSinceMil field if non-nil, zero value otherwise.

### GetMinutesSinceMilOk

`func (o *RemoteObdTestRecordType) GetMinutesSinceMilOk() (int32, bool)`

GetMinutesSinceMilOk returns a tuple with the MinutesSinceMil field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMinutesSinceMil

`func (o *RemoteObdTestRecordType) HasMinutesSinceMil() bool`

HasMinutesSinceMil returns a boolean if a field has been set.

### SetMinutesSinceMil

`func (o *RemoteObdTestRecordType) SetMinutesSinceMil(v int32)`

SetMinutesSinceMil gets a reference to the given int32 and assigns it to the MinutesSinceMil field.

### GetMinutesSinceMilValid

`func (o *RemoteObdTestRecordType) GetMinutesSinceMilValid() bool`

GetMinutesSinceMilValid returns the MinutesSinceMilValid field if non-nil, zero value otherwise.

### GetMinutesSinceMilValidOk

`func (o *RemoteObdTestRecordType) GetMinutesSinceMilValidOk() (bool, bool)`

GetMinutesSinceMilValidOk returns a tuple with the MinutesSinceMilValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMinutesSinceMilValid

`func (o *RemoteObdTestRecordType) HasMinutesSinceMilValid() bool`

HasMinutesSinceMilValid returns a boolean if a field has been set.

### SetMinutesSinceMilValid

`func (o *RemoteObdTestRecordType) SetMinutesSinceMilValid(v bool)`

SetMinutesSinceMilValid gets a reference to the given bool and assigns it to the MinutesSinceMilValid field.

### GetMisfire

`func (o *RemoteObdTestRecordType) GetMisfire() string`

GetMisfire returns the Misfire field if non-nil, zero value otherwise.

### GetMisfireOk

`func (o *RemoteObdTestRecordType) GetMisfireOk() (string, bool)`

GetMisfireOk returns a tuple with the Misfire field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMisfire

`func (o *RemoteObdTestRecordType) HasMisfire() bool`

HasMisfire returns a boolean if a field has been set.

### SetMisfire

`func (o *RemoteObdTestRecordType) SetMisfire(v string)`

SetMisfire gets a reference to the given string and assigns it to the Misfire field.

### GetNotReadyCount

`func (o *RemoteObdTestRecordType) GetNotReadyCount() int32`

GetNotReadyCount returns the NotReadyCount field if non-nil, zero value otherwise.

### GetNotReadyCountOk

`func (o *RemoteObdTestRecordType) GetNotReadyCountOk() (int32, bool)`

GetNotReadyCountOk returns a tuple with the NotReadyCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotReadyCount

`func (o *RemoteObdTestRecordType) HasNotReadyCount() bool`

HasNotReadyCount returns a boolean if a field has been set.

### SetNotReadyCount

`func (o *RemoteObdTestRecordType) SetNotReadyCount(v int32)`

SetNotReadyCount gets a reference to the given int32 and assigns it to the NotReadyCount field.

### GetO2Sensor

`func (o *RemoteObdTestRecordType) GetO2Sensor() string`

GetO2Sensor returns the O2Sensor field if non-nil, zero value otherwise.

### GetO2SensorOk

`func (o *RemoteObdTestRecordType) GetO2SensorOk() (string, bool)`

GetO2SensorOk returns a tuple with the O2Sensor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasO2Sensor

`func (o *RemoteObdTestRecordType) HasO2Sensor() bool`

HasO2Sensor returns a boolean if a field has been set.

### SetO2Sensor

`func (o *RemoteObdTestRecordType) SetO2Sensor(v string)`

SetO2Sensor gets a reference to the given string and assigns it to the O2Sensor field.

### GetObdMonitorStatusValid

`func (o *RemoteObdTestRecordType) GetObdMonitorStatusValid() bool`

GetObdMonitorStatusValid returns the ObdMonitorStatusValid field if non-nil, zero value otherwise.

### GetObdMonitorStatusValidOk

`func (o *RemoteObdTestRecordType) GetObdMonitorStatusValidOk() (bool, bool)`

GetObdMonitorStatusValidOk returns a tuple with the ObdMonitorStatusValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdMonitorStatusValid

`func (o *RemoteObdTestRecordType) HasObdMonitorStatusValid() bool`

HasObdMonitorStatusValid returns a boolean if a field has been set.

### SetObdMonitorStatusValid

`func (o *RemoteObdTestRecordType) SetObdMonitorStatusValid(v bool)`

SetObdMonitorStatusValid gets a reference to the given bool and assigns it to the ObdMonitorStatusValid field.

### GetObdVin

`func (o *RemoteObdTestRecordType) GetObdVin() string`

GetObdVin returns the ObdVin field if non-nil, zero value otherwise.

### GetObdVinOk

`func (o *RemoteObdTestRecordType) GetObdVinOk() (string, bool)`

GetObdVinOk returns a tuple with the ObdVin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdVin

`func (o *RemoteObdTestRecordType) HasObdVin() bool`

HasObdVin returns a boolean if a field has been set.

### SetObdVin

`func (o *RemoteObdTestRecordType) SetObdVin(v string)`

SetObdVin gets a reference to the given string and assigns it to the ObdVin field.

### GetObdVinValid

`func (o *RemoteObdTestRecordType) GetObdVinValid() bool`

GetObdVinValid returns the ObdVinValid field if non-nil, zero value otherwise.

### GetObdVinValidOk

`func (o *RemoteObdTestRecordType) GetObdVinValidOk() (bool, bool)`

GetObdVinValidOk returns a tuple with the ObdVinValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasObdVinValid

`func (o *RemoteObdTestRecordType) HasObdVinValid() bool`

HasObdVinValid returns a boolean if a field has been set.

### SetObdVinValid

`func (o *RemoteObdTestRecordType) SetObdVinValid(v bool)`

SetObdVinValid gets a reference to the given bool and assigns it to the ObdVinValid field.

### GetPcmId

`func (o *RemoteObdTestRecordType) GetPcmId() string`

GetPcmId returns the PcmId field if non-nil, zero value otherwise.

### GetPcmIdOk

`func (o *RemoteObdTestRecordType) GetPcmIdOk() (string, bool)`

GetPcmIdOk returns a tuple with the PcmId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPcmId

`func (o *RemoteObdTestRecordType) HasPcmId() bool`

HasPcmId returns a boolean if a field has been set.

### SetPcmId

`func (o *RemoteObdTestRecordType) SetPcmId(v string)`

SetPcmId gets a reference to the given string and assigns it to the PcmId field.

### GetPendingDtcCount

`func (o *RemoteObdTestRecordType) GetPendingDtcCount() int32`

GetPendingDtcCount returns the PendingDtcCount field if non-nil, zero value otherwise.

### GetPendingDtcCountOk

`func (o *RemoteObdTestRecordType) GetPendingDtcCountOk() (int32, bool)`

GetPendingDtcCountOk returns a tuple with the PendingDtcCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPendingDtcCount

`func (o *RemoteObdTestRecordType) HasPendingDtcCount() bool`

HasPendingDtcCount returns a boolean if a field has been set.

### SetPendingDtcCount

`func (o *RemoteObdTestRecordType) SetPendingDtcCount(v int32)`

SetPendingDtcCount gets a reference to the given int32 and assigns it to the PendingDtcCount field.

### GetPendingDtcs

`func (o *RemoteObdTestRecordType) GetPendingDtcs() string`

GetPendingDtcs returns the PendingDtcs field if non-nil, zero value otherwise.

### GetPendingDtcsOk

`func (o *RemoteObdTestRecordType) GetPendingDtcsOk() (string, bool)`

GetPendingDtcsOk returns a tuple with the PendingDtcs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPendingDtcs

`func (o *RemoteObdTestRecordType) HasPendingDtcs() bool`

HasPendingDtcs returns a boolean if a field has been set.

### SetPendingDtcs

`func (o *RemoteObdTestRecordType) SetPendingDtcs(v string)`

SetPendingDtcs gets a reference to the given string and assigns it to the PendingDtcs field.

### GetPendingDtcsValid

`func (o *RemoteObdTestRecordType) GetPendingDtcsValid() bool`

GetPendingDtcsValid returns the PendingDtcsValid field if non-nil, zero value otherwise.

### GetPendingDtcsValidOk

`func (o *RemoteObdTestRecordType) GetPendingDtcsValidOk() (bool, bool)`

GetPendingDtcsValidOk returns a tuple with the PendingDtcsValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPendingDtcsValid

`func (o *RemoteObdTestRecordType) HasPendingDtcsValid() bool`

HasPendingDtcsValid returns a boolean if a field has been set.

### SetPendingDtcsValid

`func (o *RemoteObdTestRecordType) SetPendingDtcsValid(v bool)`

SetPendingDtcsValid gets a reference to the given bool and assigns it to the PendingDtcsValid field.

### GetPermanentDtcCount

`func (o *RemoteObdTestRecordType) GetPermanentDtcCount() int32`

GetPermanentDtcCount returns the PermanentDtcCount field if non-nil, zero value otherwise.

### GetPermanentDtcCountOk

`func (o *RemoteObdTestRecordType) GetPermanentDtcCountOk() (int32, bool)`

GetPermanentDtcCountOk returns a tuple with the PermanentDtcCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPermanentDtcCount

`func (o *RemoteObdTestRecordType) HasPermanentDtcCount() bool`

HasPermanentDtcCount returns a boolean if a field has been set.

### SetPermanentDtcCount

`func (o *RemoteObdTestRecordType) SetPermanentDtcCount(v int32)`

SetPermanentDtcCount gets a reference to the given int32 and assigns it to the PermanentDtcCount field.

### GetPermanentDtcs

`func (o *RemoteObdTestRecordType) GetPermanentDtcs() string`

GetPermanentDtcs returns the PermanentDtcs field if non-nil, zero value otherwise.

### GetPermanentDtcsOk

`func (o *RemoteObdTestRecordType) GetPermanentDtcsOk() (string, bool)`

GetPermanentDtcsOk returns a tuple with the PermanentDtcs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPermanentDtcs

`func (o *RemoteObdTestRecordType) HasPermanentDtcs() bool`

HasPermanentDtcs returns a boolean if a field has been set.

### SetPermanentDtcs

`func (o *RemoteObdTestRecordType) SetPermanentDtcs(v string)`

SetPermanentDtcs gets a reference to the given string and assigns it to the PermanentDtcs field.

### GetPermanentDtcsValid

`func (o *RemoteObdTestRecordType) GetPermanentDtcsValid() bool`

GetPermanentDtcsValid returns the PermanentDtcsValid field if non-nil, zero value otherwise.

### GetPermanentDtcsValidOk

`func (o *RemoteObdTestRecordType) GetPermanentDtcsValidOk() (bool, bool)`

GetPermanentDtcsValidOk returns a tuple with the PermanentDtcsValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPermanentDtcsValid

`func (o *RemoteObdTestRecordType) HasPermanentDtcsValid() bool`

HasPermanentDtcsValid returns a boolean if a field has been set.

### SetPermanentDtcsValid

`func (o *RemoteObdTestRecordType) SetPermanentDtcsValid(v bool)`

SetPermanentDtcsValid gets a reference to the given bool and assigns it to the PermanentDtcsValid field.

### GetPidCount

`func (o *RemoteObdTestRecordType) GetPidCount() int32`

GetPidCount returns the PidCount field if non-nil, zero value otherwise.

### GetPidCountOk

`func (o *RemoteObdTestRecordType) GetPidCountOk() (int32, bool)`

GetPidCountOk returns a tuple with the PidCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPidCount

`func (o *RemoteObdTestRecordType) HasPidCount() bool`

HasPidCount returns a boolean if a field has been set.

### SetPidCount

`func (o *RemoteObdTestRecordType) SetPidCount(v int32)`

SetPidCount gets a reference to the given int32 and assigns it to the PidCount field.

### GetPidCountValid

`func (o *RemoteObdTestRecordType) GetPidCountValid() bool`

GetPidCountValid returns the PidCountValid field if non-nil, zero value otherwise.

### GetPidCountValidOk

`func (o *RemoteObdTestRecordType) GetPidCountValidOk() (bool, bool)`

GetPidCountValidOk returns a tuple with the PidCountValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPidCountValid

`func (o *RemoteObdTestRecordType) HasPidCountValid() bool`

HasPidCountValid returns a boolean if a field has been set.

### SetPidCountValid

`func (o *RemoteObdTestRecordType) SetPidCountValid(v bool)`

SetPidCountValid gets a reference to the given bool and assigns it to the PidCountValid field.

### GetRpm

`func (o *RemoteObdTestRecordType) GetRpm() int32`

GetRpm returns the Rpm field if non-nil, zero value otherwise.

### GetRpmOk

`func (o *RemoteObdTestRecordType) GetRpmOk() (int32, bool)`

GetRpmOk returns a tuple with the Rpm field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRpm

`func (o *RemoteObdTestRecordType) HasRpm() bool`

HasRpm returns a boolean if a field has been set.

### SetRpm

`func (o *RemoteObdTestRecordType) SetRpm(v int32)`

SetRpm gets a reference to the given int32 and assigns it to the Rpm field.

### GetRpmValid

`func (o *RemoteObdTestRecordType) GetRpmValid() bool`

GetRpmValid returns the RpmValid field if non-nil, zero value otherwise.

### GetRpmValidOk

`func (o *RemoteObdTestRecordType) GetRpmValidOk() (bool, bool)`

GetRpmValidOk returns a tuple with the RpmValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRpmValid

`func (o *RemoteObdTestRecordType) HasRpmValid() bool`

HasRpmValid returns a boolean if a field has been set.

### SetRpmValid

`func (o *RemoteObdTestRecordType) SetRpmValid(v bool)`

SetRpmValid gets a reference to the given bool and assigns it to the RpmValid field.

### GetSecondaryAir

`func (o *RemoteObdTestRecordType) GetSecondaryAir() string`

GetSecondaryAir returns the SecondaryAir field if non-nil, zero value otherwise.

### GetSecondaryAirOk

`func (o *RemoteObdTestRecordType) GetSecondaryAirOk() (string, bool)`

GetSecondaryAirOk returns a tuple with the SecondaryAir field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSecondaryAir

`func (o *RemoteObdTestRecordType) HasSecondaryAir() bool`

HasSecondaryAir returns a boolean if a field has been set.

### SetSecondaryAir

`func (o *RemoteObdTestRecordType) SetSecondaryAir(v string)`

SetSecondaryAir gets a reference to the given string and assigns it to the SecondaryAir field.

### GetWarmupsSinceCodesCleared

`func (o *RemoteObdTestRecordType) GetWarmupsSinceCodesCleared() int32`

GetWarmupsSinceCodesCleared returns the WarmupsSinceCodesCleared field if non-nil, zero value otherwise.

### GetWarmupsSinceCodesClearedOk

`func (o *RemoteObdTestRecordType) GetWarmupsSinceCodesClearedOk() (int32, bool)`

GetWarmupsSinceCodesClearedOk returns a tuple with the WarmupsSinceCodesCleared field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasWarmupsSinceCodesCleared

`func (o *RemoteObdTestRecordType) HasWarmupsSinceCodesCleared() bool`

HasWarmupsSinceCodesCleared returns a boolean if a field has been set.

### SetWarmupsSinceCodesCleared

`func (o *RemoteObdTestRecordType) SetWarmupsSinceCodesCleared(v int32)`

SetWarmupsSinceCodesCleared gets a reference to the given int32 and assigns it to the WarmupsSinceCodesCleared field.

### GetWarmupsSinceCodesClearedValid

`func (o *RemoteObdTestRecordType) GetWarmupsSinceCodesClearedValid() bool`

GetWarmupsSinceCodesClearedValid returns the WarmupsSinceCodesClearedValid field if non-nil, zero value otherwise.

### GetWarmupsSinceCodesClearedValidOk

`func (o *RemoteObdTestRecordType) GetWarmupsSinceCodesClearedValidOk() (bool, bool)`

GetWarmupsSinceCodesClearedValidOk returns a tuple with the WarmupsSinceCodesClearedValid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasWarmupsSinceCodesClearedValid

`func (o *RemoteObdTestRecordType) HasWarmupsSinceCodesClearedValid() bool`

HasWarmupsSinceCodesClearedValid returns a boolean if a field has been set.

### SetWarmupsSinceCodesClearedValid

`func (o *RemoteObdTestRecordType) SetWarmupsSinceCodesClearedValid(v bool)`

SetWarmupsSinceCodesClearedValid gets a reference to the given bool and assigns it to the WarmupsSinceCodesClearedValid field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


