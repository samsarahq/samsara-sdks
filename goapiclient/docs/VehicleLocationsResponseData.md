# VehicleLocationsResponseData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed. | 
**Location** | Pointer to [**VehicleLocation**](VehicleLocation.md) |  | 
**Name** | Pointer to **string** | The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time. | 

## Methods

### GetId

`func (o *VehicleLocationsResponseData) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *VehicleLocationsResponseData) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *VehicleLocationsResponseData) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *VehicleLocationsResponseData) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetLocation

`func (o *VehicleLocationsResponseData) GetLocation() VehicleLocation`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *VehicleLocationsResponseData) GetLocationOk() (VehicleLocation, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocation

`func (o *VehicleLocationsResponseData) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### SetLocation

`func (o *VehicleLocationsResponseData) SetLocation(v VehicleLocation)`

SetLocation gets a reference to the given VehicleLocation and assigns it to the Location field.

### GetName

`func (o *VehicleLocationsResponseData) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *VehicleLocationsResponseData) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *VehicleLocationsResponseData) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *VehicleLocationsResponseData) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


