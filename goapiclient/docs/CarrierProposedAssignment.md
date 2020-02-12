# CarrierProposedAssignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AcceptedTime** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 
**ActiveTime** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 
**FirstSeenTime** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 
**Id** | Pointer to **string** | Samsara ID for the assignment. | [optional] 
**RejectedTime** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 
**ShippingDocs** | Pointer to **string** | Shipping Documents that this assignment will propose to the driver. | [optional] 
**Trailers** | Pointer to [**[]TrailerNameOnlyResponse**](trailerNameOnlyResponse.md) | Trailers that this assignment will propose to the driver. | [optional] 
**Vehicle** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 

## Methods

### GetAcceptedTime

`func (o *CarrierProposedAssignment) GetAcceptedTime() map[string]interface{}`

GetAcceptedTime returns the AcceptedTime field if non-nil, zero value otherwise.

### GetAcceptedTimeOk

`func (o *CarrierProposedAssignment) GetAcceptedTimeOk() (map[string]interface{}, bool)`

GetAcceptedTimeOk returns a tuple with the AcceptedTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAcceptedTime

`func (o *CarrierProposedAssignment) HasAcceptedTime() bool`

HasAcceptedTime returns a boolean if a field has been set.

### SetAcceptedTime

`func (o *CarrierProposedAssignment) SetAcceptedTime(v map[string]interface{})`

SetAcceptedTime gets a reference to the given map[string]interface{} and assigns it to the AcceptedTime field.

### GetActiveTime

`func (o *CarrierProposedAssignment) GetActiveTime() map[string]interface{}`

GetActiveTime returns the ActiveTime field if non-nil, zero value otherwise.

### GetActiveTimeOk

`func (o *CarrierProposedAssignment) GetActiveTimeOk() (map[string]interface{}, bool)`

GetActiveTimeOk returns a tuple with the ActiveTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasActiveTime

`func (o *CarrierProposedAssignment) HasActiveTime() bool`

HasActiveTime returns a boolean if a field has been set.

### SetActiveTime

`func (o *CarrierProposedAssignment) SetActiveTime(v map[string]interface{})`

SetActiveTime gets a reference to the given map[string]interface{} and assigns it to the ActiveTime field.

### GetFirstSeenTime

`func (o *CarrierProposedAssignment) GetFirstSeenTime() map[string]interface{}`

GetFirstSeenTime returns the FirstSeenTime field if non-nil, zero value otherwise.

### GetFirstSeenTimeOk

`func (o *CarrierProposedAssignment) GetFirstSeenTimeOk() (map[string]interface{}, bool)`

GetFirstSeenTimeOk returns a tuple with the FirstSeenTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFirstSeenTime

`func (o *CarrierProposedAssignment) HasFirstSeenTime() bool`

HasFirstSeenTime returns a boolean if a field has been set.

### SetFirstSeenTime

`func (o *CarrierProposedAssignment) SetFirstSeenTime(v map[string]interface{})`

SetFirstSeenTime gets a reference to the given map[string]interface{} and assigns it to the FirstSeenTime field.

### GetId

`func (o *CarrierProposedAssignment) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CarrierProposedAssignment) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *CarrierProposedAssignment) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *CarrierProposedAssignment) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetRejectedTime

`func (o *CarrierProposedAssignment) GetRejectedTime() map[string]interface{}`

GetRejectedTime returns the RejectedTime field if non-nil, zero value otherwise.

### GetRejectedTimeOk

`func (o *CarrierProposedAssignment) GetRejectedTimeOk() (map[string]interface{}, bool)`

GetRejectedTimeOk returns a tuple with the RejectedTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRejectedTime

`func (o *CarrierProposedAssignment) HasRejectedTime() bool`

HasRejectedTime returns a boolean if a field has been set.

### SetRejectedTime

`func (o *CarrierProposedAssignment) SetRejectedTime(v map[string]interface{})`

SetRejectedTime gets a reference to the given map[string]interface{} and assigns it to the RejectedTime field.

### GetShippingDocs

`func (o *CarrierProposedAssignment) GetShippingDocs() string`

GetShippingDocs returns the ShippingDocs field if non-nil, zero value otherwise.

### GetShippingDocsOk

`func (o *CarrierProposedAssignment) GetShippingDocsOk() (string, bool)`

GetShippingDocsOk returns a tuple with the ShippingDocs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasShippingDocs

`func (o *CarrierProposedAssignment) HasShippingDocs() bool`

HasShippingDocs returns a boolean if a field has been set.

### SetShippingDocs

`func (o *CarrierProposedAssignment) SetShippingDocs(v string)`

SetShippingDocs gets a reference to the given string and assigns it to the ShippingDocs field.

### GetTrailers

`func (o *CarrierProposedAssignment) GetTrailers() []TrailerNameOnlyResponse`

GetTrailers returns the Trailers field if non-nil, zero value otherwise.

### GetTrailersOk

`func (o *CarrierProposedAssignment) GetTrailersOk() ([]TrailerNameOnlyResponse, bool)`

GetTrailersOk returns a tuple with the Trailers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailers

`func (o *CarrierProposedAssignment) HasTrailers() bool`

HasTrailers returns a boolean if a field has been set.

### SetTrailers

`func (o *CarrierProposedAssignment) SetTrailers(v []TrailerNameOnlyResponse)`

SetTrailers gets a reference to the given []TrailerNameOnlyResponse and assigns it to the Trailers field.

### GetVehicle

`func (o *CarrierProposedAssignment) GetVehicle() map[string]interface{}`

GetVehicle returns the Vehicle field if non-nil, zero value otherwise.

### GetVehicleOk

`func (o *CarrierProposedAssignment) GetVehicleOk() (map[string]interface{}, bool)`

GetVehicleOk returns a tuple with the Vehicle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicle

`func (o *CarrierProposedAssignment) HasVehicle() bool`

HasVehicle returns a boolean if a field has been set.

### SetVehicle

`func (o *CarrierProposedAssignment) SetVehicle(v map[string]interface{})`

SetVehicle gets a reference to the given map[string]interface{} and assigns it to the Vehicle field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


