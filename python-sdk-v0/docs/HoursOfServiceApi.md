# swagger_client.HoursOfServiceApi

All URIs are relative to *https://api.samsara.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1get_fleet_drivers_hos_daily_logs**](HoursOfServiceApi.md#v1get_fleet_drivers_hos_daily_logs) | **POST** /v1/fleet/drivers/{driver_id}/hos_daily_logs | Get daily HOS logs for a specific driver
[**v1get_fleet_hos_authentication_logs**](HoursOfServiceApi.md#v1get_fleet_hos_authentication_logs) | **GET** /v1/fleet/hos_authentication_logs | Get HOS signin and signout
[**v1get_fleet_hos_logs**](HoursOfServiceApi.md#v1get_fleet_hos_logs) | **POST** /v1/fleet/hos_logs | Get HOS logs for a specific driver
[**v1get_fleet_hos_logs_summary**](HoursOfServiceApi.md#v1get_fleet_hos_logs_summary) | **GET** /v1/fleet/hos_logs_summary | Get current HOS status for all drivers

# **v1get_fleet_drivers_hos_daily_logs**
> V1DriverDailyLogResponse v1get_fleet_drivers_hos_daily_logs(driver_id, body=body)

Get daily HOS logs for a specific driver

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get summarized daily HOS charts for a specified driver.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HoursOfServiceApi()
driver_id = 789 # int | ID of the driver with HOS logs.
body = NULL # object |  (optional)

try:
    # Get daily HOS logs for a specific driver
    api_response = api_instance.v1get_fleet_drivers_hos_daily_logs(driver_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HoursOfServiceApi->v1get_fleet_drivers_hos_daily_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| ID of the driver with HOS logs. | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**V1DriverDailyLogResponse**](V1DriverDailyLogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_fleet_hos_authentication_logs**
> V1HosAuthenticationLogsResponse v1get_fleet_hos_authentication_logs(driver_id, start_ms, end_ms)

Get HOS signin and signout

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the HOS (hours of service) signin and signout logs for the specified driver. The response includes 4 fields that are now deprecated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HoursOfServiceApi()
driver_id = 789 # int | Driver ID to query.
start_ms = 789 # int | Beginning of the time range, specified in milliseconds UNIX time.
end_ms = 789 # int | End of the time range, specified in milliseconds UNIX time.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_fleet_hos_logs**
> V1HosLogsResponse v1get_fleet_hos_logs(body)

Get HOS logs for a specific driver

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the HOS (hours of service) logs for the specified driver. This method returns all the HOS statuses that the driver was in during this time period.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HoursOfServiceApi()
body = NULL # object | 

try:
    # Get HOS logs for a specific driver
    api_response = api_instance.v1get_fleet_hos_logs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HoursOfServiceApi->v1get_fleet_hos_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 

### Return type

[**V1HosLogsResponse**](V1HosLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_fleet_hos_logs_summary**
> V1HosLogsSummaryResponse v1get_fleet_hos_logs_summary(after=after, limit=limit)

Get current HOS status for all drivers

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the current HOS status for all drivers. Note that this includes inactive as well as active drivers. You may need to upgrade your API token to version 2019-07-31 or later to leverage response pagination. [See here](https://kb.samsara.com/hc/en-us/articles/360026132972-Upgrading-API-Tokens)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HoursOfServiceApi()
after = 'after_example' # str | Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. (optional)
limit = 1.2 # float | Pagination parameter indicating the number of results to return in this request. Used in conjunction with 'after'. (optional)

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
 **after** | **str**| Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the &#x27;limit&#x27; parameter. | [optional] 
 **limit** | **float**| Pagination parameter indicating the number of results to return in this request. Used in conjunction with &#x27;after&#x27;. | [optional] 

### Return type

[**V1HosLogsSummaryResponse**](V1HosLogsSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

