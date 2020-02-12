# \ContactsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateContact**](ContactsApi.md#CreateContact) | **Post** /contacts | Create a contact
[**DeleteContactById**](ContactsApi.md#DeleteContactById) | **Delete** /contacts/{id} | Delete a contact
[**GetContactById**](ContactsApi.md#GetContactById) | **Get** /contacts/{id} | Retrieve a contact
[**GetContacts**](ContactsApi.md#GetContacts) | **Get** /contacts | List all contacts
[**UpdateContactById**](ContactsApi.md#UpdateContactById) | **Patch** /contacts/{id} | Update a contact



## CreateContact

> InlineResponse200 CreateContact(ctx).Contact(contact).Execute()

Create a contact



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateContactRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | [**ContactInput**](ContactInput.md) | Add a contact. | 

### Return type

[**InlineResponse200**](inline_response_200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteContactById

> DeleteContactById(ctx, id).Execute()

Delete a contact



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Unique identifier for the contact. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteContactByIdRequest struct via the builder pattern


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


## GetContactById

> InlineResponse200 GetContactById(ctx, id).Execute()

Retrieve a contact



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Unique identifier for the contact. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetContactByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**InlineResponse200**](inline_response_200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetContacts

> map[string]interface{} GetContacts(ctx).Limit(limit).After(after).Execute()

List all contacts



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetContactsRequest struct via the builder pattern


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


## UpdateContactById

> InlineResponse200 UpdateContactById(ctx, id).Contact(contact).Execute()

Update a contact



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Unique identifier for the contact. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateContactByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **contact** | [**ContactInput**](ContactInput.md) | Updates to the contact. | 

### Return type

[**InlineResponse200**](inline_response_200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

