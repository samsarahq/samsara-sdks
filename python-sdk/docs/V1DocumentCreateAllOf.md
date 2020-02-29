# V1DocumentCreateAllOf

Arguments to create a document.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type_uuid** | **str** | Universally unique identifier for the document type that this document is being created for. | 
**fields** | [**list[V1DocumentField]**](V1DocumentField.md) | List of fields for the document. The fields must be listed in the order that that they appear in the document type. Only &#x60;stringValue&#x60;, &#x60;numberValue&#x60;, &#x60;multipleChoiceValue&#x60;, and &#x60;dateTimeValue&#x60; fields are supported for document creation via the API. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


