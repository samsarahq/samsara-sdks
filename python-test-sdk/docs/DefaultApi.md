# samsara_test.DefaultApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address**](DefaultApi.md#create_address) | **POST** /addresses | Create an address
[**delete_address**](DefaultApi.md#delete_address) | **DELETE** /addresses/{id} | Delete an address
[**get_address**](DefaultApi.md#get_address) | **GET** /addresses/{id} | Retrieve an address
[**list_addresses**](DefaultApi.md#list_addresses) | **GET** /addresses | List all addresses
[**update_address**](DefaultApi.md#update_address) | **PATCH** /addresses/{id} | Update an address


# **create_address**
> AddressResponse create_address(address)

Create an address

Creates a new address in the organization

### Example

```python
from __future__ import print_function
import time
import samsara_test
from samsara_test.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara_test.DefaultApi()
address = samsara_test.CreateAddressRequest() # CreateAddressRequest | The address to create.

try:
    # Create an address
    api_response = api_instance.create_address(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**CreateAddressRequest**](CreateAddressRequest.md)| The address to create. | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created address object with ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_address**
> delete_address(id)

Delete an address

Delete a specific address.

### Example

```python
from __future__ import print_function
import time
import samsara_test
from samsara_test.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara_test.DefaultApi()
id = 'id_example' # str | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`

try:
    # Delete an address
    api_instance.delete_address(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Empty success body |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address**
> AddressResponse get_address(id)

Retrieve an address

Returns a specific address.

### Example

```python
from __future__ import print_function
import time
import samsara_test
from samsara_test.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara_test.DefaultApi()
id = 'id_example' # str | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`

try:
    # Retrieve an address
    api_response = api_instance.get_address(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60; | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Address. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_addresses**
> ListAddressesResponse list_addresses(limit=limit, after=after, tag_ids=tag_ids)

List all addresses

Returns a list of all addresses in an organization

### Example

```python
from __future__ import print_function
import time
import samsara_test
from samsara_test.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara_test.DefaultApi()
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)

try:
    # List all addresses
    api_response = api_instance.list_addresses(limit=limit, after=after, tag_ids=tag_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**ListAddressesResponse**](ListAddressesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all addresses in the organization |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address**
> AddressResponse update_address(id, address)

Update an address

Update a specific address.

### Example

```python
from __future__ import print_function
import time
import samsara_test
from samsara_test.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara_test.DefaultApi()
id = 'id_example' # str | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`
address = samsara_test.UpdateAddressRequest() # UpdateAddressRequest | The address fields to update.

try:
    # Update an address
    api_response = api_instance.update_address(id, address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60; | 
 **address** | [**UpdateAddressRequest**](UpdateAddressRequest.md)| The address fields to update. | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated address object with ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

