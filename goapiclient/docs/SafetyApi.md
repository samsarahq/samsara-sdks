# \SafetyApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetOrgDriverSafetyScores**](SafetyApi.md#GetOrgDriverSafetyScores) | **Get** /fleet/drivers/safety-scores | List all safety scores by driver
[**GetOrgHarshEvents**](SafetyApi.md#GetOrgHarshEvents) | **Get** /fleet/vehicles/harsh-events | List all harsh events
[**GetOrgVehicleSafetyScores**](SafetyApi.md#GetOrgVehicleSafetyScores) | **Get** /fleet/vehicles/safety-scores | List all safety scores by vehicle
[**V1getDriverSafetyScore**](SafetyApi.md#V1getDriverSafetyScore) | **Get** /v1/fleet/drivers/{driverId}/safety/score | Fetch driver safety score
[**V1getVehicleHarshEvent**](SafetyApi.md#V1getVehicleHarshEvent) | **Get** /v1/fleet/vehicles/{vehicleId}/safety/harsh_event | Fetch harsh events
[**V1getVehicleSafetyScore**](SafetyApi.md#V1getVehicleSafetyScore) | **Get** /v1/fleet/vehicles/{vehicleId}/safety/score | Fetch vehicle safety scores



## GetOrgDriverSafetyScores

> OrgSafetyScoresResponse GetOrgDriverSafetyScores(ctx).StartTime(startTime).EndTime(endTime).Execute()

List all safety scores by driver



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetOrgDriverSafetyScoresRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startTime** | **string** | Beginning of the time range, specified in RFC 3339 time. | 
 **endTime** | **string** | End of the time range, specified in RFC 3339 time. | 

### Return type

[**OrgSafetyScoresResponse**](OrgSafetyScoresResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetOrgHarshEvents

> OrgHarshEventsKondoResponse GetOrgHarshEvents(ctx).StartTime(startTime).EndTime(endTime).Execute()

List all harsh events



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetOrgHarshEventsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startTime** | **string** | Beginning of the time range, specified in RFC 3339 time. | 
 **endTime** | **string** | End of the time range, specified in RFC 3339 time. | 

### Return type

[**OrgHarshEventsKondoResponse**](OrgHarshEventsKondoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetOrgVehicleSafetyScores

> OrgSafetyScoresResponse GetOrgVehicleSafetyScores(ctx).StartTime(startTime).EndTime(endTime).Execute()

List all safety scores by vehicle



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetOrgVehicleSafetyScoresRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startTime** | **string** | Beginning of the time range, specified in RFC 3339 time. | 
 **endTime** | **string** | End of the time range, specified in RFC 3339 time. | 

### Return type

[**OrgSafetyScoresResponse**](OrgSafetyScoresResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getDriverSafetyScore

> V1DriverSafetyScoreResponse V1getDriverSafetyScore(ctx, driverId).StartMs(startMs).EndMs(endMs).Execute()

Fetch driver safety score



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driverId** | **int64** | ID of the driver. Must contain only digits 0-9. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1getDriverSafetyScoreRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **startMs** | **int64** | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. | 
 **endMs** | **int64** | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. | 

### Return type

[**V1DriverSafetyScoreResponse**](V1DriverSafetyScoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getVehicleHarshEvent

> V1VehicleHarshEventResponse V1getVehicleHarshEvent(ctx, vehicleId).Timestamp(timestamp).Execute()

Fetch harsh events



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**vehicleId** | **int64** | ID of the vehicle. Must contain only digits 0-9. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1getVehicleHarshEventRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **timestamp** | **int64** | Timestamp in milliseconds representing the timestamp of a harsh event. | 

### Return type

[**V1VehicleHarshEventResponse**](V1VehicleHarshEventResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getVehicleSafetyScore

> V1VehicleSafetyScoreResponse V1getVehicleSafetyScore(ctx, vehicleId).StartMs(startMs).EndMs(endMs).Execute()

Fetch vehicle safety scores



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**vehicleId** | **int64** | ID of the vehicle. Must contain only digits 0-9. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1getVehicleSafetyScoreRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **startMs** | **int64** | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. | 
 **endMs** | **int64** | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. | 

### Return type

[**V1VehicleSafetyScoreResponse**](V1VehicleSafetyScoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

