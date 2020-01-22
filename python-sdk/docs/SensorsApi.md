# samsara.SensorsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1get_sensors**](SensorsApi.md#v1get_sensors) | **POST** /v1/sensors/list | Get all sensors
[**v1get_sensors_cargo**](SensorsApi.md#v1get_sensors_cargo) | **POST** /v1/sensors/cargo | Get cargo status
[**v1get_sensors_door**](SensorsApi.md#v1get_sensors_door) | **POST** /v1/sensors/door | Get door status
[**v1get_sensors_history**](SensorsApi.md#v1get_sensors_history) | **POST** /v1/sensors/history | Get sensor history
[**v1get_sensors_humidity**](SensorsApi.md#v1get_sensors_humidity) | **POST** /v1/sensors/humidity | Get humidity
[**v1get_sensors_temperature**](SensorsApi.md#v1get_sensors_temperature) | **POST** /v1/sensors/temperature | Get temperature


# **v1get_sensors**
> InlineResponse20017 v1get_sensors()

Get all sensors

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get sensor objects. This method returns a list of the sensor objects in the Samsara Cloud and information about them.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.SensorsApi()

try:
    # Get all sensors
    api_response = api_instance.v1get_sensors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->v1get_sensors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sensor objects. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_cargo**
> V1CargoResponse v1get_sensors_cargo(v1sensor_param)

Get cargo status

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get cargo monitor status (empty / full) for requested sensors.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.SensorsApi()
v1sensor_param = samsara.InlineObject5() # InlineObject5 | 

try:
    # Get cargo status
    api_response = api_instance.v1get_sensors_cargo(v1sensor_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->v1get_sensors_cargo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1sensor_param** | [**InlineObject5**](InlineObject5.md)|  | 

### Return type

[**V1CargoResponse**](V1CargoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sensor objects containing the current cargo status reported by each sensor. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_door**
> V1DoorResponse v1get_sensors_door(v1sensor_param)

Get door status

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get door monitor status (closed / open) for requested sensors.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.SensorsApi()
v1sensor_param = samsara.InlineObject6() # InlineObject6 | 

try:
    # Get door status
    api_response = api_instance.v1get_sensors_door(v1sensor_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->v1get_sensors_door: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1sensor_param** | [**InlineObject6**](InlineObject6.md)|  | 

### Return type

[**V1DoorResponse**](V1DoorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sensor objects containing the current door status reported by each sensor. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_history**
> V1SensorHistoryResponse v1get_sensors_history(history_param)

Get sensor history

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get historical data for specified sensors. This method returns a set of historical data for the specified sensors in the specified time range and at the specified time resolution.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.SensorsApi()
history_param = samsara.InlineObject7() # InlineObject7 | 

try:
    # Get sensor history
    api_response = api_instance.v1get_sensors_history(history_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->v1get_sensors_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_param** | [**InlineObject7**](InlineObject7.md)|  | 

### Return type

[**V1SensorHistoryResponse**](V1SensorHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of results objects, each containing a time and a datapoint for each requested sensor/field pair. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_humidity**
> V1HumidityResponse v1get_sensors_humidity(v1sensor_param)

Get humidity

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get humidity for requested sensors. This method returns the current relative humidity for the requested sensors.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.SensorsApi()
v1sensor_param = samsara.InlineObject8() # InlineObject8 | 

try:
    # Get humidity
    api_response = api_instance.v1get_sensors_humidity(v1sensor_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->v1get_sensors_humidity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1sensor_param** | [**InlineObject8**](InlineObject8.md)|  | 

### Return type

[**V1HumidityResponse**](V1HumidityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sensor objects containing the current humidity reported by each sensor. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_temperature**
> V1TemperatureResponse v1get_sensors_temperature(v1sensor_param)

Get temperature

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get temperature for requested sensors. This method returns the current ambient temperature (and probe temperature if applicable) for the requested sensors.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.SensorsApi()
v1sensor_param = samsara.InlineObject9() # InlineObject9 | 

try:
    # Get temperature
    api_response = api_instance.v1get_sensors_temperature(v1sensor_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->v1get_sensors_temperature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1sensor_param** | [**InlineObject9**](InlineObject9.md)|  | 

### Return type

[**V1TemperatureResponse**](V1TemperatureResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sensor objects containing the current temperature reported by each sensor. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

