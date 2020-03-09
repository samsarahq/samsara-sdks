# \AssetsApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1getAllAssetCurrentLocations**](AssetsApi.md#V1getAllAssetCurrentLocations) | **Get** /v1/fleet/assets/locations | List current location for all assets
[**V1getAllAssets**](AssetsApi.md#V1getAllAssets) | **Get** /v1/fleet/assets | List all assets
[**V1getAssetLocation**](AssetsApi.md#V1getAssetLocation) | **Get** /v1/fleet/assets/{asset_id}/locations | List historical locations for a given asset
[**V1getAssetReefer**](AssetsApi.md#V1getAssetReefer) | **Get** /v1/fleet/assets/{asset_id}/reefer | List stats for a given reefer
[**V1getAssetsReefers**](AssetsApi.md#V1getAssetsReefers) | **Get** /v1/fleet/assets/reefers | List stats for all reefers



## V1getAllAssetCurrentLocations

> InlineResponse2007 V1getAllAssetCurrentLocations(ctx).StartingAfter(startingAfter).EndingBefore(endingBefore).Limit(limit).Execute()

List current location for all assets



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getAllAssetCurrentLocationsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startingAfter** | **string** | Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the &#39;limit&#39; parameter. Mutually exclusive with &#39;endingBefore&#39; parameter. | 
 **endingBefore** | **string** | Pagination parameter indicating the cursor position to return results before. Used in conjunction with the &#39;limit&#39; parameter. Mutually exclusive with &#39;startingAfter&#39; parameter. | 
 **limit** | **float32** | Pagination parameter indicating the number of results to return in this request. Used in conjunction with either &#39;startingAfter&#39; or &#39;endingBefore&#39;. | 

### Return type

[**InlineResponse2007**](inline_response_200_7.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getAllAssets

> InlineResponse2006 V1getAllAssets(ctx).Execute()

List all assets



### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1getAllAssetsRequest struct via the builder pattern


### Return type

[**InlineResponse2006**](inline_response_200_6.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getAssetLocation

> []map[string]interface{} V1getAssetLocation(ctx, assetId).StartMs(startMs).EndMs(endMs).Execute()

List historical locations for a given asset



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**assetId** | **int64** | ID of the asset. Must contain only digits 0-9. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1getAssetLocationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **startMs** | **int64** | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. | 
 **endMs** | **int64** | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. | 

### Return type

[**[]map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getAssetReefer

> V1AssetReeferResponse V1getAssetReefer(ctx, assetId).StartMs(startMs).EndMs(endMs).Execute()

List stats for a given reefer



### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**assetId** | **int64** | ID of the asset. Must contain only digits 0-9. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1getAssetReeferRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **startMs** | **int64** | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. | 
 **endMs** | **int64** | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. | 

### Return type

[**V1AssetReeferResponse**](V1AssetReeferResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1getAssetsReefers

> InlineResponse2008 V1getAssetsReefers(ctx).StartMs(startMs).EndMs(endMs).StartingAfter(startingAfter).EndingBefore(endingBefore).Limit(limit).Execute()

List stats for all reefers



### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1getAssetsReefersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startMs** | **int64** | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. | 
 **endMs** | **int64** | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. | 
 **startingAfter** | **string** | Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the &#39;limit&#39; parameter. Mutually exclusive with &#39;endingBefore&#39; parameter. | 
 **endingBefore** | **string** | Pagination parameter indicating the cursor position to return results before. Used in conjunction with the &#39;limit&#39; parameter. Mutually exclusive with &#39;startingAfter&#39; parameter. | 
 **limit** | **float32** | Pagination parameter indicating the number of results to return in this request. Used in conjunction with either &#39;startingAfter&#39; or &#39;endingBefore&#39;. | 

### Return type

[**InlineResponse2008**](inline_response_200_8.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

