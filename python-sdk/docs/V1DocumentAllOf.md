# V1DocumentAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | **str** | Name of the document type. | 
**driver_created_at_ms** | **int** | The time in Unix epoch milliseconds that the document was created in the driver app. | 
**driver_id** | **int** | ID of the driver for whom the document is submitted. | 
**fields** | [**list[V1DocumentField]**](V1DocumentField.md) | The fields associated with this document. | 
**id** | **str** | ID of the document. | 
**org_id** | **int** | Organization ID that the document belongs to. | 
**server_created_at_ms** | **int** | The time in Unix epoch milliseconds that the document was received by the server. | 
**server_updated_at_ms** | **int** | The time in Unix epoch milliseconds that the document was updated on the server. | 
**vehicle_id** | **int** | ID of the vehicle the driver was signed into when the document was submitted. Will be &#x60;null&#x60; if the document &#x60;state&#x60; is &#x60;Required&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


