# V1DocumentType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FieldTypes** | Pointer to [**[]V1DocumentFieldType**](V1DocumentFieldType.md) | The fields associated with this document type. | 
**Name** | Pointer to **string** | Name of the document type. | [optional] 
**OrgId** | Pointer to **int64** | ID for the organization this document belongs to. | 
**Uuid** | Pointer to **string** | Universally unique identifier for the document type. Can be passed in as the &#x60;documentTypeUuid&#x60; when creating a document for this document type. | 

## Methods

### GetFieldTypes

`func (o *V1DocumentType) GetFieldTypes() []V1DocumentFieldType`

GetFieldTypes returns the FieldTypes field if non-nil, zero value otherwise.

### GetFieldTypesOk

`func (o *V1DocumentType) GetFieldTypesOk() ([]V1DocumentFieldType, bool)`

GetFieldTypesOk returns a tuple with the FieldTypes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFieldTypes

`func (o *V1DocumentType) HasFieldTypes() bool`

HasFieldTypes returns a boolean if a field has been set.

### SetFieldTypes

`func (o *V1DocumentType) SetFieldTypes(v []V1DocumentFieldType)`

SetFieldTypes gets a reference to the given []V1DocumentFieldType and assigns it to the FieldTypes field.

### GetName

`func (o *V1DocumentType) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *V1DocumentType) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *V1DocumentType) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *V1DocumentType) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetOrgId

`func (o *V1DocumentType) GetOrgId() int64`

GetOrgId returns the OrgId field if non-nil, zero value otherwise.

### GetOrgIdOk

`func (o *V1DocumentType) GetOrgIdOk() (int64, bool)`

GetOrgIdOk returns a tuple with the OrgId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOrgId

`func (o *V1DocumentType) HasOrgId() bool`

HasOrgId returns a boolean if a field has been set.

### SetOrgId

`func (o *V1DocumentType) SetOrgId(v int64)`

SetOrgId gets a reference to the given int64 and assigns it to the OrgId field.

### GetUuid

`func (o *V1DocumentType) GetUuid() string`

GetUuid returns the Uuid field if non-nil, zero value otherwise.

### GetUuidOk

`func (o *V1DocumentType) GetUuidOk() (string, bool)`

GetUuidOk returns a tuple with the Uuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasUuid

`func (o *V1DocumentType) HasUuid() bool`

HasUuid returns a boolean if a field has been set.

### SetUuid

`func (o *V1DocumentType) SetUuid(v string)`

SetUuid gets a reference to the given string and assigns it to the Uuid field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


