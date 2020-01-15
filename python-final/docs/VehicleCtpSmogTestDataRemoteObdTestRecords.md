# VehicleCtpSmogTestDataRemoteObdTestRecords

CTP test data reported from one ECU.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cal_cvn** | **str** | Calibration Verification Numbers read from the CAN bus, separated by a pipe character. | [optional] 
**cal_cvn_valid** | **bool** | Indicates CalCvnCount was successfully read from the CAN bus. | [optional] 
**cal_id** | **str** | Calibration IDs read from the CAN bus, separated by a pipe character. | [optional] 
**cal_id_valid** | **bool** | Indicates CalId was successfully read from the CAN bus. | [optional] 
**catalyst** | **str** | OBD Monitor Status - Catalyst or NMHC Catalyst as read from the CAN bus. | [optional] 
**comprehensive** | **str** | OBD Monitor Status - Comprehensive as read from the CAN bus. | [optional] 
**compression_ignition_monitor_supported** | **str** | Compression ignition monitor supported as read from the CAN bus. | [optional] 
**compression_ignition_monitor_supported_valid** | **bool** | Indicates CompressionIgnitionMonitorSupported was successfully read from the CAN bus. | [optional] 
**distance_traveled_since_codes_cleared** | **int** | Distance Traveled Since Codes Cleared as read from the CAN bus. | [optional] 
**distance_traveled_since_codes_cleared_valid** | **bool** | Indicates DistanceTraveledSinceCodesCleared was successfully read from the CAN bus. | [optional] 
**distance_traveled_with_mil_on** | **int** | Distance Traveled With MIL On as read from the CAN bus. | [optional] 
**distance_traveled_with_mil_on_valid** | **bool** | Indicates DistanceTraveledWithMilOn was successfully read from the CAN bus. | [optional] 
**dtc_count** | **int** | Number of emissions related DTCs read from the CAN bus. | [optional] 
**egr** | **str** | OBD Monitor Status - EGR/VVT as read from the CAN bus. | [optional] 
**emission_related_dtcs** | **str** | Emission related DTCs as read from the CAN bus, separated by pipe characters. | [optional] 
**emission_related_dtcs_valid** | **bool** | Indicates EmissionRelatedDtcs was successfully read from the CAN bus. | [optional] 
**evap_system** | **str** | OBD Monitor Status - Evaporative System or ISO/SAE Reserved as read from the CAN bus. | [optional] 
**fuel** | **str** | OBD Monitor Status - Fuel as read from the CAN bus. | [optional] 
**heated_catalyst** | **str** | OBD Monitor Status - Heated Catalyst or NOx/SCR aftertreatment as read from the CAN bus. | [optional] 
**heated_o2_sensor** | **str** | OBD Monitor Status - Oxygen Sensor Heater or PM Filter as read from the CAN bus. | [optional] 
**iso_sae_reserved** | **str** | OBD Monitor Status - ISO/SAE Reserved as read from the CAN bus. | [optional] 
**mil** | **str** | Malfunction indicator lamp status as read from the CAN bus. | [optional] 
**mil_valid** | **bool** | Indicates Mil was successfully read from the CAN bus. | [optional] 
**minutes_since_codes_cleared** | **int** | Minutes Since Codes Cleared as read from the CAN bus. | [optional] 
**minutes_since_codes_cleared_valid** | **bool** | Indicates MinutesSinceCodesCleared was successfully read from the CAN bus. | [optional] 
**minutes_since_mil** | **int** | Minutes Since MIL On as read from the CAN bus. | [optional] 
**minutes_since_mil_valid** | **bool** | Indicates MinutesSinceMil was successfully read from the CAN bus. | [optional] 
**misfire** | **str** | OBD Monitor Status - Misfire as read from the CAN bus. | [optional] 
**not_ready_count** | **int** | Number of OBD Monitor Statuses reporting &#39;Supported and not ready&#39;. | [optional] 
**o2_sensor** | **str** | OBD Monitor Status - Oxygen Sensor or Exhaust Gas Sensor as read from the CAN bus. | [optional] 
**obd_monitor_status_valid** | **bool** | Indicates Obd Monitor Statuses were successfully read from the CAN bus. | [optional] 
**obd_vin** | **str** | Vehicle identification number as read from the CAN bus. | [optional] 
**obd_vin_valid** | **bool** | Indicates ObdVin was successfully read from the CAN bus. | [optional] 
**pcm_id** | **str** | ECU Address for the ECU that was read from the CAN bus. | [optional] 
**pending_dtc_count** | **int** | Number of pending DTCs read from the CAN bus. | [optional] 
**pending_dtcs** | **str** | Pending DTCs as read from the CAN bus, separated by pipe characters. | [optional] 
**pending_dtcs_valid** | **bool** | Indicates PendingDtcs was successfully read from the CAN bus. | [optional] 
**permanent_dtc_count** | **int** | Number of permanent DTCs read from the CAN bus. | [optional] 
**permanent_dtcs** | **str** | Permanent DTCs as read from the CAN bus, separated by pipe characters. | [optional] 
**permanent_dtcs_valid** | **bool** | Indicates PermanentDtcs was successfully read from the CAN bus. | [optional] 
**pid_count** | **int** | PidCount is a count of all PIDs supported for this control module as read from the CAN bus | [optional] 
**pid_count_valid** | **bool** | Indicates PidCount was successfully read from the CAN bus. | [optional] 
**rpm** | **int** | Revolutions per minute as read from the CAN bus. | [optional] 
**rpm_valid** | **bool** | Indicates Rpm was successfully read from the CAN bus. | [optional] 
**secondary_air** | **str** | OBD Monitor Status - Secondary Air System or Boost Pressure System as read from the CAN bus. | [optional] 
**warmups_since_codes_cleared** | **int** | Warmups Since Codes Cleared as read from the CAN bus. | [optional] 
**warmups_since_codes_cleared_valid** | **bool** | Indicates WarmupsSinceCodesCleared was successfully read from the CAN bus. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

