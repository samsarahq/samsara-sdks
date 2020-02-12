# \TripsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1getFleetTrips**](TripsApi.md#V1getFleetTrips) | **Get** /v1/fleet/trips | Get vehicle trips



## V1getFleetTrips

> V1TripResponse V1getFleetTrips(ctx).VehicleId(vehicleId).StartMs(startMs).EndMs(endMs).Execute()

Get vehicle trips



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getFleetTripsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicleId** | **int64** | Vehicle ID to query. | 
 **startMs** | **int32** | Beginning of the time range, specified in milliseconds UNIX time. Limited to a 90 day window with respect to startMs and endMs | 
 **endMs** | **int32** | End of the time range, specified in milliseconds UNIX time. | 

### Return type

[**V1TripResponse**](V1TripResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

