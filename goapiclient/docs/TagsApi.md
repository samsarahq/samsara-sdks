# \TagsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateTag**](TagsApi.md#CreateTag) | **Post** /tags | Create a tag
[**DeleteTagById**](TagsApi.md#DeleteTagById) | **Delete** /tags/{id} | Delete a tag
[**GetAllTags**](TagsApi.md#GetAllTags) | **Get** /tags | List all tags
[**GetTagById**](TagsApi.md#GetTagById) | **Get** /tags/{id} | Retrieve a tag
[**PutTagById**](TagsApi.md#PutTagById) | **Put** /tags/{id} | Update a tag



## CreateTag

> InlineResponse20012 CreateTag(ctx).TagCreateBody(tagCreateBody).Execute()

Create a tag



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateTagRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagCreateBody** | [**TagUpdate**](TagUpdate.md) |  | 

### Return type

[**InlineResponse20012**](inline_response_200_12.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteTagById

> DeleteTagById(ctx, id).Execute()

Delete a tag



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Unique identifier for the tag. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteTagByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAllTags

> InlineResponse20011 GetAllTags(ctx).Limit(limit).After(after).Execute()

List all tags



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetAllTagsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int64** | The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [default to 512]
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 

### Return type

[**InlineResponse20011**](inline_response_200_11.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTagById

> InlineResponse20012 GetTagById(ctx, id).Execute()

Retrieve a tag



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Unique identifier for the tag. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTagByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**InlineResponse20012**](inline_response_200_12.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PutTagById

> InlineResponse20012 PutTagById(ctx, id).TagUpdateBody(tagUpdateBody).Execute()

Update a tag



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Unique identifier for the tag. | 

### Other Parameters

Other parameters are passed through a pointer to a apiPutTagByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **tagUpdateBody** | [**TagUpdate**](TagUpdate.md) |  | 

### Return type

[**InlineResponse20012**](inline_response_200_12.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

