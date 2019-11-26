# swagger_client.TagsApi

All URIs are relative to *https://api.samsara.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagsApi.md#create_tag) | **POST** /tags | Create a tag
[**delete_tag_by_id**](TagsApi.md#delete_tag_by_id) | **DELETE** /tags/{id} | Delete a tag
[**get_all_tags**](TagsApi.md#get_all_tags) | **GET** /tags | List all tags
[**get_tag_by_id**](TagsApi.md#get_tag_by_id) | **GET** /tags/{id} | Retrieve a tag
[**put_tag_by_id**](TagsApi.md#put_tag_by_id) | **PUT** /tags/{id} | Update a tag

# **create_tag**
> object create_tag(body=body)

Create a tag

Create a new tag for the organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
body = swagger_client.TagUpdate() # TagUpdate |  (optional)

try:
    # Create a tag
    api_response = api_instance.create_tag(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->create_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TagUpdate**](TagUpdate.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag_by_id**
> delete_tag_by_id(id)

Delete a tag

Permanently deletes a tag.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
id = 'id_example' # str | Unique identifier for the tag.

try:
    # Delete a tag
    api_instance.delete_tag_by_id(id)
except ApiException as e:
    print("Exception when calling TagsApi->delete_tag_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the tag. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tags**
> object get_all_tags(limit=limit, after=after)

List all tags

Return all of the tags for an organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
limit = 789 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

try:
    # List all tags
    api_response = api_instance.get_all_tags(limit=limit, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_all_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_by_id**
> object get_tag_by_id(id)

Retrieve a tag

Fetch a tag by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
id = 'id_example' # str | Unique identifier for the tag.

try:
    # Retrieve a tag
    api_response = api_instance.get_tag_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tag_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the tag. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_tag_by_id**
> object put_tag_by_id(id, body=body)

Update a tag

Update a tag with a new name and new members. This API call would replace all old members of a tag with new members specified in the request body.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
id = 'id_example' # str | Unique identifier for the tag.
body = swagger_client.TagUpdate() # TagUpdate |  (optional)

try:
    # Update a tag
    api_response = api_instance.put_tag_by_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->put_tag_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the tag. | 
 **body** | [**TagUpdate**](TagUpdate.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

