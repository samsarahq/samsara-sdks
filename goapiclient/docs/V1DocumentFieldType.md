# V1DocumentFieldType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Label** | Pointer to **string** | Name of this field type. | 
**MultipleChoiceValueTypeMetadata** | Pointer to [**V1DocumentFieldTypeMultipleChoiceValueTypeMetadata**](V1DocumentFieldType_multipleChoiceValueTypeMetadata.md) |  | [optional] 
**NumberValueTypeMetadata** | Pointer to [**V1DocumentFieldTypeNumberValueTypeMetadata**](V1DocumentFieldType_numberValueTypeMetadata.md) |  | [optional] 
**SignatureValueTypeMetadata** | Pointer to [**V1DocumentFieldTypeSignatureValueTypeMetadata**](V1DocumentFieldType_signatureValueTypeMetadata.md) |  | [optional] 
**ValueType** | Pointer to **string** | The type of value this field can have. Valid values: &#x60;ValueType_Number&#x60;, &#x60;ValueType_String&#x60;, &#x60;ValueType_Photo&#x60;, &#x60;ValueType_MultipleChoice&#x60;, &#x60;ValueType_Signature&#x60;, &#x60;ValueType_DateTime&#x60;. | 

## Methods

### GetLabel

`func (o *V1DocumentFieldType) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *V1DocumentFieldType) GetLabelOk() (string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLabel

`func (o *V1DocumentFieldType) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### SetLabel

`func (o *V1DocumentFieldType) SetLabel(v string)`

SetLabel gets a reference to the given string and assigns it to the Label field.

### GetMultipleChoiceValueTypeMetadata

`func (o *V1DocumentFieldType) GetMultipleChoiceValueTypeMetadata() V1DocumentFieldTypeMultipleChoiceValueTypeMetadata`

GetMultipleChoiceValueTypeMetadata returns the MultipleChoiceValueTypeMetadata field if non-nil, zero value otherwise.

### GetMultipleChoiceValueTypeMetadataOk

`func (o *V1DocumentFieldType) GetMultipleChoiceValueTypeMetadataOk() (V1DocumentFieldTypeMultipleChoiceValueTypeMetadata, bool)`

GetMultipleChoiceValueTypeMetadataOk returns a tuple with the MultipleChoiceValueTypeMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMultipleChoiceValueTypeMetadata

`func (o *V1DocumentFieldType) HasMultipleChoiceValueTypeMetadata() bool`

HasMultipleChoiceValueTypeMetadata returns a boolean if a field has been set.

### SetMultipleChoiceValueTypeMetadata

`func (o *V1DocumentFieldType) SetMultipleChoiceValueTypeMetadata(v V1DocumentFieldTypeMultipleChoiceValueTypeMetadata)`

SetMultipleChoiceValueTypeMetadata gets a reference to the given V1DocumentFieldTypeMultipleChoiceValueTypeMetadata and assigns it to the MultipleChoiceValueTypeMetadata field.

### GetNumberValueTypeMetadata

`func (o *V1DocumentFieldType) GetNumberValueTypeMetadata() V1DocumentFieldTypeNumberValueTypeMetadata`

GetNumberValueTypeMetadata returns the NumberValueTypeMetadata field if non-nil, zero value otherwise.

### GetNumberValueTypeMetadataOk

`func (o *V1DocumentFieldType) GetNumberValueTypeMetadataOk() (V1DocumentFieldTypeNumberValueTypeMetadata, bool)`

GetNumberValueTypeMetadataOk returns a tuple with the NumberValueTypeMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNumberValueTypeMetadata

`func (o *V1DocumentFieldType) HasNumberValueTypeMetadata() bool`

HasNumberValueTypeMetadata returns a boolean if a field has been set.

### SetNumberValueTypeMetadata

`func (o *V1DocumentFieldType) SetNumberValueTypeMetadata(v V1DocumentFieldTypeNumberValueTypeMetadata)`

SetNumberValueTypeMetadata gets a reference to the given V1DocumentFieldTypeNumberValueTypeMetadata and assigns it to the NumberValueTypeMetadata field.

### GetSignatureValueTypeMetadata

`func (o *V1DocumentFieldType) GetSignatureValueTypeMetadata() V1DocumentFieldTypeSignatureValueTypeMetadata`

GetSignatureValueTypeMetadata returns the SignatureValueTypeMetadata field if non-nil, zero value otherwise.

### GetSignatureValueTypeMetadataOk

`func (o *V1DocumentFieldType) GetSignatureValueTypeMetadataOk() (V1DocumentFieldTypeSignatureValueTypeMetadata, bool)`

GetSignatureValueTypeMetadataOk returns a tuple with the SignatureValueTypeMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSignatureValueTypeMetadata

`func (o *V1DocumentFieldType) HasSignatureValueTypeMetadata() bool`

HasSignatureValueTypeMetadata returns a boolean if a field has been set.

### SetSignatureValueTypeMetadata

`func (o *V1DocumentFieldType) SetSignatureValueTypeMetadata(v V1DocumentFieldTypeSignatureValueTypeMetadata)`

SetSignatureValueTypeMetadata gets a reference to the given V1DocumentFieldTypeSignatureValueTypeMetadata and assigns it to the SignatureValueTypeMetadata field.

### GetValueType

`func (o *V1DocumentFieldType) GetValueType() string`

GetValueType returns the ValueType field if non-nil, zero value otherwise.

### GetValueTypeOk

`func (o *V1DocumentFieldType) GetValueTypeOk() (string, bool)`

GetValueTypeOk returns a tuple with the ValueType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasValueType

`func (o *V1DocumentFieldType) HasValueType() bool`

HasValueType returns a boolean if a field has been set.

### SetValueType

`func (o *V1DocumentFieldType) SetValueType(v string)`

SetValueType gets a reference to the given string and assigns it to the ValueType field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


