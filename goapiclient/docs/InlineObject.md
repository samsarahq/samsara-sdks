# InlineObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Annotation** | Pointer to **string** | Annotation for the driving segment. | 
**DriverId** | Pointer to **string** | ID of Driver to assign this segment to. The driver assignment is a tentative assignment until the ID is &#39;ACCEPTED&#39;. | 

## Methods

### GetAnnotation

`func (o *InlineObject) GetAnnotation() string`

GetAnnotation returns the Annotation field if non-nil, zero value otherwise.

### GetAnnotationOk

`func (o *InlineObject) GetAnnotationOk() (string, bool)`

GetAnnotationOk returns a tuple with the Annotation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasAnnotation

`func (o *InlineObject) HasAnnotation() bool`

HasAnnotation returns a boolean if a field has been set.

### SetAnnotation

`func (o *InlineObject) SetAnnotation(v string)`

SetAnnotation gets a reference to the given string and assigns it to the Annotation field.

### GetDriverId

`func (o *InlineObject) GetDriverId() string`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *InlineObject) GetDriverIdOk() (string, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *InlineObject) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *InlineObject) SetDriverId(v string)`

SetDriverId gets a reference to the given string and assigns it to the DriverId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


