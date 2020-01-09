# samsara.DocumentsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1create_driver_document**](DocumentsApi.md#v1create_driver_document) | **POST** /v1/fleet/drivers/{driver_id}/documents | Create a document
[**v1get_driver_document_by_id_and_driver_id**](DocumentsApi.md#v1get_driver_document_by_id_and_driver_id) | **GET** /v1/fleet/drivers/{driver_id}/documents/{document_id} | Fetches a document
[**v1get_driver_document_types_by_org_id**](DocumentsApi.md#v1get_driver_document_types_by_org_id) | **GET** /v1/fleet/drivers/document_types | Fetch document types
[**v1get_driver_documents_by_org_id**](DocumentsApi.md#v1get_driver_documents_by_org_id) | **GET** /v1/fleet/drivers/documents | Fetch all documents


# **v1create_driver_document**
> V1Document v1create_driver_document(driver_id, create_document_params)

Create a document

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Create a document for the given driver.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.DocumentsApi()
driver_id = 56 # int | ID of the driver for whom the document is created. Must contain only digits 0-9.
create_document_params = samsara.V1DocumentCreate() # V1DocumentCreate | To create a document for a given document type, the document type's uuid needs to be passed in to documentTypeUuid. The list of fields passed in should match the document type’s list of field types in the correct order. In other words, a field's valueType and value (i.e. only one of: stringValue, numberValue, or photoValue) at index _i_ should match with the document field type’s valueType at index _i_.

try:
    # Create a document
    api_response = api_instance.v1create_driver_document(driver_id, create_document_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->v1create_driver_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| ID of the driver for whom the document is created. Must contain only digits 0-9. | 
 **create_document_params** | [**V1DocumentCreate**](V1DocumentCreate.md)| To create a document for a given document type, the document type&#39;s uuid needs to be passed in to documentTypeUuid. The list of fields passed in should match the document type’s list of field types in the correct order. In other words, a field&#39;s valueType and value (i.e. only one of: stringValue, numberValue, or photoValue) at index _i_ should match with the document field type’s valueType at index _i_. | 

### Return type

[**V1Document**](V1Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the created document. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_driver_document_by_id_and_driver_id**
> V1Document v1get_driver_document_by_id_and_driver_id(driver_id, document_id)

Fetches a document

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetches a single document submission by a specific driver.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.DocumentsApi()
driver_id = 56 # int | ID of the driver who submitted the document. Must contain only digits 0-9.
document_id = 'document_id_example' # str | ID of document.

try:
    # Fetches a document
    api_response = api_instance.v1get_driver_document_by_id_and_driver_id(driver_id, document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->v1get_driver_document_by_id_and_driver_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| ID of the driver who submitted the document. Must contain only digits 0-9. | 
 **document_id** | **str**| ID of document. | 

### Return type

[**V1Document**](V1Document.md)

### Authorization

No authorization required

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
> list[object] v1get_driver_document_types_by_org_id()

Fetch document types

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all of the document types.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.DocumentsApi()

try:
    # Fetch document types
    api_response = api_instance.v1get_driver_document_types_by_org_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->v1get_driver_document_types_by_org_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**200** | Returns all of the document types. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_driver_documents_by_org_id**
> list[object] v1get_driver_documents_by_org_id(end_ms=end_ms, duration_ms=duration_ms, query_by=query_by)

Fetch all documents

<n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch all of the documents.

### Example

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = samsara.DocumentsApi()
end_ms = 56 # int | Time in unix milliseconds that represents the oldest documents to return. Used in combination with durationMs. Defaults to now. (optional)
duration_ms = 56 # int | Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours. (optional)
query_by = 'query_by_example' # str | Retrieve most recent documents based on either driverCreatedAtMs or serverUpdatedAtMs. If no value is provided, the default is driverCreatedAtMs. (optional)

try:
    # Fetch all documents
    api_response = api_instance.v1get_driver_documents_by_org_id(end_ms=end_ms, duration_ms=duration_ms, query_by=query_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->v1get_driver_documents_by_org_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_ms** | **int**| Time in unix milliseconds that represents the oldest documents to return. Used in combination with durationMs. Defaults to now. | [optional] 
 **duration_ms** | **int**| Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours. | [optional] 
 **query_by** | **str**| Retrieve most recent documents based on either driverCreatedAtMs or serverUpdatedAtMs. If no value is provided, the default is driverCreatedAtMs. | [optional] 

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
**200** | Returns all of the documents. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

