# swagger_client.VehiclesApi

All URIs are relative to *https://api.samsara.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vehicle_by_id**](VehiclesApi.md#get_vehicle_by_id) | **GET** /fleet/vehicles/{id} | Retrieve a vehicle
[**get_vehicle_locations**](VehiclesApi.md#get_vehicle_locations) | **GET** /fleet/vehicles/locations | List most recent vehicle locations
[**get_vehicle_locations_feed**](VehiclesApi.md#get_vehicle_locations_feed) | **GET** /fleet/vehicles/locations/feed | Follow a real-time feed of vehicle locations
[**get_vehicle_locations_history**](VehiclesApi.md#get_vehicle_locations_history) | **GET** /fleet/vehicles/locations/history | Get historical vehicle locations
[**get_vehicle_stats_feed**](VehiclesApi.md#get_vehicle_stats_feed) | **GET** /fleet/vehicles/stats/feed | Follow a real-time feed of vehicle stats
[**get_vehicle_stats_history**](VehiclesApi.md#get_vehicle_stats_history) | **GET** /fleet/vehicles/stats/history | Get historical vehicle stats
[**get_vehicle_stats_snapshot**](VehiclesApi.md#get_vehicle_stats_snapshot) | **GET** /fleet/vehicles/stats | List most recent vehicle stats
[**list_vehicles_kondo**](VehiclesApi.md#list_vehicles_kondo) | **GET** /fleet/vehicles | List all vehicles
[**update_vehicle_by_id**](VehiclesApi.md#update_vehicle_by_id) | **PATCH** /fleet/vehicles/{id} | Update a vehicle

# **get_vehicle_by_id**
> object get_vehicle_by_id(id)

Retrieve a vehicle

Get information about a specific vehicle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
id = 'id_example' # str | ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `maintenanceId:250020`

try:
    # Retrieve a vehicle
    api_response = api_instance.get_vehicle_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->get_vehicle_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;maintenanceId:250020&#x60; | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_locations**
> VehicleLocationsSnapshotResponse get_vehicle_locations(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

List most recent vehicle locations

Returns last known location for all vehicles (Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

try:
    # List most recent vehicle locations
    api_response = api_instance.get_vehicle_locations(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->get_vehicle_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleLocationsSnapshotResponse**](VehicleLocationsSnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_locations_feed**
> VehicleLocationsListResponse get_vehicle_locations_feed(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Follow a real-time feed of vehicle locations

Follow a continuous feed of all vehicle locations from Samsara Vehicle Gateways.  Your first call to this endpoint will provide you with the most recent location for each vehicle and a `pagination` object that contains an `endCursor`.  You can provide the `endCursor` to the `after` parameter of this endpoint to get location updates since that `endCursor`.   If `hasNextPage` is `false`, no updates are readily available yet. Each stat type has a different refresh rate, but in general we'd suggest waiting a minimum of 5 seconds before requesting updates.  See [this guide](https://developers.samsara.com/docs/vehicle-locations#section-follow-a-real-time-feed-of-vehicle-locations) for more details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

try:
    # Follow a real-time feed of vehicle locations
    api_response = api_instance.get_vehicle_locations_feed(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->get_vehicle_locations_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleLocationsListResponse**](VehicleLocationsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_locations_history**
> VehicleLocationsListResponse get_vehicle_locations_history(start_time, end_time, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Get historical vehicle locations

Returns all known vehicle location changes during the given time range for all vehicles (Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
start_time = '2013-10-20T19:20:30+01:00' # datetime | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = '2013-10-20T19:20:30+01:00' # datetime | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

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
 **tag_ids** | [**list[str]**](str.md)| A comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleLocationsListResponse**](VehicleLocationsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_stats_feed**
> VehicleStatsListResponse get_vehicle_stats_feed(types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Follow a real-time feed of vehicle stats

Follow a continuous feed of all vehicle stats from Samsara Vehicle Gateways.  Your first call to this endpoint will provide you with the most recent stats for each vehicle and a `pagination` object that contains an `endCursor`.  You can provide the `endCursor` to the `after` parameter of this endpoint to get vehicle stat updates since that `endCursor`.  If `hasNextPage` is `false`, no updates are readily available yet. Each stat type has a different refresh rate, but in general we'd suggest waiting a minimum of 5 seconds before requesting updates.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
types = 'types_example' # str | The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `obdOdometerMeters`: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using `gpsOdometerMeters`. - `gpsOdometerMeters`: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara's dashboard UI or through the `odometerMeters` field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. `gpsOdometerMeters` is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to on-board diagnostics.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

try:
    # Follow a real-time feed of vehicle stats
    api_response = api_instance.get_vehicle_stats_feed(types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->get_vehicle_stats_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | **str**| The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;obdOdometerMeters&#x60;: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using &#x60;gpsOdometerMeters&#x60;. - &#x60;gpsOdometerMeters&#x60;: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara&#x27;s dashboard UI or through the &#x60;odometerMeters&#x60; field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. &#x60;gpsOdometerMeters&#x60; is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to on-board diagnostics. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleStatsListResponse**](VehicleStatsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_stats_history**
> VehicleStatsListResponse get_vehicle_stats_history(start_time, end_time, types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Get historical vehicle stats

Returns all known vehicle stats changes during the given time range for all vehicles (Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
start_time = '2013-10-20T19:20:30+01:00' # datetime | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = '2013-10-20T19:20:30+01:00' # datetime | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
types = 'types_example' # str | The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `obdOdometerMeters`: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using `gpsOdometerMeters`. - `gpsOdometerMeters`: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara's dashboard UI or through the `odometerMeters` field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. `gpsOdometerMeters` is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to on-board diagnostics.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

try:
    # Get historical vehicle stats
    api_response = api_instance.get_vehicle_stats_history(start_time, end_time, types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->get_vehicle_stats_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **datetime**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **types** | **str**| The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;obdOdometerMeters&#x60;: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using &#x60;gpsOdometerMeters&#x60;. - &#x60;gpsOdometerMeters&#x60;: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara&#x27;s dashboard UI or through the &#x60;odometerMeters&#x60; field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. &#x60;gpsOdometerMeters&#x60; is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to on-board diagnostics. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleStatsListResponse**](VehicleStatsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_stats_snapshot**
> object get_vehicle_stats_snapshot(types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

List most recent vehicle stats

Returns last known stats for all vehicles. This can be optionally filtered by tags or specific vehicle IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
types = 'types_example' # str | The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `obdOdometerMeters`: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using `gpsOdometerMeters`. - `gpsOdometerMeters`: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara's dashboard UI or through the `odometerMeters` field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. `gpsOdometerMeters` is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to on-board diagnostics.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

try:
    # List most recent vehicle stats
    api_response = api_instance.get_vehicle_stats_snapshot(types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->get_vehicle_stats_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | **str**| The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;obdOdometerMeters&#x60;: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using &#x60;gpsOdometerMeters&#x60;. - &#x60;gpsOdometerMeters&#x60;: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara&#x27;s dashboard UI or through the &#x60;odometerMeters&#x60; field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. &#x60;gpsOdometerMeters&#x60; is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to on-board diagnostics. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vehicles_kondo**
> VehicleListResponse list_vehicles_kondo(limit=limit, after=after, tag_ids=tag_ids)

List all vehicles

Returns a list of all vehicles in an organization, ordered by vehicle ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
limit = 789 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)

try:
    # List all vehicles
    api_response = api_instance.list_vehicles_kondo(limit=limit, after=after, tag_ids=tag_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->list_vehicles_kondo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleListResponse**](VehicleListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vehicle_by_id**
> object update_vehicle_by_id(id, body=body)

Update a vehicle

Patches the given vehicle object.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
id = 'id_example' # str | ID of the vehicle. This can either be the Samsara-specified ID, or an external ID.
body = swagger_client.VehiclePatch() # VehiclePatch | Fields that can be patched on a vehicle. (optional)

try:
    # Update a vehicle
    api_response = api_instance.update_vehicle_by_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->update_vehicle_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. | 
 **body** | [**VehiclePatch**](VehiclePatch.md)| Fields that can be patched on a vehicle. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

