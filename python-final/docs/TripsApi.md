# samsara.TripsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1get_fleet_trips**](TripsApi.md#v1get_fleet_trips) | **GET** /v1/fleet/trips | Get vehicle trips


# **v1get_fleet_trips**
> V1TripResponse v1get_fleet_trips(vehicle_id, start_ms, end_ms)

Get vehicle trips

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get historical trips data for specified vehicle. This method returns a set of historical trips data for the specified vehicle in the specified time range.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.TripsApi()
vehicle_id = 56 # int | Vehicle ID to query.
start_ms = 56 # int | Beginning of the time range, specified in milliseconds UNIX time. Limited to a 90 day window with respect to startMs and endMs
end_ms = 56 # int | End of the time range, specified in milliseconds UNIX time.

try:
    # Get vehicle trips
    api_response = api_instance.v1get_fleet_trips(vehicle_id, start_ms, end_ms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TripsApi->v1get_fleet_trips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| Vehicle ID to query. | 
 **start_ms** | **int**| Beginning of the time range, specified in milliseconds UNIX time. Limited to a 90 day window with respect to startMs and endMs | 
 **end_ms** | **int**| End of the time range, specified in milliseconds UNIX time. | 

### Return type

[**V1TripResponse**](V1TripResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of trips taken by the requested vehicle within the specified timeframe. Ongoing trips will be returned with 9223372036854775807 as their endMs. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

