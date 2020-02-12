# samsara_test.VehiclesApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vehicle_locations**](VehiclesApi.md#get_vehicle_locations) | **GET** /fleet/vehicles/locations | Get most recent vehicle locations
[**get_vehicle_locations_feed**](VehiclesApi.md#get_vehicle_locations_feed) | **GET** /fleet/vehicles/locations/feed | Follow a feed of vehicle locations
[**get_vehicle_locations_history**](VehiclesApi.md#get_vehicle_locations_history) | **GET** /fleet/vehicles/locations/history | Get historical vehicle locations


# **get_vehicle_locations**
> VehicleLocationsResponse get_vehicle_locations(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Get most recent vehicle locations

Returns last known location for all vehicles (Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-locations) for more details.

### Example

```python
from __future__ import print_function
import time
import samsara_test
from samsara_test.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with samsara_test.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = samsara_test.VehiclesApi(api_client)
    after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

    try:
        # Get most recent vehicle locations
        api_response = api_instance.get_vehicle_locations(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VehiclesApi->get_vehicle_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleLocationsResponse**](VehicleLocationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all locations for the specified vehicles and time range. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_locations_feed**
> VehicleLocationsListResponse get_vehicle_locations_feed(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Follow a feed of vehicle locations

Follow a continuous feed of all vehicle locations from Samsara Vehicle Gateways.  Your first call to this endpoint will provide you with the most recent location for each vehicle and a `pagination` object that contains an `endCursor`.  You can provide the `endCursor` to the `after` parameter of this endpoint to get location updates since that `endCursor`.   If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest waiting a minimum of 5 seconds before requesting updates.  See [this guide](https://developers.samsara.com/docs/vehicle-locations#section-follow-a-real-time-feed-of-vehicle-locations) for more details.

### Example

```python
from __future__ import print_function
import time
import samsara_test
from samsara_test.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with samsara_test.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = samsara_test.VehiclesApi(api_client)
    after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

    try:
        # Follow a feed of vehicle locations
        api_response = api_instance.get_vehicle_locations_feed(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VehiclesApi->get_vehicle_locations_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleLocationsListResponse**](VehicleLocationsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all locations for the specified vehicles. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_locations_history**
> VehicleLocationsListResponse get_vehicle_locations_history(start_time, end_time, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Get historical vehicle locations

Returns all known vehicle location changes during the given time range for all vehicles (Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-locations) for more details.

### Example

```python
from __future__ import print_function
import time
import samsara_test
from samsara_test.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with samsara_test.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = samsara_test.VehiclesApi(api_client)
    start_time = '2013-10-20T19:20:30+01:00' # datetime | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = '2013-10-20T19:20:30+01:00' # datetime | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

    try:
        # Get historical vehicle locations
        api_response = api_instance.get_vehicle_locations_history(start_time, end_time, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VehiclesApi->get_vehicle_locations_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **datetime**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleLocationsListResponse**](VehicleLocationsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all locations for the specified vehicles and time range. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

