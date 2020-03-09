# \SensorsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1getSensors**](SensorsApi.md#V1getSensors) | **Post** /v1/sensors/list | Get all sensors
[**V1getSensorsCargo**](SensorsApi.md#V1getSensorsCargo) | **Post** /v1/sensors/cargo | Get cargo status
[**V1getSensorsDoor**](SensorsApi.md#V1getSensorsDoor) | **Post** /v1/sensors/door | Get door status
[**V1getSensorsHistory**](SensorsApi.md#V1getSensorsHistory) | **Post** /v1/sensors/history | Get sensor history
[**V1getSensorsHumidity**](SensorsApi.md#V1getSensorsHumidity) | **Post** /v1/sensors/humidity | Get humidity
[**V1getSensorsTemperature**](SensorsApi.md#V1getSensorsTemperature) | **Post** /v1/sensors/temperature | Get temperature



## V1getSensors

> InlineResponse20015 V1getSensors(ctx).Execute()

Get all sensors



### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1getSensorsRequest struct via the builder pattern


### Return type

[**InlineResponse20015**](inline_response_200_15.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getSensorsCargo

> V1CargoResponse V1getSensorsCargo(ctx).V1sensorParam(v1sensorParam).Execute()

Get cargo status



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getSensorsCargoRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1sensorParam** | [**InlineObject7**](InlineObject7.md) |  | 

### Return type

[**V1CargoResponse**](V1CargoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getSensorsDoor

> V1DoorResponse V1getSensorsDoor(ctx).V1sensorParam(v1sensorParam).Execute()

Get door status



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getSensorsDoorRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1sensorParam** | [**InlineObject8**](InlineObject8.md) |  | 

### Return type

[**V1DoorResponse**](V1DoorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getSensorsHistory

> V1SensorHistoryResponse V1getSensorsHistory(ctx).HistoryParam(historyParam).Execute()

Get sensor history



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getSensorsHistoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **historyParam** | [**InlineObject9**](InlineObject9.md) |  | 

### Return type

[**V1SensorHistoryResponse**](V1SensorHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getSensorsHumidity

> V1HumidityResponse V1getSensorsHumidity(ctx).V1sensorParam(v1sensorParam).Execute()

Get humidity



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getSensorsHumidityRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1sensorParam** | [**InlineObject10**](InlineObject10.md) |  | 

### Return type

[**V1HumidityResponse**](V1HumidityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getSensorsTemperature

> V1TemperatureResponse V1getSensorsTemperature(ctx).V1sensorParam(v1sensorParam).Execute()

Get temperature



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getSensorsTemperatureRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1sensorParam** | [**InlineObject11**](InlineObject11.md) |  | 

### Return type

[**V1TemperatureResponse**](V1TemperatureResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

