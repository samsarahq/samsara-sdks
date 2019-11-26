# swagger_client.RoutesApi

All URIs are relative to *https://api.samsara.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1create_dispatch_route**](RoutesApi.md#v1create_dispatch_route) | **POST** /v1/fleet/dispatch/routes | Create a new route
[**v1delete_dispatch_route_by_id**](RoutesApi.md#v1delete_dispatch_route_by_id) | **DELETE** /v1/fleet/dispatch/routes/{route_id} | Delete a route
[**v1fetch_all_dispatch_routes**](RoutesApi.md#v1fetch_all_dispatch_routes) | **GET** /v1/fleet/dispatch/routes | Get all routes
[**v1fetch_all_route_job_updates**](RoutesApi.md#v1fetch_all_route_job_updates) | **GET** /v1/fleet/dispatch/routes/job_updates | Get route updates
[**v1get_dispatch_route_by_id**](RoutesApi.md#v1get_dispatch_route_by_id) | **GET** /v1/fleet/dispatch/routes/{route_id} | Get a route
[**v1get_dispatch_route_history**](RoutesApi.md#v1get_dispatch_route_history) | **GET** /v1/fleet/dispatch/routes/{route_id}/history | Get route history
[**v1update_dispatch_route_by_id**](RoutesApi.md#v1update_dispatch_route_by_id) | **PUT** /v1/fleet/dispatch/routes/{route_id} | Update a route

# **v1create_dispatch_route**
> V1DispatchRoute v1create_dispatch_route(body)

Create a new route

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Create a new dispatch route.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutesApi()
body = swagger_client.V1DispatchRouteCreate() # V1DispatchRouteCreate | 

try:
    # Create a new route
    api_response = api_instance.v1create_dispatch_route(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->v1create_dispatch_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DispatchRouteCreate**](V1DispatchRouteCreate.md)|  | 

### Return type

[**V1DispatchRoute**](V1DispatchRoute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1delete_dispatch_route_by_id**
> v1delete_dispatch_route_by_id(route_id)

Delete a route

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Delete a dispatch route and its associated jobs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutesApi()
route_id = 789 # int | ID of the dispatch route. Must contain only digits 0-9.

try:
    # Delete a route
    api_instance.v1delete_dispatch_route_by_id(route_id)
except ApiException as e:
    print("Exception when calling RoutesApi->v1delete_dispatch_route_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| ID of the dispatch route. Must contain only digits 0-9. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1fetch_all_dispatch_routes**
> V1DispatchRoutes v1fetch_all_dispatch_routes(end_time=end_time, duration=duration)

Get all routes

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all of the dispatch routes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutesApi()
end_time = 789 # int | Time in unix milliseconds that represents the oldest routes to return. Used in combination with duration. Defaults to now. (optional)
duration = 789 # int | Time in milliseconds that represents the duration before end_time to query. Defaults to 24 hours. (optional)

try:
    # Get all routes
    api_response = api_instance.v1fetch_all_dispatch_routes(end_time=end_time, duration=duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->v1fetch_all_dispatch_routes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_time** | **int**| Time in unix milliseconds that represents the oldest routes to return. Used in combination with duration. Defaults to now. | [optional] 
 **duration** | **int**| Time in milliseconds that represents the duration before end_time to query. Defaults to 24 hours. | [optional] 

### Return type

[**V1DispatchRoutes**](V1DispatchRoutes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1fetch_all_route_job_updates**
> V1allRouteJobUpdates v1fetch_all_route_job_updates(sequence_id=sequence_id, include=include)

Get route updates

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all updates to a job including route data in the last 24 hours or subsequent to an sequence ID. Returns a maximum of 500 job updates. If more than 500 job updates are available, another request made with the prior request's sequence_id will return the next set of available job updates.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutesApi()
sequence_id = 'sequence_id_example' # str | Sequence ID from the response payload of the last request. Defaults to fetching updates from last 24 hours. (optional)
include = 'include_example' # str | Optionally set include=route to include route object in response payload. (optional)

try:
    # Get route updates
    api_response = api_instance.v1fetch_all_route_job_updates(sequence_id=sequence_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->v1fetch_all_route_job_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **str**| Sequence ID from the response payload of the last request. Defaults to fetching updates from last 24 hours. | [optional] 
 **include** | **str**| Optionally set include&#x3D;route to include route object in response payload. | [optional] 

### Return type

[**V1allRouteJobUpdates**](V1allRouteJobUpdates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_dispatch_route_by_id**
> V1DispatchRoute v1get_dispatch_route_by_id(route_id)

Get a route

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch a dispatch route by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutesApi()
route_id = 789 # int | ID of the dispatch route. Must contain only digits 0-9.

try:
    # Get a route
    api_response = api_instance.v1get_dispatch_route_by_id(route_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->v1get_dispatch_route_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| ID of the dispatch route. Must contain only digits 0-9. | 

### Return type

[**V1DispatchRoute**](V1DispatchRoute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_dispatch_route_history**
> V1DispatchRouteHistory v1get_dispatch_route_history(route_id, start_time=start_time, end_time=end_time)

Get route history

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch the history of a dispatch route.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutesApi()
route_id = 789 # int | ID of the route with history. Must contain only digits 0-9.
start_time = 789 # int | Timestamp representing the start of the period to fetch, inclusive. Used in combination with end_time. Defaults to 0. (optional)
end_time = 789 # int | Timestamp representing the end of the period to fetch, inclusive. Used in combination with start_time. Defaults to nowMs. (optional)

try:
    # Get route history
    api_response = api_instance.v1get_dispatch_route_history(route_id, start_time=start_time, end_time=end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->v1get_dispatch_route_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| ID of the route with history. Must contain only digits 0-9. | 
 **start_time** | **int**| Timestamp representing the start of the period to fetch, inclusive. Used in combination with end_time. Defaults to 0. | [optional] 
 **end_time** | **int**| Timestamp representing the end of the period to fetch, inclusive. Used in combination with start_time. Defaults to nowMs. | [optional] 

### Return type

[**V1DispatchRouteHistory**](V1DispatchRouteHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1update_dispatch_route_by_id**
> V1DispatchRoute v1update_dispatch_route_by_id(body, route_id)

Update a route

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Update the dispatch route. Allowable updates include adding or removing jobs, and changing job locations and times.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutesApi()
body = swagger_client.V1DispatchRouteUpdate() # V1DispatchRouteUpdate | 
route_id = 789 # int | ID of the dispatch route. Must contain only digits 0-9.

try:
    # Update a route
    api_response = api_instance.v1update_dispatch_route_by_id(body, route_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->v1update_dispatch_route_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DispatchRouteUpdate**](V1DispatchRouteUpdate.md)|  | 
 **route_id** | **int**| ID of the dispatch route. Must contain only digits 0-9. | 

### Return type

[**V1DispatchRoute**](V1DispatchRoute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

