# \DriversApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateDriver**](DriversApi.md#CreateDriver) | **Post** /fleet/drivers | Create a driver
[**GetDriverById**](DriversApi.md#GetDriverById) | **Get** /fleet/drivers/{id} | Retrieve a driver
[**GetDriverTachographActivity**](DriversApi.md#GetDriverTachographActivity) | **Get** /fleet/drivers/tachograph-activity/history | Get driver tachograph activity
[**GetDrivers**](DriversApi.md#GetDrivers) | **Get** /fleet/drivers | List all drivers
[**UpdateDriverById**](DriversApi.md#UpdateDriverById) | **Patch** /fleet/drivers/{id} | Update a driver



## CreateDriver

> InlineResponse2003 CreateDriver(ctx).Driver(driver).Execute()

Create a driver



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateDriverRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver** | [**DriverCreate**](DriverCreate.md) | The driver to create. | 

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


## GetDriverById

> InlineResponse2003 GetDriverById(ctx, id).Execute()

Retrieve a driver



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDriverByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**InlineResponse2003**](inline_response_200_3.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDriverTachographActivity

> DriverTachographActivityResponse GetDriverTachographActivity(ctx).StartTime(startTime).EndTime(endTime).DriverIds(driverIds).After(after).Execute()

Get driver tachograph activity



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetDriverTachographActivityRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startTime** | **time.Time** | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **endTime** | **time.Time** | An end time in RFC 3339 format. It can&#39;t be more than 30 days past startTime. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **driverIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of driver IDs. Currently only support querying by a single ID. Example: &#x60;driverIds&#x3D;1234&#x60; | 
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 

### Return type

[**DriverTachographActivityResponse**](DriverTachographActivityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDrivers

> map[string]interface{} GetDrivers(ctx).IsDeactivated(isDeactivated).Limit(limit).After(after).TagIds(tagIds).Execute()

List all drivers



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetDriversRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isDeactivated** | **bool** | If value is true, only drivers that are deactivated will appear in the response. This parameter will default to false if not provided (fetching only active drivers). | 
 **limit** | **int64** | The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [default to 512]
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 

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


## UpdateDriverById

> InlineResponse2003 UpdateDriverById(ctx, id).Driver(driver).Execute()

Update a driver



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateDriverByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **driver** | [**DriverUpdate**](DriverUpdate.md) | Updates to the driver properties. | 

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

