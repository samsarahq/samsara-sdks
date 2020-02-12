# V1DriverDailyLogResponseDays

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ActiveHours** | Pointer to **float64** | Hours spent on duty or driving, rounded to two decimal places. | [optional] 
**ActiveMs** | Pointer to **int64** | Milliseconds spent on duty or driving. | [optional] 
**Certified** | Pointer to **bool** | Whether this HOS day chart was certified by the driver. | [optional] 
**CertifiedAtMs** | Pointer to **float32** | Unix epoch time (in ms) of time when this chart was certified. If this chart is uncertified, 0. | [optional] 
**DistanceMiles** | Pointer to **float64** | Distance driven in miles, rounded to two decimal places. | [optional] 
**EndMs** | Pointer to **int32** | End of the HOS day, specified in milliseconds UNIX time. | [optional] 
**ShippingDocIds** | Pointer to [**map[string]interface{}**](.md) | List of customer shipping document IDs associated with the driver for the day. | [optional] 
**StartMs** | Pointer to **int32** | End of the HOS day, specified in milliseconds UNIX time. | [optional] 
**TrailerIds** | Pointer to [**map[string]interface{}**](.md) | List of trailer ID&#39;s associated with the driver for the day. | [optional] 
**VehicleIds** | Pointer to [**map[string]interface{}**](.md) | List of vehicle ID&#39;s associated with the driver for the day. | [optional] 

## Methods

### GetActiveHours

`func (o *V1DriverDailyLogResponseDays) GetActiveHours() float64`

GetActiveHours returns the ActiveHours field if non-nil, zero value otherwise.

### GetActiveHoursOk

`func (o *V1DriverDailyLogResponseDays) GetActiveHoursOk() (float64, bool)`

GetActiveHoursOk returns a tuple with the ActiveHours field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasActiveHours

`func (o *V1DriverDailyLogResponseDays) HasActiveHours() bool`

HasActiveHours returns a boolean if a field has been set.

### SetActiveHours

`func (o *V1DriverDailyLogResponseDays) SetActiveHours(v float64)`

SetActiveHours gets a reference to the given float64 and assigns it to the ActiveHours field.

### GetActiveMs

`func (o *V1DriverDailyLogResponseDays) GetActiveMs() int64`

GetActiveMs returns the ActiveMs field if non-nil, zero value otherwise.

### GetActiveMsOk

`func (o *V1DriverDailyLogResponseDays) GetActiveMsOk() (int64, bool)`

GetActiveMsOk returns a tuple with the ActiveMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasActiveMs

`func (o *V1DriverDailyLogResponseDays) HasActiveMs() bool`

HasActiveMs returns a boolean if a field has been set.

### SetActiveMs

`func (o *V1DriverDailyLogResponseDays) SetActiveMs(v int64)`

SetActiveMs gets a reference to the given int64 and assigns it to the ActiveMs field.

### GetCertified

`func (o *V1DriverDailyLogResponseDays) GetCertified() bool`

GetCertified returns the Certified field if non-nil, zero value otherwise.

### GetCertifiedOk

`func (o *V1DriverDailyLogResponseDays) GetCertifiedOk() (bool, bool)`

GetCertifiedOk returns a tuple with the Certified field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCertified

`func (o *V1DriverDailyLogResponseDays) HasCertified() bool`

HasCertified returns a boolean if a field has been set.

### SetCertified

`func (o *V1DriverDailyLogResponseDays) SetCertified(v bool)`

SetCertified gets a reference to the given bool and assigns it to the Certified field.

### GetCertifiedAtMs

`func (o *V1DriverDailyLogResponseDays) GetCertifiedAtMs() float32`

GetCertifiedAtMs returns the CertifiedAtMs field if non-nil, zero value otherwise.

### GetCertifiedAtMsOk

`func (o *V1DriverDailyLogResponseDays) GetCertifiedAtMsOk() (float32, bool)`

GetCertifiedAtMsOk returns a tuple with the CertifiedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCertifiedAtMs

`func (o *V1DriverDailyLogResponseDays) HasCertifiedAtMs() bool`

HasCertifiedAtMs returns a boolean if a field has been set.

### SetCertifiedAtMs

`func (o *V1DriverDailyLogResponseDays) SetCertifiedAtMs(v float32)`

SetCertifiedAtMs gets a reference to the given float32 and assigns it to the CertifiedAtMs field.

### GetDistanceMiles

`func (o *V1DriverDailyLogResponseDays) GetDistanceMiles() float64`

GetDistanceMiles returns the DistanceMiles field if non-nil, zero value otherwise.

### GetDistanceMilesOk

`func (o *V1DriverDailyLogResponseDays) GetDistanceMilesOk() (float64, bool)`

GetDistanceMilesOk returns a tuple with the DistanceMiles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDistanceMiles

`func (o *V1DriverDailyLogResponseDays) HasDistanceMiles() bool`

HasDistanceMiles returns a boolean if a field has been set.

### SetDistanceMiles

`func (o *V1DriverDailyLogResponseDays) SetDistanceMiles(v float64)`

SetDistanceMiles gets a reference to the given float64 and assigns it to the DistanceMiles field.

### GetEndMs

`func (o *V1DriverDailyLogResponseDays) GetEndMs() int32`

GetEndMs returns the EndMs field if non-nil, zero value otherwise.

### GetEndMsOk

`func (o *V1DriverDailyLogResponseDays) GetEndMsOk() (int32, bool)`

GetEndMsOk returns a tuple with the EndMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEndMs

`func (o *V1DriverDailyLogResponseDays) HasEndMs() bool`

HasEndMs returns a boolean if a field has been set.

### SetEndMs

`func (o *V1DriverDailyLogResponseDays) SetEndMs(v int32)`

SetEndMs gets a reference to the given int32 and assigns it to the EndMs field.

### GetShippingDocIds

`func (o *V1DriverDailyLogResponseDays) GetShippingDocIds() map[string]interface{}`

GetShippingDocIds returns the ShippingDocIds field if non-nil, zero value otherwise.

### GetShippingDocIdsOk

`func (o *V1DriverDailyLogResponseDays) GetShippingDocIdsOk() (map[string]interface{}, bool)`

GetShippingDocIdsOk returns a tuple with the ShippingDocIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasShippingDocIds

`func (o *V1DriverDailyLogResponseDays) HasShippingDocIds() bool`

HasShippingDocIds returns a boolean if a field has been set.

### SetShippingDocIds

`func (o *V1DriverDailyLogResponseDays) SetShippingDocIds(v map[string]interface{})`

SetShippingDocIds gets a reference to the given map[string]interface{} and assigns it to the ShippingDocIds field.

### GetStartMs

`func (o *V1DriverDailyLogResponseDays) GetStartMs() int32`

GetStartMs returns the StartMs field if non-nil, zero value otherwise.

### GetStartMsOk

`func (o *V1DriverDailyLogResponseDays) GetStartMsOk() (int32, bool)`

GetStartMsOk returns a tuple with the StartMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartMs

`func (o *V1DriverDailyLogResponseDays) HasStartMs() bool`

HasStartMs returns a boolean if a field has been set.

### SetStartMs

`func (o *V1DriverDailyLogResponseDays) SetStartMs(v int32)`

SetStartMs gets a reference to the given int32 and assigns it to the StartMs field.

### GetTrailerIds

`func (o *V1DriverDailyLogResponseDays) GetTrailerIds() map[string]interface{}`

GetTrailerIds returns the TrailerIds field if non-nil, zero value otherwise.

### GetTrailerIdsOk

`func (o *V1DriverDailyLogResponseDays) GetTrailerIdsOk() (map[string]interface{}, bool)`

GetTrailerIdsOk returns a tuple with the TrailerIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerIds

`func (o *V1DriverDailyLogResponseDays) HasTrailerIds() bool`

HasTrailerIds returns a boolean if a field has been set.

### SetTrailerIds

`func (o *V1DriverDailyLogResponseDays) SetTrailerIds(v map[string]interface{})`

SetTrailerIds gets a reference to the given map[string]interface{} and assigns it to the TrailerIds field.

### GetVehicleIds

`func (o *V1DriverDailyLogResponseDays) GetVehicleIds() map[string]interface{}`

GetVehicleIds returns the VehicleIds field if non-nil, zero value otherwise.

### GetVehicleIdsOk

`func (o *V1DriverDailyLogResponseDays) GetVehicleIdsOk() (map[string]interface{}, bool)`

GetVehicleIdsOk returns a tuple with the VehicleIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleIds

`func (o *V1DriverDailyLogResponseDays) HasVehicleIds() bool`

HasVehicleIds returns a boolean if a field has been set.

### SetVehicleIds

`func (o *V1DriverDailyLogResponseDays) SetVehicleIds(v map[string]interface{})`

SetVehicleIds gets a reference to the given map[string]interface{} and assigns it to the VehicleIds field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


