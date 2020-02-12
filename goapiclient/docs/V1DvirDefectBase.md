# V1DvirDefectBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Comment** | Pointer to **string** | The comment describing the type of DVIR defect. | [optional] 
**DefectType** | Pointer to **string** | The type of DVIR defect. Possible values: [&#x60;AIR_COMPRESSOR&#x60;, &#x60;AIR_CONDITIONER&#x60;, &#x60;AIR_LINES&#x60;, &#x60;BATTERY&#x60;, &#x60;BELTS_HOSES&#x60;, &#x60;BRAKE_ACCESSORIES&#x60;, &#x60;BRAKE_CHECK&#x60;, &#x60;BRAKE_CONNECTIONS&#x60;, &#x60;BRAKES&#x60;, &#x60;CLUTCH&#x60;, &#x60;COUPLING_DEVICES&#x60;, &#x60;DEFROSTER_HEATER&#x60;, &#x60;DOORS&#x60;, &#x60;DRIVE_LINE&#x60;, &#x60;EMERGENCY_DOOR_AND_BUZZER&#x60;, &#x60;ENGINE&#x60;, &#x60;ENTRANCE_STEPS&#x60;, &#x60;EXHAUST&#x60;, &#x60;FIFTH_WHEEL&#x60;, &#x60;FIRST_AID_KIT&#x60;, &#x60;FLUID_LEVELS&#x60;, &#x60;FRAME_ASSEMBLY&#x60;, &#x60;FRONT_AXLE&#x60;, &#x60;FUEL_TANKS&#x60;, &#x60;HORN&#x60;, &#x60;INTERIOR_AND_FLOOR&#x60;, &#x60;LANDING_GEAR&#x60;, &#x60;LIGHTS&#x60;, &#x60;MIRRORS&#x60;, &#x60;MUFFLER&#x60;, &#x60;OIL_PRESSURE&#x60;, &#x60;OTHER&#x60;, &#x60;RADIATOR&#x60;, &#x60;REAR_END&#x60;, &#x60;REFLECTORS&#x60;, &#x60;ROOF&#x60;, &#x60;SAFETY_EQUIPMENT&#x60;, &#x60;STARTER&#x60;, &#x60;STEERING&#x60;, &#x60;STOP_ARM_CONTROL&#x60;, &#x60;STOP_ARM&#x60;, &#x60;SUSPENSION&#x60;, &#x60;TIRE_CHAINS&#x60;, &#x60;TIRES&#x60;, &#x60;TRANSMISSION&#x60;, &#x60;TRIP_RECORDER&#x60;, &#x60;WHEELS_RIMS&#x60;, &#x60;WINDOWS&#x60;, &#x60;WINDSHIELD_WIPERS&#x60;, &#x60;UNSET&#x60;] | [optional] 
**Id** | Pointer to **int64** | The id of this defect. | [optional] 
**Resolved** | Pointer to **bool** | Signifies if this defect is resolved. | [optional] 
**ResolvedAt** | Pointer to **int64** | Timestamp when this defect was resolved, in UNIX milliseconds.  Will not be returned if the defect is unresolved. | [optional] 
**ResolvedByDriverId** | Pointer to **int64** | ID of the driver who resolved this defect. Will not be returned if the defect is unresolved or resolvedByMechanicId is returned. | [optional] 
**ResolvedByMechanicId** | Pointer to **int64** | ID of the mechanic who resolved this defect. Will not be returned if the defect is unresolved or resolvedByDriverId is returned. | [optional] 

## Methods

### GetComment

`func (o *V1DvirDefectBase) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *V1DvirDefectBase) GetCommentOk() (string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasComment

`func (o *V1DvirDefectBase) HasComment() bool`

HasComment returns a boolean if a field has been set.

### SetComment

`func (o *V1DvirDefectBase) SetComment(v string)`

SetComment gets a reference to the given string and assigns it to the Comment field.

### GetDefectType

`func (o *V1DvirDefectBase) GetDefectType() string`

GetDefectType returns the DefectType field if non-nil, zero value otherwise.

### GetDefectTypeOk

`func (o *V1DvirDefectBase) GetDefectTypeOk() (string, bool)`

GetDefectTypeOk returns a tuple with the DefectType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDefectType

`func (o *V1DvirDefectBase) HasDefectType() bool`

HasDefectType returns a boolean if a field has been set.

### SetDefectType

`func (o *V1DvirDefectBase) SetDefectType(v string)`

SetDefectType gets a reference to the given string and assigns it to the DefectType field.

### GetId

`func (o *V1DvirDefectBase) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1DvirDefectBase) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1DvirDefectBase) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1DvirDefectBase) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetResolved

`func (o *V1DvirDefectBase) GetResolved() bool`

GetResolved returns the Resolved field if non-nil, zero value otherwise.

### GetResolvedOk

`func (o *V1DvirDefectBase) GetResolvedOk() (bool, bool)`

GetResolvedOk returns a tuple with the Resolved field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasResolved

`func (o *V1DvirDefectBase) HasResolved() bool`

HasResolved returns a boolean if a field has been set.

### SetResolved

`func (o *V1DvirDefectBase) SetResolved(v bool)`

SetResolved gets a reference to the given bool and assigns it to the Resolved field.

### GetResolvedAt

`func (o *V1DvirDefectBase) GetResolvedAt() int64`

GetResolvedAt returns the ResolvedAt field if non-nil, zero value otherwise.

### GetResolvedAtOk

`func (o *V1DvirDefectBase) GetResolvedAtOk() (int64, bool)`

GetResolvedAtOk returns a tuple with the ResolvedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasResolvedAt

`func (o *V1DvirDefectBase) HasResolvedAt() bool`

HasResolvedAt returns a boolean if a field has been set.

### SetResolvedAt

`func (o *V1DvirDefectBase) SetResolvedAt(v int64)`

SetResolvedAt gets a reference to the given int64 and assigns it to the ResolvedAt field.

### GetResolvedByDriverId

`func (o *V1DvirDefectBase) GetResolvedByDriverId() int64`

GetResolvedByDriverId returns the ResolvedByDriverId field if non-nil, zero value otherwise.

### GetResolvedByDriverIdOk

`func (o *V1DvirDefectBase) GetResolvedByDriverIdOk() (int64, bool)`

GetResolvedByDriverIdOk returns a tuple with the ResolvedByDriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasResolvedByDriverId

`func (o *V1DvirDefectBase) HasResolvedByDriverId() bool`

HasResolvedByDriverId returns a boolean if a field has been set.

### SetResolvedByDriverId

`func (o *V1DvirDefectBase) SetResolvedByDriverId(v int64)`

SetResolvedByDriverId gets a reference to the given int64 and assigns it to the ResolvedByDriverId field.

### GetResolvedByMechanicId

`func (o *V1DvirDefectBase) GetResolvedByMechanicId() int64`

GetResolvedByMechanicId returns the ResolvedByMechanicId field if non-nil, zero value otherwise.

### GetResolvedByMechanicIdOk

`func (o *V1DvirDefectBase) GetResolvedByMechanicIdOk() (int64, bool)`

GetResolvedByMechanicIdOk returns a tuple with the ResolvedByMechanicId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasResolvedByMechanicId

`func (o *V1DvirDefectBase) HasResolvedByMechanicId() bool`

HasResolvedByMechanicId returns a boolean if a field has been set.

### SetResolvedByMechanicId

`func (o *V1DvirDefectBase) SetResolvedByMechanicId(v int64)`

SetResolvedByMechanicId gets a reference to the given int64 and assigns it to the ResolvedByMechanicId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


