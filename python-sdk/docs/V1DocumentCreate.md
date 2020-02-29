# V1DocumentCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type_uuid** | **str** | Universally unique identifier for the document type that this document is being created for. | 
**fields** | [**list[V1DocumentField]**](V1DocumentField.md) | List of fields for the document. The fields must be listed in the order that that they appear in the document type. Only &#x60;stringValue&#x60;, &#x60;numberValue&#x60;, &#x60;multipleChoiceValue&#x60;, and &#x60;dateTimeValue&#x60; fields are supported for document creation via the API. | 
**dispatch_job_id** | **int** | ID of the Samsara dispatch job for which the document is submitted. | [optional] 
**notes** | **str** | Notes submitted with this document. | [optional] 
**state** | **str** | The condition of the document created for the driver. Can be either &#x60;Required&#x60; or &#x60;Submitted&#x60;. If no value is specified, &#x60;state&#x60; defaults to &#x60;Required&#x60;. &#x60;Required&#x60; documents are pre-populated documents for the Driver to fill out in the Driver App and have not yet been submitted. &#x60;Submitted&#x60; documents will show up as submitted by the driver through the driver app. | [optional] [default to 'Required']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


