# DocumentField

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FieldType** | Pointer to **string** | The kind of value that can be submitted for this field. | 
**Label** | Pointer to **string** | Descriptive name of this field. | 
**MultipleChoiceMetadata** | Pointer to [**DocumentFieldMultipleChoiceMetadata**](DocumentField_multipleChoiceMetadata.md) |  | [optional] 
**NumberMetadata** | Pointer to [**DocumentFieldNumberMetadata**](DocumentField_numberMetadata.md) |  | [optional] 
**SignatureMetadata** | Pointer to [**DocumentFieldSignatureMetadata**](DocumentField_signatureMetadata.md) |  | [optional] 

## Methods

### GetFieldType

`func (o *DocumentField) GetFieldType() string`

GetFieldType returns the FieldType field if non-nil, zero value otherwise.

### GetFieldTypeOk

`func (o *DocumentField) GetFieldTypeOk() (string, bool)`

GetFieldTypeOk returns a tuple with the FieldType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFieldType

`func (o *DocumentField) HasFieldType() bool`

HasFieldType returns a boolean if a field has been set.

### SetFieldType

`func (o *DocumentField) SetFieldType(v string)`

SetFieldType gets a reference to the given string and assigns it to the FieldType field.

### GetLabel

`func (o *DocumentField) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *DocumentField) GetLabelOk() (string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLabel

`func (o *DocumentField) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### SetLabel

`func (o *DocumentField) SetLabel(v string)`

SetLabel gets a reference to the given string and assigns it to the Label field.

### GetMultipleChoiceMetadata

`func (o *DocumentField) GetMultipleChoiceMetadata() DocumentFieldMultipleChoiceMetadata`

GetMultipleChoiceMetadata returns the MultipleChoiceMetadata field if non-nil, zero value otherwise.

### GetMultipleChoiceMetadataOk

`func (o *DocumentField) GetMultipleChoiceMetadataOk() (DocumentFieldMultipleChoiceMetadata, bool)`

GetMultipleChoiceMetadataOk returns a tuple with the MultipleChoiceMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMultipleChoiceMetadata

`func (o *DocumentField) HasMultipleChoiceMetadata() bool`

HasMultipleChoiceMetadata returns a boolean if a field has been set.

### SetMultipleChoiceMetadata

`func (o *DocumentField) SetMultipleChoiceMetadata(v DocumentFieldMultipleChoiceMetadata)`

SetMultipleChoiceMetadata gets a reference to the given DocumentFieldMultipleChoiceMetadata and assigns it to the MultipleChoiceMetadata field.

### GetNumberMetadata

`func (o *DocumentField) GetNumberMetadata() DocumentFieldNumberMetadata`

GetNumberMetadata returns the NumberMetadata field if non-nil, zero value otherwise.

### GetNumberMetadataOk

`func (o *DocumentField) GetNumberMetadataOk() (DocumentFieldNumberMetadata, bool)`

GetNumberMetadataOk returns a tuple with the NumberMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNumberMetadata

`func (o *DocumentField) HasNumberMetadata() bool`

HasNumberMetadata returns a boolean if a field has been set.

### SetNumberMetadata

`func (o *DocumentField) SetNumberMetadata(v DocumentFieldNumberMetadata)`

SetNumberMetadata gets a reference to the given DocumentFieldNumberMetadata and assigns it to the NumberMetadata field.

### GetSignatureMetadata

`func (o *DocumentField) GetSignatureMetadata() DocumentFieldSignatureMetadata`

GetSignatureMetadata returns the SignatureMetadata field if non-nil, zero value otherwise.

### GetSignatureMetadataOk

`func (o *DocumentField) GetSignatureMetadataOk() (DocumentFieldSignatureMetadata, bool)`

GetSignatureMetadataOk returns a tuple with the SignatureMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSignatureMetadata

`func (o *DocumentField) HasSignatureMetadata() bool`

HasSignatureMetadata returns a boolean if a field has been set.

### SetSignatureMetadata

`func (o *DocumentField) SetSignatureMetadata(v DocumentFieldSignatureMetadata)`

SetSignatureMetadata gets a reference to the given DocumentFieldSignatureMetadata and assigns it to the SignatureMetadata field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


