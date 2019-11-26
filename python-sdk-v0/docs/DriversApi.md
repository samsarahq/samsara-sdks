# swagger_client.DriversApi

All URIs are relative to *https://api.samsara.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_driver**](DriversApi.md#create_driver) | **POST** /fleet/drivers | Create a driver
[**get_driver_by_id**](DriversApi.md#get_driver_by_id) | **GET** /fleet/drivers/{id} | Retrieve a driver
[**get_drivers**](DriversApi.md#get_drivers) | **GET** /fleet/drivers | List all drivers
[**update_driver_by_id**](DriversApi.md#update_driver_by_id) | **PATCH** /fleet/drivers/{id} | Update a driver

# **create_driver**
> object create_driver(body=body)

Create a driver

Add a driver to the organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DriversApi()
body = swagger_client.DriverCreate() # DriverCreate | The driver to create. (optional)

try:
    # Create a driver
    api_response = api_instance.create_driver(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriversApi->create_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DriverCreate**](DriverCreate.md)| The driver to create. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_driver_by_id**
> object get_driver_by_id(id)

Retrieve a driver

Get information about a driver.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DriversApi()
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

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drivers**
> object get_drivers(is_deactivated=is_deactivated, limit=limit, after=after, tag_ids=tag_ids)

List all drivers

Get all drivers in organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DriversApi()
is_deactivated = true # bool | If value is true, only drivers that are deactivated will appear in the response. This parameter will default to false if not provided (fetching only active drivers). (optional)
limit = 789 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)

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
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_driver_by_id**
> object update_driver_by_id(id, body=body)

Update a driver

Update a specific driver's information. This can also be used to activate or de-activate a given driver

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DriversApi()
id = 'id_example' # str | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
body = swagger_client.DriverUpdate() # DriverUpdate | Updates to the driver properties. (optional)

try:
    # Update a driver
    api_response = api_instance.update_driver_by_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriversApi->update_driver_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 
 **body** | [**DriverUpdate**](DriverUpdate.md)| Updates to the driver properties. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

