# swagger_client.IndustrialApi

All URIs are relative to *https://api.samsara.com/*

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
> V1VisionRunsByCameraResponse get_vision_runs_by_camera(camera_id, duration_ms, end_ms=end_ms)

Fetch runs by camera

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch runs by camera.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustrialApi()
camera_id = 789 # int | The camera_id should be valid for the given accessToken.
duration_ms = 789 # int | DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched
end_ms = 789 # int | EndMs is an optional param. It will default to the current time. (optional)

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

[**V1VisionRunsByCameraResponse**](V1VisionRunsByCameraResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_all_data_inputs**
> object v1get_all_data_inputs(start_ms=start_ms, end_ms=end_ms)

Get industrial data

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all of the data inputs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustrialApi()
start_ms = 789 # int | Timestamp in unix milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. defaults to nowMs. (optional)
end_ms = 789 # int | Timestamp in unix milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Defaults to nowMs. (optional)

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

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_cameras**
> V1VisionCamerasResponse v1get_cameras()

Fetch industrial cameras

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all cameras.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustrialApi()

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

[**V1VisionCamerasResponse**](V1VisionCamerasResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_data_input**
> V1DataInputHistoryResponse v1get_data_input(data_input_id, start_ms=start_ms, end_ms=end_ms)

Get industrial data from a specific device

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch datapoints from a given data input.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustrialApi()
data_input_id = 789 # int | ID of the data input. Must contain only digits 0-9.
start_ms = 789 # int | Timestamp in unix milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. defaults to nowMs. (optional)
end_ms = 789 # int | Timestamp in unix milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Defaults to nowMs. (optional)

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_machines**
> object v1get_machines()

Get machines

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get machine objects. This method returns a list of the machine objects in the Samsara Cloud and information about them.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustrialApi()

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

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_machines_history**
> V1MachineHistoryResponse v1get_machines_history(body)

Get machine history

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get historical data for machine objects. This method returns a set of historical data for all machines

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustrialApi()
body = NULL # object | Time range to query for events

try:
    # Get machine history
    api_response = api_instance.v1get_machines_history(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustrialApi->v1get_machines_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Time range to query for events | 

### Return type

[**V1MachineHistoryResponse**](V1MachineHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vision_latest_run_camera**
> V1VisionRunByCameraResponse v1get_vision_latest_run_camera(camera_id, program_id=program_id, started_at_ms=started_at_ms, include=include, limit=limit)

Fetch the latest run for a camera or program

Fetch the latest run for a camera or program by default. If startedAtMs is supplied, fetch the specific run that corresponds to that start time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustrialApi()
camera_id = 789 # int | The camera_id should be valid for the given accessToken.
program_id = 789 # int | The configured program's ID on the camera. (optional)
started_at_ms = 789 # int | EndMs is an optional param. It will default to the current time. (optional)
include = 'include_example' # str | Include is a filter parameter. Accepts 'pass', 'reject' or 'no_read'. (optional)
limit = 789 # int | Limit is an integer value from 1 to 1,000. (optional)

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
 **program_id** | **int**| The configured program&#x27;s ID on the camera. | [optional] 
 **started_at_ms** | **int**| EndMs is an optional param. It will default to the current time. | [optional] 
 **include** | **str**| Include is a filter parameter. Accepts &#x27;pass&#x27;, &#x27;reject&#x27; or &#x27;no_read&#x27;. | [optional] 
 **limit** | **int**| Limit is an integer value from 1 to 1,000. | [optional] 

### Return type

[**V1VisionRunByCameraResponse**](V1VisionRunByCameraResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vision_programs_by_camera**
> V1ProgramsForTheCameraResponse v1get_vision_programs_by_camera(camera_id)

Fetch industrial camera programs

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch configured programs on the camera.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustrialApi()
camera_id = 789 # int | The camera_id should be valid for the given accessToken.

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

[**V1ProgramsForTheCameraResponse**](V1ProgramsForTheCameraResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vision_runs**
> V1VisionRunsResponse v1get_vision_runs(duration_ms, end_ms=end_ms)

Fetch runs

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch runs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustrialApi()
duration_ms = 789 # int | DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched
end_ms = 789 # int | EndMs is an optional param. It will default to the current time. (optional)

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vision_runs_by_camera_and_program**
> V1VisionRunsByCameraAndProgramResponse v1get_vision_runs_by_camera_and_program(camera_id, program_id, started_at_ms, include=include)

Fetch runs by camera and program

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch runs by camera and program.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustrialApi()
camera_id = 789 # int | The camera_id should be valid for the given accessToken.
program_id = 789 # int | The configured program's ID on the camera.
started_at_ms = 789 # int | Started_at_ms is a required param. Indicates the start time of the run to be fetched.
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
 **program_id** | **int**| The configured program&#x27;s ID on the camera. | 
 **started_at_ms** | **int**| Started_at_ms is a required param. Indicates the start time of the run to be fetched. | 
 **include** | **str**| Include is a filter parameter. Accepts &#x27;pass&#x27;, &#x27;reject&#x27; or &#x27;no_read&#x27;. | [optional] 

### Return type

[**V1VisionRunsByCameraAndProgramResponse**](V1VisionRunsByCameraAndProgramResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

