# TachographActivityListWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Activity** | Pointer to [**[]TachographActivity**](TachographActivity.md) | List of all driver tachograph activities in a specified time range. | [optional] 
**Id** | Pointer to **string** | ID of the driver | [optional] 

## Methods

### GetActivity

`func (o *TachographActivityListWrapper) GetActivity() []TachographActivity`

GetActivity returns the Activity field if non-nil, zero value otherwise.

### GetActivityOk

`func (o *TachographActivityListWrapper) GetActivityOk() ([]TachographActivity, bool)`

GetActivityOk returns a tuple with the Activity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasActivity

`func (o *TachographActivityListWrapper) HasActivity() bool`

HasActivity returns a boolean if a field has been set.

### SetActivity

`func (o *TachographActivityListWrapper) SetActivity(v []TachographActivity)`

SetActivity gets a reference to the given []TachographActivity and assigns it to the Activity field.

### GetId

`func (o *TachographActivityListWrapper) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TachographActivityListWrapper) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *TachographActivityListWrapper) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *TachographActivityListWrapper) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


