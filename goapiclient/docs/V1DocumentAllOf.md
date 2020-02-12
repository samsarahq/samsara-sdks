# V1DocumentAllOf

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

## Methods

### GetDocumentType

`func (o *V1DocumentAllOf) GetDocumentType() string`

GetDocumentType returns the DocumentType field if non-nil, zero value otherwise.

### GetDocumentTypeOk

`func (o *V1DocumentAllOf) GetDocumentTypeOk() (string, bool)`

GetDocumentTypeOk returns a tuple with the DocumentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDocumentType

`func (o *V1DocumentAllOf) HasDocumentType() bool`

HasDocumentType returns a boolean if a field has been set.

### SetDocumentType

`func (o *V1DocumentAllOf) SetDocumentType(v string)`

SetDocumentType gets a reference to the given string and assigns it to the DocumentType field.

### GetDriverCreatedAtMs

`func (o *V1DocumentAllOf) GetDriverCreatedAtMs() int64`

GetDriverCreatedAtMs returns the DriverCreatedAtMs field if non-nil, zero value otherwise.

### GetDriverCreatedAtMsOk

`func (o *V1DocumentAllOf) GetDriverCreatedAtMsOk() (int64, bool)`

GetDriverCreatedAtMsOk returns a tuple with the DriverCreatedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverCreatedAtMs

`func (o *V1DocumentAllOf) HasDriverCreatedAtMs() bool`

HasDriverCreatedAtMs returns a boolean if a field has been set.

### SetDriverCreatedAtMs

`func (o *V1DocumentAllOf) SetDriverCreatedAtMs(v int64)`

SetDriverCreatedAtMs gets a reference to the given int64 and assigns it to the DriverCreatedAtMs field.

### GetDriverId

`func (o *V1DocumentAllOf) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1DocumentAllOf) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1DocumentAllOf) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1DocumentAllOf) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetFields

`func (o *V1DocumentAllOf) GetFields() []V1DocumentField`

GetFields returns the Fields field if non-nil, zero value otherwise.

### GetFieldsOk

`func (o *V1DocumentAllOf) GetFieldsOk() ([]V1DocumentField, bool)`

GetFieldsOk returns a tuple with the Fields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFields

`func (o *V1DocumentAllOf) HasFields() bool`

HasFields returns a boolean if a field has been set.

### SetFields

`func (o *V1DocumentAllOf) SetFields(v []V1DocumentField)`

SetFields gets a reference to the given []V1DocumentField and assigns it to the Fields field.

### GetId

`func (o *V1DocumentAllOf) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1DocumentAllOf) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1DocumentAllOf) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1DocumentAllOf) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetOrgId

`func (o *V1DocumentAllOf) GetOrgId() int64`

GetOrgId returns the OrgId field if non-nil, zero value otherwise.

### GetOrgIdOk

`func (o *V1DocumentAllOf) GetOrgIdOk() (int64, bool)`

GetOrgIdOk returns a tuple with the OrgId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOrgId

`func (o *V1DocumentAllOf) HasOrgId() bool`

HasOrgId returns a boolean if a field has been set.

### SetOrgId

`func (o *V1DocumentAllOf) SetOrgId(v int64)`

SetOrgId gets a reference to the given int64 and assigns it to the OrgId field.

### GetServerCreatedAtMs

`func (o *V1DocumentAllOf) GetServerCreatedAtMs() int64`

GetServerCreatedAtMs returns the ServerCreatedAtMs field if non-nil, zero value otherwise.

### GetServerCreatedAtMsOk

`func (o *V1DocumentAllOf) GetServerCreatedAtMsOk() (int64, bool)`

GetServerCreatedAtMsOk returns a tuple with the ServerCreatedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasServerCreatedAtMs

`func (o *V1DocumentAllOf) HasServerCreatedAtMs() bool`

HasServerCreatedAtMs returns a boolean if a field has been set.

### SetServerCreatedAtMs

`func (o *V1DocumentAllOf) SetServerCreatedAtMs(v int64)`

SetServerCreatedAtMs gets a reference to the given int64 and assigns it to the ServerCreatedAtMs field.

### GetServerUpdatedAtMs

`func (o *V1DocumentAllOf) GetServerUpdatedAtMs() int64`

GetServerUpdatedAtMs returns the ServerUpdatedAtMs field if non-nil, zero value otherwise.

### GetServerUpdatedAtMsOk

`func (o *V1DocumentAllOf) GetServerUpdatedAtMsOk() (int64, bool)`

GetServerUpdatedAtMsOk returns a tuple with the ServerUpdatedAtMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasServerUpdatedAtMs

`func (o *V1DocumentAllOf) HasServerUpdatedAtMs() bool`

HasServerUpdatedAtMs returns a boolean if a field has been set.

### SetServerUpdatedAtMs

`func (o *V1DocumentAllOf) SetServerUpdatedAtMs(v int64)`

SetServerUpdatedAtMs gets a reference to the given int64 and assigns it to the ServerUpdatedAtMs field.

### GetVehicleId

`func (o *V1DocumentAllOf) GetVehicleId() int64`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1DocumentAllOf) GetVehicleIdOk() (int64, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1DocumentAllOf) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1DocumentAllOf) SetVehicleId(v int64)`

SetVehicleId gets a reference to the given int64 and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


