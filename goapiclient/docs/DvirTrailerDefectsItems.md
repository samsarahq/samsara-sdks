# DvirTrailerDefectsItems

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Comment** | Pointer to **string** | Comment on the defect. | [optional] 
**CreatedAtTime** | Pointer to **string** | Time when the defect was created. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**DefectType** | Pointer to **string** | The type of DVIR defect. | [optional] 
**Id** | Pointer to **string** | ID of the defect. | 
**IsResolved** | Pointer to **bool** | Signifies if this defect is resolved. | 
**ResolvedAtTime** | Pointer to **string** | Time when this defect was resolved. Will not be returned if the defect is unresolved. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**ResolvedBy** | Pointer to [**DefectResolvedBy**](Defect_resolvedBy.md) |  | [optional] 
**Trailer** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 
**Vehicle** | Pointer to [**map[string]interface{}**](map[string]interface{}.md) |  | [optional] 

## Methods

### GetComment

`func (o *DvirTrailerDefectsItems) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *DvirTrailerDefectsItems) GetCommentOk() (string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasComment

`func (o *DvirTrailerDefectsItems) HasComment() bool`

HasComment returns a boolean if a field has been set.

### SetComment

`func (o *DvirTrailerDefectsItems) SetComment(v string)`

SetComment gets a reference to the given string and assigns it to the Comment field.

### GetCreatedAtTime

`func (o *DvirTrailerDefectsItems) GetCreatedAtTime() string`

GetCreatedAtTime returns the CreatedAtTime field if non-nil, zero value otherwise.

### GetCreatedAtTimeOk

`func (o *DvirTrailerDefectsItems) GetCreatedAtTimeOk() (string, bool)`

GetCreatedAtTimeOk returns a tuple with the CreatedAtTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCreatedAtTime

`func (o *DvirTrailerDefectsItems) HasCreatedAtTime() bool`

HasCreatedAtTime returns a boolean if a field has been set.

### SetCreatedAtTime

`func (o *DvirTrailerDefectsItems) SetCreatedAtTime(v string)`

SetCreatedAtTime gets a reference to the given string and assigns it to the CreatedAtTime field.

### GetDefectType

`func (o *DvirTrailerDefectsItems) GetDefectType() string`

GetDefectType returns the DefectType field if non-nil, zero value otherwise.

### GetDefectTypeOk

`func (o *DvirTrailerDefectsItems) GetDefectTypeOk() (string, bool)`

GetDefectTypeOk returns a tuple with the DefectType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDefectType

`func (o *DvirTrailerDefectsItems) HasDefectType() bool`

HasDefectType returns a boolean if a field has been set.

### SetDefectType

`func (o *DvirTrailerDefectsItems) SetDefectType(v string)`

SetDefectType gets a reference to the given string and assigns it to the DefectType field.

### GetId

`func (o *DvirTrailerDefectsItems) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DvirTrailerDefectsItems) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *DvirTrailerDefectsItems) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *DvirTrailerDefectsItems) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetIsResolved

`func (o *DvirTrailerDefectsItems) GetIsResolved() bool`

GetIsResolved returns the IsResolved field if non-nil, zero value otherwise.

### GetIsResolvedOk

`func (o *DvirTrailerDefectsItems) GetIsResolvedOk() (bool, bool)`

GetIsResolvedOk returns a tuple with the IsResolved field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasIsResolved

`func (o *DvirTrailerDefectsItems) HasIsResolved() bool`

HasIsResolved returns a boolean if a field has been set.

### SetIsResolved

`func (o *DvirTrailerDefectsItems) SetIsResolved(v bool)`

SetIsResolved gets a reference to the given bool and assigns it to the IsResolved field.

### GetResolvedAtTime

`func (o *DvirTrailerDefectsItems) GetResolvedAtTime() string`

GetResolvedAtTime returns the ResolvedAtTime field if non-nil, zero value otherwise.

### GetResolvedAtTimeOk

`func (o *DvirTrailerDefectsItems) GetResolvedAtTimeOk() (string, bool)`

GetResolvedAtTimeOk returns a tuple with the ResolvedAtTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasResolvedAtTime

`func (o *DvirTrailerDefectsItems) HasResolvedAtTime() bool`

HasResolvedAtTime returns a boolean if a field has been set.

### SetResolvedAtTime

`func (o *DvirTrailerDefectsItems) SetResolvedAtTime(v string)`

SetResolvedAtTime gets a reference to the given string and assigns it to the ResolvedAtTime field.

### GetResolvedBy

`func (o *DvirTrailerDefectsItems) GetResolvedBy() DefectResolvedBy`

GetResolvedBy returns the ResolvedBy field if non-nil, zero value otherwise.

### GetResolvedByOk

`func (o *DvirTrailerDefectsItems) GetResolvedByOk() (DefectResolvedBy, bool)`

GetResolvedByOk returns a tuple with the ResolvedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasResolvedBy

`func (o *DvirTrailerDefectsItems) HasResolvedBy() bool`

HasResolvedBy returns a boolean if a field has been set.

### SetResolvedBy

`func (o *DvirTrailerDefectsItems) SetResolvedBy(v DefectResolvedBy)`

SetResolvedBy gets a reference to the given DefectResolvedBy and assigns it to the ResolvedBy field.

### GetTrailer

`func (o *DvirTrailerDefectsItems) GetTrailer() map[string]interface{}`

GetTrailer returns the Trailer field if non-nil, zero value otherwise.

### GetTrailerOk

`func (o *DvirTrailerDefectsItems) GetTrailerOk() (map[string]interface{}, bool)`

GetTrailerOk returns a tuple with the Trailer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailer

`func (o *DvirTrailerDefectsItems) HasTrailer() bool`

HasTrailer returns a boolean if a field has been set.

### SetTrailer

`func (o *DvirTrailerDefectsItems) SetTrailer(v map[string]interface{})`

SetTrailer gets a reference to the given map[string]interface{} and assigns it to the Trailer field.

### GetVehicle

`func (o *DvirTrailerDefectsItems) GetVehicle() map[string]interface{}`

GetVehicle returns the Vehicle field if non-nil, zero value otherwise.

### GetVehicleOk

`func (o *DvirTrailerDefectsItems) GetVehicleOk() (map[string]interface{}, bool)`

GetVehicleOk returns a tuple with the Vehicle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicle

`func (o *DvirTrailerDefectsItems) HasVehicle() bool`

HasVehicle returns a boolean if a field has been set.

### SetVehicle

`func (o *DvirTrailerDefectsItems) SetVehicle(v map[string]interface{})`

SetVehicle gets a reference to the given map[string]interface{} and assigns it to the Vehicle field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


