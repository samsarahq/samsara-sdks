# swagger_client.UsersApi

All URIs are relative to *https://api.samsara.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /users | Create a user
[**delete_user_by_id**](UsersApi.md#delete_user_by_id) | **DELETE** /users/{id} | Delete a user
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /users/{id} | Retrieve a user
[**get_user_roles**](UsersApi.md#get_user_roles) | **GET** /user-roles | List all user roles
[**get_users**](UsersApi.md#get_users) | **GET** /users | List all users
[**update_user_by_id**](UsersApi.md#update_user_by_id) | **PATCH** /users/{id} | Update a user

# **create_user**
> object create_user(body=body)

Create a user

Add a user to the organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.UserCreate() # UserCreate | The user to create. (optional)

try:
    # Create a user
    api_response = api_instance.create_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreate**](UserCreate.md)| The user to create. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_by_id**
> delete_user_by_id(id)

Delete a user

Delete the given user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | Unique identifier for the user.

try:
    # Delete a user
    api_instance.delete_user_by_id(id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the user. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> object get_user_by_id(id)

Retrieve a user

Get a specific user's information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | Unique identifier for the user.

try:
    # Retrieve a user
    api_response = api_instance.get_user_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the user. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> object get_user_roles(limit=limit, after=after)

List all user roles

Returns a list of all user roles in an organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
limit = 789 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

try:
    # List all user roles
    api_response = api_instance.get_user_roles(limit=limit, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_roles: %s\n" % e)
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

# **get_users**
> object get_users(limit=limit, after=after)

List all users

Returns a list of all users in an organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
limit = 789 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

try:
    # List all users
    api_response = api_instance.get_users(limit=limit, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
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

# **update_user_by_id**
> object update_user_by_id(id, body=body)

Update a user

Update a specific user's information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | Unique identifier for the user.
body = swagger_client.UserUpdate() # UserUpdate | Updates to the user. (optional)

try:
    # Update a user
    api_response = api_instance.update_user_by_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the user. | 
 **body** | [**UserUpdate**](UserUpdate.md)| Updates to the user. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

