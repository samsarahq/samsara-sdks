# samsara.DriversApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_driver**](DriversApi.md#create_driver) | **POST** /fleet/drivers | Create a driver
[**get_driver_by_id**](DriversApi.md#get_driver_by_id) | **GET** /fleet/drivers/{id} | Retrieve a driver
[**get_drivers**](DriversApi.md#get_drivers) | **GET** /fleet/drivers | List all drivers
[**update_driver_by_id**](DriversApi.md#update_driver_by_id) | **PATCH** /fleet/drivers/{id} | Update a driver


# **create_driver**
> InlineResponse2002 create_driver(driver=driver)

Create a driver

Add a driver to the organization.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.DriversApi()
driver = samsara.DriverCreate() # DriverCreate | The driver to create. (optional)

try:
    # Create a driver
    api_response = api_instance.create_driver(driver=driver)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriversApi->create_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver** | [**DriverCreate**](DriverCreate.md)| The driver to create. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created driver object, with Samsara-generated ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_driver_by_id**
> InlineResponse2002 get_driver_by_id(id)

Retrieve a driver

Get information about a driver.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.DriversApi()
id = 'id_example' # str | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`

try:
    # Retrieve a driver
    api_response = api_instance.get_driver_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriversApi->get_driver_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified driver. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drivers**
> object get_drivers(is_deactivated=is_deactivated, limit=limit, after=after, tag_ids=tag_ids)

List all drivers

Get all drivers in organization.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.DriversApi()
is_deactivated = True # bool | If value is true, only drivers that are deactivated will appear in the response. This parameter will default to false if not provided (fetching only active drivers). (optional)
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)

try:
    # List all drivers
    api_response = api_instance.get_drivers(is_deactivated=is_deactivated, limit=limit, after=after, tag_ids=tag_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriversApi->get_drivers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_deactivated** | **bool**| If value is true, only drivers that are deactivated will appear in the response. This parameter will default to false if not provided (fetching only active drivers). | [optional] 
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all driver objects. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_driver_by_id**
> InlineResponse2002 update_driver_by_id(id, driver=driver)

Update a driver

Update a specific driver's information. This can also be used to activate or de-activate a given driver

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.DriversApi()
id = 'id_example' # str | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
driver = samsara.DriverUpdate() # DriverUpdate | Updates to the driver properties. (optional)

try:
    # Update a driver
    api_response = api_instance.update_driver_by_id(id, driver=driver)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriversApi->update_driver_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 
 **driver** | [**DriverUpdate**](DriverUpdate.md)| Updates to the driver properties. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated driver object, with ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

