# samsara.DriversApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_driver**](DriversApi.md#create_driver) | **POST** /fleet/drivers | Create a driver
[**get_driver**](DriversApi.md#get_driver) | **GET** /fleet/drivers/{id} | Retrieve a driver
[**list_drivers**](DriversApi.md#list_drivers) | **GET** /fleet/drivers | List all drivers
[**update_driver**](DriversApi.md#update_driver) | **PATCH** /fleet/drivers/{id} | Update a driver


# **create_driver**
> DriverResponse create_driver(driver)

Create a driver

Add a driver to the organization.

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
    api_instance = samsara.DriversApi(api_client)
    driver = samsara.CreateDriverRequest() # CreateDriverRequest | The driver to create.

    try:
        # Create a driver
        api_response = api_instance.create_driver(driver)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DriversApi->create_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver** | [**CreateDriverRequest**](CreateDriverRequest.md)| The driver to create. | 

### Return type

[**DriverResponse**](DriverResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created driver object, with Samsara-generated ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_driver**
> DriverResponse get_driver(id)

Retrieve a driver

Get information about a driver.

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
    api_instance = samsara.DriversApi(api_client)
    id = 'id_example' # str | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`

    try:
        # Retrieve a driver
        api_response = api_instance.get_driver(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DriversApi->get_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 

### Return type

[**DriverResponse**](DriverResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified driver. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_drivers**
> ListDriversResponse list_drivers(is_deactivated=is_deactivated, limit=limit, after=after, tag_ids=tag_ids, updated_after_time=updated_after_time, created_after_time=created_after_time)

List all drivers

Get all drivers in organization.

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
    api_instance = samsara.DriversApi(api_client)
    is_deactivated = True # bool | If value is true, only drivers that are deactivated will appear in the response. This parameter will default to false if not provided (fetching only active drivers). (optional)
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
updated_after_time = '2013-10-20T19:20:30+01:00' # datetime | A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). (optional)
created_after_time = '2013-10-20T19:20:30+01:00' # datetime | A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). (optional)

    try:
        # List all drivers
        api_response = api_instance.list_drivers(is_deactivated=is_deactivated, limit=limit, after=after, tag_ids=tag_ids, updated_after_time=updated_after_time, created_after_time=created_after_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DriversApi->list_drivers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_deactivated** | **bool**| If value is true, only drivers that are deactivated will appear in the response. This parameter will default to false if not provided (fetching only active drivers). | [optional] 
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **updated_after_time** | **datetime**| A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 
 **created_after_time** | **datetime**| A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 

### Return type

[**ListDriversResponse**](ListDriversResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all driver objects. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_driver**
> DriverResponse update_driver(id, driver)

Update a driver

Update a specific driver's information. This can also be used to activate or de-activate a given driver

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
    api_instance = samsara.DriversApi(api_client)
    id = 'id_example' # str | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
driver = samsara.UpdateDriverRequest() # UpdateDriverRequest | Updates to the driver properties.

    try:
        # Update a driver
        api_response = api_instance.update_driver(id, driver)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DriversApi->update_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 
 **driver** | [**UpdateDriverRequest**](UpdateDriverRequest.md)| Updates to the driver properties. | 

### Return type

[**DriverResponse**](DriverResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated driver object, with ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

