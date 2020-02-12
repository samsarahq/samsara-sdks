# DriverAllOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | Samsara ID for the driver. | [optional] 
**StaticAssignedVehicle** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 
**Tags** | Pointer to [**[]TagTinyResponse**](tagTinyResponse.md) | The tags this driver belongs to. | [optional] 
**VehicleGroupTag** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 

## Methods

### GetId

`func (o *DriverAllOf) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DriverAllOf) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *DriverAllOf) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *DriverAllOf) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetStaticAssignedVehicle

`func (o *DriverAllOf) GetStaticAssignedVehicle() map[string]interface{}`

GetStaticAssignedVehicle returns the StaticAssignedVehicle field if non-nil, zero value otherwise.

### GetStaticAssignedVehicleOk

`func (o *DriverAllOf) GetStaticAssignedVehicleOk() (map[string]interface{}, bool)`

GetStaticAssignedVehicleOk returns a tuple with the StaticAssignedVehicle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStaticAssignedVehicle

`func (o *DriverAllOf) HasStaticAssignedVehicle() bool`

HasStaticAssignedVehicle returns a boolean if a field has been set.

### SetStaticAssignedVehicle

`func (o *DriverAllOf) SetStaticAssignedVehicle(v map[string]interface{})`

SetStaticAssignedVehicle gets a reference to the given map[string]interface{} and assigns it to the StaticAssignedVehicle field.

### GetTags

`func (o *DriverAllOf) GetTags() []TagTinyResponse`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *DriverAllOf) GetTagsOk() ([]TagTinyResponse, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTags

`func (o *DriverAllOf) HasTags() bool`

HasTags returns a boolean if a field has been set.

### SetTags

`func (o *DriverAllOf) SetTags(v []TagTinyResponse)`

SetTags gets a reference to the given []TagTinyResponse and assigns it to the Tags field.

### GetVehicleGroupTag

`func (o *DriverAllOf) GetVehicleGroupTag() map[string]interface{}`

GetVehicleGroupTag returns the VehicleGroupTag field if non-nil, zero value otherwise.

### GetVehicleGroupTagOk

`func (o *DriverAllOf) GetVehicleGroupTagOk() (map[string]interface{}, bool)`

GetVehicleGroupTagOk returns a tuple with the VehicleGroupTag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleGroupTag

`func (o *DriverAllOf) HasVehicleGroupTag() bool`

HasVehicleGroupTag returns a boolean if a field has been set.

### SetVehicleGroupTag

`func (o *DriverAllOf) SetVehicleGroupTag(v map[string]interface{})`

SetVehicleGroupTag gets a reference to the given map[string]interface{} and assigns it to the VehicleGroupTag field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


