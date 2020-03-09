# \DriversApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateDriver**](DriversApi.md#CreateDriver) | **Post** /fleet/drivers | Create a driver
[**GetDriver**](DriversApi.md#GetDriver) | **Get** /fleet/drivers/{id} | Retrieve a driver
[**GetDriverTachographActivity**](DriversApi.md#GetDriverTachographActivity) | **Get** /fleet/drivers/tachograph-activity/history | Get driver tachograph activity
[**ListDrivers**](DriversApi.md#ListDrivers) | **Get** /fleet/drivers | List all drivers
[**UpdateDriver**](DriversApi.md#UpdateDriver) | **Patch** /fleet/drivers/{id} | Update a driver



## CreateDriver

> DriverResponse CreateDriver(ctx).Driver(driver).Execute()

Create a driver



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateDriverRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver** | [**CreateDriverRequest**](CreateDriverRequest.md) | The driver to create. | 

### Return type

[**DriverResponse**](DriverResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDriver

> DriverResponse GetDriver(ctx, id).Execute()

Retrieve a driver



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDriverRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**DriverResponse**](DriverResponse.md)

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


## ListDrivers

> ListDriversResponse ListDrivers(ctx).DriverActivationStatus(driverActivationStatus).Limit(limit).After(after).TagIds(tagIds).UpdatedAfterTime(updatedAfterTime).CreatedAfterTime(createdAfterTime).Execute()

List all drivers



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListDriversRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driverActivationStatus** | **string** | If value is &#x60;deactivated&#x60;, only drivers that are deactivated will appear in the response. This parameter will default to &#x60;active&#x60; if not provided (fetching only active drivers). | 
 **limit** | **int64** | The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [default to 512]
 **after** | **string** | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | 
 **tagIds** | [**[]string**](string.md) | A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | 
 **updatedAfterTime** | **time.Time** | A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **createdAfterTime** | **time.Time** | A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 

### Return type

[**ListDriversResponse**](ListDriversResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateDriver

> DriverResponse UpdateDriver(ctx, id).Driver(driver).Execute()

Update a driver



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateDriverRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **driver** | [**UpdateDriverRequest**](UpdateDriverRequest.md) | Updates to the driver properties. | 

### Return type

[**DriverResponse**](DriverResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

