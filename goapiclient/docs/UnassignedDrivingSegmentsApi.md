# \UnassignedDrivingSegmentsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetUnassignedDrivingSegments**](UnassignedDrivingSegmentsApi.md#GetUnassignedDrivingSegments) | **Get** /fleet/unassigned-driving-segments | List all unassigned driving segments
[**PatchUnassignedDrivingSegments**](UnassignedDrivingSegmentsApi.md#PatchUnassignedDrivingSegments) | **Patch** /fleet/unassigned-driving-segments/{id} | Assign an unassigned driving segment



## GetUnassignedDrivingSegments

> InlineResponse2002 GetUnassignedDrivingSegments(ctx).After(after).Id(id).StartTime(startTime).EndTime(endTime).Execute()

List all unassigned driving segments



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetUnassignedDrivingSegmentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **id** | [**[]string**](string.md) | ID(s) of a specific unassigned driving segment(s). Takes precedent over filter time range params. Supports multiple comma-separated IDs using csv format (ex. ?id&#x3D;1,2,3). | 
 **startTime** | **time.Time** | Beginning of the filter time range, specified in RFC 3339 format. (Example: 2019-06-13T18:08:25Z) Filters based on the server timestamp, i.e. createAtTime. | 
 **endTime** | **time.Time** | End of the filter time range, specified in RFC 3339 format. (Example: 2019-06-13T19:08:25Z) Filters based on the server timestamp, i.e. createAtTime. | 

### Return type

[**InlineResponse2002**](inline_response_200_2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchUnassignedDrivingSegments

> InlineResponse2003 PatchUnassignedDrivingSegments(ctx, id).UpdateUnassignedDrivingSegment(updateUnassignedDrivingSegment).Execute()

Assign an unassigned driving segment



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | [**string**](.md) | ID of a specific unassigned driving segment. | 

### Other Parameters

Other parameters are passed through a pointer to a apiPatchUnassignedDrivingSegmentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateUnassignedDrivingSegment** | [**InlineObject**](InlineObject.md) |  | 

### Return type

[**InlineResponse2003**](inline_response_200_3.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

