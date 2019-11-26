# swagger_client.SensorsApi

All URIs are relative to *https://api.samsara.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1get_sensors**](SensorsApi.md#v1get_sensors) | **POST** /v1/sensors/list | Get all sensors
[**v1get_sensors_cargo**](SensorsApi.md#v1get_sensors_cargo) | **POST** /v1/sensors/cargo | Get cargo status
[**v1get_sensors_door**](SensorsApi.md#v1get_sensors_door) | **POST** /v1/sensors/door | Get door status
[**v1get_sensors_history**](SensorsApi.md#v1get_sensors_history) | **POST** /v1/sensors/history | Get sensor history
[**v1get_sensors_humidity**](SensorsApi.md#v1get_sensors_humidity) | **POST** /v1/sensors/humidity | Get humidity
[**v1get_sensors_temperature**](SensorsApi.md#v1get_sensors_temperature) | **POST** /v1/sensors/temperature | Get temperature

# **v1get_sensors**
> object v1get_sensors(body=body)

Get all sensors

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get sensor objects. This method returns a list of the sensor objects in the Samsara Cloud and information about them.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorsApi()
body = NULL # object | Group ID (optional)

try:
    # Get all sensors
    api_response = api_instance.v1get_sensors(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->v1get_sensors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Group ID | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_cargo**
> V1CargoResponse v1get_sensors_cargo(body)

Get cargo status

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get cargo monitor status (empty / full) for requested sensors.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorsApi()
body = NULL # object | Group ID and list of sensor IDs to query.

try:
    # Get cargo status
    api_response = api_instance.v1get_sensors_cargo(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->v1get_sensors_cargo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Group ID and list of sensor IDs to query. | 

### Return type

[**V1CargoResponse**](V1CargoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_door**
> V1DoorResponse v1get_sensors_door(body)

Get door status

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get door monitor status (closed / open) for requested sensors.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorsApi()
body = NULL # object | Group ID and list of sensor IDs to query.

try:
    # Get door status
    api_response = api_instance.v1get_sensors_door(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->v1get_sensors_door: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Group ID and list of sensor IDs to query. | 

### Return type

[**V1DoorResponse**](V1DoorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_history**
> V1SensorHistoryResponse v1get_sensors_history(body)

Get sensor history

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get historical data for specified sensors. This method returns a set of historical data for the specified sensors in the specified time range and at the specified time resolution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorsApi()
body = NULL # object | Group ID, time range and resolution, and list of sensor ID, field pairs to query.

try:
    # Get sensor history
    api_response = api_instance.v1get_sensors_history(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->v1get_sensors_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Group ID, time range and resolution, and list of sensor ID, field pairs to query. | 

### Return type

[**V1SensorHistoryResponse**](V1SensorHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_humidity**
> V1HumidityResponse v1get_sensors_humidity(body)

Get humidity

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get humidity for requested sensors. This method returns the current relative humidity for the requested sensors.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorsApi()
body = NULL # object | Group ID and list of sensor IDs to query.

try:
    # Get humidity
    api_response = api_instance.v1get_sensors_humidity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->v1get_sensors_humidity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Group ID and list of sensor IDs to query. | 

### Return type

[**V1HumidityResponse**](V1HumidityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_temperature**
> V1TemperatureResponse v1get_sensors_temperature(body)

Get temperature

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get temperature for requested sensors. This method returns the current ambient temperature (and probe temperature if applicable) for the requested sensors.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorsApi()
body = NULL # object | Group ID and list of sensor IDs to query.

try:
    # Get temperature
    api_response = api_instance.v1get_sensors_temperature(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->v1get_sensors_temperature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Group ID and list of sensor IDs to query. | 

### Return type

[**V1TemperatureResponse**](V1TemperatureResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

