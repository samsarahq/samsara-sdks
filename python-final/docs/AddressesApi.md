# samsara.AddressesApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_addresses**](AddressesApi.md#list_addresses) | **GET** /addresses | List all addresses


# **list_addresses**
> AddressResponse list_addresses(limit=limit, after=after, tag_ids=tag_ids)

List all addresses

Returns a list of all addresses in the organization's Address Book.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.AddressesApi()
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. If the provided `limit` is less than the total number of objects, the results will be [paginated](https://developers.samsara.com/docs/common-structures#section-pagination). (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the `endCursor` value from the previous page of results. If specified, this request will return the next page of results that occur immediately after the previous page of results. See more details [here](https://developers.samsara.com/docs/common-structures#section-pagination). (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,1235`. (optional)

try:
    # List all addresses
    api_response = api_instance.list_addresses(limit=limit, after=after, tag_ids=tag_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->list_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. If the provided &#x60;limit&#x60; is less than the total number of objects, the results will be [paginated](https://developers.samsara.com/docs/common-structures#section-pagination). | [optional] [default to 512]
 **after** | **str**| If specified, this should be the &#x60;endCursor&#x60; value from the previous page of results. If specified, this request will return the next page of results that occur immediately after the previous page of results. See more details [here](https://developers.samsara.com/docs/common-structures#section-pagination). | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,1235&#x60;. | [optional] 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all addresses in the organization&#39;s Address Book. |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

