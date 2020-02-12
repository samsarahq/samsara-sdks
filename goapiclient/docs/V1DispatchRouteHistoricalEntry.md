# V1DispatchRouteHistoricalEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ChangedAtMs** | Pointer to **int64** | Timestamp that the route was updated, represented as Unix milliseconds since epoch. | [optional] 
**Route** | Pointer to [**V1DispatchRoute**](V1DispatchRoute.md) |  | [optional] 

## Methods

### GetChangedAtMs

`func (o *V1DispatchRouteHistoricalEntry) GetChangedAtMs() int64`

GetChangedAtMs returns the ChangedAtMs field if non-nil, zero value otherwise.

### GetChangedAtMsOk

`func (o *V1DispatchRouteHistoricalEntry) GetChangedAtMsOk() (int64, bool)`

GetChangedAtMsOk returns a tuple with the ChangedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasChangedAtMs

`func (o *V1DispatchRouteHistoricalEntry) HasChangedAtMs() bool`

HasChangedAtMs returns a boolean if a field has been set.

### SetChangedAtMs

`func (o *V1DispatchRouteHistoricalEntry) SetChangedAtMs(v int64)`

SetChangedAtMs gets a reference to the given int64 and assigns it to the ChangedAtMs field.

### GetRoute

`func (o *V1DispatchRouteHistoricalEntry) GetRoute() V1DispatchRoute`

GetRoute returns the Route field if non-nil, zero value otherwise.

### GetRouteOk

`func (o *V1DispatchRouteHistoricalEntry) GetRouteOk() (V1DispatchRoute, bool)`

GetRouteOk returns a tuple with the Route field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRoute

`func (o *V1DispatchRouteHistoricalEntry) HasRoute() bool`

HasRoute returns a boolean if a field has been set.

### SetRoute

`func (o *V1DispatchRouteHistoricalEntry) SetRoute(v V1DispatchRoute)`

SetRoute gets a reference to the given V1DispatchRoute and assigns it to the Route field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


