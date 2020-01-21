# openapi_client.AssetsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1get_all_asset_current_locations**](AssetsApi.md#v1get_all_asset_current_locations) | **GET** /v1/fleet/assets/locations | List current location for all assets
[**v1get_all_assets**](AssetsApi.md#v1get_all_assets) | **GET** /v1/fleet/assets | List all assets
[**v1get_asset_location**](AssetsApi.md#v1get_asset_location) | **GET** /v1/fleet/assets/{asset_id}/locations | List historical locations for a given asset
[**v1get_asset_reefer**](AssetsApi.md#v1get_asset_reefer) | **GET** /v1/fleet/assets/{asset_id}/reefer | List stats for a given reefer
[**v1get_assets_reefers**](AssetsApi.md#v1get_assets_reefers) | **GET** /v1/fleet/assets/reefers | List stats for all reefers


# **v1get_all_asset_current_locations**
> InlineResponse2009 v1get_all_asset_current_locations(starting_after=starting_after, ending_before=ending_before, limit=limit)

List current location for all assets

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch current locations of all assets.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AssetsApi()
starting_after = 'starting_after_example' # str | Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter. (optional)
ending_before = 'ending_before_example' # str | Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter. (optional)
limit = 3.4 # float | Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'. (optional)

try:
    # List current location for all assets
    api_response = api_instance.v1get_all_asset_current_locations(starting_after=starting_after, ending_before=ending_before, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->v1get_all_asset_current_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starting_after** | **str**| Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the &#39;limit&#39; parameter. Mutually exclusive with &#39;endingBefore&#39; parameter. | [optional] 
 **ending_before** | **str**| Pagination parameter indicating the cursor position to return results before. Used in conjunction with the &#39;limit&#39; parameter. Mutually exclusive with &#39;startingAfter&#39; parameter. | [optional] 
 **limit** | **float**| Pagination parameter indicating the number of results to return in this request. Used in conjunction with either &#39;startingAfter&#39; or &#39;endingBefore&#39;. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

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
> InlineResponse2008 v1get_all_assets()

List all assets

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all of the assets.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AssetsApi()

try:
    # List all assets
    api_response = api_instance.v1get_all_assets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->v1get_all_assets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of assets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_asset_location**
> list[object] v1get_asset_location(asset_id, start_ms, end_ms)

List historical locations for a given asset

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  List historical locations for a given asset

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AssetsApi()
asset_id = 56 # int | ID of the asset. Must contain only digits 0-9.
start_ms = 56 # int | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs.
end_ms = 56 # int | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs.

try:
    # List historical locations for a given asset
    api_response = api_instance.v1get_asset_location(asset_id, start_ms, end_ms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->v1get_asset_location: %s\n" % e)
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

No authorization required

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

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AssetsApi()
asset_id = 56 # int | ID of the asset. Must contain only digits 0-9.
start_ms = 56 # int | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs.
end_ms = 56 # int | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs.

try:
    # List stats for a given reefer
    api_response = api_instance.v1get_asset_reefer(asset_id, start_ms, end_ms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->v1get_asset_reefer: %s\n" % e)
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

No authorization required

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
> InlineResponse20010 v1get_assets_reefers(start_ms, end_ms, starting_after=starting_after, ending_before=ending_before, limit=limit)

List stats for all reefers

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetches all reefers and reefer-specific stats.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AssetsApi()
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
    print("Exception when calling AssetsApi->v1get_assets_reefers: %s\n" % e)
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

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All org reefers and reefer-specific details. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

