# samsara.TagsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagsApi.md#create_tag) | **POST** /tags | Create a tag
[**delete_tag**](TagsApi.md#delete_tag) | **DELETE** /tags/{id} | Delete a tag
[**get_tag**](TagsApi.md#get_tag) | **GET** /tags/{id} | Retrieve a tag
[**list_tags**](TagsApi.md#list_tags) | **GET** /tags | List all tags
[**replace_tag**](TagsApi.md#replace_tag) | **PUT** /tags/{id} | Update a tag


# **create_tag**
> TagResponse create_tag(tag_create_body_)

Create a tag

Create a new tag for the organization.

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
    api_instance = samsara.TagsApi(api_client)
    tag_create_body_ = samsara.CreateTagRequest() # CreateTagRequest | 

    try:
        # Create a tag
        api_response = api_instance.create_tag(tag_create_body_)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->create_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_create_body_** | [**CreateTagRequest**](CreateTagRequest.md)|  | 

### Return type

[**TagResponse**](TagResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created tag object, including the new tag ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(id)

Delete a tag

Permanently deletes a tag.

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
    api_instance = samsara.TagsApi(api_client)
    id = 'id_example' # str | Unique identifier for the tag.

    try:
        # Delete a tag
        api_instance.delete_tag(id)
    except ApiException as e:
        print("Exception when calling TagsApi->delete_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the tag. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted the tag. No response body is returned. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> TagResponse get_tag(id)

Retrieve a tag

Fetch a tag by id.

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
    api_instance = samsara.TagsApi(api_client)
    id = 'id_example' # str | Unique identifier for the tag.

    try:
        # Retrieve a tag
        api_response = api_instance.get_tag(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->get_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the tag. | 

### Return type

[**TagResponse**](TagResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tag corresponding to request id. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags**
> ListTagsResponse list_tags(limit=limit, after=after)

List all tags

Return all of the tags for an organization.

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
    api_instance = samsara.TagsApi(api_client)
    limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

    try:
        # List all tags
        api_response = api_instance.list_tags(limit=limit, after=after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->list_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

### Return type

[**ListTagsResponse**](ListTagsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tags. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_tag**
> TagResponse replace_tag(id, tag_update_body_)

Update a tag

Update a tag with a new name and new members. This API call would replace all old members of a tag with new members specified in the request body.

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
    api_instance = samsara.TagsApi(api_client)
    id = 'id_example' # str | Unique identifier for the tag.
tag_update_body_ = samsara.ReplaceTagRequest() # ReplaceTagRequest | 

    try:
        # Update a tag
        api_response = api_instance.replace_tag(id, tag_update_body_)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->replace_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the tag. | 
 **tag_update_body_** | [**ReplaceTagRequest**](ReplaceTagRequest.md)|  | 

### Return type

[**TagResponse**](TagResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated tag data. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

