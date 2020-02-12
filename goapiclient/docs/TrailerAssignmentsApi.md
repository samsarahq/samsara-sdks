# \TrailerAssignmentsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1getAllTrailerAssignments**](TrailerAssignmentsApi.md#V1getAllTrailerAssignments) | **Get** /v1/fleet/trailers/assignments | List trailer assignments for all trailers
[**V1getFleetTrailerAssignments**](TrailerAssignmentsApi.md#V1getFleetTrailerAssignments) | **Get** /v1/fleet/trailers/{trailerId}/assignments | List trailer assignments for a given trailer



## V1getAllTrailerAssignments

> InlineResponse20021 V1getAllTrailerAssignments(ctx).StartMs(startMs).EndMs(endMs).Limit(limit).StartingAfter(startingAfter).EndingBefore(endingBefore).Execute()

List trailer assignments for all trailers



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getAllTrailerAssignmentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startMs** | **int64** | Timestamp in Unix epoch miliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments. | 
 **endMs** | **int64** | Timestamp in Unix epoch miliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time | 
 **limit** | **float32** | Pagination parameter indicating the number of results to return in this request. Used in conjunction with either &#39;startingAfter&#39; or &#39;endingBefore&#39;. | 
 **startingAfter** | **string** | Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the &#39;limit&#39; parameter. Mutually exclusive with &#39;endingBefore&#39; parameter. | 
 **endingBefore** | **string** | Pagination parameter indicating the cursor position to return results before. Used in conjunction with the &#39;limit&#39; parameter. Mutually exclusive with &#39;startingAfter&#39; parameter. | 

### Return type

[**InlineResponse20021**](inline_response_200_21.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getFleetTrailerAssignments

> V1TrailerAssignmentsResponse V1getFleetTrailerAssignments(ctx, trailerId).StartMs(startMs).EndMs(endMs).Execute()

List trailer assignments for a given trailer



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**trailerId** | **int64** | ID of trailer. Must contain only digits 0-9. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1getFleetTrailerAssignmentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **startMs** | **int64** | Timestamp in Unix epoch milliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments. | 
 **endMs** | **int64** | Timestamp in Unix epoch milliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time | 

### Return type

[**V1TrailerAssignmentsResponse**](V1TrailerAssignmentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

