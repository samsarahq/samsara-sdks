# samsara.SafetyApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1get_driver_safety_score**](SafetyApi.md#v1get_driver_safety_score) | **GET** /v1/fleet/drivers/{driverId}/safety/score | Fetch driver safety score
[**v1get_vehicle_harsh_event**](SafetyApi.md#v1get_vehicle_harsh_event) | **GET** /v1/fleet/vehicles/{vehicleId}/safety/harsh_event | Fetch harsh events
[**v1get_vehicle_safety_score**](SafetyApi.md#v1get_vehicle_safety_score) | **GET** /v1/fleet/vehicles/{vehicleId}/safety/score | Fetch vehicle safety scores


# **v1get_driver_safety_score**
> V1DriverSafetyScoreResponse v1get_driver_safety_score(driver_id, start_ms, end_ms)

Fetch driver safety score

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch the safety score for the driver.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.SafetyApi()
driver_id = 56 # int | ID of the driver. Must contain only digits 0-9.
start_ms = 56 # int | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.
end_ms = 56 # int | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.

try:
    # Fetch driver safety score
    api_response = api_instance.v1get_driver_safety_score(driver_id, start_ms, end_ms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SafetyApi->v1get_driver_safety_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| ID of the driver. Must contain only digits 0-9. | 
 **start_ms** | **int**| Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. | 
 **end_ms** | **int**| Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. | 

### Return type

[**V1DriverSafetyScoreResponse**](V1DriverSafetyScoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Safety score details. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vehicle_harsh_event**
> V1VehicleHarshEventResponse v1get_vehicle_harsh_event(vehicle_id, timestamp)

Fetch harsh events

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch harsh event details for a vehicle.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.SafetyApi()
vehicle_id = 56 # int | ID of the vehicle. Must contain only digits 0-9.
timestamp = 56 # int | Timestamp in milliseconds representing the timestamp of a harsh event.

try:
    # Fetch harsh events
    api_response = api_instance.v1get_vehicle_harsh_event(vehicle_id, timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SafetyApi->v1get_vehicle_harsh_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| ID of the vehicle. Must contain only digits 0-9. | 
 **timestamp** | **int**| Timestamp in milliseconds representing the timestamp of a harsh event. | 

### Return type

[**V1VehicleHarshEventResponse**](V1VehicleHarshEventResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Harsh event details. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vehicle_safety_score**
> V1VehicleSafetyScoreResponse v1get_vehicle_safety_score(vehicle_id, start_ms, end_ms)

Fetch vehicle safety scores

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch the safety score for the vehicle.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.SafetyApi()
vehicle_id = 56 # int | ID of the vehicle. Must contain only digits 0-9.
start_ms = 56 # int | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.
end_ms = 56 # int | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.

try:
    # Fetch vehicle safety scores
    api_response = api_instance.v1get_vehicle_safety_score(vehicle_id, start_ms, end_ms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SafetyApi->v1get_vehicle_safety_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| ID of the vehicle. Must contain only digits 0-9. | 
 **start_ms** | **int**| Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. | 
 **end_ms** | **int**| Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. | 

### Return type

[**V1VehicleSafetyScoreResponse**](V1VehicleSafetyScoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Safety score details. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

