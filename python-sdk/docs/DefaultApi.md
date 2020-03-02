# samsara.DefaultApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address**](DefaultApi.md#create_address) | **POST** /addresses | Create an address
[**create_contact**](DefaultApi.md#create_contact) | **POST** /contacts | Create a contact
[**create_driver**](DefaultApi.md#create_driver) | **POST** /fleet/drivers | Create a driver
[**create_tag**](DefaultApi.md#create_tag) | **POST** /tags | Create a tag
[**create_user**](DefaultApi.md#create_user) | **POST** /users | Create a user
[**delete_address**](DefaultApi.md#delete_address) | **DELETE** /addresses/{id} | Delete an address
[**delete_contact**](DefaultApi.md#delete_contact) | **DELETE** /contacts/{id} | Delete a contact
[**delete_tag**](DefaultApi.md#delete_tag) | **DELETE** /tags/{id} | Delete a tag
[**delete_user**](DefaultApi.md#delete_user) | **DELETE** /users/{id} | Delete a user
[**get_address**](DefaultApi.md#get_address) | **GET** /addresses/{id} | Retrieve an address
[**get_contact**](DefaultApi.md#get_contact) | **GET** /contacts/{id} | Retrieve a contact
[**get_driver**](DefaultApi.md#get_driver) | **GET** /fleet/drivers/{id} | Retrieve a driver
[**get_tag**](DefaultApi.md#get_tag) | **GET** /tags/{id} | Retrieve a tag
[**get_user**](DefaultApi.md#get_user) | **GET** /users/{id} | Retrieve a user
[**get_vehicle**](DefaultApi.md#get_vehicle) | **GET** /fleet/vehicles/{id} | Retrieve a vehicle
[**get_vehicle_locations**](DefaultApi.md#get_vehicle_locations) | **GET** /fleet/vehicles/locations | Get most recent vehicle locations
[**get_vehicle_locations_feed**](DefaultApi.md#get_vehicle_locations_feed) | **GET** /fleet/vehicles/locations/feed | Follow a feed of vehicle locations
[**get_vehicle_locations_history**](DefaultApi.md#get_vehicle_locations_history) | **GET** /fleet/vehicles/locations/history | Get historical vehicle locations
[**get_vehicle_stats**](DefaultApi.md#get_vehicle_stats) | **GET** /fleet/vehicles/stats | List most recent vehicle stats
[**get_vehicle_stats_feed**](DefaultApi.md#get_vehicle_stats_feed) | **GET** /fleet/vehicles/stats/feed | Follow a feed of vehicle stats
[**get_vehicle_stats_history**](DefaultApi.md#get_vehicle_stats_history) | **GET** /fleet/vehicles/stats/history | Get historical vehicle stats
[**get_vision_runs_by_camera**](DefaultApi.md#get_vision_runs_by_camera) | **GET** /v1/industrial/vision/runs/{camera_id} | Fetch runs by camera
[**list_addresses**](DefaultApi.md#list_addresses) | **GET** /addresses | List all addresses
[**list_contacts**](DefaultApi.md#list_contacts) | **GET** /contacts | List all contacts
[**list_drivers**](DefaultApi.md#list_drivers) | **GET** /fleet/drivers | List all drivers
[**list_tags**](DefaultApi.md#list_tags) | **GET** /tags | List all tags
[**list_user_roles**](DefaultApi.md#list_user_roles) | **GET** /user-roles | List all user roles
[**list_users**](DefaultApi.md#list_users) | **GET** /users | List all users
[**list_vehicles**](DefaultApi.md#list_vehicles) | **GET** /fleet/vehicles | List all vehicles
[**replace_tag**](DefaultApi.md#replace_tag) | **PUT** /tags/{id} | Update a tag
[**update_address**](DefaultApi.md#update_address) | **PATCH** /addresses/{id} | Update an address
[**update_contact**](DefaultApi.md#update_contact) | **PATCH** /contacts/{id} | Update a contact
[**update_driver**](DefaultApi.md#update_driver) | **PATCH** /fleet/drivers/{id} | Update a driver
[**update_user**](DefaultApi.md#update_user) | **PATCH** /users/{id} | Update a user
[**update_vehicle**](DefaultApi.md#update_vehicle) | **PATCH** /fleet/vehicles/{id} | Update a vehicle
[**v1create_dispatch_route**](DefaultApi.md#v1create_dispatch_route) | **POST** /v1/fleet/dispatch/routes | Create a new route
[**v1create_driver_document**](DefaultApi.md#v1create_driver_document) | **POST** /v1/fleet/drivers/{driver_id}/documents | Create a document
[**v1create_dvir**](DefaultApi.md#v1create_dvir) | **POST** /v1/fleet/maintenance/dvirs | Create a DVIR
[**v1create_messages**](DefaultApi.md#v1create_messages) | **POST** /v1/fleet/messages | Send a message to a list of driver ids.
[**v1delete_dispatch_route_by_id**](DefaultApi.md#v1delete_dispatch_route_by_id) | **DELETE** /v1/fleet/dispatch/routes/{route_id} | Delete a route
[**v1fetch_all_dispatch_routes**](DefaultApi.md#v1fetch_all_dispatch_routes) | **GET** /v1/fleet/dispatch/routes | Get all routes
[**v1fetch_all_route_job_updates**](DefaultApi.md#v1fetch_all_route_job_updates) | **GET** /v1/fleet/dispatch/routes/job_updates | Get route updates
[**v1get_all_asset_current_locations**](DefaultApi.md#v1get_all_asset_current_locations) | **GET** /v1/fleet/assets/locations | List current location for all assets
[**v1get_all_assets**](DefaultApi.md#v1get_all_assets) | **GET** /v1/fleet/assets | List all assets
[**v1get_all_data_inputs**](DefaultApi.md#v1get_all_data_inputs) | **GET** /v1/industrial/data | Get industrial data
[**v1get_all_trailer_assignments**](DefaultApi.md#v1get_all_trailer_assignments) | **GET** /v1/fleet/trailers/assignments | List trailer assignments for all trailers
[**v1get_asset_location**](DefaultApi.md#v1get_asset_location) | **GET** /v1/fleet/assets/{asset_id}/locations | List historical locations for a given asset
[**v1get_asset_reefer**](DefaultApi.md#v1get_asset_reefer) | **GET** /v1/fleet/assets/{asset_id}/reefer | List stats for a given reefer
[**v1get_assets_reefers**](DefaultApi.md#v1get_assets_reefers) | **GET** /v1/fleet/assets/reefers | List stats for all reefers
[**v1get_cameras**](DefaultApi.md#v1get_cameras) | **GET** /v1/industrial/vision/cameras | Fetch industrial cameras
[**v1get_data_input**](DefaultApi.md#v1get_data_input) | **GET** /v1/industrial/data/{data_input_id} | Get industrial data from a specific device
[**v1get_dispatch_route_by_id**](DefaultApi.md#v1get_dispatch_route_by_id) | **GET** /v1/fleet/dispatch/routes/{route_id} | Get a route
[**v1get_dispatch_route_history**](DefaultApi.md#v1get_dispatch_route_history) | **GET** /v1/fleet/dispatch/routes/{route_id}/history | Get route history
[**v1get_driver_document_by_id_and_driver_id**](DefaultApi.md#v1get_driver_document_by_id_and_driver_id) | **GET** /v1/fleet/drivers/{driver_id}/documents/{document_id} | Fetches a document
[**v1get_driver_document_types_by_org_id**](DefaultApi.md#v1get_driver_document_types_by_org_id) | **GET** /v1/fleet/drivers/document_types | Fetch document types
[**v1get_driver_documents_by_org_id**](DefaultApi.md#v1get_driver_documents_by_org_id) | **GET** /v1/fleet/drivers/documents | Fetch all documents
[**v1get_driver_safety_score**](DefaultApi.md#v1get_driver_safety_score) | **GET** /v1/fleet/drivers/{driverId}/safety/score | Fetch driver safety score
[**v1get_dvirs**](DefaultApi.md#v1get_dvirs) | **GET** /v1/fleet/maintenance/dvirs | Get DVIRs
[**v1get_fleet_drivers_hos_daily_logs**](DefaultApi.md#v1get_fleet_drivers_hos_daily_logs) | **POST** /v1/fleet/drivers/{driver_id}/hos_daily_logs | Get daily HOS logs for a specific driver
[**v1get_fleet_hos_authentication_logs**](DefaultApi.md#v1get_fleet_hos_authentication_logs) | **GET** /v1/fleet/hos_authentication_logs | Get HOS signin and signout
[**v1get_fleet_hos_logs**](DefaultApi.md#v1get_fleet_hos_logs) | **POST** /v1/fleet/hos_logs | Get HOS logs for a specific driver
[**v1get_fleet_hos_logs_summary**](DefaultApi.md#v1get_fleet_hos_logs_summary) | **GET** /v1/fleet/hos_logs_summary | Get current HOS status for all drivers
[**v1get_fleet_maintenance_list**](DefaultApi.md#v1get_fleet_maintenance_list) | **GET** /v1/fleet/maintenance/list | Get vehicles with engine faults or check lights
[**v1get_fleet_trailer_assignments**](DefaultApi.md#v1get_fleet_trailer_assignments) | **GET** /v1/fleet/trailers/{trailerId}/assignments | List trailer assignments for a given trailer
[**v1get_fleet_trips**](DefaultApi.md#v1get_fleet_trips) | **GET** /v1/fleet/trips | Get vehicle trips
[**v1get_machines**](DefaultApi.md#v1get_machines) | **POST** /v1/machines/list | Get machines
[**v1get_machines_history**](DefaultApi.md#v1get_machines_history) | **POST** /v1/machines/history | Get machine history
[**v1get_messages**](DefaultApi.md#v1get_messages) | **GET** /v1/fleet/messages | Get all messages.
[**v1get_sensors**](DefaultApi.md#v1get_sensors) | **POST** /v1/sensors/list | Get all sensors
[**v1get_sensors_cargo**](DefaultApi.md#v1get_sensors_cargo) | **POST** /v1/sensors/cargo | Get cargo status
[**v1get_sensors_door**](DefaultApi.md#v1get_sensors_door) | **POST** /v1/sensors/door | Get door status
[**v1get_sensors_history**](DefaultApi.md#v1get_sensors_history) | **POST** /v1/sensors/history | Get sensor history
[**v1get_sensors_humidity**](DefaultApi.md#v1get_sensors_humidity) | **POST** /v1/sensors/humidity | Get humidity
[**v1get_sensors_temperature**](DefaultApi.md#v1get_sensors_temperature) | **POST** /v1/sensors/temperature | Get temperature
[**v1get_vehicle_harsh_event**](DefaultApi.md#v1get_vehicle_harsh_event) | **GET** /v1/fleet/vehicles/{vehicleId}/safety/harsh_event | Fetch harsh events
[**v1get_vehicle_safety_score**](DefaultApi.md#v1get_vehicle_safety_score) | **GET** /v1/fleet/vehicles/{vehicleId}/safety/score | Fetch vehicle safety scores
[**v1get_vision_latest_run_camera**](DefaultApi.md#v1get_vision_latest_run_camera) | **GET** /v1/industrial/vision/run/camera/{camera_id} | Fetch the latest run for a camera or program
[**v1get_vision_programs_by_camera**](DefaultApi.md#v1get_vision_programs_by_camera) | **GET** /v1/industrial/vision/cameras/{camera_id}/programs | Fetch industrial camera programs
[**v1get_vision_runs**](DefaultApi.md#v1get_vision_runs) | **GET** /v1/industrial/vision/runs | Fetch runs
[**v1get_vision_runs_by_camera_and_program**](DefaultApi.md#v1get_vision_runs_by_camera_and_program) | **GET** /v1/industrial/vision/runs/{camera_id}/{program_id}/{started_at_ms} | Fetch runs by camera and program
[**v1update_dispatch_route_by_id**](DefaultApi.md#v1update_dispatch_route_by_id) | **PUT** /v1/fleet/dispatch/routes/{route_id} | Update a route


# **create_address**
> AddressResponse create_address(address)

Create an address

Creates a new address in the organization

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
    api_instance = samsara.DefaultApi(api_client)
    address = samsara.CreateAddressRequest() # CreateAddressRequest | The address to create.

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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created address object with ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact**
> ContactResponse create_contact(contact)

Create a contact

Add a contact to the organization

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
    api_instance = samsara.DefaultApi(api_client)
    contact = samsara.CreateContactRequest() # CreateContactRequest | The contact create parameters.

    try:
        # Create a contact
        api_response = api_instance.create_contact(contact)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | [**CreateContactRequest**](CreateContactRequest.md)| The contact create parameters. | 

### Return type

[**ContactResponse**](ContactResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact was successfully added. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_driver**
> DriverResponse create_driver(driver)

Create a driver

Add a driver to the organization.

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
    api_instance = samsara.DefaultApi(api_client)
    driver = samsara.CreateDriverRequest() # CreateDriverRequest | The driver to create.

    try:
        # Create a driver
        api_response = api_instance.create_driver(driver)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver** | [**CreateDriverRequest**](CreateDriverRequest.md)| The driver to create. | 

### Return type

[**DriverResponse**](DriverResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created driver object, with Samsara-generated ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = samsara.DefaultApi(api_client)
    tag_create_body_ = samsara.CreateTagRequest() # CreateTagRequest | 

    try:
        # Create a tag
        api_response = api_instance.create_tag(tag_create_body_)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_tag: %s\n" % e)
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

# **create_user**
> UserResponse create_user(user)

Create a user

Add a user to the organization.

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
    api_instance = samsara.DefaultApi(api_client)
    user = samsara.CreateUserRequest() # CreateUserRequest | The user to create.

    try:
        # Create a user
        api_response = api_instance.create_user(user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**CreateUserRequest**](CreateUserRequest.md)| The user to create. | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created user object with ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_address**
> delete_address(id)

Delete an address

Delete a specific address.

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
    api_instance = samsara.DefaultApi(api_client)
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Empty success body |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> delete_contact(id)

Delete a contact

Delete the given contact.

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
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the contact.

    try:
        # Delete a contact
        api_instance.delete_contact(id)
    except ApiException as e:
        print("Exception when calling DefaultApi->delete_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the contact. | 

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
**204** | Returns an empty success response. |  -  |
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
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the tag.

    try:
        # Delete a tag
        api_instance.delete_tag(id)
    except ApiException as e:
        print("Exception when calling DefaultApi->delete_tag: %s\n" % e)
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

# **delete_user**
> delete_user(id)

Delete a user

Delete the given user.

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
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the user.

    try:
        # Delete a user
        api_instance.delete_user(id)
    except ApiException as e:
        print("Exception when calling DefaultApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the user. | 

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
**204** | Returns an empty success response. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address**
> AddressResponse get_address(id)

Retrieve an address

Returns a specific address.

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
    api_instance = samsara.DefaultApi(api_client)
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Address. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact**
> ContactResponse get_contact(id)

Retrieve a contact

Get a specific contact's information.

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
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the contact.

    try:
        # Retrieve a contact
        api_response = api_instance.get_contact(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the contact. | 

### Return type

[**ContactResponse**](ContactResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified contact. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_driver**
> DriverResponse get_driver(id)

Retrieve a driver

Get information about a driver.

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
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`

    try:
        # Retrieve a driver
        api_response = api_instance.get_driver(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 

### Return type

[**DriverResponse**](DriverResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified driver. |  -  |
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
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the tag.

    try:
        # Retrieve a tag
        api_response = api_instance.get_tag(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_tag: %s\n" % e)
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

# **get_user**
> UserResponse get_user(id)

Retrieve a user

Get a specific user's information.

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
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the user.

    try:
        # Retrieve a user
        api_response = api_instance.get_user(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the user. | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified user. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle**
> VehicleResponse get_vehicle(id)

Retrieve a vehicle

Get information about a specific vehicle.

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
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `maintenanceId:250020`

    try:
        # Retrieve a vehicle
        api_response = api_instance.get_vehicle(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;maintenanceId:250020&#x60; | 

### Return type

[**VehicleResponse**](VehicleResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified vehicle object. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_locations**
> VehicleLocationsResponse get_vehicle_locations(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Get most recent vehicle locations

Returns last known location for all vehicles (connected via Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-locations) for more details.

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
    api_instance = samsara.DefaultApi(api_client)
    after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

    try:
        # Get most recent vehicle locations
        api_response = api_instance.get_vehicle_locations(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_vehicle_locations: %s\n" % e)
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the most recent locations for the specified vehicles. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_locations_feed**
> VehicleLocationsListResponse get_vehicle_locations_feed(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Follow a feed of vehicle locations

Follow a continuous feed of all vehicle locations from Samsara Vehicle Gateways.  Your first call to this endpoint will provide you with the most recent location for each vehicle and a `pagination` object that contains an `endCursor`.  You can provide the `endCursor` to the `after` parameter of this endpoint to get location updates since that `endCursor`.   If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest waiting a minimum of 5 seconds before requesting updates.  See [this guide](https://developers.samsara.com/docs/vehicle-locations#section-follow-a-real-time-feed-of-vehicle-locations) for more details.

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
    api_instance = samsara.DefaultApi(api_client)
    after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

    try:
        # Follow a feed of vehicle locations
        api_response = api_instance.get_vehicle_locations_feed(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_vehicle_locations_feed: %s\n" % e)
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of locations events for the specified vehicles. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_locations_history**
> VehicleLocationsListResponse get_vehicle_locations_history(start_time, end_time, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Get historical vehicle locations

Returns all known vehicle locations during the given time range for all vehicles (connected via Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-locations) for more details.

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
    api_instance = samsara.DefaultApi(api_client)
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
        print("Exception when calling DefaultApi->get_vehicle_locations_history: %s\n" % e)
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all locations for the specified vehicles and time range. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_stats**
> VehicleStatsResponse get_vehicle_stats(types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

List most recent vehicle stats

Returns last known stats for all vehicles (connected via Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-stats) for more details.

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
    api_instance = samsara.DefaultApi(api_client)
    types = 'types_example' # str | The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `obdOdometerMeters`: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using `gpsOdometerMeters`. - `gpsOdometerMeters`: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara's dashboard UI or through the `odometerMeters` field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. `gpsOdometerMeters` is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to on-board diagnostics. - `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

    try:
        # List most recent vehicle stats
        api_response = api_instance.get_vehicle_stats(types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_vehicle_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | **str**| The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;obdOdometerMeters&#x60;: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using &#x60;gpsOdometerMeters&#x60;. - &#x60;gpsOdometerMeters&#x60;: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara&#39;s dashboard UI or through the &#x60;odometerMeters&#x60; field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. &#x60;gpsOdometerMeters&#x60; is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to on-board diagnostics. - &#x60;gpsDistanceMeters&#x60;: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleStatsResponse**](VehicleStatsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the most recent stats for the specified vehicles and stat types. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_stats_feed**
> VehicleStatsListResponse get_vehicle_stats_feed(types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Follow a feed of vehicle stats

Follow a continuous feed of vehicle stats from Samsara Vehicle Gateways.  Your first call to this endpoint will provide you with the most recent stats for each vehicle and a `pagination` object that contains an `endCursor`.  You can provide the `endCursor` to the `after` parameter of this endpoint to get vehicle stat updates since that `endCursor`.  If `hasNextPage` is `false`, no updates are readily available yet. Each stat type has a different refresh rate, but in general we'd suggest waiting a minimum of 5 seconds before requesting updates. See [this guide](https://developers.samsara.com/docs/vehicle-stats#section-follow-a-real-time-feed-of-vehicle-stats) for more details.

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
    api_instance = samsara.DefaultApi(api_client)
    types = 'types_example' # str | The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `obdOdometerMeters`: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using `gpsOdometerMeters`. - `gpsOdometerMeters`: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara's dashboard UI or through the `odometerMeters` field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. `gpsOdometerMeters` is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to on-board diagnostics. - `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

    try:
        # Follow a feed of vehicle stats
        api_response = api_instance.get_vehicle_stats_feed(types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_vehicle_stats_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | **str**| The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;obdOdometerMeters&#x60;: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using &#x60;gpsOdometerMeters&#x60;. - &#x60;gpsOdometerMeters&#x60;: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara&#39;s dashboard UI or through the &#x60;odometerMeters&#x60; field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. &#x60;gpsOdometerMeters&#x60; is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to on-board diagnostics. - &#x60;gpsDistanceMeters&#x60;: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleStatsListResponse**](VehicleStatsListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of stat events for the specified vehicles and stat types. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_stats_history**
> VehicleStatsListResponse get_vehicle_stats_history(start_time, end_time, types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Get historical vehicle stats

Returns vehicle stats events during the given time range for all vehicles (connected via Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-stats) for more details.

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
    api_instance = samsara.DefaultApi(api_client)
    start_time = '2013-10-20T19:20:30+01:00' # datetime | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = '2013-10-20T19:20:30+01:00' # datetime | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
types = 'types_example' # str | The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `obdOdometerMeters`: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using `gpsOdometerMeters`. - `gpsOdometerMeters`: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara's dashboard UI or through the `odometerMeters` field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. `gpsOdometerMeters` is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to on-board diagnostics. - `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

    try:
        # Get historical vehicle stats
        api_response = api_instance.get_vehicle_stats_history(start_time, end_time, types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_vehicle_stats_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **datetime**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **types** | **str**| The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;obdOdometerMeters&#x60;: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using &#x60;gpsOdometerMeters&#x60;. - &#x60;gpsOdometerMeters&#x60;: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara&#39;s dashboard UI or through the &#x60;odometerMeters&#x60; field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. &#x60;gpsOdometerMeters&#x60; is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to on-board diagnostics. - &#x60;gpsDistanceMeters&#x60;: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleStatsListResponse**](VehicleStatsListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of vehicle stats for the specified vehicles, stat type, and time range. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vision_runs_by_camera**
> list[object] get_vision_runs_by_camera(camera_id, duration_ms, end_ms=end_ms)

Fetch runs by camera

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch runs by camera.

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
    api_instance = samsara.DefaultApi(api_client)
    camera_id = 56 # int | The camera_id should be valid for the given accessToken.
duration_ms = 56 # int | DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched
end_ms = 56 # int | EndMs is an optional param. It will default to the current time. (optional)

    try:
        # Fetch runs by camera
        api_response = api_instance.get_vision_runs_by_camera(camera_id, duration_ms, end_ms=end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_vision_runs_by_camera: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **camera_id** | **int**| The camera_id should be valid for the given accessToken. | 
 **duration_ms** | **int**| DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched | 
 **end_ms** | **int**| EndMs is an optional param. It will default to the current time. | [optional] 

### Return type

**list[object]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return runs by cameraId. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_addresses**
> ListAddressesResponse list_addresses(limit=limit, after=after, tag_ids=tag_ids)

List all addresses

Returns a list of all addresses in an organization

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
    api_instance = samsara.DefaultApi(api_client)
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all addresses in the organization |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contacts**
> ListContactsResponse list_contacts(limit=limit, after=after)

List all contacts

Returns a list of all contacts in an organization.

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
    api_instance = samsara.DefaultApi(api_client)
    limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

    try:
        # List all contacts
        api_response = api_instance.list_contacts(limit=limit, after=after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

### Return type

[**ListContactsResponse**](ListContactsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all contacts |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_drivers**
> ListDriversResponse list_drivers(is_deactivated=is_deactivated, limit=limit, after=after, tag_ids=tag_ids, updated_after_time=updated_after_time, created_after_time=created_after_time)

List all drivers

Get all drivers in organization.

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
    api_instance = samsara.DefaultApi(api_client)
    is_deactivated = True # bool | If value is true, only drivers that are deactivated will appear in the response. This parameter will default to false if not provided (fetching only active drivers). (optional)
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
updated_after_time = '2013-10-20T19:20:30+01:00' # datetime | A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). (optional)
created_after_time = '2013-10-20T19:20:30+01:00' # datetime | A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). (optional)

    try:
        # List all drivers
        api_response = api_instance.list_drivers(is_deactivated=is_deactivated, limit=limit, after=after, tag_ids=tag_ids, updated_after_time=updated_after_time, created_after_time=created_after_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_drivers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_deactivated** | **bool**| If value is true, only drivers that are deactivated will appear in the response. This parameter will default to false if not provided (fetching only active drivers). | [optional] 
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **updated_after_time** | **datetime**| A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 
 **created_after_time** | **datetime**| A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 

### Return type

[**ListDriversResponse**](ListDriversResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all driver objects. |  -  |
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
    api_instance = samsara.DefaultApi(api_client)
    limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

    try:
        # List all tags
        api_response = api_instance.list_tags(limit=limit, after=after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_tags: %s\n" % e)
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

# **list_user_roles**
> ListUserTagRolesResponse list_user_roles(limit=limit, after=after)

List all user roles

Returns a list of all user roles in an organization.

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
    api_instance = samsara.DefaultApi(api_client)
    limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

    try:
        # List all user roles
        api_response = api_instance.list_user_roles(limit=limit, after=after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

### Return type

[**ListUserTagRolesResponse**](ListUserTagRolesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all user roles. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ListUsersResponse list_users(limit=limit, after=after)

List all users

Returns a list of all users in an organization.

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
    api_instance = samsara.DefaultApi(api_client)
    limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

    try:
        # List all users
        api_response = api_instance.list_users(limit=limit, after=after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all users. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vehicles**
> ListVehiclesResponse list_vehicles(limit=limit, after=after, tag_ids=tag_ids)

List all vehicles

Returns a list of all vehicles.

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
    api_instance = samsara.DefaultApi(api_client)
    limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)

    try:
        # List all vehicles
        api_response = api_instance.list_vehicles(limit=limit, after=after, tag_ids=tag_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_vehicles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**ListVehiclesResponse**](ListVehiclesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all vehicle objects, and pagination parameters. |  -  |
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
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the tag.
tag_update_body_ = samsara.ReplaceTagRequest() # ReplaceTagRequest | 

    try:
        # Update a tag
        api_response = api_instance.replace_tag(id, tag_update_body_)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->replace_tag: %s\n" % e)
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

# **update_address**
> AddressResponse update_address(id, address)

Update an address

Update a specific address.

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
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`
address = samsara.UpdateAddressRequest() # UpdateAddressRequest | The address fields to update.

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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated address object with ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> ContactResponse update_contact(id, contact)

Update a contact

Update a specific contact's information.

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
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the contact.
contact = samsara.UpdateContactRequest() # UpdateContactRequest | Updates to the contact.

    try:
        # Update a contact
        api_response = api_instance.update_contact(id, contact)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the contact. | 
 **contact** | [**UpdateContactRequest**](UpdateContactRequest.md)| Updates to the contact. | 

### Return type

[**ContactResponse**](ContactResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated contact object with given ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_driver**
> DriverResponse update_driver(id, driver)

Update a driver

Update a specific driver's information. This can also be used to activate or de-activate a given driver

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
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
driver = samsara.UpdateDriverRequest() # UpdateDriverRequest | Updates to the driver properties.

    try:
        # Update a driver
        api_response = api_instance.update_driver(id, driver)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 
 **driver** | [**UpdateDriverRequest**](UpdateDriverRequest.md)| Updates to the driver properties. | 

### Return type

[**DriverResponse**](DriverResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated driver object, with ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserResponse update_user(id, user)

Update a user

Update a specific user's information.

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
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the user.
user = samsara.UpdateUserRequest() # UpdateUserRequest | Updates to the user.

    try:
        # Update a user
        api_response = api_instance.update_user(id, user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the user. | 
 **user** | [**UpdateUserRequest**](UpdateUserRequest.md)| Updates to the user. | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user object with ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vehicle**
> VehicleResponse update_vehicle(id, vehicle)

Update a vehicle

Updates the given Vehicle object.  **Note:** Vehicle objects are automatically created when Samsara Vehicle Gateways are installed. You cannot create a Vehicle object via API.  You are able to *update* many of the fields of a Vehicle.  **Note**: There are no required fields in the request body, and you only need to provide the fields you wish to update.

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
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `maintenanceId:250020`
vehicle = samsara.UpdateVehicleRequest() # UpdateVehicleRequest | Fields that can be patched on a vehicle.

    try:
        # Update a vehicle
        api_response = api_instance.update_vehicle(id, vehicle)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;maintenanceId:250020&#x60; | 
 **vehicle** | [**UpdateVehicleRequest**](UpdateVehicleRequest.md)| Fields that can be patched on a vehicle. | 

### Return type

[**VehicleResponse**](VehicleResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified vehicle object. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1create_dispatch_route**
> V1DispatchRoute v1create_dispatch_route(create_dispatch_route_params)

Create a new route

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Create a new dispatch route.

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
    api_instance = samsara.DefaultApi(api_client)
    create_dispatch_route_params = samsara.V1DispatchRouteCreate() # V1DispatchRouteCreate | 

    try:
        # Create a new route
        api_response = api_instance.v1create_dispatch_route(create_dispatch_route_params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1create_dispatch_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dispatch_route_params** | [**V1DispatchRouteCreate**](V1DispatchRouteCreate.md)|  | 

### Return type

[**V1DispatchRoute**](V1DispatchRoute.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created route object including the new route ID. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1create_driver_document**
> V1Document v1create_driver_document(driver_id, create_document_params)

Create a document

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Create a document for the given driver.

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
    api_instance = samsara.DefaultApi(api_client)
    driver_id = 56 # int | ID of the driver for whom the document is created. Must contain only digits 0-9.
create_document_params = samsara.V1DocumentCreate() # V1DocumentCreate | To create a document for a given document type, provide the `documentTypeUuid` of the type of document you'd like to create. Then, pass in the `fields` of the document in the same order that they show up in the given document type.

    try:
        # Create a document
        api_response = api_instance.v1create_driver_document(driver_id, create_document_params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1create_driver_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| ID of the driver for whom the document is created. Must contain only digits 0-9. | 
 **create_document_params** | [**V1DocumentCreate**](V1DocumentCreate.md)| To create a document for a given document type, provide the &#x60;documentTypeUuid&#x60; of the type of document you&#39;d like to create. Then, pass in the &#x60;fields&#x60; of the document in the same order that they show up in the given document type. | 

### Return type

[**V1Document**](V1Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the created document. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1create_dvir**
> V1DvirBase v1create_dvir(create_dvir_param)

Create a DVIR

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Create a new dvir, marking a vehicle or trailer safe or unsafe.

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
    api_instance = samsara.DefaultApi(api_client)
    create_dvir_param = samsara.InlineObject2() # InlineObject2 | 

    try:
        # Create a DVIR
        api_response = api_instance.v1create_dvir(create_dvir_param)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1create_dvir: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dvir_param** | [**InlineObject2**](InlineObject2.md)|  | 

### Return type

[**V1DvirBase**](V1DvirBase.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created DVIR. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1create_messages**
> InlineResponse2005 v1create_messages(create_messages)

Send a message to a list of driver ids.

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Send a message to a list of driver ids.

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
    api_instance = samsara.DefaultApi(api_client)
    create_messages = samsara.InlineObject3() # InlineObject3 | 

    try:
        # Send a message to a list of driver ids.
        api_response = api_instance.v1create_messages(create_messages)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1create_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_messages** | [**InlineObject3**](InlineObject3.md)|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the created messages. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1delete_dispatch_route_by_id**
> v1delete_dispatch_route_by_id(route_id)

Delete a route

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Delete a dispatch route and its associated jobs.

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
    api_instance = samsara.DefaultApi(api_client)
    route_id = 56 # int | ID of the dispatch route. Must contain only digits 0-9.

    try:
        # Delete a route
        api_instance.v1delete_dispatch_route_by_id(route_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1delete_dispatch_route_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| ID of the dispatch route. Must contain only digits 0-9. | 

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
**200** | Successfully deleted the dispatch route. No response body is returned. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1fetch_all_dispatch_routes**
> list[V1DispatchRouteWithoutETA] v1fetch_all_dispatch_routes(end_time=end_time, duration=duration)

Get all routes

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all dispatch routes for a given time period. The time period is defined as `end_time` and the `duration` before which to query.  Routes are returned if the route's `scheduled_start_ms` and `scheduled_end_ms` overlap with the requested time period.  More concretely, if the route's `scheduled_start_ms` is before `end_time` and the `scheduled_end_ms` is within or after the given duration, then the route is returned.

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
    api_instance = samsara.DefaultApi(api_client)
    end_time = 56 # int | Time in unix milliseconds that represents the end time of the requested time interval. See above for a description of how routes are returned. Defaults to now. (optional)
duration = 56 # int | Time in milliseconds that represents the duration before end_time to query. Defaults to 24 hours. (optional)

    try:
        # Get all routes
        api_response = api_instance.v1fetch_all_dispatch_routes(end_time=end_time, duration=duration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1fetch_all_dispatch_routes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_time** | **int**| Time in unix milliseconds that represents the end time of the requested time interval. See above for a description of how routes are returned. Defaults to now. | [optional] 
 **duration** | **int**| Time in milliseconds that represents the duration before end_time to query. Defaults to 24 hours. | [optional] 

### Return type

[**list[V1DispatchRouteWithoutETA]**](V1DispatchRouteWithoutETA.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All dispatch route objects. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1fetch_all_route_job_updates**
> V1allRouteJobUpdates v1fetch_all_route_job_updates(sequence_id=sequence_id, include=include)

Get route updates

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all updates to a job including route data in the last 24 hours or subsequent to an sequence ID. Returns a maximum of 500 job updates. If more than 500 job updates are available, another request made with the prior request's sequence_id will return the next set of available job updates.

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
    api_instance = samsara.DefaultApi(api_client)
    sequence_id = 'sequence_id_example' # str | Sequence ID from the response payload of the last request. Defaults to fetching updates from last 24 hours. (optional)
include = 'include_example' # str | Optionally set include=route to include route object in response payload. (optional)

    try:
        # Get route updates
        api_response = api_instance.v1fetch_all_route_job_updates(sequence_id=sequence_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1fetch_all_route_job_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **str**| Sequence ID from the response payload of the last request. Defaults to fetching updates from last 24 hours. | [optional] 
 **include** | **str**| Optionally set include&#x3D;route to include route object in response payload. | [optional] 

### Return type

[**V1allRouteJobUpdates**](V1allRouteJobUpdates.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All job updates on routes. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_all_asset_current_locations**
> InlineResponse2001 v1get_all_asset_current_locations(starting_after=starting_after, ending_before=ending_before, limit=limit)

List current location for all assets

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch current locations of all assets.

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
    api_instance = samsara.DefaultApi(api_client)
    starting_after = 'starting_after_example' # str | Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter. (optional)
ending_before = 'ending_before_example' # str | Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter. (optional)
limit = 3.4 # float | Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'. (optional)

    try:
        # List current location for all assets
        api_response = api_instance.v1get_all_asset_current_locations(starting_after=starting_after, ending_before=ending_before, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_all_asset_current_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starting_after** | **str**| Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the &#39;limit&#39; parameter. Mutually exclusive with &#39;endingBefore&#39; parameter. | [optional] 
 **ending_before** | **str**| Pagination parameter indicating the cursor position to return results before. Used in conjunction with the &#39;limit&#39; parameter. Mutually exclusive with &#39;startingAfter&#39; parameter. | [optional] 
 **limit** | **float**| Pagination parameter indicating the number of results to return in this request. Used in conjunction with either &#39;startingAfter&#39; or &#39;endingBefore&#39;. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of assets and their current locations. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_all_assets**
> InlineResponse200 v1get_all_assets()

List all assets

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all of the assets.

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
    api_instance = samsara.DefaultApi(api_client)
    
    try:
        # List all assets
        api_response = api_instance.v1get_all_assets()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_all_assets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of assets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_all_data_inputs**
> InlineResponse2007 v1get_all_data_inputs(start_ms=start_ms, end_ms=end_ms)

Get industrial data

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all of the data inputs.

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
    api_instance = samsara.DefaultApi(api_client)
    start_ms = 56 # int | Timestamp in unix milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. defaults to nowMs. (optional)
end_ms = 56 # int | Timestamp in unix milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Defaults to nowMs. (optional)

    try:
        # Get industrial data
        api_response = api_instance.v1get_all_data_inputs(start_ms=start_ms, end_ms=end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_all_data_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_ms** | **int**| Timestamp in unix milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. defaults to nowMs. | [optional] 
 **end_ms** | **int**| Timestamp in unix milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Defaults to nowMs. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of data inputs. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = samsara.DefaultApi(api_client)
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
        print("Exception when calling DefaultApi->v1get_all_trailer_assignments: %s\n" % e)
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

# **v1get_asset_location**
> list[object] v1get_asset_location(asset_id, start_ms, end_ms)

List historical locations for a given asset

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  List historical locations for a given asset

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
    api_instance = samsara.DefaultApi(api_client)
    asset_id = 56 # int | ID of the asset. Must contain only digits 0-9.
start_ms = 56 # int | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs.
end_ms = 56 # int | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs.

    try:
        # List historical locations for a given asset
        api_response = api_instance.v1get_asset_location(asset_id, start_ms, end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_asset_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| ID of the asset. Must contain only digits 0-9. | 
 **start_ms** | **int**| Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. | 
 **end_ms** | **int**| Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. | 

### Return type

**list[object]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset location details. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_asset_reefer**
> V1AssetReeferResponse v1get_asset_reefer(asset_id, start_ms, end_ms)

List stats for a given reefer

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch the reefer-specific stats of an asset.

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
    api_instance = samsara.DefaultApi(api_client)
    asset_id = 56 # int | ID of the asset. Must contain only digits 0-9.
start_ms = 56 # int | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs.
end_ms = 56 # int | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs.

    try:
        # List stats for a given reefer
        api_response = api_instance.v1get_asset_reefer(asset_id, start_ms, end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_asset_reefer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| ID of the asset. Must contain only digits 0-9. | 
 **start_ms** | **int**| Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. | 
 **end_ms** | **int**| Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. | 

### Return type

[**V1AssetReeferResponse**](V1AssetReeferResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reefer-specific asset details. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_assets_reefers**
> InlineResponse2002 v1get_assets_reefers(start_ms, end_ms, starting_after=starting_after, ending_before=ending_before, limit=limit)

List stats for all reefers

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetches all reefers and reefer-specific stats.

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
    api_instance = samsara.DefaultApi(api_client)
    start_ms = 56 # int | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs.
end_ms = 56 # int | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs.
starting_after = 'starting_after_example' # str | Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter. (optional)
ending_before = 'ending_before_example' # str | Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter. (optional)
limit = 3.4 # float | Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'. (optional)

    try:
        # List stats for all reefers
        api_response = api_instance.v1get_assets_reefers(start_ms, end_ms, starting_after=starting_after, ending_before=ending_before, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_assets_reefers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_ms** | **int**| Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. | 
 **end_ms** | **int**| Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. | 
 **starting_after** | **str**| Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the &#39;limit&#39; parameter. Mutually exclusive with &#39;endingBefore&#39; parameter. | [optional] 
 **ending_before** | **str**| Pagination parameter indicating the cursor position to return results before. Used in conjunction with the &#39;limit&#39; parameter. Mutually exclusive with &#39;startingAfter&#39; parameter. | [optional] 
 **limit** | **float**| Pagination parameter indicating the number of results to return in this request. Used in conjunction with either &#39;startingAfter&#39; or &#39;endingBefore&#39;. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All org reefers and reefer-specific details. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_cameras**
> list[object] v1get_cameras()

Fetch industrial cameras

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all cameras.

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
    api_instance = samsara.DefaultApi(api_client)
    
    try:
        # Fetch industrial cameras
        api_response = api_instance.v1get_cameras()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_cameras: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns details about a camera. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_data_input**
> V1DataInputHistoryResponse v1get_data_input(data_input_id, start_ms=start_ms, end_ms=end_ms)

Get industrial data from a specific device

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch datapoints from a given data input.

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
    api_instance = samsara.DefaultApi(api_client)
    data_input_id = 56 # int | ID of the data input. Must contain only digits 0-9.
start_ms = 56 # int | Timestamp in unix milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. defaults to nowMs. (optional)
end_ms = 56 # int | Timestamp in unix milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Defaults to nowMs. (optional)

    try:
        # Get industrial data from a specific device
        api_response = api_instance.v1get_data_input(data_input_id, start_ms=start_ms, end_ms=end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_data_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_input_id** | **int**| ID of the data input. Must contain only digits 0-9. | 
 **start_ms** | **int**| Timestamp in unix milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. defaults to nowMs. | [optional] 
 **end_ms** | **int**| Timestamp in unix milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Defaults to nowMs. | [optional] 

### Return type

[**V1DataInputHistoryResponse**](V1DataInputHistoryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns datapoints for the given data input |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_dispatch_route_by_id**
> V1DispatchRoute v1get_dispatch_route_by_id(route_id)

Get a route

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch a dispatch route by id.

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
    api_instance = samsara.DefaultApi(api_client)
    route_id = 56 # int | ID of the dispatch route. Must contain only digits 0-9.

    try:
        # Get a route
        api_response = api_instance.v1get_dispatch_route_by_id(route_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_dispatch_route_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| ID of the dispatch route. Must contain only digits 0-9. | 

### Return type

[**V1DispatchRoute**](V1DispatchRoute.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The dispatch route corresponding to route_id. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_dispatch_route_history**
> V1DispatchRouteHistory v1get_dispatch_route_history(route_id, start_time=start_time, end_time=end_time)

Get route history

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch the history of a dispatch route.

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
    api_instance = samsara.DefaultApi(api_client)
    route_id = 56 # int | ID of the route with history. Must contain only digits 0-9.
start_time = 56 # int | Timestamp representing the start of the period to fetch, inclusive. Used in combination with end_time. Defaults to 0. (optional)
end_time = 56 # int | Timestamp representing the end of the period to fetch, inclusive. Used in combination with start_time. Defaults to nowMs. (optional)

    try:
        # Get route history
        api_response = api_instance.v1get_dispatch_route_history(route_id, start_time=start_time, end_time=end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_dispatch_route_history: %s\n" % e)
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The historical route state changes between start_time and end_time. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_driver_document_by_id_and_driver_id**
> V1Document v1get_driver_document_by_id_and_driver_id(driver_id, document_id)

Fetches a document

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetches a single document submission by a specific driver.

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
    api_instance = samsara.DefaultApi(api_client)
    driver_id = 56 # int | ID of the driver who submitted the document. Must contain only digits 0-9.
document_id = 'document_id_example' # str | ID of document.

    try:
        # Fetches a document
        api_response = api_instance.v1get_driver_document_by_id_and_driver_id(driver_id, document_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_driver_document_by_id_and_driver_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| ID of the driver who submitted the document. Must contain only digits 0-9. | 
 **document_id** | **str**| ID of document. | 

### Return type

[**V1Document**](V1Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified document. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_driver_document_types_by_org_id**
> list[V1DocumentType] v1get_driver_document_types_by_org_id()

Fetch document types

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all of the document types.

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
    api_instance = samsara.DefaultApi(api_client)
    
    try:
        # Fetch document types
        api_response = api_instance.v1get_driver_document_types_by_org_id()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_driver_document_types_by_org_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1DocumentType]**](V1DocumentType.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all of the document types. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_driver_documents_by_org_id**
> V1Documents v1get_driver_documents_by_org_id(end_ms=end_ms, duration_ms=duration_ms, query_by=query_by)

Fetch all documents

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all of the documents.

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
    api_instance = samsara.DefaultApi(api_client)
    end_ms = 56 # int | Time in unix milliseconds that represents the oldest documents to return. Used in combination with durationMs. Defaults to now. (optional)
duration_ms = 56 # int | Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours. (optional)
query_by = 'query_by_example' # str | Retrieve most recent documents based on either driverCreatedAtMs or serverUpdatedAtMs. If no value is provided, the default is driverCreatedAtMs. (optional)

    try:
        # Fetch all documents
        api_response = api_instance.v1get_driver_documents_by_org_id(end_ms=end_ms, duration_ms=duration_ms, query_by=query_by)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_driver_documents_by_org_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_ms** | **int**| Time in unix milliseconds that represents the oldest documents to return. Used in combination with durationMs. Defaults to now. | [optional] 
 **duration_ms** | **int**| Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours. | [optional] 
 **query_by** | **str**| Retrieve most recent documents based on either driverCreatedAtMs or serverUpdatedAtMs. If no value is provided, the default is driverCreatedAtMs. | [optional] 

### Return type

[**V1Documents**](V1Documents.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all of the documents. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_driver_safety_score**
> V1DriverSafetyScoreResponse v1get_driver_safety_score(driver_id, start_ms, end_ms)

Fetch driver safety score

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch the safety score for the driver.

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
    api_instance = samsara.DefaultApi(api_client)
    driver_id = 56 # int | ID of the driver. Must contain only digits 0-9.
start_ms = 56 # int | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.
end_ms = 56 # int | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.

    try:
        # Fetch driver safety score
        api_response = api_instance.v1get_driver_safety_score(driver_id, start_ms, end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_driver_safety_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| ID of the driver. Must contain only digits 0-9. | 
 **start_ms** | **int**| Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. | 
 **end_ms** | **int**| Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. | 

### Return type

[**V1DriverSafetyScoreResponse**](V1DriverSafetyScoreResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Safety score details. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_dvirs**
> V1DvirListResponse v1get_dvirs(end_ms, duration_ms)

Get DVIRs

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get DVIRs for the org within provided time constraints

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
    api_instance = samsara.DefaultApi(api_client)
    end_ms = 56 # int | Time in millis until the last dvir log.
duration_ms = 3.4 # float | Time in millis which corresponds to the duration before the end_ms. Must be less than or equal to 90 days.

    try:
        # Get DVIRs
        api_response = api_instance.v1get_dvirs(end_ms, duration_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_dvirs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_ms** | **int**| Time in millis until the last dvir log. | 
 **duration_ms** | **float**| Time in millis which corresponds to the duration before the end_ms. Must be less than or equal to 90 days. | 

### Return type

[**V1DvirListResponse**](V1DvirListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DVIRs for the specified duration. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_fleet_drivers_hos_daily_logs**
> V1DriverDailyLogResponse v1get_fleet_drivers_hos_daily_logs(driver_id, hos_logs_param=hos_logs_param)

Get daily HOS logs for a specific driver

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get summarized daily Hours of Service charts for a specified driver.  The response will contain a list of `days`, where each entry in the list is the driver's summarized hours of service for that entire day.  The time range for a \"day\" is defined by the `driver`'s `eldDayStartHour`. By default, this is `0`, which indicates the `driver`'s \"day\" is from midnight to midnight in the `driver`'s respective `timezone`. This value is configurable per driver.  The `startMs` and `endMs` parameters indicate start and end for the date range you'd like to query. These parameters are inclusive. This means that the response will include the \"day\" that contains `startMs` and the \"day\" that contains `endMs`. For example:  Let's say a `driver`'s `eldDayStartHour` is `0` and their timezone is `America/Chicago`.  If `startMs` was `1576080000000` (December 11, 2019 10:00:00 AM America/Chicago) and an `endMs` was `1576166400000` (December 12, 2019 10:00:00 AM America/Los_Angeles), then the response will contain a two `day` entries: [December 11, 2019 12:00:00 AM America/Chicago to December 12, 2019 12:00:00 AM America/Chicago], and [December 12, 2019 12:00:00 AM America/Chicago to December 13, 2019 12:00:00 AM America/Chicago].

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
    api_instance = samsara.DefaultApi(api_client)
    driver_id = 56 # int | ID of the driver with HOS logs.
hos_logs_param = samsara.InlineObject() # InlineObject |  (optional)

    try:
        # Get daily HOS logs for a specific driver
        api_response = api_instance.v1get_fleet_drivers_hos_daily_logs(driver_id, hos_logs_param=hos_logs_param)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_fleet_drivers_hos_daily_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| ID of the driver with HOS logs. | 
 **hos_logs_param** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

[**V1DriverDailyLogResponse**](V1DriverDailyLogResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Distance traveled and time active for each driver in the organization over the specified time period. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_fleet_hos_authentication_logs**
> V1HosAuthenticationLogsResponse v1get_fleet_hos_authentication_logs(driver_id, start_ms, end_ms)

Get HOS signin and signout

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the HOS (hours of service) signin and signout logs for the specified driver. The response includes 4 fields that are now deprecated.

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
    api_instance = samsara.DefaultApi(api_client)
    driver_id = 56 # int | Driver ID to query.
start_ms = 56 # int | Beginning of the time range, specified in milliseconds UNIX time.
end_ms = 56 # int | End of the time range, specified in milliseconds UNIX time.

    try:
        # Get HOS signin and signout
        api_response = api_instance.v1get_fleet_hos_authentication_logs(driver_id, start_ms, end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_fleet_hos_authentication_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| Driver ID to query. | 
 **start_ms** | **int**| Beginning of the time range, specified in milliseconds UNIX time. | 
 **end_ms** | **int**| End of the time range, specified in milliseconds UNIX time. | 

### Return type

[**V1HosAuthenticationLogsResponse**](V1HosAuthenticationLogsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HOS authentication logs for the specified driver. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_fleet_hos_logs**
> V1HosLogsResponse v1get_fleet_hos_logs(hos_logs_param)

Get HOS logs for a specific driver

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the HOS (hours of service) logs for the specified driver. This method returns all the HOS statuses that the driver was in during this time period.

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
    api_instance = samsara.DefaultApi(api_client)
    hos_logs_param = samsara.InlineObject1() # InlineObject1 | 

    try:
        # Get HOS logs for a specific driver
        api_response = api_instance.v1get_fleet_hos_logs(hos_logs_param)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_fleet_hos_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hos_logs_param** | [**InlineObject1**](InlineObject1.md)|  | 

### Return type

[**V1HosLogsResponse**](V1HosLogsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HOS logs for the specified driver. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_fleet_hos_logs_summary**
> V1HosLogsSummaryResponse v1get_fleet_hos_logs_summary(after=after, limit=limit)

Get current HOS status for all drivers

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the current HOS status for all drivers. Note that this includes inactive as well as active drivers. You may need to upgrade your API token to version 2019-07-31 or later to leverage response pagination. [See here](https://kb.samsara.com/hc/en-us/articles/360026132972-Upgrading-API-Tokens)

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
    api_instance = samsara.DefaultApi(api_client)
    after = 'after_example' # str | Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. (optional)
limit = 3.4 # float | Pagination parameter indicating the number of results to return in this request. Used in conjunction with 'after'. (optional)

    try:
        # Get current HOS status for all drivers
        api_response = api_instance.v1get_fleet_hos_logs_summary(after=after, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_fleet_hos_logs_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the &#39;limit&#39; parameter. | [optional] 
 **limit** | **float**| Pagination parameter indicating the number of results to return in this request. Used in conjunction with &#39;after&#39;. | [optional] 

### Return type

[**V1HosLogsSummaryResponse**](V1HosLogsSummaryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HOS logs for the specified driver. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_fleet_maintenance_list**
> InlineResponse2003 v1get_fleet_maintenance_list()

Get vehicles with engine faults or check lights

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get list of the vehicles with any engine faults or check light data.

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
    api_instance = samsara.DefaultApi(api_client)
    
    try:
        # Get vehicles with engine faults or check lights
        api_response = api_instance.v1get_fleet_maintenance_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_fleet_maintenance_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of vehicles and maintenance information about each. |  -  |
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
    api_instance = samsara.DefaultApi(api_client)
    trailer_id = 56 # int | ID of trailer. Must contain only digits 0-9.
start_ms = 56 # int | Timestamp in Unix epoch milliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments. (optional)
end_ms = 56 # int | Timestamp in Unix epoch milliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time (optional)

    try:
        # List trailer assignments for a given trailer
        api_response = api_instance.v1get_fleet_trailer_assignments(trailer_id, start_ms=start_ms, end_ms=end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_fleet_trailer_assignments: %s\n" % e)
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

# **v1get_fleet_trips**
> V1TripResponse v1get_fleet_trips(vehicle_id, start_ms, end_ms)

Get vehicle trips

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get historical trips data for specified vehicle. This method returns a set of historical trips data for the specified vehicle in the specified time range.

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
    api_instance = samsara.DefaultApi(api_client)
    vehicle_id = 56 # int | Vehicle ID to query.
start_ms = 56 # int | Beginning of the time range, specified in milliseconds UNIX time. Limited to a 90 day window with respect to startMs and endMs
end_ms = 56 # int | End of the time range, specified in milliseconds UNIX time.

    try:
        # Get vehicle trips
        api_response = api_instance.v1get_fleet_trips(vehicle_id, start_ms, end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_fleet_trips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| Vehicle ID to query. | 
 **start_ms** | **int**| Beginning of the time range, specified in milliseconds UNIX time. Limited to a 90 day window with respect to startMs and endMs | 
 **end_ms** | **int**| End of the time range, specified in milliseconds UNIX time. | 

### Return type

[**V1TripResponse**](V1TripResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of trips taken by the requested vehicle within the specified timeframe. Ongoing trips will be returned with 9223372036854775807 as their endMs. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_machines**
> InlineResponse2008 v1get_machines()

Get machines

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get machine objects. This method returns a list of the machine objects in the Samsara Cloud and information about them.

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
    api_instance = samsara.DefaultApi(api_client)
    
    try:
        # Get machines
        api_response = api_instance.v1get_machines()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_machines: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of machine objects. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_machines_history**
> V1MachineHistoryResponse v1get_machines_history(history_param)

Get machine history

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get historical data for machine objects. This method returns a set of historical data for all machines

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
    api_instance = samsara.DefaultApi(api_client)
    history_param = samsara.InlineObject4() # InlineObject4 | 

    try:
        # Get machine history
        api_response = api_instance.v1get_machines_history(history_param)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_machines_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_param** | [**InlineObject4**](InlineObject4.md)|  | 

### Return type

[**V1MachineHistoryResponse**](V1MachineHistoryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of machine results objects, each containing a time and a datapoint. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_messages**
> InlineResponse2004 v1get_messages(end_ms=end_ms, duration_ms=duration_ms)

Get all messages.

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get all messages.

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
    api_instance = samsara.DefaultApi(api_client)
    end_ms = 56 # int | Time in unix milliseconds that represents the end of time range of messages to return. Used in combination with durationMs. Defaults to now. (optional)
duration_ms = 56 # int | Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours. (optional)

    try:
        # Get all messages.
        api_response = api_instance.v1get_messages(end_ms=end_ms, duration_ms=duration_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_ms** | **int**| Time in unix milliseconds that represents the end of time range of messages to return. Used in combination with durationMs. Defaults to now. | [optional] 
 **duration_ms** | **int**| Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the fetched messages from most recently sent to least recently sent. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors**
> InlineResponse2009 v1get_sensors()

Get all sensors

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get sensor objects. This method returns a list of the sensor objects in the Samsara Cloud and information about them.

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
    api_instance = samsara.DefaultApi(api_client)
    
    try:
        # Get all sensors
        api_response = api_instance.v1get_sensors()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_sensors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sensor objects. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_cargo**
> V1CargoResponse v1get_sensors_cargo(v1sensor_param)

Get cargo status

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get cargo monitor status (empty / full) for requested sensors.

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
    api_instance = samsara.DefaultApi(api_client)
    v1sensor_param = samsara.InlineObject5() # InlineObject5 | 

    try:
        # Get cargo status
        api_response = api_instance.v1get_sensors_cargo(v1sensor_param)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_sensors_cargo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1sensor_param** | [**InlineObject5**](InlineObject5.md)|  | 

### Return type

[**V1CargoResponse**](V1CargoResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sensor objects containing the current cargo status reported by each sensor. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_door**
> V1DoorResponse v1get_sensors_door(v1sensor_param)

Get door status

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get door monitor status (closed / open) for requested sensors.

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
    api_instance = samsara.DefaultApi(api_client)
    v1sensor_param = samsara.InlineObject6() # InlineObject6 | 

    try:
        # Get door status
        api_response = api_instance.v1get_sensors_door(v1sensor_param)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_sensors_door: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1sensor_param** | [**InlineObject6**](InlineObject6.md)|  | 

### Return type

[**V1DoorResponse**](V1DoorResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sensor objects containing the current door status reported by each sensor. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_history**
> V1SensorHistoryResponse v1get_sensors_history(history_param)

Get sensor history

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get historical data for specified sensors. This method returns a set of historical data for the specified sensors in the specified time range and at the specified time resolution.

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
    api_instance = samsara.DefaultApi(api_client)
    history_param = samsara.InlineObject7() # InlineObject7 | 

    try:
        # Get sensor history
        api_response = api_instance.v1get_sensors_history(history_param)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_sensors_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_param** | [**InlineObject7**](InlineObject7.md)|  | 

### Return type

[**V1SensorHistoryResponse**](V1SensorHistoryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of results objects, each containing a time and a datapoint for each requested sensor/field pair. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_humidity**
> V1HumidityResponse v1get_sensors_humidity(v1sensor_param)

Get humidity

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get humidity for requested sensors. This method returns the current relative humidity for the requested sensors.

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
    api_instance = samsara.DefaultApi(api_client)
    v1sensor_param = samsara.InlineObject8() # InlineObject8 | 

    try:
        # Get humidity
        api_response = api_instance.v1get_sensors_humidity(v1sensor_param)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_sensors_humidity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1sensor_param** | [**InlineObject8**](InlineObject8.md)|  | 

### Return type

[**V1HumidityResponse**](V1HumidityResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sensor objects containing the current humidity reported by each sensor. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_sensors_temperature**
> V1TemperatureResponse v1get_sensors_temperature(v1sensor_param)

Get temperature

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get temperature for requested sensors. This method returns the current ambient temperature (and probe temperature if applicable) for the requested sensors.

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
    api_instance = samsara.DefaultApi(api_client)
    v1sensor_param = samsara.InlineObject9() # InlineObject9 | 

    try:
        # Get temperature
        api_response = api_instance.v1get_sensors_temperature(v1sensor_param)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_sensors_temperature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1sensor_param** | [**InlineObject9**](InlineObject9.md)|  | 

### Return type

[**V1TemperatureResponse**](V1TemperatureResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sensor objects containing the current temperature reported by each sensor. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vehicle_harsh_event**
> V1VehicleHarshEventResponse v1get_vehicle_harsh_event(vehicle_id, timestamp)

Fetch harsh events

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch harsh event details for a vehicle.

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
    api_instance = samsara.DefaultApi(api_client)
    vehicle_id = 56 # int | ID of the vehicle. Must contain only digits 0-9.
timestamp = 56 # int | Timestamp in milliseconds representing the timestamp of a harsh event.

    try:
        # Fetch harsh events
        api_response = api_instance.v1get_vehicle_harsh_event(vehicle_id, timestamp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_vehicle_harsh_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| ID of the vehicle. Must contain only digits 0-9. | 
 **timestamp** | **int**| Timestamp in milliseconds representing the timestamp of a harsh event. | 

### Return type

[**V1VehicleHarshEventResponse**](V1VehicleHarshEventResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Harsh event details. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vehicle_safety_score**
> V1VehicleSafetyScoreResponse v1get_vehicle_safety_score(vehicle_id, start_ms, end_ms)

Fetch vehicle safety scores

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch the safety score for the vehicle.

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
    api_instance = samsara.DefaultApi(api_client)
    vehicle_id = 56 # int | ID of the vehicle. Must contain only digits 0-9.
start_ms = 56 # int | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.
end_ms = 56 # int | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.

    try:
        # Fetch vehicle safety scores
        api_response = api_instance.v1get_vehicle_safety_score(vehicle_id, start_ms, end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_vehicle_safety_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| ID of the vehicle. Must contain only digits 0-9. | 
 **start_ms** | **int**| Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. | 
 **end_ms** | **int**| Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. | 

### Return type

[**V1VehicleSafetyScoreResponse**](V1VehicleSafetyScoreResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Safety score details. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vision_latest_run_camera**
> V1VisionRunByCameraResponse v1get_vision_latest_run_camera(camera_id, program_id=program_id, started_at_ms=started_at_ms, include=include, limit=limit)

Fetch the latest run for a camera or program

Fetch the latest run for a camera or program by default. If startedAtMs is supplied, fetch the specific run that corresponds to that start time.

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
    api_instance = samsara.DefaultApi(api_client)
    camera_id = 56 # int | The camera_id should be valid for the given accessToken.
program_id = 56 # int | The configured program's ID on the camera. (optional)
started_at_ms = 56 # int | EndMs is an optional param. It will default to the current time. (optional)
include = 'include_example' # str | Include is a filter parameter. Accepts 'pass', 'reject' or 'no_read'. (optional)
limit = 56 # int | Limit is an integer value from 1 to 1,000. (optional)

    try:
        # Fetch the latest run for a camera or program
        api_response = api_instance.v1get_vision_latest_run_camera(camera_id, program_id=program_id, started_at_ms=started_at_ms, include=include, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_vision_latest_run_camera: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **camera_id** | **int**| The camera_id should be valid for the given accessToken. | 
 **program_id** | **int**| The configured program&#39;s ID on the camera. | [optional] 
 **started_at_ms** | **int**| EndMs is an optional param. It will default to the current time. | [optional] 
 **include** | **str**| Include is a filter parameter. Accepts &#39;pass&#39;, &#39;reject&#39; or &#39;no_read&#39;. | [optional] 
 **limit** | **int**| Limit is an integer value from 1 to 1,000. | [optional] 

### Return type

[**V1VisionRunByCameraResponse**](V1VisionRunByCameraResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the details for this run. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vision_programs_by_camera**
> list[object] v1get_vision_programs_by_camera(camera_id)

Fetch industrial camera programs

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch configured programs on the camera.

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
    api_instance = samsara.DefaultApi(api_client)
    camera_id = 56 # int | The camera_id should be valid for the given accessToken.

    try:
        # Fetch industrial camera programs
        api_response = api_instance.v1get_vision_programs_by_camera(camera_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_vision_programs_by_camera: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **camera_id** | **int**| The camera_id should be valid for the given accessToken. | 

### Return type

**list[object]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns programs configured on the camera. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vision_runs**
> V1VisionRunsResponse v1get_vision_runs(duration_ms, end_ms=end_ms)

Fetch runs

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch runs.

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
    api_instance = samsara.DefaultApi(api_client)
    duration_ms = 56 # int | DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched
end_ms = 56 # int | EndMs is an optional param. It will default to the current time. (optional)

    try:
        # Fetch runs
        api_response = api_instance.v1get_vision_runs(duration_ms, end_ms=end_ms)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_vision_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duration_ms** | **int**| DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched | 
 **end_ms** | **int**| EndMs is an optional param. It will default to the current time. | [optional] 

### Return type

[**V1VisionRunsResponse**](V1VisionRunsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return runs. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_vision_runs_by_camera_and_program**
> V1VisionRunsByCameraAndProgramResponse v1get_vision_runs_by_camera_and_program(camera_id, program_id, started_at_ms, include=include)

Fetch runs by camera and program

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch runs by camera and program.

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
    api_instance = samsara.DefaultApi(api_client)
    camera_id = 56 # int | The camera_id should be valid for the given accessToken.
program_id = 56 # int | The configured program's ID on the camera.
started_at_ms = 56 # int | Started_at_ms is a required param. Indicates the start time of the run to be fetched.
include = 'include_example' # str | Include is a filter parameter. Accepts 'pass', 'reject' or 'no_read'. (optional)

    try:
        # Fetch runs by camera and program
        api_response = api_instance.v1get_vision_runs_by_camera_and_program(camera_id, program_id, started_at_ms, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1get_vision_runs_by_camera_and_program: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **camera_id** | **int**| The camera_id should be valid for the given accessToken. | 
 **program_id** | **int**| The configured program&#39;s ID on the camera. | 
 **started_at_ms** | **int**| Started_at_ms is a required param. Indicates the start time of the run to be fetched. | 
 **include** | **str**| Include is a filter parameter. Accepts &#39;pass&#39;, &#39;reject&#39; or &#39;no_read&#39;. | [optional] 

### Return type

[**V1VisionRunsByCameraAndProgramResponse**](V1VisionRunsByCameraAndProgramResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return runs by camera ID and program ID. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1update_dispatch_route_by_id**
> V1DispatchRoute v1update_dispatch_route_by_id(route_id, update_dispatch_route_params)

Update a route

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Update the dispatch route. Allowable updates include adding or removing jobs, and changing job locations and times.

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
    api_instance = samsara.DefaultApi(api_client)
    route_id = 56 # int | ID of the dispatch route. Must contain only digits 0-9.
update_dispatch_route_params = samsara.V1DispatchRouteUpdate() # V1DispatchRouteUpdate | 

    try:
        # Update a route
        api_response = api_instance.v1update_dispatch_route_by_id(route_id, update_dispatch_route_params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->v1update_dispatch_route_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| ID of the dispatch route. Must contain only digits 0-9. | 
 **update_dispatch_route_params** | [**V1DispatchRouteUpdate**](V1DispatchRouteUpdate.md)|  | 

### Return type

[**V1DispatchRoute**](V1DispatchRoute.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated route corresponding to route_id. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

