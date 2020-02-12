# V1MessageResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DriverId** | Pointer to **int64** | ID of the driver for whom the message is sent to or sent by. | 
**IsRead** | Pointer to **bool** | True if the message was read by the recipient. | 
**Sender** | Pointer to [**V1MessageSender**](V1MessageSender.md) |  | 
**SentAtMs** | Pointer to **int64** | The time in Unix epoch milliseconds that the message is sent to the recipient. | 
**Text** | Pointer to **string** | The text sent in the message. | 

## Methods

### GetDriverId

`func (o *V1MessageResponse) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1MessageResponse) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1MessageResponse) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1MessageResponse) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetIsRead

`func (o *V1MessageResponse) GetIsRead() bool`

GetIsRead returns the IsRead field if non-nil, zero value otherwise.

### GetIsReadOk

`func (o *V1MessageResponse) GetIsReadOk() (bool, bool)`

GetIsReadOk returns a tuple with the IsRead field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasIsRead

`func (o *V1MessageResponse) HasIsRead() bool`

HasIsRead returns a boolean if a field has been set.

### SetIsRead

`func (o *V1MessageResponse) SetIsRead(v bool)`

SetIsRead gets a reference to the given bool and assigns it to the IsRead field.

### GetSender

`func (o *V1MessageResponse) GetSender() V1MessageSender`

GetSender returns the Sender field if non-nil, zero value otherwise.

### GetSenderOk

`func (o *V1MessageResponse) GetSenderOk() (V1MessageSender, bool)`

GetSenderOk returns a tuple with the Sender field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSender

`func (o *V1MessageResponse) HasSender() bool`

HasSender returns a boolean if a field has been set.

### SetSender

`func (o *V1MessageResponse) SetSender(v V1MessageSender)`

SetSender gets a reference to the given V1MessageSender and assigns it to the Sender field.

### GetSentAtMs

`func (o *V1MessageResponse) GetSentAtMs() int64`

GetSentAtMs returns the SentAtMs field if non-nil, zero value otherwise.

### GetSentAtMsOk

`func (o *V1MessageResponse) GetSentAtMsOk() (int64, bool)`

GetSentAtMsOk returns a tuple with the SentAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSentAtMs

`func (o *V1MessageResponse) HasSentAtMs() bool`

HasSentAtMs returns a boolean if a field has been set.

### SetSentAtMs

`func (o *V1MessageResponse) SetSentAtMs(v int64)`

SetSentAtMs gets a reference to the given int64 and assigns it to the SentAtMs field.

### GetText

`func (o *V1MessageResponse) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *V1MessageResponse) GetTextOk() (string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasText

`func (o *V1MessageResponse) HasText() bool`

HasText returns a boolean if a field has been set.

### SetText

`func (o *V1MessageResponse) SetText(v string)`

SetText gets a reference to the given string and assigns it to the Text field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


