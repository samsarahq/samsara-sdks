# \IndustrialApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetDataInputDataFeed**](IndustrialApi.md#GetDataInputDataFeed) | **Get** /industrial/data-inputs/data-points/feed | Follow a real-time feed of data input data points
[**GetDataInputDataHistory**](IndustrialApi.md#GetDataInputDataHistory) | **Get** /industrial/data-inputs/data-points/history | List historical data input data points
[**GetDataInputDataSnapshot**](IndustrialApi.md#GetDataInputDataSnapshot) | **Get** /industrial/data-inputs/data-points | List most recent data input data points
[**GetDataInputs**](IndustrialApi.md#GetDataInputs) | **Get** /industrial/data-inputs | List all data inputs
[**GetVisionRunsByCamera**](IndustrialApi.md#GetVisionRunsByCamera) | **Get** /v1/industrial/vision/runs/{camera_id} | Fetch runs by camera
[**V1getAllDataInputs**](IndustrialApi.md#V1getAllDataInputs) | **Get** /v1/industrial/data | Get industrial data
[**V1getCameras**](IndustrialApi.md#V1getCameras) | **Get** /v1/industrial/vision/cameras | Fetch industrial cameras
[**V1getDataInput**](IndustrialApi.md#V1getDataInput) | **Get** /v1/industrial/data/{data_input_id} | Get industrial data from a specific device
[**V1getMachines**](IndustrialApi.md#V1getMachines) | **Post** /v1/machines/list | Get machines
[**V1getMachinesHistory**](IndustrialApi.md#V1getMachinesHistory) | **Post** /v1/machines/history | Get machine history
[**V1getVisionLatestRunCamera**](IndustrialApi.md#V1getVisionLatestRunCamera) | **Get** /v1/industrial/vision/run/camera/{camera_id} | Fetch the latest run for a camera or program
[**V1getVisionProgramsByCamera**](IndustrialApi.md#V1getVisionProgramsByCamera) | **Get** /v1/industrial/vision/cameras/{camera_id}/programs | Fetch industrial camera programs
[**V1getVisionRuns**](IndustrialApi.md#V1getVisionRuns) | **Get** /v1/industrial/vision/runs | Fetch runs
[**V1getVisionRunsByCameraAndProgram**](IndustrialApi.md#V1getVisionRunsByCameraAndProgram) | **Get** /v1/industrial/vision/runs/{camera_id}/{program_id}/{started_at_ms} | Fetch runs by camera and program



## GetDataInputDataFeed

> DataInputListResponse GetDataInputDataFeed(ctx).After(after).TagIds(tagIds).DataInputIds(dataInputIds).Execute()

Follow a real-time feed of data input data points



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetDataInputDataFeedRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 
 **dataInputIds** | [**[]string**](string.md) | A comma-separated list of data input IDs. Example: &#x60;dataInputIds&#x3D;1234,5678&#x60; | 

### Return type

[**DataInputListResponse**](DataInputListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDataInputDataHistory

> DataInputListResponse GetDataInputDataHistory(ctx).StartTime(startTime).EndTime(endTime).After(after).TagIds(tagIds).DataInputIds(dataInputIds).Execute()

List historical data input data points



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetDataInputDataHistoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startTime** | **time.Time** | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **endTime** | **time.Time** | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 
 **dataInputIds** | [**[]string**](string.md) | A comma-separated list of data input IDs. Example: &#x60;dataInputIds&#x3D;1234,5678&#x60; | 

### Return type

[**DataInputListResponse**](DataInputListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDataInputDataSnapshot

> DataInputSnapshotResponse GetDataInputDataSnapshot(ctx).After(after).TagIds(tagIds).DataInputIds(dataInputIds).Execute()

List most recent data input data points



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetDataInputDataSnapshotRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 
 **dataInputIds** | [**[]string**](string.md) | A comma-separated list of data input IDs. Example: &#x60;dataInputIds&#x3D;1234,5678&#x60; | 

### Return type

[**DataInputSnapshotResponse**](DataInputSnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDataInputs

> InlineResponse2004 GetDataInputs(ctx).Limit(limit).After(after).TagIds(tagIds).Execute()

List all data inputs



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetDataInputsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int64** | The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [default to 512]
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 

### Return type

[**InlineResponse2004**](inline_response_200_4.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetVisionRunsByCamera

> []map[string]interface{} GetVisionRunsByCamera(ctx, cameraId).DurationMs(durationMs).EndMs(endMs).Execute()

Fetch runs by camera



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**cameraId** | **int64** | The camera_id should be valid for the given accessToken. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetVisionRunsByCameraRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **durationMs** | **int64** | DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched | 
 **endMs** | **int64** | EndMs is an optional param. It will default to the current time. | 

### Return type

[**[]map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getAllDataInputs

> InlineResponse20013 V1getAllDataInputs(ctx).StartMs(startMs).EndMs(endMs).Execute()

Get industrial data



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getAllDataInputsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startMs** | **int64** | Timestamp in unix milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. defaults to nowMs. | 
 **endMs** | **int64** | Timestamp in unix milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Defaults to nowMs. | 

### Return type

[**InlineResponse20013**](inline_response_200_13.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getCameras

> []map[string]interface{} V1getCameras(ctx).Execute()

Fetch industrial cameras



### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1getCamerasRequest struct via the builder pattern


### Return type

[**[]map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getDataInput

> V1DataInputHistoryResponse V1getDataInput(ctx, dataInputId).StartMs(startMs).EndMs(endMs).Execute()

Get industrial data from a specific device



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**dataInputId** | **int64** | ID of the data input. Must contain only digits 0-9. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1getDataInputRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **startMs** | **int64** | Timestamp in unix milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. defaults to nowMs. | 
 **endMs** | **int64** | Timestamp in unix milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Defaults to nowMs. | 

### Return type

[**V1DataInputHistoryResponse**](V1DataInputHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getMachines

> InlineResponse20014 V1getMachines(ctx).Execute()

Get machines



### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1getMachinesRequest struct via the builder pattern


### Return type

[**InlineResponse20014**](inline_response_200_14.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getMachinesHistory

> V1MachineHistoryResponse V1getMachinesHistory(ctx).HistoryParam(historyParam).Execute()

Get machine history



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getMachinesHistoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **historyParam** | [**InlineObject6**](InlineObject6.md) |  | 

### Return type

[**V1MachineHistoryResponse**](V1MachineHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getVisionLatestRunCamera

> V1VisionRunByCameraResponse V1getVisionLatestRunCamera(ctx, cameraId).ProgramId(programId).StartedAtMs(startedAtMs).Include(include).Limit(limit).Execute()

Fetch the latest run for a camera or program



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**cameraId** | **int64** | The camera_id should be valid for the given accessToken. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1getVisionLatestRunCameraRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **programId** | **int64** | The configured program&#39;s ID on the camera. | 
 **startedAtMs** | **int64** | EndMs is an optional param. It will default to the current time. | 
 **include** | **string** | Include is a filter parameter. Accepts &#39;pass&#39;, &#39;reject&#39; or &#39;no_read&#39;. | 
 **limit** | **int64** | Limit is an integer value from 1 to 1,000. | 

### Return type

[**V1VisionRunByCameraResponse**](V1VisionRunByCameraResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getVisionProgramsByCamera

> []map[string]interface{} V1getVisionProgramsByCamera(ctx, cameraId).Execute()

Fetch industrial camera programs



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**cameraId** | **int64** | The camera_id should be valid for the given accessToken. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1getVisionProgramsByCameraRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**[]map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getVisionRuns

> V1VisionRunsResponse V1getVisionRuns(ctx).DurationMs(durationMs).EndMs(endMs).Execute()

Fetch runs



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getVisionRunsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **durationMs** | **int64** | DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched | 
 **endMs** | **int64** | EndMs is an optional param. It will default to the current time. | 

### Return type

[**V1VisionRunsResponse**](V1VisionRunsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getVisionRunsByCameraAndProgram

> V1VisionRunsByCameraAndProgramResponse V1getVisionRunsByCameraAndProgram(ctx, cameraId, programId, startedAtMs).Include(include).Execute()

Fetch runs by camera and program



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**cameraId** | **int64** | The camera_id should be valid for the given accessToken. | 
**programId** | **int64** | The configured program&#39;s ID on the camera. | 
**startedAtMs** | **int64** | Started_at_ms is a required param. Indicates the start time of the run to be fetched. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1getVisionRunsByCameraAndProgramRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **include** | **string** | Include is a filter parameter. Accepts &#39;pass&#39;, &#39;reject&#39; or &#39;no_read&#39;. | 

### Return type

[**V1VisionRunsByCameraAndProgramResponse**](V1VisionRunsByCameraAndProgramResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

