# V1DocumentCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DocumentTypeUuid** | Pointer to **string** | Universally unique identifier for the document type that this document is being created for. | 
**Fields** | Pointer to [**[]V1DocumentField**](V1DocumentField.md) | List of fields for the document. The fields must be listed in the order that that they appear in the document type. Only &#x60;stringValue&#x60;, &#x60;numberValue&#x60;, &#x60;multipleChoiceValue&#x60;, and &#x60;dateTimeValue&#x60; fields are supported for document creation via the API. | 
**DispatchJobId** | Pointer to **int64** | ID of the Samsara dispatch job for which the document is submitted. | [optional] 
**Notes** | Pointer to **string** | Notes submitted with this document. | [optional] 
**State** | Pointer to **string** | The condition of the document created for the driver. Can be either &#x60;Required&#x60; or &#x60;Submitted&#x60;. If no value is specified, &#x60;state&#x60; defaults to &#x60;Required&#x60;. &#x60;Required&#x60; documents are pre-populated documents for the Driver to fill out in the Driver App and have not yet been submitted. &#x60;Submitted&#x60; documents will show up as submitted by the driver through the driver app. | [optional] [default to STATE_REQUIRED]

## Methods

### GetDocumentTypeUuid

`func (o *V1DocumentCreate) GetDocumentTypeUuid() string`

GetDocumentTypeUuid returns the DocumentTypeUuid field if non-nil, zero value otherwise.

### GetDocumentTypeUuidOk

`func (o *V1DocumentCreate) GetDocumentTypeUuidOk() (string, bool)`

GetDocumentTypeUuidOk returns a tuple with the DocumentTypeUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDocumentTypeUuid

`func (o *V1DocumentCreate) HasDocumentTypeUuid() bool`

HasDocumentTypeUuid returns a boolean if a field has been set.

### SetDocumentTypeUuid

`func (o *V1DocumentCreate) SetDocumentTypeUuid(v string)`

SetDocumentTypeUuid gets a reference to the given string and assigns it to the DocumentTypeUuid field.

### GetFields

`func (o *V1DocumentCreate) GetFields() []V1DocumentField`

GetFields returns the Fields field if non-nil, zero value otherwise.

### GetFieldsOk

`func (o *V1DocumentCreate) GetFieldsOk() ([]V1DocumentField, bool)`

GetFieldsOk returns a tuple with the Fields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFields

`func (o *V1DocumentCreate) HasFields() bool`

HasFields returns a boolean if a field has been set.

### SetFields

`func (o *V1DocumentCreate) SetFields(v []V1DocumentField)`

SetFields gets a reference to the given []V1DocumentField and assigns it to the Fields field.

### GetDispatchJobId

`func (o *V1DocumentCreate) GetDispatchJobId() int64`

GetDispatchJobId returns the DispatchJobId field if non-nil, zero value otherwise.

### GetDispatchJobIdOk

`func (o *V1DocumentCreate) GetDispatchJobIdOk() (int64, bool)`

GetDispatchJobIdOk returns a tuple with the DispatchJobId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDispatchJobId

`func (o *V1DocumentCreate) HasDispatchJobId() bool`

HasDispatchJobId returns a boolean if a field has been set.

### SetDispatchJobId

`func (o *V1DocumentCreate) SetDispatchJobId(v int64)`

SetDispatchJobId gets a reference to the given int64 and assigns it to the DispatchJobId field.

### GetNotes

`func (o *V1DocumentCreate) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *V1DocumentCreate) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *V1DocumentCreate) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *V1DocumentCreate) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetState

`func (o *V1DocumentCreate) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *V1DocumentCreate) GetStateOk() (string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasState

`func (o *V1DocumentCreate) HasState() bool`

HasState returns a boolean if a field has been set.

### SetState

`func (o *V1DocumentCreate) SetState(v string)`

SetState gets a reference to the given string and assigns it to the State field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


