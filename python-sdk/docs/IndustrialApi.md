# samsara.IndustrialApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vision_runs_by_camera**](IndustrialApi.md#get_vision_runs_by_camera) | **GET** /v1/industrial/vision/runs/{camera_id} | Fetch runs by camera
[**v1get_all_data_inputs**](IndustrialApi.md#v1get_all_data_inputs) | **GET** /v1/industrial/data | Get industrial data
[**v1get_cameras**](IndustrialApi.md#v1get_cameras) | **GET** /v1/industrial/vision/cameras | Fetch industrial cameras
[**v1get_data_input**](IndustrialApi.md#v1get_data_input) | **GET** /v1/industrial/data/{data_input_id} | Get industrial data from a specific device
[**v1get_machines**](IndustrialApi.md#v1get_machines) | **POST** /v1/machines/list | Get machines
[**v1get_machines_history**](IndustrialApi.md#v1get_machines_history) | **POST** /v1/machines/history | Get machine history
[**v1get_vision_latest_run_camera**](IndustrialApi.md#v1get_vision_latest_run_camera) | **GET** /v1/industrial/vision/run/camera/{camera_id} | Fetch the latest run for a camera or program
[**v1get_vision_programs_by_camera**](IndustrialApi.md#v1get_vision_programs_by_camera) | **GET** /v1/industrial/vision/cameras/{camera_id}/programs | Fetch industrial camera programs
[**v1get_vision_runs**](IndustrialApi.md#v1get_vision_runs) | **GET** /v1/industrial/vision/runs | Fetch runs
[**v1get_vision_runs_by_camera_and_program**](IndustrialApi.md#v1get_vision_runs_by_camera_and_program) | **GET** /v1/industrial/vision/runs/{camera_id}/{program_id}/{started_at_ms} | Fetch runs by camera and program


# **get_vision_runs_by_camera**
> list[object] get_vision_runs_by_camera(camera_id, duration_ms, end_ms=end_ms)

Fetch runs by camera

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch runs by camera.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.IndustrialApi(api_client)
    camera_id = 56 # int | The camera_id should be valid for the given accessToken.
duration_ms = 56 # int | DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched
end_ms = 56 # int | EndMs is an optional param. It will default to the current time. (optional)

    try:
        # Fetch runs by camera
        api_response = api_instance.get_vision_runs_by_camera(camera_id, duration_ms, end_ms=end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndustrialApi->get_vision_runs_by_camera: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **camera_id** | **int**| The camera_id should be valid for the given accessToken. | 
 **duration_ms** | **int**| DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched | 
 **end_ms** | **int**| EndMs is an optional param. It will default to the current time. | [optional] 

### Return type

**list[object]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return runs by cameraId. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_all_data_inputs**
> InlineResponse2007 v1get_all_data_inputs(start_ms=start_ms, end_ms=end_ms)

Get industrial data

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all of the data inputs.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.IndustrialApi(api_client)
    start_ms = 56 # int | Timestamp in unix milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. defaults to nowMs. (optional)
end_ms = 56 # int | Timestamp in unix milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Defaults to nowMs. (optional)

    try:
        # Get industrial data
        api_response = api_instance.v1get_all_data_inputs(start_ms=start_ms, end_ms=end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndustrialApi->v1get_all_data_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_ms** | **int**| Timestamp in unix milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. defaults to nowMs. | [optional] 
 **end_ms** | **int**| Timestamp in unix milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Defaults to nowMs. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of data inputs. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_cameras**
> list[object] v1get_cameras()

Fetch industrial cameras

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all cameras.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.IndustrialApi(api_client)
    
    try:
        # Fetch industrial cameras
        api_response = api_instance.v1get_cameras()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndustrialApi->v1get_cameras: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns details about a camera. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_data_input**
> V1DataInputHistoryResponse v1get_data_input(data_input_id, start_ms=start_ms, end_ms=end_ms)

Get industrial data from a specific device

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch datapoints from a given data input.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.IndustrialApi(api_client)
    data_input_id = 56 # int | ID of the data input. Must contain only digits 0-9.
start_ms = 56 # int | Timestamp in unix milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. defaults to nowMs. (optional)
end_ms = 56 # int | Timestamp in unix milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Defaults to nowMs. (optional)

    try:
        # Get industrial data from a specific device
        api_response = api_instance.v1get_data_input(data_input_id, start_ms=start_ms, end_ms=end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndustrialApi->v1get_data_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_input_id** | **int**| ID of the data input. Must contain only digits 0-9. | 
 **start_ms** | **int**| Timestamp in unix milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. defaults to nowMs. | [optional] 
 **end_ms** | **int**| Timestamp in unix milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Defaults to nowMs. | [optional] 

### Return type

[**V1DataInputHistoryResponse**](V1DataInputHistoryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns datapoints for the given data input |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_machines**
> InlineResponse2008 v1get_machines()

Get machines

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get machine objects. This method returns a list of the machine objects in the Samsara Cloud and information about them.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.IndustrialApi(api_client)
    
    try:
        # Get machines
        api_response = api_instance.v1get_machines()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndustrialApi->v1get_machines: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of machine objects. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_machines_history**
> V1MachineHistoryResponse v1get_machines_history(history_param)

Get machine history

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get historical data for machine objects. This method returns a set of historical data for all machines

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.IndustrialApi(api_client)
    history_param = samsara.InlineObject4() # InlineObject4 | 

    try:
        # Get machine history
        api_response = api_instance.v1get_machines_history(history_param)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndustrialApi->v1get_machines_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_param** | [**InlineObject4**](InlineObject4.md)|  | 

### Return type

[**V1MachineHistoryResponse**](V1MachineHistoryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of machine results objects, each containing a time and a datapoint. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vision_latest_run_camera**
> V1VisionRunByCameraResponse v1get_vision_latest_run_camera(camera_id, program_id=program_id, started_at_ms=started_at_ms, include=include, limit=limit)

Fetch the latest run for a camera or program

Fetch the latest run for a camera or program by default. If startedAtMs is supplied, fetch the specific run that corresponds to that start time.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.IndustrialApi(api_client)
    camera_id = 56 # int | The camera_id should be valid for the given accessToken.
program_id = 56 # int | The configured program's ID on the camera. (optional)
started_at_ms = 56 # int | EndMs is an optional param. It will default to the current time. (optional)
include = 'include_example' # str | Include is a filter parameter. Accepts 'pass', 'reject' or 'no_read'. (optional)
limit = 56 # int | Limit is an integer value from 1 to 1,000. (optional)

    try:
        # Fetch the latest run for a camera or program
        api_response = api_instance.v1get_vision_latest_run_camera(camera_id, program_id=program_id, started_at_ms=started_at_ms, include=include, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndustrialApi->v1get_vision_latest_run_camera: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **camera_id** | **int**| The camera_id should be valid for the given accessToken. | 
 **program_id** | **int**| The configured program&#39;s ID on the camera. | [optional] 
 **started_at_ms** | **int**| EndMs is an optional param. It will default to the current time. | [optional] 
 **include** | **str**| Include is a filter parameter. Accepts &#39;pass&#39;, &#39;reject&#39; or &#39;no_read&#39;. | [optional] 
 **limit** | **int**| Limit is an integer value from 1 to 1,000. | [optional] 

### Return type

[**V1VisionRunByCameraResponse**](V1VisionRunByCameraResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the details for this run. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vision_programs_by_camera**
> list[object] v1get_vision_programs_by_camera(camera_id)

Fetch industrial camera programs

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch configured programs on the camera.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.IndustrialApi(api_client)
    camera_id = 56 # int | The camera_id should be valid for the given accessToken.

    try:
        # Fetch industrial camera programs
        api_response = api_instance.v1get_vision_programs_by_camera(camera_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndustrialApi->v1get_vision_programs_by_camera: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **camera_id** | **int**| The camera_id should be valid for the given accessToken. | 

### Return type

**list[object]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns programs configured on the camera. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vision_runs**
> V1VisionRunsResponse v1get_vision_runs(duration_ms, end_ms=end_ms)

Fetch runs

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch runs.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.IndustrialApi(api_client)
    duration_ms = 56 # int | DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched
end_ms = 56 # int | EndMs is an optional param. It will default to the current time. (optional)

    try:
        # Fetch runs
        api_response = api_instance.v1get_vision_runs(duration_ms, end_ms=end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndustrialApi->v1get_vision_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duration_ms** | **int**| DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched | 
 **end_ms** | **int**| EndMs is an optional param. It will default to the current time. | [optional] 

### Return type

[**V1VisionRunsResponse**](V1VisionRunsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return runs. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vision_runs_by_camera_and_program**
> V1VisionRunsByCameraAndProgramResponse v1get_vision_runs_by_camera_and_program(camera_id, program_id, started_at_ms, include=include)

Fetch runs by camera and program

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch runs by camera and program.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.IndustrialApi(api_client)
    camera_id = 56 # int | The camera_id should be valid for the given accessToken.
program_id = 56 # int | The configured program's ID on the camera.
started_at_ms = 56 # int | Started_at_ms is a required param. Indicates the start time of the run to be fetched.
include = 'include_example' # str | Include is a filter parameter. Accepts 'pass', 'reject' or 'no_read'. (optional)

    try:
        # Fetch runs by camera and program
        api_response = api_instance.v1get_vision_runs_by_camera_and_program(camera_id, program_id, started_at_ms, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndustrialApi->v1get_vision_runs_by_camera_and_program: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **camera_id** | **int**| The camera_id should be valid for the given accessToken. | 
 **program_id** | **int**| The configured program&#39;s ID on the camera. | 
 **started_at_ms** | **int**| Started_at_ms is a required param. Indicates the start time of the run to be fetched. | 
 **include** | **str**| Include is a filter parameter. Accepts &#39;pass&#39;, &#39;reject&#39; or &#39;no_read&#39;. | [optional] 

### Return type

[**V1VisionRunsByCameraAndProgramResponse**](V1VisionRunsByCameraAndProgramResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return runs by camera ID and program ID. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

