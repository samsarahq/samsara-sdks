# V1DocumentFieldCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DateTimeValue** | Pointer to [**V1DocumentFieldCreateDateTimeValue**](V1DocumentFieldCreate_dateTimeValue.md) |  | [optional] 
**MultipleChoiceValue** | Pointer to [**[]V1DocumentFieldCreateMultipleChoiceValue**](V1DocumentFieldCreate_multipleChoiceValue.md) | The value of a &#x60;ValueType_MultipleChoice&#x60; field. | [optional] 
**NumberValue** | Pointer to **float64** | The value of a &#x60;ValueType_Number&#x60; field. | [optional] 
**PhotoValue** | Pointer to [**[]V1DocumentFieldCreatePhotoValue**](V1DocumentFieldCreate_photoValue.md) | The value of a &#x60;ValueType_Photo&#x60; field. | [optional] 
**StringValue** | Pointer to **string** | The value of a &#x60;ValueType_String&#x60; field. | [optional] 
**ValueType** | Pointer to **string** | The type of this field. Valid values: &#x60;ValueType_Number&#x60;, &#x60;ValueType_String&#x60;, &#x60;ValueType_Photo&#x60;, &#x60;ValueType_MultipleChoice&#x60;, &#x60;ValueType_Signature&#x60;, &#x60;ValueType_DateTime&#x60;. When creating documents via API, only &#x60;ValueType_Number&#x60;, &#x60;ValueType_String&#x60;, &#x60;ValueType_MultipleChoice&#x60;, and &#x60;ValueType_DateTime&#x60; are accepted. | 

## Methods

### GetDateTimeValue

`func (o *V1DocumentFieldCreate) GetDateTimeValue() V1DocumentFieldCreateDateTimeValue`

GetDateTimeValue returns the DateTimeValue field if non-nil, zero value otherwise.

### GetDateTimeValueOk

`func (o *V1DocumentFieldCreate) GetDateTimeValueOk() (V1DocumentFieldCreateDateTimeValue, bool)`

GetDateTimeValueOk returns a tuple with the DateTimeValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDateTimeValue

`func (o *V1DocumentFieldCreate) HasDateTimeValue() bool`

HasDateTimeValue returns a boolean if a field has been set.

### SetDateTimeValue

`func (o *V1DocumentFieldCreate) SetDateTimeValue(v V1DocumentFieldCreateDateTimeValue)`

SetDateTimeValue gets a reference to the given V1DocumentFieldCreateDateTimeValue and assigns it to the DateTimeValue field.

### GetMultipleChoiceValue

`func (o *V1DocumentFieldCreate) GetMultipleChoiceValue() []V1DocumentFieldCreateMultipleChoiceValue`

GetMultipleChoiceValue returns the MultipleChoiceValue field if non-nil, zero value otherwise.

### GetMultipleChoiceValueOk

`func (o *V1DocumentFieldCreate) GetMultipleChoiceValueOk() ([]V1DocumentFieldCreateMultipleChoiceValue, bool)`

GetMultipleChoiceValueOk returns a tuple with the MultipleChoiceValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasMultipleChoiceValue

`func (o *V1DocumentFieldCreate) HasMultipleChoiceValue() bool`

HasMultipleChoiceValue returns a boolean if a field has been set.

### SetMultipleChoiceValue

`func (o *V1DocumentFieldCreate) SetMultipleChoiceValue(v []V1DocumentFieldCreateMultipleChoiceValue)`

SetMultipleChoiceValue gets a reference to the given []V1DocumentFieldCreateMultipleChoiceValue and assigns it to the MultipleChoiceValue field.

### GetNumberValue

`func (o *V1DocumentFieldCreate) GetNumberValue() float64`

GetNumberValue returns the NumberValue field if non-nil, zero value otherwise.

### GetNumberValueOk

`func (o *V1DocumentFieldCreate) GetNumberValueOk() (float64, bool)`

GetNumberValueOk returns a tuple with the NumberValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNumberValue

`func (o *V1DocumentFieldCreate) HasNumberValue() bool`

HasNumberValue returns a boolean if a field has been set.

### SetNumberValue

`func (o *V1DocumentFieldCreate) SetNumberValue(v float64)`

SetNumberValue gets a reference to the given float64 and assigns it to the NumberValue field.

### GetPhotoValue

`func (o *V1DocumentFieldCreate) GetPhotoValue() []V1DocumentFieldCreatePhotoValue`

GetPhotoValue returns the PhotoValue field if non-nil, zero value otherwise.

### GetPhotoValueOk

`func (o *V1DocumentFieldCreate) GetPhotoValueOk() ([]V1DocumentFieldCreatePhotoValue, bool)`

GetPhotoValueOk returns a tuple with the PhotoValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPhotoValue

`func (o *V1DocumentFieldCreate) HasPhotoValue() bool`

HasPhotoValue returns a boolean if a field has been set.

### SetPhotoValue

`func (o *V1DocumentFieldCreate) SetPhotoValue(v []V1DocumentFieldCreatePhotoValue)`

SetPhotoValue gets a reference to the given []V1DocumentFieldCreatePhotoValue and assigns it to the PhotoValue field.

### GetStringValue

`func (o *V1DocumentFieldCreate) GetStringValue() string`

GetStringValue returns the StringValue field if non-nil, zero value otherwise.

### GetStringValueOk

`func (o *V1DocumentFieldCreate) GetStringValueOk() (string, bool)`

GetStringValueOk returns a tuple with the StringValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStringValue

`func (o *V1DocumentFieldCreate) HasStringValue() bool`

HasStringValue returns a boolean if a field has been set.

### SetStringValue

`func (o *V1DocumentFieldCreate) SetStringValue(v string)`

SetStringValue gets a reference to the given string and assigns it to the StringValue field.

### GetValueType

`func (o *V1DocumentFieldCreate) GetValueType() string`

GetValueType returns the ValueType field if non-nil, zero value otherwise.

### GetValueTypeOk

`func (o *V1DocumentFieldCreate) GetValueTypeOk() (string, bool)`

GetValueTypeOk returns a tuple with the ValueType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasValueType

`func (o *V1DocumentFieldCreate) HasValueType() bool`

HasValueType returns a boolean if a field has been set.

### SetValueType

`func (o *V1DocumentFieldCreate) SetValueType(v string)`

SetValueType gets a reference to the given string and assigns it to the ValueType field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


