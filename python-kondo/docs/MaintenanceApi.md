# openapi_client.MaintenanceApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1create_dvir**](MaintenanceApi.md#v1create_dvir) | **POST** /v1/fleet/maintenance/dvirs | Create a DVIR
[**v1get_dvirs**](MaintenanceApi.md#v1get_dvirs) | **GET** /v1/fleet/maintenance/dvirs | Get DVIRs
[**v1get_fleet_maintenance_list**](MaintenanceApi.md#v1get_fleet_maintenance_list) | **GET** /v1/fleet/maintenance/list | Get vehicles with engine faults or check lights


# **v1create_dvir**
> V1DvirBase v1create_dvir(create_dvir_param)

Create a DVIR

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Create a new dvir, marking a vehicle or trailer safe or unsafe.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.MaintenanceApi()
create_dvir_param = openapi_client.InlineObject2() # InlineObject2 | 

try:
    # Create a DVIR
    api_response = api_instance.v1create_dvir(create_dvir_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->v1create_dvir: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dvir_param** | [**InlineObject2**](InlineObject2.md)|  | 

### Return type

[**V1DvirBase**](V1DvirBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created DVIR. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_dvirs**
> V1DvirListResponse v1get_dvirs(end_ms, duration_ms)

Get DVIRs

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get DVIRs for the org within provided time constraints

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.MaintenanceApi()
end_ms = 56 # int | Time in millis until the last dvir log.
duration_ms = 56 # int | Time in millis which corresponds to the duration before the end_ms. Must be less than or equal to 90 days.

try:
    # Get DVIRs
    api_response = api_instance.v1get_dvirs(end_ms, duration_ms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->v1get_dvirs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_ms** | **int**| Time in millis until the last dvir log. | 
 **duration_ms** | **int**| Time in millis which corresponds to the duration before the end_ms. Must be less than or equal to 90 days. | 

### Return type

[**V1DvirListResponse**](V1DvirListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DVIRs for the specified duration. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_fleet_maintenance_list**
> InlineResponse20011 v1get_fleet_maintenance_list()

Get vehicles with engine faults or check lights

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get list of the vehicles with any engine faults or check light data.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.MaintenanceApi()

try:
    # Get vehicles with engine faults or check lights
    api_response = api_instance.v1get_fleet_maintenance_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->v1get_fleet_maintenance_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of vehicles and maintenance information about each. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

