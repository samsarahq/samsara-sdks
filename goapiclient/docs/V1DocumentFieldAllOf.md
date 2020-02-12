# V1DocumentFieldAllOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Label** | Pointer to **string** | The name of the field. | 
**Value** | Pointer to [**map[string]interface{}**](.md) | DEPRECATED: Please use &#x60;stringValue&#x60;, &#x60;numberValue&#x60;, &#x60;photoValue&#x60;, &#x60;multipleChoiceValue&#x60;, &#x60;signatureValue&#x60;, or &#x60;dateTimeValue&#x60; instead. | [optional] 

## Methods

### GetLabel

`func (o *V1DocumentFieldAllOf) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *V1DocumentFieldAllOf) GetLabelOk() (string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLabel

`func (o *V1DocumentFieldAllOf) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### SetLabel

`func (o *V1DocumentFieldAllOf) SetLabel(v string)`

SetLabel gets a reference to the given string and assigns it to the Label field.

### GetValue

`func (o *V1DocumentFieldAllOf) GetValue() map[string]interface{}`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *V1DocumentFieldAllOf) GetValueOk() (map[string]interface{}, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasValue

`func (o *V1DocumentFieldAllOf) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValue

`func (o *V1DocumentFieldAllOf) SetValue(v map[string]interface{})`

SetValue gets a reference to the given map[string]interface{} and assigns it to the Value field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


