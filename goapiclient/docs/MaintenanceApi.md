# \MaintenanceApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateDvir**](MaintenanceApi.md#CreateDvir) | **Post** /fleet/dvirs | Create a mechanic DVIR
[**GetDvirById**](MaintenanceApi.md#GetDvirById) | **Get** /fleet/dvirs/{id} | Retrieve a DVIR
[**GetDvirDefects**](MaintenanceApi.md#GetDvirDefects) | **Get** /fleet/defects | Get all defects
[**GetDvirHistory**](MaintenanceApi.md#GetDvirHistory) | **Get** /fleet/dvirs/history | Get all DVIRs
[**ResolveDvirDefect**](MaintenanceApi.md#ResolveDvirDefect) | **Patch** /fleet/defects/{id} | Resolve a defect
[**UpdateDvirById**](MaintenanceApi.md#UpdateDvirById) | **Patch** /fleet/dvirs/{id} | Resolve a DVIR
[**V1createDvir**](MaintenanceApi.md#V1createDvir) | **Post** /v1/fleet/maintenance/dvirs | Create a DVIR
[**V1getDvirs**](MaintenanceApi.md#V1getDvirs) | **Get** /v1/fleet/maintenance/dvirs | Get DVIRs
[**V1getFleetMaintenanceList**](MaintenanceApi.md#V1getFleetMaintenanceList) | **Get** /v1/fleet/maintenance/list | Get vehicles with engine faults or check lights



## CreateDvir

> DvirResponse CreateDvir(ctx).Dvir(dvir).Execute()

Create a mechanic DVIR



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateDvirRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dvir** | [**CreateDvirRequest**](CreateDvirRequest.md) | The DVIR to create. | 

### Return type

[**DvirResponse**](DvirResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDvirById

> DvirResponse GetDvirById(ctx, id).Execute()

Retrieve a DVIR



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | ID of the DVIR. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDvirByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**DvirResponse**](DvirResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDvirDefects

> map[string]interface{} GetDvirDefects(ctx).StartTime(startTime).EndTime(endTime).Limit(limit).After(after).IsResolved(isResolved).Execute()

Get all defects



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetDvirDefectsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startTime** | **time.Time** | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). *The maximum time period you can query for is 30 days.* | 
 **endTime** | **time.Time** | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). *The maximum time period you can query for is 30 days.* | 
 **limit** | **int64** | The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [default to 512]
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **isResolved** | **bool** | A filter on the data based on resolution status. Example: &#x60;isResolved&#x3D;true&#x60; | 

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


## GetDvirHistory

> DvirsListResponse GetDvirHistory(ctx).StartTime(startTime).EndTime(endTime).Limit(limit).After(after).TagIds(tagIds).VehicleIds(vehicleIds).TrailerIds(trailerIds).Execute()

Get all DVIRs



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetDvirHistoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startTime** | **time.Time** | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **endTime** | **time.Time** | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **limit** | **int64** | The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [default to 512]
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 
 **vehicleIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | 
 **trailerIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of trailer IDs. Example: &#x60;trailerIds&#x3D;1234,5678&#x60; | 

### Return type

[**DvirsListResponse**](DvirsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ResolveDvirDefect

> map[string]interface{} ResolveDvirDefect(ctx, id).Defect(defect).Execute()

Resolve a defect



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | ID of the defect. | 

### Other Parameters

Other parameters are passed through a pointer to a apiResolveDvirDefectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **defect** | [**DefectPatch**](DefectPatch.md) | The DVIR defect fields to update. | 

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


## UpdateDvirById

> DvirResponse UpdateDvirById(ctx, id).Dvir(dvir).Execute()

Resolve a DVIR



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | ID of the DVIR. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateDvirByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **dvir** | [**UpdateDvirRequest**](UpdateDvirRequest.md) | The dvir fields to update. | 

### Return type

[**DvirResponse**](DvirResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1createDvir

> V1DvirBase V1createDvir(ctx).CreateDvirParam(createDvirParam).Execute()

Create a DVIR



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1createDvirRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createDvirParam** | [**InlineObject4**](InlineObject4.md) |  | 

### Return type

[**V1DvirBase**](V1DvirBase.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getDvirs

> V1DvirListResponse V1getDvirs(ctx).EndMs(endMs).DurationMs(durationMs).Execute()

Get DVIRs



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getDvirsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endMs** | **int32** | Time in millis until the last dvir log. | 
 **durationMs** | **float32** | Time in millis which corresponds to the duration before the end_ms. Must be less than or equal to 90 days. | 

### Return type

[**V1DvirListResponse**](V1DvirListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getFleetMaintenanceList

> InlineResponse2009 V1getFleetMaintenanceList(ctx).Execute()

Get vehicles with engine faults or check lights



### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1getFleetMaintenanceListRequest struct via the builder pattern


### Return type

[**InlineResponse2009**](inline_response_200_9.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

