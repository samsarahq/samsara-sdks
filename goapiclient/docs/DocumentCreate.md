# DocumentCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DocumentTypeId** | Pointer to **string** | Unique Samsara ID for the document type. | 
**DriverId** | Pointer to **string** | ID of the driver. | 
**Fields** | Pointer to [**[]DocumentCreateFields**](DocumentCreate_fields.md) | The fields associated with the new document. The fields must be listed in the order that that they appear in the specified document type. | [optional] 
**Notes** | Pointer to **string** | Notes | [optional] 
**RouteStopId** | Pointer to **string** | Unique Samsara ID for the route stop. | [optional] 
**State** | Pointer to **string** | The condition of the document created for the driver. Can be either &#x60;required&#x60; or &#x60;submitted&#x60;, if no value is specified, &#x60;state&#x60; defaults to &#x60;required&#x60;. &#x60;required&#x60; documents are pre-populated documents for the Driver to fill out in the Driver App. | [optional] [default to STATE_REQUIRED]

## Methods

### GetDocumentTypeId

`func (o *DocumentCreate) GetDocumentTypeId() string`

GetDocumentTypeId returns the DocumentTypeId field if non-nil, zero value otherwise.

### GetDocumentTypeIdOk

`func (o *DocumentCreate) GetDocumentTypeIdOk() (string, bool)`

GetDocumentTypeIdOk returns a tuple with the DocumentTypeId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDocumentTypeId

`func (o *DocumentCreate) HasDocumentTypeId() bool`

HasDocumentTypeId returns a boolean if a field has been set.

### SetDocumentTypeId

`func (o *DocumentCreate) SetDocumentTypeId(v string)`

SetDocumentTypeId gets a reference to the given string and assigns it to the DocumentTypeId field.

### GetDriverId

`func (o *DocumentCreate) GetDriverId() string`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *DocumentCreate) GetDriverIdOk() (string, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *DocumentCreate) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *DocumentCreate) SetDriverId(v string)`

SetDriverId gets a reference to the given string and assigns it to the DriverId field.

### GetFields

`func (o *DocumentCreate) GetFields() []DocumentCreateFields`

GetFields returns the Fields field if non-nil, zero value otherwise.

### GetFieldsOk

`func (o *DocumentCreate) GetFieldsOk() ([]DocumentCreateFields, bool)`

GetFieldsOk returns a tuple with the Fields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFields

`func (o *DocumentCreate) HasFields() bool`

HasFields returns a boolean if a field has been set.

### SetFields

`func (o *DocumentCreate) SetFields(v []DocumentCreateFields)`

SetFields gets a reference to the given []DocumentCreateFields and assigns it to the Fields field.

### GetNotes

`func (o *DocumentCreate) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *DocumentCreate) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *DocumentCreate) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *DocumentCreate) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetRouteStopId

`func (o *DocumentCreate) GetRouteStopId() string`

GetRouteStopId returns the RouteStopId field if non-nil, zero value otherwise.

### GetRouteStopIdOk

`func (o *DocumentCreate) GetRouteStopIdOk() (string, bool)`

GetRouteStopIdOk returns a tuple with the RouteStopId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRouteStopId

`func (o *DocumentCreate) HasRouteStopId() bool`

HasRouteStopId returns a boolean if a field has been set.

### SetRouteStopId

`func (o *DocumentCreate) SetRouteStopId(v string)`

SetRouteStopId gets a reference to the given string and assigns it to the RouteStopId field.

### GetState

`func (o *DocumentCreate) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *DocumentCreate) GetStateOk() (string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasState

`func (o *DocumentCreate) HasState() bool`

HasState returns a boolean if a field has been set.

### SetState

`func (o *DocumentCreate) SetState(v string)`

SetState gets a reference to the given string and assigns it to the State field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


