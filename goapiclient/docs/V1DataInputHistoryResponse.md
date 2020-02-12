# V1DataInputHistoryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int64** | The ID of this data input | [optional] 
**Name** | Pointer to **string** | Name of this data input | 
**Points** | Pointer to [**[]V1DataInputHistoryResponsePoints**](V1DataInputHistoryResponse_points.md) | Data points from this data input | [optional] 

## Methods

### GetId

`func (o *V1DataInputHistoryResponse) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1DataInputHistoryResponse) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1DataInputHistoryResponse) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1DataInputHistoryResponse) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetName

`func (o *V1DataInputHistoryResponse) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *V1DataInputHistoryResponse) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *V1DataInputHistoryResponse) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *V1DataInputHistoryResponse) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetPoints

`func (o *V1DataInputHistoryResponse) GetPoints() []V1DataInputHistoryResponsePoints`

GetPoints returns the Points field if non-nil, zero value otherwise.

### GetPointsOk

`func (o *V1DataInputHistoryResponse) GetPointsOk() ([]V1DataInputHistoryResponsePoints, bool)`

GetPointsOk returns a tuple with the Points field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPoints

`func (o *V1DataInputHistoryResponse) HasPoints() bool`

HasPoints returns a boolean if a field has been set.

### SetPoints

`func (o *V1DataInputHistoryResponse) SetPoints(v []V1DataInputHistoryResponsePoints)`

SetPoints gets a reference to the given []V1DataInputHistoryResponsePoints and assigns it to the Points field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


