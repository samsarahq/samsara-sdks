# \MessagesApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateMessagesKondo**](MessagesApi.md#CreateMessagesKondo) | **Post** /messages | Create a message
[**V1createMessages**](MessagesApi.md#V1createMessages) | **Post** /v1/fleet/messages | Send a message to a list of driver ids.
[**V1getMessages**](MessagesApi.md#V1getMessages) | **Get** /v1/fleet/messages | Get all messages.



## CreateMessagesKondo

> InlineResponse2005 CreateMessagesKondo(ctx).CreateMessages(createMessages).Execute()

Create a message



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateMessagesKondoRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createMessages** | [**InlineObject1**](InlineObject1.md) |  | 

### Return type

[**InlineResponse2005**](inline_response_200_5.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1createMessages

> InlineResponse20011 V1createMessages(ctx).CreateMessages(createMessages).Execute()

Send a message to a list of driver ids.



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1createMessagesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createMessages** | [**InlineObject5**](InlineObject5.md) |  | 

### Return type

[**InlineResponse20011**](inline_response_200_11.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getMessages

> InlineResponse20010 V1getMessages(ctx).EndMs(endMs).DurationMs(durationMs).Execute()

Get all messages.



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getMessagesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endMs** | **int64** | Time in unix milliseconds that represents the end of time range of messages to return. Used in combination with durationMs. Defaults to now. | 
 **durationMs** | **int64** | Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours. | 

### Return type

[**InlineResponse20010**](inline_response_200_10.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

