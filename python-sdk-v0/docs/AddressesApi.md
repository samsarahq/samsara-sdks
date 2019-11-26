# swagger_client.AddressesApi

All URIs are relative to *https://api.samsara.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address**](AddressesApi.md#create_address) | **POST** /addresses | Create an address
[**delete_address_by_id**](AddressesApi.md#delete_address_by_id) | **DELETE** /addresses/{id} | Delete an address
[**get_address_by_id**](AddressesApi.md#get_address_by_id) | **GET** /addresses/{id} | Retrieve an address
[**get_addresses**](AddressesApi.md#get_addresses) | **GET** /addresses | List all addresses
[**update_address_by_id**](AddressesApi.md#update_address_by_id) | **PATCH** /addresses/{id} | Update an address

# **create_address**
> object create_address(body=body)

Create an address

Creates a new address in the organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressesApi()
body = swagger_client.AddressCreate() # AddressCreate | The address to create. (optional)

try:
    # Create an address
    api_response = api_instance.create_address(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->create_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddressCreate**](AddressCreate.md)| The address to create. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_address_by_id**
> delete_address_by_id(id)

Delete an address

Delete a specific address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressesApi()
id = 'id_example' # str | Unique Samsara ID for the address

try:
    # Delete an address
    api_instance.delete_address_by_id(id)
except ApiException as e:
    print("Exception when calling AddressesApi->delete_address_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique Samsara ID for the address | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_by_id**
> object get_address_by_id(id)

Retrieve an address

Returns a specific address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressesApi()
id = 'id_example' # str | Unique Samsara ID for the address

try:
    # Retrieve an address
    api_response = api_instance.get_address_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique Samsara ID for the address | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addresses**
> object get_addresses(limit=limit, after=after, tag_ids=tag_ids)

List all addresses

Returns a list of all addresses in an organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressesApi()
limit = 789 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)

try:
    # List all addresses
    api_response = api_instance.get_addresses(limit=limit, after=after, tag_ids=tag_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **update_address_by_id**
> object update_address_by_id(id, body=body)

Update an address

Update a specific address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressesApi()
id = 'id_example' # str | Unique Samsara ID for the address
body = swagger_client.AddressPatch() # AddressPatch | The address fields to update. (optional)

try:
    # Update an address
    api_response = api_instance.update_address_by_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->update_address_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique Samsara ID for the address | 
 **body** | [**AddressPatch**](AddressPatch.md)| The address fields to update. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

