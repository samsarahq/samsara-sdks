# \CarrierProposedAssignmentsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateCarrierProposedAssignment**](CarrierProposedAssignmentsApi.md#CreateCarrierProposedAssignment) | **Post** /fleet/carrier-proposed-assignments | Create an assignment
[**DeleteCarrierProposedAssignmentById**](CarrierProposedAssignmentsApi.md#DeleteCarrierProposedAssignmentById) | **Delete** /fleet/carrier-proposed-assignments/{id} | Delete an assignment
[**GetCarrierProposedAssignment**](CarrierProposedAssignmentsApi.md#GetCarrierProposedAssignment) | **Get** /fleet/carrier-proposed-assignments | Retrieve assignments



## CreateCarrierProposedAssignment

> map[string]interface{} CreateCarrierProposedAssignment(ctx).CarrierProposedAssignment(carrierProposedAssignment).Execute()

Create an assignment



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateCarrierProposedAssignmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrierProposedAssignment** | [**CarrierProposedAssignmentCreate**](CarrierProposedAssignmentCreate.md) | The assignment to create. | 

### Return type

[**map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteCarrierProposedAssignmentById

> DeleteCarrierProposedAssignmentById(ctx, id).Execute()

Delete an assignment



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | ID of the assignment. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteCarrierProposedAssignmentByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCarrierProposedAssignment

> InlineResponse2001 GetCarrierProposedAssignment(ctx).Limit(limit).After(after).DriverIds(driverIds).ActiveTime(activeTime).Execute()

Retrieve assignments



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetCarrierProposedAssignmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int64** | The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [default to 512]
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **driverIds** | **string** | If specified, limits the results to those for these drivers. e.g. driverIds&#x3D;1,2,3 | 
 **activeTime** | **time.Time** | If specified, shows assignments that will be active after this time. In RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 

### Return type

[**InlineResponse2001**](inline_response_200_1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

