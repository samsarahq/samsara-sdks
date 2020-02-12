# \HoursOfServiceApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1getFleetDriversHosDailyLogs**](HoursOfServiceApi.md#V1getFleetDriversHosDailyLogs) | **Post** /v1/fleet/drivers/{driver_id}/hos_daily_logs | Get daily HOS logs for a specific driver
[**V1getFleetHosAuthenticationLogs**](HoursOfServiceApi.md#V1getFleetHosAuthenticationLogs) | **Get** /v1/fleet/hos_authentication_logs | Get HOS signin and signout
[**V1getFleetHosLogs**](HoursOfServiceApi.md#V1getFleetHosLogs) | **Post** /v1/fleet/hos_logs | Get HOS logs for a specific driver
[**V1getFleetHosLogsSummary**](HoursOfServiceApi.md#V1getFleetHosLogsSummary) | **Get** /v1/fleet/hos_logs_summary | Get current HOS status for all drivers



## V1getFleetDriversHosDailyLogs

> V1DriverDailyLogResponse V1getFleetDriversHosDailyLogs(ctx, driverId).HosLogsParam(hosLogsParam).Execute()

Get daily HOS logs for a specific driver



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driverId** | **int64** | ID of the driver with HOS logs. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1getFleetDriversHosDailyLogsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **hosLogsParam** | [**InlineObject2**](InlineObject2.md) |  | 

### Return type

[**V1DriverDailyLogResponse**](V1DriverDailyLogResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getFleetHosAuthenticationLogs

> V1HosAuthenticationLogsResponse V1getFleetHosAuthenticationLogs(ctx).DriverId(driverId).StartMs(startMs).EndMs(endMs).Execute()

Get HOS signin and signout



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getFleetHosAuthenticationLogsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driverId** | **int64** | Driver ID to query. | 
 **startMs** | **int64** | Beginning of the time range, specified in milliseconds UNIX time. | 
 **endMs** | **int64** | End of the time range, specified in milliseconds UNIX time. | 

### Return type

[**V1HosAuthenticationLogsResponse**](V1HosAuthenticationLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getFleetHosLogs

> V1HosLogsResponse V1getFleetHosLogs(ctx).HosLogsParam(hosLogsParam).Execute()

Get HOS logs for a specific driver



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getFleetHosLogsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hosLogsParam** | [**InlineObject3**](InlineObject3.md) |  | 

### Return type

[**V1HosLogsResponse**](V1HosLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getFleetHosLogsSummary

> V1HosLogsSummaryResponse V1getFleetHosLogsSummary(ctx).After(after).Limit(limit).Execute()

Get current HOS status for all drivers



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getFleetHosLogsSummaryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **string** | Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the &#39;limit&#39; parameter. | 
 **limit** | **float32** | Pagination parameter indicating the number of results to return in this request. Used in conjunction with &#39;after&#39;. | 

### Return type

[**V1HosLogsSummaryResponse**](V1HosLogsSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

