# DocumentType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Fields** | Pointer to [**[]DocumentField**](DocumentField.md) | The fields determine the names of fields for this document type. They also determine the types of values a document submitted for this document type can have. | [optional] 
**Id** | Pointer to **string** | Universally unique identifier for the document type. Can be passed in as a documentTypeId when creating a document for this document type. | [optional] 
**Name** | Pointer to **string** | Name of the document type. | [optional] 

## Methods

### GetFields

`func (o *DocumentType) GetFields() []DocumentField`

GetFields returns the Fields field if non-nil, zero value otherwise.

### GetFieldsOk

`func (o *DocumentType) GetFieldsOk() ([]DocumentField, bool)`

GetFieldsOk returns a tuple with the Fields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFields

`func (o *DocumentType) HasFields() bool`

HasFields returns a boolean if a field has been set.

### SetFields

`func (o *DocumentType) SetFields(v []DocumentField)`

SetFields gets a reference to the given []DocumentField and assigns it to the Fields field.

### GetId

`func (o *DocumentType) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DocumentType) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *DocumentType) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *DocumentType) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetName

`func (o *DocumentType) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *DocumentType) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *DocumentType) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *DocumentType) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


