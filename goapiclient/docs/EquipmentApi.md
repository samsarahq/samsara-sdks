# \EquipmentApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetEquipmentById**](EquipmentApi.md#GetEquipmentById) | **Get** /fleet/equipment/{id} | Retrieve a unit of equipment
[**GetEquipmentList**](EquipmentApi.md#GetEquipmentList) | **Get** /fleet/equipment | List all equipment
[**GetEquipmentLocationSnapshot**](EquipmentApi.md#GetEquipmentLocationSnapshot) | **Get** /fleet/equipment/locations | List most recent equipment locations
[**GetEquipmentLocationsFeed**](EquipmentApi.md#GetEquipmentLocationsFeed) | **Get** /fleet/equipment/locations/feed | Follow a real-time feed of equipment locations
[**GetEquipmentLocationsHistory**](EquipmentApi.md#GetEquipmentLocationsHistory) | **Get** /fleet/equipment/locations/history | Get historical equipment locations
[**GetEquipmentStatsFeed**](EquipmentApi.md#GetEquipmentStatsFeed) | **Get** /fleet/equipment/stats/feed | Follow a real-time feed of equipment stats
[**GetEquipmentStatsHistory**](EquipmentApi.md#GetEquipmentStatsHistory) | **Get** /fleet/equipment/stats/history | Get historical equipment stats
[**GetEquipmentStatsSnapshot**](EquipmentApi.md#GetEquipmentStatsSnapshot) | **Get** /fleet/equipment/stats | List most recent equipment stats



## GetEquipmentById

> InlineResponse2005 GetEquipmentById(ctx, id).Execute()

Retrieve a unit of equipment



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Samsara ID of the equipment. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetEquipmentByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**InlineResponse2005**](inline_response_200_5.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetEquipmentList

> EquipmentListResponse GetEquipmentList(ctx).Limit(limit).After(after).TagIds(tagIds).Execute()

List all equipment



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetEquipmentListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int64** | The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [default to 512]
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 

### Return type

[**EquipmentListResponse**](EquipmentListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetEquipmentLocationSnapshot

> map[string]interface{} GetEquipmentLocationSnapshot(ctx).After(after).TagIds(tagIds).EquipmentIds(equipmentIds).Execute()

List most recent equipment locations



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetEquipmentLocationSnapshotRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 
 **equipmentIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of equipment IDs. Example: &#x60;equipmentIds&#x3D;1234,5678&#x60; | 

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


## GetEquipmentLocationsFeed

> map[string]interface{} GetEquipmentLocationsFeed(ctx).After(after).TagIds(tagIds).EquipmentIds(equipmentIds).Execute()

Follow a real-time feed of equipment locations



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetEquipmentLocationsFeedRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 
 **equipmentIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of equipment IDs. Example: &#x60;equipmentIds&#x3D;1234,5678&#x60; | 

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


## GetEquipmentLocationsHistory

> map[string]interface{} GetEquipmentLocationsHistory(ctx).StartTime(startTime).EndTime(endTime).After(after).TagIds(tagIds).EquipmentIds(equipmentIds).Execute()

Get historical equipment locations



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetEquipmentLocationsHistoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startTime** | **time.Time** | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **endTime** | **time.Time** | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 
 **equipmentIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of equipment IDs. Example: &#x60;equipmentIds&#x3D;1234,5678&#x60; | 

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


## GetEquipmentStatsFeed

> map[string]interface{} GetEquipmentStatsFeed(ctx).After(after).TagIds(tagIds).EquipmentIds(equipmentIds).Types(types).Execute()

Follow a real-time feed of equipment stats



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetEquipmentStatsFeedRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 
 **equipmentIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of equipment IDs. Example: &#x60;equipmentIds&#x3D;1234,5678&#x60; | 
 **types** | [**[]string**](string.md) | A comma separated list of stat types. | 

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


## GetEquipmentStatsHistory

> map[string]interface{} GetEquipmentStatsHistory(ctx).StartTime(startTime).EndTime(endTime).After(after).TagIds(tagIds).EquipmentIds(equipmentIds).Types(types).Execute()

Get historical equipment stats



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetEquipmentStatsHistoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startTime** | **time.Time** | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **endTime** | **time.Time** | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 
 **equipmentIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of equipment IDs. Example: &#x60;equipmentIds&#x3D;1234,5678&#x60; | 
 **types** | [**[]string**](string.md) | A comma separated list of stat types. | 

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


## GetEquipmentStatsSnapshot

> map[string]interface{} GetEquipmentStatsSnapshot(ctx).After(after).TagIds(tagIds).EquipmentIds(equipmentIds).Types(types).Execute()

List most recent equipment stats



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetEquipmentStatsSnapshotRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 
 **equipmentIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of equipment IDs. Example: &#x60;equipmentIds&#x3D;1234,5678&#x60; | 
 **types** | [**[]string**](string.md) | A comma separated list of stat types. | 

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

