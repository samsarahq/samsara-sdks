# CreateCarrierProposedAssignmentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ActiveTime** | Pointer to [**time.Time**](time.Time.md) | Time after which this assignment will be active and visible to the driver on the mobile app. Not setting it makes it active now. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**DriverId** | Pointer to **string** | Samsara ID for the driver that this assignment is for. | 
**ShippingDocs** | Pointer to **string** | Shipping Documents that this assignment will propose to the driver. | [optional] 
**TrailerNames** | Pointer to **[]string** | Names of trailers to propose. | [optional] 
**VehicleId** | Pointer to **string** | Samsara ID for the vehicle to propose. | 

## Methods

### GetActiveTime

`func (o *CreateCarrierProposedAssignmentRequest) GetActiveTime() time.Time`

GetActiveTime returns the ActiveTime field if non-nil, zero value otherwise.

### GetActiveTimeOk

`func (o *CreateCarrierProposedAssignmentRequest) GetActiveTimeOk() (time.Time, bool)`

GetActiveTimeOk returns a tuple with the ActiveTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasActiveTime

`func (o *CreateCarrierProposedAssignmentRequest) HasActiveTime() bool`

HasActiveTime returns a boolean if a field has been set.

### SetActiveTime

`func (o *CreateCarrierProposedAssignmentRequest) SetActiveTime(v time.Time)`

SetActiveTime gets a reference to the given time.Time and assigns it to the ActiveTime field.

### GetDriverId

`func (o *CreateCarrierProposedAssignmentRequest) GetDriverId() string`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *CreateCarrierProposedAssignmentRequest) GetDriverIdOk() (string, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *CreateCarrierProposedAssignmentRequest) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *CreateCarrierProposedAssignmentRequest) SetDriverId(v string)`

SetDriverId gets a reference to the given string and assigns it to the DriverId field.

### GetShippingDocs

`func (o *CreateCarrierProposedAssignmentRequest) GetShippingDocs() string`

GetShippingDocs returns the ShippingDocs field if non-nil, zero value otherwise.

### GetShippingDocsOk

`func (o *CreateCarrierProposedAssignmentRequest) GetShippingDocsOk() (string, bool)`

GetShippingDocsOk returns a tuple with the ShippingDocs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasShippingDocs

`func (o *CreateCarrierProposedAssignmentRequest) HasShippingDocs() bool`

HasShippingDocs returns a boolean if a field has been set.

### SetShippingDocs

`func (o *CreateCarrierProposedAssignmentRequest) SetShippingDocs(v string)`

SetShippingDocs gets a reference to the given string and assigns it to the ShippingDocs field.

### GetTrailerNames

`func (o *CreateCarrierProposedAssignmentRequest) GetTrailerNames() []string`

GetTrailerNames returns the TrailerNames field if non-nil, zero value otherwise.

### GetTrailerNamesOk

`func (o *CreateCarrierProposedAssignmentRequest) GetTrailerNamesOk() ([]string, bool)`

GetTrailerNamesOk returns a tuple with the TrailerNames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerNames

`func (o *CreateCarrierProposedAssignmentRequest) HasTrailerNames() bool`

HasTrailerNames returns a boolean if a field has been set.

### SetTrailerNames

`func (o *CreateCarrierProposedAssignmentRequest) SetTrailerNames(v []string)`

SetTrailerNames gets a reference to the given []string and assigns it to the TrailerNames field.

### GetVehicleId

`func (o *CreateCarrierProposedAssignmentRequest) GetVehicleId() string`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *CreateCarrierProposedAssignmentRequest) GetVehicleIdOk() (string, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *CreateCarrierProposedAssignmentRequest) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *CreateCarrierProposedAssignmentRequest) SetVehicleId(v string)`

SetVehicleId gets a reference to the given string and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


