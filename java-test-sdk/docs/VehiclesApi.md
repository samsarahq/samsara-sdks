# VehiclesApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVehicleLocations**](VehiclesApi.md#getVehicleLocations) | **GET** /fleet/vehicles/locations | Get most recent vehicle locations
[**getVehicleLocationsFeed**](VehiclesApi.md#getVehicleLocationsFeed) | **GET** /fleet/vehicles/locations/feed | Follow a feed of vehicle locations
[**getVehicleLocationsHistory**](VehiclesApi.md#getVehicleLocationsHistory) | **GET** /fleet/vehicles/locations/history | Get historical vehicle locations


<a name="getVehicleLocations"></a>
# **getVehicleLocations**
> VehicleLocationsResponse getVehicleLocations(after, tagIds, vehicleIds)

Get most recent vehicle locations

Returns last known location for all vehicles (Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-locations) for more details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.samsara.com");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    String after = "after_example"; // String | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    List<String> tagIds = Arrays.asList(); // List<String> | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    List<String> vehicleIds = Arrays.asList(); // List<String> | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    try {
      VehicleLocationsResponse result = apiInstance.getVehicleLocations(after, tagIds, vehicleIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehicleLocations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **String**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional]
 **tagIds** | [**List&lt;String&gt;**](String.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional]
 **vehicleIds** | [**List&lt;String&gt;**](String.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional]

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

<a name="getVehicleLocationsFeed"></a>
# **getVehicleLocationsFeed**
> VehicleLocationsListResponse getVehicleLocationsFeed(after, tagIds, vehicleIds)

Follow a feed of vehicle locations

Follow a continuous feed of all vehicle locations from Samsara Vehicle Gateways.  Your first call to this endpoint will provide you with the most recent location for each vehicle and a &#x60;pagination&#x60; object that contains an &#x60;endCursor&#x60;.  You can provide the &#x60;endCursor&#x60; to the &#x60;after&#x60; parameter of this endpoint to get location updates since that &#x60;endCursor&#x60;.   If &#x60;hasNextPage&#x60; is &#x60;false&#x60;, no updates are readily available yet. We&#39;d suggest waiting a minimum of 5 seconds before requesting updates.  See [this guide](https://developers.samsara.com/docs/vehicle-locations#section-follow-a-real-time-feed-of-vehicle-locations) for more details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.samsara.com");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    String after = "after_example"; // String | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    List<String> tagIds = Arrays.asList(); // List<String> | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    List<String> vehicleIds = Arrays.asList(); // List<String> | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    try {
      VehicleLocationsListResponse result = apiInstance.getVehicleLocationsFeed(after, tagIds, vehicleIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehicleLocationsFeed");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **String**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional]
 **tagIds** | [**List&lt;String&gt;**](String.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional]
 **vehicleIds** | [**List&lt;String&gt;**](String.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional]

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

<a name="getVehicleLocationsHistory"></a>
# **getVehicleLocationsHistory**
> VehicleLocationsListResponse getVehicleLocationsHistory(startTime, endTime, after, tagIds, vehicleIds)

Get historical vehicle locations

Returns all known vehicle location changes during the given time range for all vehicles (Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-locations) for more details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.samsara.com");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    OffsetDateTime startTime = new OffsetDateTime(); // OffsetDateTime | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    OffsetDateTime endTime = new OffsetDateTime(); // OffsetDateTime | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    String after = "after_example"; // String | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    List<String> tagIds = Arrays.asList(); // List<String> | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    List<String> vehicleIds = Arrays.asList(); // List<String> | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    try {
      VehicleLocationsListResponse result = apiInstance.getVehicleLocationsHistory(startTime, endTime, after, tagIds, vehicleIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehicleLocationsHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startTime** | **OffsetDateTime**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). |
 **endTime** | **OffsetDateTime**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). |
 **after** | **String**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional]
 **tagIds** | [**List&lt;String&gt;**](String.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional]
 **vehicleIds** | [**List&lt;String&gt;**](String.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional]

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

