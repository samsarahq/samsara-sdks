# V1MachineHistoryResponseMachines

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int32** | Machine ID | [optional] 
**Name** | Pointer to **string** | Machine name | [optional] 
**Vibrations** | Pointer to [**[]V1MachineHistoryResponseVibrations**](V1MachineHistoryResponse_vibrations.md) | List of vibration datapoints, with timestamp and vibration measurement for x/y/z axis in mm/s | [optional] 

## Methods

### GetId

`func (o *V1MachineHistoryResponseMachines) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1MachineHistoryResponseMachines) GetIdOk() (int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1MachineHistoryResponseMachines) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1MachineHistoryResponseMachines) SetId(v int32)`

SetId gets a reference to the given int32 and assigns it to the Id field.

### GetName

`func (o *V1MachineHistoryResponseMachines) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *V1MachineHistoryResponseMachines) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *V1MachineHistoryResponseMachines) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *V1MachineHistoryResponseMachines) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetVibrations

`func (o *V1MachineHistoryResponseMachines) GetVibrations() []V1MachineHistoryResponseVibrations`

GetVibrations returns the Vibrations field if non-nil, zero value otherwise.

### GetVibrationsOk

`func (o *V1MachineHistoryResponseMachines) GetVibrationsOk() ([]V1MachineHistoryResponseVibrations, bool)`

GetVibrationsOk returns a tuple with the Vibrations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVibrations

`func (o *V1MachineHistoryResponseMachines) HasVibrations() bool`

HasVibrations returns a boolean if a field has been set.

### SetVibrations

`func (o *V1MachineHistoryResponseMachines) SetVibrations(v []V1MachineHistoryResponseVibrations)`

SetVibrations gets a reference to the given []V1MachineHistoryResponseVibrations and assigns it to the Vibrations field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


