# Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DriverId** | Pointer to **int64** | ID of the driver for whom the message is sent to or sent by. | 
**Text** | Pointer to **string** | The text sent in the message. | 

## Methods

### GetDriverId

`func (o *Message) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *Message) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *Message) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *Message) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetText

`func (o *Message) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *Message) GetTextOk() (string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasText

`func (o *Message) HasText() bool`

HasText returns a boolean if a field has been set.

### SetText

`func (o *Message) SetText(v string)`

SetText gets a reference to the given string and assigns it to the Text field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


