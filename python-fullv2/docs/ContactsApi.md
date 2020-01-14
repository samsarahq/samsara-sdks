# openapi_client.ContactsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact**](ContactsApi.md#create_contact) | **POST** /contacts | Create a contact
[**delete_contact_by_id**](ContactsApi.md#delete_contact_by_id) | **DELETE** /contacts/{id} | Delete a contact
[**get_contact_by_id**](ContactsApi.md#get_contact_by_id) | **GET** /contacts/{id} | Retrieve a contact
[**get_contacts**](ContactsApi.md#get_contacts) | **GET** /contacts | List all contacts
[**update_contact_by_id**](ContactsApi.md#update_contact_by_id) | **PATCH** /contacts/{id} | Update a contact


# **create_contact**
> InlineResponse2001 create_contact(contact)

Create a contact

Add a contact to the organization

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.ContactsApi()
contact = openapi_client.ContactInput() # ContactInput | Add a contact.

try:
    # Create a contact
    api_response = api_instance.create_contact(contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | [**ContactInput**](ContactInput.md)| Add a contact. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact was successfully added. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_by_id**
> delete_contact_by_id(id)

Delete a contact

Delete the given contact.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.ContactsApi()
id = 'id_example' # str | Unique identifier for the contact.

try:
    # Delete a contact
    api_instance.delete_contact_by_id(id)
except ApiException as e:
    print("Exception when calling ContactsApi->delete_contact_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the contact. | 

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
**204** | Returns an empty success response. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_by_id**
> InlineResponse2001 get_contact_by_id(id)

Retrieve a contact

Get a specific contact's information.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.ContactsApi()
id = 'id_example' # str | Unique identifier for the contact.

try:
    # Retrieve a contact
    api_response = api_instance.get_contact_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_contact_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the contact. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified contact. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts**
> object get_contacts(limit=limit, after=after)

List all contacts

Returns a list of all contacts in an organization.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.ContactsApi()
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

try:
    # List all contacts
    api_response = api_instance.get_contacts(limit=limit, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

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
**200** | List of all contacts |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact_by_id**
> InlineResponse2001 update_contact_by_id(id, contact=contact)

Update a contact

Update a specific contact's information.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.ContactsApi()
id = 'id_example' # str | Unique identifier for the contact.
contact = openapi_client.ContactInput() # ContactInput | Updates to the contact. (optional)

try:
    # Update a contact
    api_response = api_instance.update_contact_by_id(id, contact=contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->update_contact_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the contact. | 
 **contact** | [**ContactInput**](ContactInput.md)| Updates to the contact. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated contact object with given ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

