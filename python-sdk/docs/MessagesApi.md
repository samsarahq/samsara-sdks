# samsara.MessagesApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1create_messages**](MessagesApi.md#v1create_messages) | **POST** /v1/fleet/messages | Send a message to a list of driver ids.
[**v1get_messages**](MessagesApi.md#v1get_messages) | **GET** /v1/fleet/messages | Get all messages.


# **v1create_messages**
> InlineResponse2005 v1create_messages(create_messages)

Send a message to a list of driver ids.

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Send a message to a list of driver ids.

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
    api_instance = samsara.MessagesApi(api_client)
    create_messages = samsara.InlineObject3() # InlineObject3 | 

    try:
        # Send a message to a list of driver ids.
        api_response = api_instance.v1create_messages(create_messages)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->v1create_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_messages** | [**InlineObject3**](InlineObject3.md)|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the created messages. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_messages**
> InlineResponse2004 v1get_messages(end_ms=end_ms, duration_ms=duration_ms)

Get all messages.

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get all messages.

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
    api_instance = samsara.MessagesApi(api_client)
    end_ms = 56 # int | Time in unix milliseconds that represents the end of time range of messages to return. Used in combination with durationMs. Defaults to now. (optional)
duration_ms = 56 # int | Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours. (optional)

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

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the fetched messages from most recently sent to least recently sent. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

