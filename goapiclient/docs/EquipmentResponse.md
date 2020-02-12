# EquipmentResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssetSerial** | Pointer to **string** | An equipment identification number. | [optional] 
**Id** | Pointer to **string** | Unique Samsara ID for the equipment. | 
**Name** | Pointer to **string** | Name of the equipment. | [optional] 
**Notes** | Pointer to **string** | Notes about a piece of equipment. Samsara supports a maximum of 255 chars. | [optional] 
**Tags** | Pointer to [**[]TagTinyResponse**](tagTinyResponse.md) | An array of all tag mini-objects that are associated with the given equipment. | [optional] 

## Methods

### GetAssetSerial

`func (o *EquipmentResponse) GetAssetSerial() string`

GetAssetSerial returns the AssetSerial field if non-nil, zero value otherwise.

### GetAssetSerialOk

`func (o *EquipmentResponse) GetAssetSerialOk() (string, bool)`

GetAssetSerialOk returns a tuple with the AssetSerial field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAssetSerial

`func (o *EquipmentResponse) HasAssetSerial() bool`

HasAssetSerial returns a boolean if a field has been set.

### SetAssetSerial

`func (o *EquipmentResponse) SetAssetSerial(v string)`

SetAssetSerial gets a reference to the given string and assigns it to the AssetSerial field.

### GetId

`func (o *EquipmentResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *EquipmentResponse) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *EquipmentResponse) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *EquipmentResponse) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetName

`func (o *EquipmentResponse) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *EquipmentResponse) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *EquipmentResponse) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *EquipmentResponse) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetNotes

`func (o *EquipmentResponse) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *EquipmentResponse) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *EquipmentResponse) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *EquipmentResponse) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetTags

`func (o *EquipmentResponse) GetTags() []TagTinyResponse`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *EquipmentResponse) GetTagsOk() ([]TagTinyResponse, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTags

`func (o *EquipmentResponse) HasTags() bool`

HasTags returns a boolean if a field has been set.

### SetTags

`func (o *EquipmentResponse) SetTags(v []TagTinyResponse)`

SetTags gets a reference to the given []TagTinyResponse and assigns it to the Tags field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


