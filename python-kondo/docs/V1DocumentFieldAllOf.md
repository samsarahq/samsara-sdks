# V1DocumentFieldAllOf

A field of a document. A field can be a string type, number type, or photo type, which can be identified from its valueType. Between stringValue, numberValue, and photoValue, only one can exist for a single document field depending on the valueType.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Descriptive name of this field. | 
**value** | [**object**](.md) | DEPRECATED: Please use stringValue, numberValue, or photoValue instead. Value of this field. Depending on what kind of field it is, this may be one of the following: an array of image urls, a float, an integer, or a string. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


