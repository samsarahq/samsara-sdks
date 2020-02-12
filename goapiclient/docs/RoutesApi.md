# \RoutesApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateRoute**](RoutesApi.md#CreateRoute) | **Post** /fleet/routes | Create a route.
[**DeleteRouteById**](RoutesApi.md#DeleteRouteById) | **Delete** /fleet/routes/{id} | Delete a single route
[**GetRoute**](RoutesApi.md#GetRoute) | **Get** /fleet/routes/{id} | Get information about a single route
[**V1createDispatchRoute**](RoutesApi.md#V1createDispatchRoute) | **Post** /v1/fleet/dispatch/routes | Create a new route
[**V1deleteDispatchRouteById**](RoutesApi.md#V1deleteDispatchRouteById) | **Delete** /v1/fleet/dispatch/routes/{route_id} | Delete a route
[**V1fetchAllDispatchRoutes**](RoutesApi.md#V1fetchAllDispatchRoutes) | **Get** /v1/fleet/dispatch/routes | Get all routes
[**V1fetchAllRouteJobUpdates**](RoutesApi.md#V1fetchAllRouteJobUpdates) | **Get** /v1/fleet/dispatch/routes/job_updates | Get route updates
[**V1getDispatchRouteById**](RoutesApi.md#V1getDispatchRouteById) | **Get** /v1/fleet/dispatch/routes/{route_id} | Get a route
[**V1getDispatchRouteHistory**](RoutesApi.md#V1getDispatchRouteHistory) | **Get** /v1/fleet/dispatch/routes/{route_id}/history | Get route history
[**V1updateDispatchRouteById**](RoutesApi.md#V1updateDispatchRouteById) | **Put** /v1/fleet/dispatch/routes/{route_id} | Update a route



## CreateRoute

> map[string]interface{} CreateRoute(ctx).Route(route).Execute()

Create a route.



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateRouteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route** | [**CreateRouteRequest**](CreateRouteRequest.md) | Add a route. | 

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


## DeleteRouteById

> DeleteRouteById(ctx, id).Execute()

Delete a single route



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Unique identifier for the route. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteRouteByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetRoute

> map[string]interface{} GetRoute(ctx, id).Execute()

Get information about a single route



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Unique identifier for the route. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetRouteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


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


## V1createDispatchRoute

> V1DispatchRoute V1createDispatchRoute(ctx).CreateDispatchRouteParams(createDispatchRouteParams).Execute()

Create a new route



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1createDispatchRouteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createDispatchRouteParams** | [**V1DispatchRouteCreate**](V1DispatchRouteCreate.md) |  | 

### Return type

[**V1DispatchRoute**](V1DispatchRoute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1deleteDispatchRouteById

> V1deleteDispatchRouteById(ctx, routeId).Execute()

Delete a route



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**routeId** | **int64** | ID of the dispatch route. Must contain only digits 0-9. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1deleteDispatchRouteByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1fetchAllDispatchRoutes

> []V1DispatchRouteWithoutEta V1fetchAllDispatchRoutes(ctx).EndTime(endTime).Duration(duration).Execute()

Get all routes



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1fetchAllDispatchRoutesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endTime** | **int64** | Time in unix milliseconds that represents the end time of the requested time interval. See above for a description of how routes are returned. Defaults to now. | 
 **duration** | **int64** | Time in milliseconds that represents the duration before end_time to query. Defaults to 24 hours. | 

### Return type

[**[]V1DispatchRouteWithoutEta**](V1DispatchRouteWithoutETA.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1fetchAllRouteJobUpdates

> V1allRouteJobUpdates V1fetchAllRouteJobUpdates(ctx).SequenceId(sequenceId).Include(include).Execute()

Get route updates



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1fetchAllRouteJobUpdatesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequenceId** | **string** | Sequence ID from the response payload of the last request. Defaults to fetching updates from last 24 hours. | 
 **include** | **string** | Optionally set include&#x3D;route to include route object in response payload. | 

### Return type

[**V1allRouteJobUpdates**](V1allRouteJobUpdates.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getDispatchRouteById

> V1DispatchRoute V1getDispatchRouteById(ctx, routeId).Execute()

Get a route



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**routeId** | **int64** | ID of the dispatch route. Must contain only digits 0-9. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1getDispatchRouteByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**V1DispatchRoute**](V1DispatchRoute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getDispatchRouteHistory

> V1DispatchRouteHistory V1getDispatchRouteHistory(ctx, routeId).StartTime(startTime).EndTime(endTime).Execute()

Get route history



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**routeId** | **int64** | ID of the route with history. Must contain only digits 0-9. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1getDispatchRouteHistoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **startTime** | **int64** | Timestamp representing the start of the period to fetch, inclusive. Used in combination with end_time. Defaults to 0. | 
 **endTime** | **int64** | Timestamp representing the end of the period to fetch, inclusive. Used in combination with start_time. Defaults to nowMs. | 

### Return type

[**V1DispatchRouteHistory**](V1DispatchRouteHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1updateDispatchRouteById

> V1DispatchRoute V1updateDispatchRouteById(ctx, routeId).UpdateDispatchRouteParams(updateDispatchRouteParams).Execute()

Update a route



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**routeId** | **int64** | ID of the dispatch route. Must contain only digits 0-9. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1updateDispatchRouteByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateDispatchRouteParams** | [**V1DispatchRouteUpdate**](V1DispatchRouteUpdate.md) |  | 

### Return type

[**V1DispatchRoute**](V1DispatchRoute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

