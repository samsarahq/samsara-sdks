# V1DocumentFieldCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_time_value** | [**V1DocumentFieldCreateDateTimeValue**](V1DocumentFieldCreateDateTimeValue.md) |  | [optional] 
**multiple_choice_value** | [**list[V1DocumentFieldCreateMultipleChoiceValue]**](V1DocumentFieldCreateMultipleChoiceValue.md) | The value of a &#x60;ValueType_MultipleChoice&#x60; field. | [optional] 
**number_value** | **float** | The value of a &#x60;ValueType_Number&#x60; field. | [optional] 
**string_value** | **str** | The value of a &#x60;ValueType_String&#x60; field. | [optional] 
**value_type** | **str** | The type of this field. Valid values: &#x60;ValueType_Number&#x60;, &#x60;ValueType_String&#x60;, &#x60;ValueType_Photo&#x60;, &#x60;ValueType_MultipleChoice&#x60;, &#x60;ValueType_Signature&#x60;, &#x60;ValueType_DateTime&#x60;. When creating documents via API, only &#x60;ValueType_Number&#x60;, &#x60;ValueType_String&#x60;, &#x60;ValueType_MultipleChoice&#x60;, and &#x60;ValueType_DateTime&#x60; are accepted. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


