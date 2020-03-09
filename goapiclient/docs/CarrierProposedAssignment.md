# CarrierProposedAssignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AcceptedTime** | Pointer to [**time.Time**](time.Time.md) | Time when the driver accepted this assignment in the mobile app. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**ActiveTime** | Pointer to [**time.Time**](time.Time.md) | Time after which this assignment will be active and visible to the driver on the mobile app. Not setting it makes it active now. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | 
**FirstSeenTime** | Pointer to [**time.Time**](time.Time.md) | Time when the driver first saw this assignment in the mobile app. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**RejectedTime** | Pointer to [**time.Time**](time.Time.md) | Time when the driver rejected this assignment in the mobile app. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**ShippingDocs** | Pointer to **string** | Shipping Documents that this assignment will propose to the driver. | [optional] 
**Trailers** | Pointer to [**[]TrailerNameOnlyResponse**](trailerNameOnlyResponse.md) | Trailers that this assignment will propose to the driver. | [optional] 
**Uuid** | Pointer to **string** | Samsara ID for the assignment. | 
**Vehicle** | Pointer to [**CarrierProposedAssignmentVehicle**](CarrierProposedAssignmentVehicle.md) |  | [optional] 

## Methods

### GetAcceptedTime

`func (o *CarrierProposedAssignment) GetAcceptedTime() time.Time`

GetAcceptedTime returns the AcceptedTime field if non-nil, zero value otherwise.

### GetAcceptedTimeOk

`func (o *CarrierProposedAssignment) GetAcceptedTimeOk() (time.Time, bool)`

GetAcceptedTimeOk returns a tuple with the AcceptedTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAcceptedTime

`func (o *CarrierProposedAssignment) HasAcceptedTime() bool`

HasAcceptedTime returns a boolean if a field has been set.

### SetAcceptedTime

`func (o *CarrierProposedAssignment) SetAcceptedTime(v time.Time)`

SetAcceptedTime gets a reference to the given time.Time and assigns it to the AcceptedTime field.

### GetActiveTime

`func (o *CarrierProposedAssignment) GetActiveTime() time.Time`

GetActiveTime returns the ActiveTime field if non-nil, zero value otherwise.

### GetActiveTimeOk

`func (o *CarrierProposedAssignment) GetActiveTimeOk() (time.Time, bool)`

GetActiveTimeOk returns a tuple with the ActiveTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasActiveTime

`func (o *CarrierProposedAssignment) HasActiveTime() bool`

HasActiveTime returns a boolean if a field has been set.

### SetActiveTime

`func (o *CarrierProposedAssignment) SetActiveTime(v time.Time)`

SetActiveTime gets a reference to the given time.Time and assigns it to the ActiveTime field.

### GetFirstSeenTime

`func (o *CarrierProposedAssignment) GetFirstSeenTime() time.Time`

GetFirstSeenTime returns the FirstSeenTime field if non-nil, zero value otherwise.

### GetFirstSeenTimeOk

`func (o *CarrierProposedAssignment) GetFirstSeenTimeOk() (time.Time, bool)`

GetFirstSeenTimeOk returns a tuple with the FirstSeenTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFirstSeenTime

`func (o *CarrierProposedAssignment) HasFirstSeenTime() bool`

HasFirstSeenTime returns a boolean if a field has been set.

### SetFirstSeenTime

`func (o *CarrierProposedAssignment) SetFirstSeenTime(v time.Time)`

SetFirstSeenTime gets a reference to the given time.Time and assigns it to the FirstSeenTime field.

### GetRejectedTime

`func (o *CarrierProposedAssignment) GetRejectedTime() time.Time`

GetRejectedTime returns the RejectedTime field if non-nil, zero value otherwise.

### GetRejectedTimeOk

`func (o *CarrierProposedAssignment) GetRejectedTimeOk() (time.Time, bool)`

GetRejectedTimeOk returns a tuple with the RejectedTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRejectedTime

`func (o *CarrierProposedAssignment) HasRejectedTime() bool`

HasRejectedTime returns a boolean if a field has been set.

### SetRejectedTime

`func (o *CarrierProposedAssignment) SetRejectedTime(v time.Time)`

SetRejectedTime gets a reference to the given time.Time and assigns it to the RejectedTime field.

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

### GetUuid

`func (o *CarrierProposedAssignment) GetUuid() string`

GetUuid returns the Uuid field if non-nil, zero value otherwise.

### GetUuidOk

`func (o *CarrierProposedAssignment) GetUuidOk() (string, bool)`

GetUuidOk returns a tuple with the Uuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasUuid

`func (o *CarrierProposedAssignment) HasUuid() bool`

HasUuid returns a boolean if a field has been set.

### SetUuid

`func (o *CarrierProposedAssignment) SetUuid(v string)`

SetUuid gets a reference to the given string and assigns it to the Uuid field.

### GetVehicle

`func (o *CarrierProposedAssignment) GetVehicle() CarrierProposedAssignmentVehicle`

GetVehicle returns the Vehicle field if non-nil, zero value otherwise.

### GetVehicleOk

`func (o *CarrierProposedAssignment) GetVehicleOk() (CarrierProposedAssignmentVehicle, bool)`

GetVehicleOk returns a tuple with the Vehicle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicle

`func (o *CarrierProposedAssignment) HasVehicle() bool`

HasVehicle returns a boolean if a field has been set.

### SetVehicle

`func (o *CarrierProposedAssignment) SetVehicle(v CarrierProposedAssignmentVehicle)`

SetVehicle gets a reference to the given CarrierProposedAssignmentVehicle and assigns it to the Vehicle field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


