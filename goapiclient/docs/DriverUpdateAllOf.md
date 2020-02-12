# DriverUpdateAllOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Password** | Pointer to **string** | Password that the driver can use to login to the Samsara driver app. | [optional] 
**StaticAssignedVehicleId** | Pointer to **string** | ID of vehicle assigned to the driver for static vehicle assignments. (uncommon). | [optional] 
**TagIds** | Pointer to **[]string** | IDs of tags the driver is associated with. | [optional] 
**VehicleGroupTagId** | Pointer to **string** | Tag ID which determines which vehicles a driver will see when selecting vehicles. | [optional] 

## Methods

### GetPassword

`func (o *DriverUpdateAllOf) GetPassword() string`

GetPassword returns the Password field if non-nil, zero value otherwise.

### GetPasswordOk

`func (o *DriverUpdateAllOf) GetPasswordOk() (string, bool)`

GetPasswordOk returns a tuple with the Password field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPassword

`func (o *DriverUpdateAllOf) HasPassword() bool`

HasPassword returns a boolean if a field has been set.

### SetPassword

`func (o *DriverUpdateAllOf) SetPassword(v string)`

SetPassword gets a reference to the given string and assigns it to the Password field.

### GetStaticAssignedVehicleId

`func (o *DriverUpdateAllOf) GetStaticAssignedVehicleId() string`

GetStaticAssignedVehicleId returns the StaticAssignedVehicleId field if non-nil, zero value otherwise.

### GetStaticAssignedVehicleIdOk

`func (o *DriverUpdateAllOf) GetStaticAssignedVehicleIdOk() (string, bool)`

GetStaticAssignedVehicleIdOk returns a tuple with the StaticAssignedVehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStaticAssignedVehicleId

`func (o *DriverUpdateAllOf) HasStaticAssignedVehicleId() bool`

HasStaticAssignedVehicleId returns a boolean if a field has been set.

### SetStaticAssignedVehicleId

`func (o *DriverUpdateAllOf) SetStaticAssignedVehicleId(v string)`

SetStaticAssignedVehicleId gets a reference to the given string and assigns it to the StaticAssignedVehicleId field.

### GetTagIds

`func (o *DriverUpdateAllOf) GetTagIds() []string`

GetTagIds returns the TagIds field if non-nil, zero value otherwise.

### GetTagIdsOk

`func (o *DriverUpdateAllOf) GetTagIdsOk() ([]string, bool)`

GetTagIdsOk returns a tuple with the TagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTagIds

`func (o *DriverUpdateAllOf) HasTagIds() bool`

HasTagIds returns a boolean if a field has been set.

### SetTagIds

`func (o *DriverUpdateAllOf) SetTagIds(v []string)`

SetTagIds gets a reference to the given []string and assigns it to the TagIds field.

### GetVehicleGroupTagId

`func (o *DriverUpdateAllOf) GetVehicleGroupTagId() string`

GetVehicleGroupTagId returns the VehicleGroupTagId field if non-nil, zero value otherwise.

### GetVehicleGroupTagIdOk

`func (o *DriverUpdateAllOf) GetVehicleGroupTagIdOk() (string, bool)`

GetVehicleGroupTagIdOk returns a tuple with the VehicleGroupTagId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleGroupTagId

`func (o *DriverUpdateAllOf) HasVehicleGroupTagId() bool`

HasVehicleGroupTagId returns a boolean if a field has been set.

### SetVehicleGroupTagId

`func (o *DriverUpdateAllOf) SetVehicleGroupTagId(v string)`

SetVehicleGroupTagId gets a reference to the given string and assigns it to the VehicleGroupTagId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


