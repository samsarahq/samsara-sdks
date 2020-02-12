# V1Document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DocumentType** | Pointer to **string** | Name of the document type. | 
**DriverCreatedAtMs** | Pointer to **int64** | The time in Unix epoch milliseconds that the document was created in the driver app. | 
**DriverId** | Pointer to **int64** | ID of the driver for whom the document is submitted. | 
**Fields** | Pointer to [**[]V1DocumentField**](V1DocumentField.md) | The fields associated with this document. | 
**Id** | Pointer to **string** | ID of the document. | 
**OrgId** | Pointer to **int64** | Organization ID that the document belongs to. | 
**ServerCreatedAtMs** | Pointer to **int64** | The time in Unix epoch milliseconds that the document was received by the server. | 
**ServerUpdatedAtMs** | Pointer to **int64** | The time in Unix epoch milliseconds that the document was updated on the server. | 
**VehicleId** | Pointer to **int64** | ID of the vehicle the driver was signed into when the document was submitted. Will be &#x60;null&#x60; if the document &#x60;state&#x60; is &#x60;Required&#x60;. | 
**DispatchJobId** | Pointer to **int64** | ID of the Samsara dispatch job for which the document is submitted. | 
**Notes** | Pointer to **string** | Notes submitted with this document. | 
**State** | Pointer to **string** | The condition of the document created for the driver. Can be either &#x60;Required&#x60; or &#x60;Submitted&#x60;. If no value is specified, &#x60;state&#x60; defaults to &#x60;Required&#x60;. &#x60;Required&#x60; documents are pre-populated documents for the Driver to fill out in the Driver App and have not yet been submitted. &#x60;Submitted&#x60; documents have been submitted by the driver in the Driver App. | [optional] [default to STATE_REQUIRED]

## Methods

### GetDocumentType

`func (o *V1Document) GetDocumentType() string`

GetDocumentType returns the DocumentType field if non-nil, zero value otherwise.

### GetDocumentTypeOk

`func (o *V1Document) GetDocumentTypeOk() (string, bool)`

GetDocumentTypeOk returns a tuple with the DocumentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDocumentType

`func (o *V1Document) HasDocumentType() bool`

HasDocumentType returns a boolean if a field has been set.

### SetDocumentType

`func (o *V1Document) SetDocumentType(v string)`

SetDocumentType gets a reference to the given string and assigns it to the DocumentType field.

### GetDriverCreatedAtMs

`func (o *V1Document) GetDriverCreatedAtMs() int64`

GetDriverCreatedAtMs returns the DriverCreatedAtMs field if non-nil, zero value otherwise.

### GetDriverCreatedAtMsOk

`func (o *V1Document) GetDriverCreatedAtMsOk() (int64, bool)`

GetDriverCreatedAtMsOk returns a tuple with the DriverCreatedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverCreatedAtMs

`func (o *V1Document) HasDriverCreatedAtMs() bool`

HasDriverCreatedAtMs returns a boolean if a field has been set.

### SetDriverCreatedAtMs

`func (o *V1Document) SetDriverCreatedAtMs(v int64)`

SetDriverCreatedAtMs gets a reference to the given int64 and assigns it to the DriverCreatedAtMs field.

### GetDriverId

`func (o *V1Document) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1Document) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1Document) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1Document) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetFields

`func (o *V1Document) GetFields() []V1DocumentField`

GetFields returns the Fields field if non-nil, zero value otherwise.

### GetFieldsOk

`func (o *V1Document) GetFieldsOk() ([]V1DocumentField, bool)`

GetFieldsOk returns a tuple with the Fields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFields

`func (o *V1Document) HasFields() bool`

HasFields returns a boolean if a field has been set.

### SetFields

`func (o *V1Document) SetFields(v []V1DocumentField)`

SetFields gets a reference to the given []V1DocumentField and assigns it to the Fields field.

### GetId

`func (o *V1Document) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1Document) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1Document) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1Document) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetOrgId

`func (o *V1Document) GetOrgId() int64`

GetOrgId returns the OrgId field if non-nil, zero value otherwise.

### GetOrgIdOk

`func (o *V1Document) GetOrgIdOk() (int64, bool)`

GetOrgIdOk returns a tuple with the OrgId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOrgId

`func (o *V1Document) HasOrgId() bool`

HasOrgId returns a boolean if a field has been set.

### SetOrgId

`func (o *V1Document) SetOrgId(v int64)`

SetOrgId gets a reference to the given int64 and assigns it to the OrgId field.

### GetServerCreatedAtMs

`func (o *V1Document) GetServerCreatedAtMs() int64`

GetServerCreatedAtMs returns the ServerCreatedAtMs field if non-nil, zero value otherwise.

### GetServerCreatedAtMsOk

`func (o *V1Document) GetServerCreatedAtMsOk() (int64, bool)`

GetServerCreatedAtMsOk returns a tuple with the ServerCreatedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasServerCreatedAtMs

`func (o *V1Document) HasServerCreatedAtMs() bool`

HasServerCreatedAtMs returns a boolean if a field has been set.

### SetServerCreatedAtMs

`func (o *V1Document) SetServerCreatedAtMs(v int64)`

SetServerCreatedAtMs gets a reference to the given int64 and assigns it to the ServerCreatedAtMs field.

### GetServerUpdatedAtMs

`func (o *V1Document) GetServerUpdatedAtMs() int64`

GetServerUpdatedAtMs returns the ServerUpdatedAtMs field if non-nil, zero value otherwise.

### GetServerUpdatedAtMsOk

`func (o *V1Document) GetServerUpdatedAtMsOk() (int64, bool)`

GetServerUpdatedAtMsOk returns a tuple with the ServerUpdatedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasServerUpdatedAtMs

`func (o *V1Document) HasServerUpdatedAtMs() bool`

HasServerUpdatedAtMs returns a boolean if a field has been set.

### SetServerUpdatedAtMs

`func (o *V1Document) SetServerUpdatedAtMs(v int64)`

SetServerUpdatedAtMs gets a reference to the given int64 and assigns it to the ServerUpdatedAtMs field.

### GetVehicleId

`func (o *V1Document) GetVehicleId() int64`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1Document) GetVehicleIdOk() (int64, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1Document) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1Document) SetVehicleId(v int64)`

SetVehicleId gets a reference to the given int64 and assigns it to the VehicleId field.

### GetDispatchJobId

`func (o *V1Document) GetDispatchJobId() int64`

GetDispatchJobId returns the DispatchJobId field if non-nil, zero value otherwise.

### GetDispatchJobIdOk

`func (o *V1Document) GetDispatchJobIdOk() (int64, bool)`

GetDispatchJobIdOk returns a tuple with the DispatchJobId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDispatchJobId

`func (o *V1Document) HasDispatchJobId() bool`

HasDispatchJobId returns a boolean if a field has been set.

### SetDispatchJobId

`func (o *V1Document) SetDispatchJobId(v int64)`

SetDispatchJobId gets a reference to the given int64 and assigns it to the DispatchJobId field.

### GetNotes

`func (o *V1Document) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *V1Document) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *V1Document) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *V1Document) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetState

`func (o *V1Document) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *V1Document) GetStateOk() (string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasState

`func (o *V1Document) HasState() bool`

HasState returns a boolean if a field has been set.

### SetState

`func (o *V1Document) SetState(v string)`

SetState gets a reference to the given string and assigns it to the State field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


