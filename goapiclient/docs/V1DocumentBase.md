# V1DocumentBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DispatchJobId** | Pointer to **int64** | ID of the Samsara dispatch job for which the document is submitted. | 
**Notes** | Pointer to **string** | Notes submitted with this document. | 
**State** | Pointer to **string** | The condition of the document created for the driver. Can be either &#x60;Required&#x60; or &#x60;Submitted&#x60;. If no value is specified, &#x60;state&#x60; defaults to &#x60;Required&#x60;. &#x60;Required&#x60; documents are pre-populated documents for the Driver to fill out in the Driver App and have not yet been submitted. &#x60;Submitted&#x60; documents have been submitted by the driver in the Driver App. | [optional] [default to STATE_REQUIRED]

## Methods

### GetDispatchJobId

`func (o *V1DocumentBase) GetDispatchJobId() int64`

GetDispatchJobId returns the DispatchJobId field if non-nil, zero value otherwise.

### GetDispatchJobIdOk

`func (o *V1DocumentBase) GetDispatchJobIdOk() (int64, bool)`

GetDispatchJobIdOk returns a tuple with the DispatchJobId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDispatchJobId

`func (o *V1DocumentBase) HasDispatchJobId() bool`

HasDispatchJobId returns a boolean if a field has been set.

### SetDispatchJobId

`func (o *V1DocumentBase) SetDispatchJobId(v int64)`

SetDispatchJobId gets a reference to the given int64 and assigns it to the DispatchJobId field.

### GetNotes

`func (o *V1DocumentBase) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *V1DocumentBase) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *V1DocumentBase) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *V1DocumentBase) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetState

`func (o *V1DocumentBase) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *V1DocumentBase) GetStateOk() (string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasState

`func (o *V1DocumentBase) HasState() bool`

HasState returns a boolean if a field has been set.

### SetState

`func (o *V1DocumentBase) SetState(v string)`

SetState gets a reference to the given string and assigns it to the State field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


