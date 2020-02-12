# Document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CreatedAtTime** | Pointer to **string** | Time the document was created in RFC 3339 format. | [optional] 
**DocumentType** | Pointer to [**DocumentTypeTinyResponse**](documentTypeTinyResponse.md) |  | [optional] 
**Driver** | Pointer to [**DriverTinyResponse**](driverTinyResponse.md) |  | [optional] 
**Fields** | Pointer to [**[]DocumentFields**](Document_fields.md) | The fields associated with this document. | [optional] 
**Id** | Pointer to **string** | Unique Samsara UUID for the document | [optional] 
**Notes** | Pointer to **string** | Notes on the document. | [optional] 
**RouteStop** | Pointer to [**RouteStopTinyResponse**](routeStopTinyResponse.md) |  | [optional] 
**State** | Pointer to **string** | The condition of the document created for the driver. Can be either &#x60;required&#x60; or &#x60;submitted&#x60;, if no value is specified, &#x60;state&#x60; defaults to &#x60;required&#x60;. &#x60;required&#x60; documents are pre-populated documents for the Driver to fill out in the Driver App. | [optional] [default to STATE_REQUIRED]
**UpdatedAtTime** | Pointer to **string** | Time the document was updated in RFC 3339 format. | [optional] 
**Vehicle** | Pointer to [**VehicleTinyResponse**](vehicleTinyResponse.md) |  | [optional] 

## Methods

### GetCreatedAtTime

`func (o *Document) GetCreatedAtTime() string`

GetCreatedAtTime returns the CreatedAtTime field if non-nil, zero value otherwise.

### GetCreatedAtTimeOk

`func (o *Document) GetCreatedAtTimeOk() (string, bool)`

GetCreatedAtTimeOk returns a tuple with the CreatedAtTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasCreatedAtTime

`func (o *Document) HasCreatedAtTime() bool`

HasCreatedAtTime returns a boolean if a field has been set.

### SetCreatedAtTime

`func (o *Document) SetCreatedAtTime(v string)`

SetCreatedAtTime gets a reference to the given string and assigns it to the CreatedAtTime field.

### GetDocumentType

`func (o *Document) GetDocumentType() DocumentTypeTinyResponse`

GetDocumentType returns the DocumentType field if non-nil, zero value otherwise.

### GetDocumentTypeOk

`func (o *Document) GetDocumentTypeOk() (DocumentTypeTinyResponse, bool)`

GetDocumentTypeOk returns a tuple with the DocumentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDocumentType

`func (o *Document) HasDocumentType() bool`

HasDocumentType returns a boolean if a field has been set.

### SetDocumentType

`func (o *Document) SetDocumentType(v DocumentTypeTinyResponse)`

SetDocumentType gets a reference to the given DocumentTypeTinyResponse and assigns it to the DocumentType field.

### GetDriver

`func (o *Document) GetDriver() DriverTinyResponse`

GetDriver returns the Driver field if non-nil, zero value otherwise.

### GetDriverOk

`func (o *Document) GetDriverOk() (DriverTinyResponse, bool)`

GetDriverOk returns a tuple with the Driver field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriver

`func (o *Document) HasDriver() bool`

HasDriver returns a boolean if a field has been set.

### SetDriver

`func (o *Document) SetDriver(v DriverTinyResponse)`

SetDriver gets a reference to the given DriverTinyResponse and assigns it to the Driver field.

### GetFields

`func (o *Document) GetFields() []DocumentFields`

GetFields returns the Fields field if non-nil, zero value otherwise.

### GetFieldsOk

`func (o *Document) GetFieldsOk() ([]DocumentFields, bool)`

GetFieldsOk returns a tuple with the Fields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFields

`func (o *Document) HasFields() bool`

HasFields returns a boolean if a field has been set.

### SetFields

`func (o *Document) SetFields(v []DocumentFields)`

SetFields gets a reference to the given []DocumentFields and assigns it to the Fields field.

### GetId

`func (o *Document) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Document) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *Document) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *Document) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetNotes

`func (o *Document) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *Document) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *Document) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *Document) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetRouteStop

`func (o *Document) GetRouteStop() RouteStopTinyResponse`

GetRouteStop returns the RouteStop field if non-nil, zero value otherwise.

### GetRouteStopOk

`func (o *Document) GetRouteStopOk() (RouteStopTinyResponse, bool)`

GetRouteStopOk returns a tuple with the RouteStop field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasRouteStop

`func (o *Document) HasRouteStop() bool`

HasRouteStop returns a boolean if a field has been set.

### SetRouteStop

`func (o *Document) SetRouteStop(v RouteStopTinyResponse)`

SetRouteStop gets a reference to the given RouteStopTinyResponse and assigns it to the RouteStop field.

### GetState

`func (o *Document) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *Document) GetStateOk() (string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasState

`func (o *Document) HasState() bool`

HasState returns a boolean if a field has been set.

### SetState

`func (o *Document) SetState(v string)`

SetState gets a reference to the given string and assigns it to the State field.

### GetUpdatedAtTime

`func (o *Document) GetUpdatedAtTime() string`

GetUpdatedAtTime returns the UpdatedAtTime field if non-nil, zero value otherwise.

### GetUpdatedAtTimeOk

`func (o *Document) GetUpdatedAtTimeOk() (string, bool)`

GetUpdatedAtTimeOk returns a tuple with the UpdatedAtTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasUpdatedAtTime

`func (o *Document) HasUpdatedAtTime() bool`

HasUpdatedAtTime returns a boolean if a field has been set.

### SetUpdatedAtTime

`func (o *Document) SetUpdatedAtTime(v string)`

SetUpdatedAtTime gets a reference to the given string and assigns it to the UpdatedAtTime field.

### GetVehicle

`func (o *Document) GetVehicle() VehicleTinyResponse`

GetVehicle returns the Vehicle field if non-nil, zero value otherwise.

### GetVehicleOk

`func (o *Document) GetVehicleOk() (VehicleTinyResponse, bool)`

GetVehicleOk returns a tuple with the Vehicle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicle

`func (o *Document) HasVehicle() bool`

HasVehicle returns a boolean if a field has been set.

### SetVehicle

`func (o *Document) SetVehicle(v VehicleTinyResponse)`

SetVehicle gets a reference to the given VehicleTinyResponse and assigns it to the Vehicle field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


