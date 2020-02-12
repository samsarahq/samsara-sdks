# DefectResolvedBy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | ID of the entity that resolved this defect. If the defect was resolved by a driver, this will be a Samsara Driver ID. If the defect was resolved by a mechanic, this will be the Samsara Dashboard User ID of the mechanic. | [optional] 
**Name** | Pointer to **string** | Name of the person who resolved this defect. | [optional] 
**Type** | Pointer to **string** | Indicates whether this defect was resolved by a &#x60;driver&#x60; or a &#x60;mechanic&#x60;. | [optional] 

## Methods

### GetId

`func (o *DefectResolvedBy) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DefectResolvedBy) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *DefectResolvedBy) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *DefectResolvedBy) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetName

`func (o *DefectResolvedBy) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *DefectResolvedBy) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *DefectResolvedBy) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *DefectResolvedBy) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetType

`func (o *DefectResolvedBy) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *DefectResolvedBy) GetTypeOk() (string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasType

`func (o *DefectResolvedBy) HasType() bool`

HasType returns a boolean if a field has been set.

### SetType

`func (o *DefectResolvedBy) SetType(v string)`

SetType gets a reference to the given string and assigns it to the Type field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


