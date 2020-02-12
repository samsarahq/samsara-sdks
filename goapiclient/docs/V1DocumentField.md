# V1DocumentField

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Label** | Pointer to **string** | The name of the field. | 
**Value** | Pointer to [**map[string]interface{}**](.md) | DEPRECATED: Please use &#x60;stringValue&#x60;, &#x60;numberValue&#x60;, &#x60;photoValue&#x60;, &#x60;multipleChoiceValue&#x60;, &#x60;signatureValue&#x60;, or &#x60;dateTimeValue&#x60; instead. | [optional] 
**DateTimeValue** | Pointer to [**V1DocumentFieldCreateDateTimeValue**](V1DocumentFieldCreate_dateTimeValue.md) |  | [optional] 
**MultipleChoiceValue** | Pointer to [**[]V1DocumentFieldCreateMultipleChoiceValue**](V1DocumentFieldCreate_multipleChoiceValue.md) | The value of a &#x60;ValueType_MultipleChoice&#x60; field. | [optional] 
**NumberValue** | Pointer to **float64** | The value of a &#x60;ValueType_Number&#x60; field. | [optional] 
**PhotoValue** | Pointer to [**[]V1DocumentFieldCreatePhotoValue**](V1DocumentFieldCreate_photoValue.md) | The value of a &#x60;ValueType_Photo&#x60; field. | [optional] 
**StringValue** | Pointer to **string** | The value of a &#x60;ValueType_String&#x60; field. | [optional] 
**ValueType** | Pointer to **string** | The type of this field. Valid values: &#x60;ValueType_Number&#x60;, &#x60;ValueType_String&#x60;, &#x60;ValueType_Photo&#x60;, &#x60;ValueType_MultipleChoice&#x60;, &#x60;ValueType_Signature&#x60;, &#x60;ValueType_DateTime&#x60;. When creating documents via API, only &#x60;ValueType_Number&#x60;, &#x60;ValueType_String&#x60;, &#x60;ValueType_MultipleChoice&#x60;, and &#x60;ValueType_DateTime&#x60; are accepted. | 

## Methods

### GetLabel

`func (o *V1DocumentField) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *V1DocumentField) GetLabelOk() (string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLabel

`func (o *V1DocumentField) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### SetLabel

`func (o *V1DocumentField) SetLabel(v string)`

SetLabel gets a reference to the given string and assigns it to the Label field.

### GetValue

`func (o *V1DocumentField) GetValue() map[string]interface{}`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *V1DocumentField) GetValueOk() (map[string]interface{}, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasValue

`func (o *V1DocumentField) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValue

`func (o *V1DocumentField) SetValue(v map[string]interface{})`

SetValue gets a reference to the given map[string]interface{} and assigns it to the Value field.

### GetDateTimeValue

`func (o *V1DocumentField) GetDateTimeValue() V1DocumentFieldCreateDateTimeValue`

GetDateTimeValue returns the DateTimeValue field if non-nil, zero value otherwise.

### GetDateTimeValueOk

`func (o *V1DocumentField) GetDateTimeValueOk() (V1DocumentFieldCreateDateTimeValue, bool)`

GetDateTimeValueOk returns a tuple with the DateTimeValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDateTimeValue

`func (o *V1DocumentField) HasDateTimeValue() bool`

HasDateTimeValue returns a boolean if a field has been set.

### SetDateTimeValue

`func (o *V1DocumentField) SetDateTimeValue(v V1DocumentFieldCreateDateTimeValue)`

SetDateTimeValue gets a reference to the given V1DocumentFieldCreateDateTimeValue and assigns it to the DateTimeValue field.

### GetMultipleChoiceValue

`func (o *V1DocumentField) GetMultipleChoiceValue() []V1DocumentFieldCreateMultipleChoiceValue`

GetMultipleChoiceValue returns the MultipleChoiceValue field if non-nil, zero value otherwise.

### GetMultipleChoiceValueOk

`func (o *V1DocumentField) GetMultipleChoiceValueOk() ([]V1DocumentFieldCreateMultipleChoiceValue, bool)`

GetMultipleChoiceValueOk returns a tuple with the MultipleChoiceValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMultipleChoiceValue

`func (o *V1DocumentField) HasMultipleChoiceValue() bool`

HasMultipleChoiceValue returns a boolean if a field has been set.

### SetMultipleChoiceValue

`func (o *V1DocumentField) SetMultipleChoiceValue(v []V1DocumentFieldCreateMultipleChoiceValue)`

SetMultipleChoiceValue gets a reference to the given []V1DocumentFieldCreateMultipleChoiceValue and assigns it to the MultipleChoiceValue field.

### GetNumberValue

`func (o *V1DocumentField) GetNumberValue() float64`

GetNumberValue returns the NumberValue field if non-nil, zero value otherwise.

### GetNumberValueOk

`func (o *V1DocumentField) GetNumberValueOk() (float64, bool)`

GetNumberValueOk returns a tuple with the NumberValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNumberValue

`func (o *V1DocumentField) HasNumberValue() bool`

HasNumberValue returns a boolean if a field has been set.

### SetNumberValue

`func (o *V1DocumentField) SetNumberValue(v float64)`

SetNumberValue gets a reference to the given float64 and assigns it to the NumberValue field.

### GetPhotoValue

`func (o *V1DocumentField) GetPhotoValue() []V1DocumentFieldCreatePhotoValue`

GetPhotoValue returns the PhotoValue field if non-nil, zero value otherwise.

### GetPhotoValueOk

`func (o *V1DocumentField) GetPhotoValueOk() ([]V1DocumentFieldCreatePhotoValue, bool)`

GetPhotoValueOk returns a tuple with the PhotoValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPhotoValue

`func (o *V1DocumentField) HasPhotoValue() bool`

HasPhotoValue returns a boolean if a field has been set.

### SetPhotoValue

`func (o *V1DocumentField) SetPhotoValue(v []V1DocumentFieldCreatePhotoValue)`

SetPhotoValue gets a reference to the given []V1DocumentFieldCreatePhotoValue and assigns it to the PhotoValue field.

### GetStringValue

`func (o *V1DocumentField) GetStringValue() string`

GetStringValue returns the StringValue field if non-nil, zero value otherwise.

### GetStringValueOk

`func (o *V1DocumentField) GetStringValueOk() (string, bool)`

GetStringValueOk returns a tuple with the StringValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStringValue

`func (o *V1DocumentField) HasStringValue() bool`

HasStringValue returns a boolean if a field has been set.

### SetStringValue

`func (o *V1DocumentField) SetStringValue(v string)`

SetStringValue gets a reference to the given string and assigns it to the StringValue field.

### GetValueType

`func (o *V1DocumentField) GetValueType() string`

GetValueType returns the ValueType field if non-nil, zero value otherwise.

### GetValueTypeOk

`func (o *V1DocumentField) GetValueTypeOk() (string, bool)`

GetValueTypeOk returns a tuple with the ValueType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasValueType

`func (o *V1DocumentField) HasValueType() bool`

HasValueType returns a boolean if a field has been set.

### SetValueType

`func (o *V1DocumentField) SetValueType(v string)`

SetValueType gets a reference to the given string and assigns it to the ValueType field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


