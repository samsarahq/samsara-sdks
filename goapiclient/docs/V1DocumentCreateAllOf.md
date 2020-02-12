# V1DocumentCreateAllOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DocumentTypeUuid** | Pointer to **string** | Universally unique identifier for the document type that this document is being created for. | 
**Fields** | Pointer to [**[]V1DocumentField**](V1DocumentField.md) | List of fields for the document. The fields must be listed in the order that that they appear in the document type. Only &#x60;stringValue&#x60;, &#x60;numberValue&#x60;, &#x60;multipleChoiceValue&#x60;, and &#x60;dateTimeValue&#x60; fields are supported for document creation via the API. | 

## Methods

### GetDocumentTypeUuid

`func (o *V1DocumentCreateAllOf) GetDocumentTypeUuid() string`

GetDocumentTypeUuid returns the DocumentTypeUuid field if non-nil, zero value otherwise.

### GetDocumentTypeUuidOk

`func (o *V1DocumentCreateAllOf) GetDocumentTypeUuidOk() (string, bool)`

GetDocumentTypeUuidOk returns a tuple with the DocumentTypeUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDocumentTypeUuid

`func (o *V1DocumentCreateAllOf) HasDocumentTypeUuid() bool`

HasDocumentTypeUuid returns a boolean if a field has been set.

### SetDocumentTypeUuid

`func (o *V1DocumentCreateAllOf) SetDocumentTypeUuid(v string)`

SetDocumentTypeUuid gets a reference to the given string and assigns it to the DocumentTypeUuid field.

### GetFields

`func (o *V1DocumentCreateAllOf) GetFields() []V1DocumentField`

GetFields returns the Fields field if non-nil, zero value otherwise.

### GetFieldsOk

`func (o *V1DocumentCreateAllOf) GetFieldsOk() ([]V1DocumentField, bool)`

GetFieldsOk returns a tuple with the Fields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFields

`func (o *V1DocumentCreateAllOf) HasFields() bool`

HasFields returns a boolean if a field has been set.

### SetFields

`func (o *V1DocumentCreateAllOf) SetFields(v []V1DocumentField)`

SetFields gets a reference to the given []V1DocumentField and assigns it to the Fields field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


