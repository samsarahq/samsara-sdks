# DataInputResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | Unique identifier for the data input. | [optional] 
**Name** | Pointer to **string** | Name of this data input. | [optional] 
**Units** | Pointer to **string** | Units of data for this data input. | [optional] 
**NumberPoints** | Pointer to [**[]NumberDataPoint**](NumberDataPoint.md) | List of numeric data points from the data input. | [optional] 

## Methods

### GetId

`func (o *DataInputResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DataInputResponse) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *DataInputResponse) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *DataInputResponse) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetName

`func (o *DataInputResponse) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *DataInputResponse) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *DataInputResponse) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *DataInputResponse) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetUnits

`func (o *DataInputResponse) GetUnits() string`

GetUnits returns the Units field if non-nil, zero value otherwise.

### GetUnitsOk

`func (o *DataInputResponse) GetUnitsOk() (string, bool)`

GetUnitsOk returns a tuple with the Units field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasUnits

`func (o *DataInputResponse) HasUnits() bool`

HasUnits returns a boolean if a field has been set.

### SetUnits

`func (o *DataInputResponse) SetUnits(v string)`

SetUnits gets a reference to the given string and assigns it to the Units field.

### GetNumberPoints

`func (o *DataInputResponse) GetNumberPoints() []NumberDataPoint`

GetNumberPoints returns the NumberPoints field if non-nil, zero value otherwise.

### GetNumberPointsOk

`func (o *DataInputResponse) GetNumberPointsOk() ([]NumberDataPoint, bool)`

GetNumberPointsOk returns a tuple with the NumberPoints field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNumberPoints

`func (o *DataInputResponse) HasNumberPoints() bool`

HasNumberPoints returns a boolean if a field has been set.

### SetNumberPoints

`func (o *DataInputResponse) SetNumberPoints(v []NumberDataPoint)`

SetNumberPoints gets a reference to the given []NumberDataPoint and assigns it to the NumberPoints field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


