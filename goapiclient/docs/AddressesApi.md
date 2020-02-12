# \AddressesApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateAddress**](AddressesApi.md#CreateAddress) | **Post** /addresses | Create an address
[**DeleteAddress**](AddressesApi.md#DeleteAddress) | **Delete** /addresses/{id} | Delete an address
[**GetAddress**](AddressesApi.md#GetAddress) | **Get** /addresses/{id} | Retrieve an address
[**ListAddresses**](AddressesApi.md#ListAddresses) | **Get** /addresses | List all addresses
[**UpdateAddress**](AddressesApi.md#UpdateAddress) | **Patch** /addresses/{id} | Update an address



## CreateAddress

> AddressResponse CreateAddress(ctx).Address(address).Execute()

Create an address



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateAddressRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**CreateAddressRequest**](CreateAddressRequest.md) | The address to create. | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteAddress

> DeleteAddress(ctx, id).Execute()

Delete an address



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteAddressRequest struct via the builder pattern


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


## GetAddress

> AddressResponse GetAddress(ctx, id).Execute()

Retrieve an address



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAddressRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListAddresses

> ListAddressesResponse ListAddresses(ctx).Limit(limit).After(after).TagIds(tagIds).Execute()

List all addresses



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListAddressesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int64** | The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [default to 512]
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 

### Return type

[**ListAddressesResponse**](ListAddressesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateAddress

> AddressResponse UpdateAddress(ctx, id).Address(address).Execute()

Update an address



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateAddressRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **address** | [**UpdateAddressRequest**](UpdateAddressRequest.md) | The address fields to update. | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

