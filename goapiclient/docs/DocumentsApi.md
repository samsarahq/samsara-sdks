# \DocumentsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateDocument**](DocumentsApi.md#CreateDocument) | **Post** /fleet/documents | Create a document
[**GetDocumentTypes**](DocumentsApi.md#GetDocumentTypes) | **Get** /fleet/document-types | List all document types
[**GetDocuments**](DocumentsApi.md#GetDocuments) | **Get** /fleet/documents | List all documents
[**V1createDriverDocument**](DocumentsApi.md#V1createDriverDocument) | **Post** /v1/fleet/drivers/{driver_id}/documents | Create a document
[**V1getDriverDocumentByIdAndDriverId**](DocumentsApi.md#V1getDriverDocumentByIdAndDriverId) | **Get** /v1/fleet/drivers/{driver_id}/documents/{document_id} | Fetches a document
[**V1getDriverDocumentTypesByOrgId**](DocumentsApi.md#V1getDriverDocumentTypesByOrgId) | **Get** /v1/fleet/drivers/document_types | Fetch document types
[**V1getDriverDocumentsByOrgId**](DocumentsApi.md#V1getDriverDocumentsByOrgId) | **Get** /v1/fleet/drivers/documents | Fetch all documents



## CreateDocument

> InlineResponse2002 CreateDocument(ctx).Document(document).Execute()

Create a document



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateDocumentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document** | [**DocumentCreate**](DocumentCreate.md) | The document to create. | 

### Return type

[**InlineResponse2002**](inline_response_200_2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDocumentTypes

> map[string]interface{} GetDocumentTypes(ctx).Limit(limit).After(after).Execute()

List all document types



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetDocumentTypesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int64** | The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [default to 512]
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 

### Return type

[**map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDocuments

> map[string]interface{} GetDocuments(ctx).Limit(limit).After(after).StartTime(startTime).EndTime(endTime).DocumentTypeId(documentTypeId).Execute()

List all documents



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetDocumentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int64** | The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [default to 512]
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **startTime** | **time.Time** | A start time in RFC 3339 format. Queries documents on createdAtTime. Is required if an endTime is specified. Defaults to current time - 1 day if startTime and endTime are not provided. (Example: 2019-06-13T19:08:25Z). | 
 **endTime** | **time.Time** | An end time in RFC 3339 format. Queries documents on createdAtTime. Defaults to startTime + 1 day if not specified. (Example: 2019-06-13T19:08:25Z). Time range cannot exceed 3 days (72 hours). | 
 **documentTypeId** | **string** | A document type ID. | 

### Return type

[**map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1createDriverDocument

> V1Document V1createDriverDocument(ctx, driverId).CreateDocumentParams(createDocumentParams).Execute()

Create a document



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driverId** | **int64** | ID of the driver for whom the document is created. Must contain only digits 0-9. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1createDriverDocumentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **createDocumentParams** | [**V1DocumentCreate**](V1DocumentCreate.md) | To create a document for a given document type, provide the &#x60;documentTypeUuid&#x60; of the type of document you&#39;d like to create. Then, pass in the &#x60;fields&#x60; of the document in the same order that they show up in the given document type. | 

### Return type

[**V1Document**](V1Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getDriverDocumentByIdAndDriverId

> V1Document V1getDriverDocumentByIdAndDriverId(ctx, driverId, documentId).Execute()

Fetches a document



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driverId** | **int64** | ID of the driver who submitted the document. Must contain only digits 0-9. | 
**documentId** | **string** | ID of document. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1getDriverDocumentByIdAndDriverIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**V1Document**](V1Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getDriverDocumentTypesByOrgId

> []V1DocumentType V1getDriverDocumentTypesByOrgId(ctx).Execute()

Fetch document types



### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1getDriverDocumentTypesByOrgIdRequest struct via the builder pattern


### Return type

[**[]V1DocumentType**](V1DocumentType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getDriverDocumentsByOrgId

> V1Documents V1getDriverDocumentsByOrgId(ctx).EndMs(endMs).DurationMs(durationMs).QueryBy(queryBy).Execute()

Fetch all documents



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getDriverDocumentsByOrgIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endMs** | **int64** | Time in unix milliseconds that represents the oldest documents to return. Used in combination with durationMs. Defaults to now. | 
 **durationMs** | **int64** | Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours. | 
 **queryBy** | **string** | Retrieve most recent documents based on either driverCreatedAtMs or serverUpdatedAtMs. If no value is provided, the default is driverCreatedAtMs. | 

### Return type

[**V1Documents**](V1Documents.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

