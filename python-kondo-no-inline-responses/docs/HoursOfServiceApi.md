# openapi_client.HoursOfServiceApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1get_fleet_drivers_hos_daily_logs**](HoursOfServiceApi.md#v1get_fleet_drivers_hos_daily_logs) | **POST** /v1/fleet/drivers/{driver_id}/hos_daily_logs | Get daily HOS logs for a specific driver
[**v1get_fleet_hos_authentication_logs**](HoursOfServiceApi.md#v1get_fleet_hos_authentication_logs) | **GET** /v1/fleet/hos_authentication_logs | Get HOS signin and signout
[**v1get_fleet_hos_logs**](HoursOfServiceApi.md#v1get_fleet_hos_logs) | **POST** /v1/fleet/hos_logs | Get HOS logs for a specific driver
[**v1get_fleet_hos_logs_summary**](HoursOfServiceApi.md#v1get_fleet_hos_logs_summary) | **GET** /v1/fleet/hos_logs_summary | Get current HOS status for all drivers


# **v1get_fleet_drivers_hos_daily_logs**
> V1DriverDailyLogResponse v1get_fleet_drivers_hos_daily_logs(driver_id, hos_logs_param=hos_logs_param)

Get daily HOS logs for a specific driver

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get summarized daily Hours of Service charts for a specified driver.  The response will contain a list of `days`, where each entry in the list is the driver's summarized hours of service for that entire day.  The time range for a \"day\" is defined by the `driver`'s `eldDayStartHour`. By default, this is `0`, which indicates the `driver`'s \"day\" is from midnight to midnight in the `driver`'s respective `timezone`. This value is configurable per driver.  The `startMs` and `endMs` parameters indicate start and end for the date range you'd like to query. These parameters are inclusive. This means that the response will include the \"day\" that contains `startMs` and the \"day\" that contains `endMs`. For example:  Let's say a `driver`'s `eldDayStartHour` is `0` and their timezone is `America/Chicago`.  If `startMs` was `1576080000000` (December 11, 2019 10:00:00 AM America/Chicago) and an `endMs` was `1576166400000` (December 12, 2019 10:00:00 AM America/Los_Angeles), then the response will contain a two `day` entries: [December 11, 2019 12:00:00 AM America/Chicago to December 12, 2019 12:00:00 AM America/Chicago], and [December 12, 2019 12:00:00 AM America/Chicago to December 13, 2019 12:00:00 AM America/Chicago].

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.HoursOfServiceApi()
driver_id = 56 # int | ID of the driver with HOS logs.
hos_logs_param = openapi_client.InlineObject() # InlineObject |  (optional)

try:
    # Get daily HOS logs for a specific driver
    api_response = api_instance.v1get_fleet_drivers_hos_daily_logs(driver_id, hos_logs_param=hos_logs_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HoursOfServiceApi->v1get_fleet_drivers_hos_daily_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| ID of the driver with HOS logs. | 
 **hos_logs_param** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

[**V1DriverDailyLogResponse**](V1DriverDailyLogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Distance traveled and time active for each driver in the organization over the specified time period. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_fleet_hos_authentication_logs**
> V1HosAuthenticationLogsResponse v1get_fleet_hos_authentication_logs(driver_id, start_ms, end_ms)

Get HOS signin and signout

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the HOS (hours of service) signin and signout logs for the specified driver. The response includes 4 fields that are now deprecated.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.HoursOfServiceApi()
driver_id = 56 # int | Driver ID to query.
start_ms = 56 # int | Beginning of the time range, specified in milliseconds UNIX time.
end_ms = 56 # int | End of the time range, specified in milliseconds UNIX time.

try:
    # Get HOS signin and signout
    api_response = api_instance.v1get_fleet_hos_authentication_logs(driver_id, start_ms, end_ms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HoursOfServiceApi->v1get_fleet_hos_authentication_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| Driver ID to query. | 
 **start_ms** | **int**| Beginning of the time range, specified in milliseconds UNIX time. | 
 **end_ms** | **int**| End of the time range, specified in milliseconds UNIX time. | 

### Return type

[**V1HosAuthenticationLogsResponse**](V1HosAuthenticationLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HOS authentication logs for the specified driver. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_fleet_hos_logs**
> V1HosLogsResponse v1get_fleet_hos_logs(hos_logs_param)

Get HOS logs for a specific driver

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the HOS (hours of service) logs for the specified driver. This method returns all the HOS statuses that the driver was in during this time period.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.HoursOfServiceApi()
hos_logs_param = openapi_client.InlineObject1() # InlineObject1 | 

try:
    # Get HOS logs for a specific driver
    api_response = api_instance.v1get_fleet_hos_logs(hos_logs_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HoursOfServiceApi->v1get_fleet_hos_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hos_logs_param** | [**InlineObject1**](InlineObject1.md)|  | 

### Return type

[**V1HosLogsResponse**](V1HosLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HOS logs for the specified driver. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_fleet_hos_logs_summary**
> V1HosLogsSummaryResponse v1get_fleet_hos_logs_summary(after=after, limit=limit)

Get current HOS status for all drivers

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the current HOS status for all drivers. Note that this includes inactive as well as active drivers. You may need to upgrade your API token to version 2019-07-31 or later to leverage response pagination. [See here](https://kb.samsara.com/hc/en-us/articles/360026132972-Upgrading-API-Tokens)

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.HoursOfServiceApi()
after = 'after_example' # str | Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. (optional)
limit = 3.4 # float | Pagination parameter indicating the number of results to return in this request. Used in conjunction with 'after'. (optional)

try:
    # Get current HOS status for all drivers
    api_response = api_instance.v1get_fleet_hos_logs_summary(after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HoursOfServiceApi->v1get_fleet_hos_logs_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the &#39;limit&#39; parameter. | [optional] 
 **limit** | **float**| Pagination parameter indicating the number of results to return in this request. Used in conjunction with &#39;after&#39;. | [optional] 

### Return type

[**V1HosLogsSummaryResponse**](V1HosLogsSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HOS logs for the specified driver. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

