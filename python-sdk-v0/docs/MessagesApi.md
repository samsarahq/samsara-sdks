# swagger_client.MessagesApi

All URIs are relative to *https://api.samsara.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1create_messages**](MessagesApi.md#v1create_messages) | **POST** /v1/fleet/messages | Send a message to a list of driver ids.
[**v1get_messages**](MessagesApi.md#v1get_messages) | **GET** /v1/fleet/messages | Get all messages.

# **v1create_messages**
> object v1create_messages(body)

Send a message to a list of driver ids.

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Send a message to a list of driver ids.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagesApi()
body = NULL # object | Text to send to a list of driverIds.

try:
    # Send a message to a list of driver ids.
    api_response = api_instance.v1create_messages(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->v1create_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Text to send to a list of driverIds. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_messages**
> object v1get_messages(end_ms=end_ms, duration_ms=duration_ms)

Get all messages.

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get all messages.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagesApi()
end_ms = 789 # int | Time in unix milliseconds that represents the end of time range of messages to return. Used in combination with durationMs. Defaults to now. (optional)
duration_ms = 789 # int | Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours. (optional)

try:
    # Get all messages.
    api_response = api_instance.v1get_messages(end_ms=end_ms, duration_ms=duration_ms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->v1get_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_ms** | **int**| Time in unix milliseconds that represents the end of time range of messages to return. Used in combination with durationMs. Defaults to now. | [optional] 
 **duration_ms** | **int**| Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

