# samsara.TrailerAssignmentsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1get_all_trailer_assignments**](TrailerAssignmentsApi.md#v1get_all_trailer_assignments) | **GET** /v1/fleet/trailers/assignments | List trailer assignments for all trailers
[**v1get_fleet_trailer_assignments**](TrailerAssignmentsApi.md#v1get_fleet_trailer_assignments) | **GET** /v1/fleet/trailers/{trailerId}/assignments | List trailer assignments for a given trailer


# **v1get_all_trailer_assignments**
> InlineResponse2006 v1get_all_trailer_assignments(start_ms=start_ms, end_ms=end_ms, limit=limit, starting_after=starting_after, ending_before=ending_before)

List trailer assignments for all trailers

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch trailer assignment data for all trailers in your organization.

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
    api_instance = samsara.TrailerAssignmentsApi(api_client)
    start_ms = 56 # int | Timestamp in Unix epoch miliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments. (optional)
end_ms = 56 # int | Timestamp in Unix epoch miliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time (optional)
limit = 3.4 # float | Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'. (optional)
starting_after = 'starting_after_example' # str | Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter. (optional)
ending_before = 'ending_before_example' # str | Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter. (optional)

    try:
        # List trailer assignments for all trailers
        api_response = api_instance.v1get_all_trailer_assignments(start_ms=start_ms, end_ms=end_ms, limit=limit, starting_after=starting_after, ending_before=ending_before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TrailerAssignmentsApi->v1get_all_trailer_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_ms** | **int**| Timestamp in Unix epoch miliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments. | [optional] 
 **end_ms** | **int**| Timestamp in Unix epoch miliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time | [optional] 
 **limit** | **float**| Pagination parameter indicating the number of results to return in this request. Used in conjunction with either &#39;startingAfter&#39; or &#39;endingBefore&#39;. | [optional] 
 **starting_after** | **str**| Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the &#39;limit&#39; parameter. Mutually exclusive with &#39;endingBefore&#39; parameter. | [optional] 
 **ending_before** | **str**| Pagination parameter indicating the cursor position to return results before. Used in conjunction with the &#39;limit&#39; parameter. Mutually exclusive with &#39;startingAfter&#39; parameter. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns trailer assignment data for all trailers in your organization |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_fleet_trailer_assignments**
> V1TrailerAssignmentsResponse v1get_fleet_trailer_assignments(trailer_id, start_ms=start_ms, end_ms=end_ms)

List trailer assignments for a given trailer

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch trailer assignment data for a single trailer.

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
    api_instance = samsara.TrailerAssignmentsApi(api_client)
    trailer_id = 56 # int | ID of trailer. Must contain only digits 0-9.
start_ms = 56 # int | Timestamp in Unix epoch milliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments. (optional)
end_ms = 56 # int | Timestamp in Unix epoch milliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time (optional)

    try:
        # List trailer assignments for a given trailer
        api_response = api_instance.v1get_fleet_trailer_assignments(trailer_id, start_ms=start_ms, end_ms=end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TrailerAssignmentsApi->v1get_fleet_trailer_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trailer_id** | **int**| ID of trailer. Must contain only digits 0-9. | 
 **start_ms** | **int**| Timestamp in Unix epoch milliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments. | [optional] 
 **end_ms** | **int**| Timestamp in Unix epoch milliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time | [optional] 

### Return type

[**V1TrailerAssignmentsResponse**](V1TrailerAssignmentsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns trailer assignment data for a single trailer |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

