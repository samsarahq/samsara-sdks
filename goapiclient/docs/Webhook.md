# Webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EventType** | Pointer to **string** | The eventType that will trigger this webhook. | 
**Id** | Pointer to **string** | A unique identifier for the webhook. | 
**Name** | Pointer to **string** | The name of the webhook. | 
**Secret** | Pointer to **string** | The secret that this webhook is signed with. | 
**Url** | Pointer to **string** | The URL of the webserver endpoint that the webhook payload should be sent to. Must be a https URL. | 

## Methods

### GetEventType

`func (o *Webhook) GetEventType() string`

GetEventType returns the EventType field if non-nil, zero value otherwise.

### GetEventTypeOk

`func (o *Webhook) GetEventTypeOk() (string, bool)`

GetEventTypeOk returns a tuple with the EventType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEventType

`func (o *Webhook) HasEventType() bool`

HasEventType returns a boolean if a field has been set.

### SetEventType

`func (o *Webhook) SetEventType(v string)`

SetEventType gets a reference to the given string and assigns it to the EventType field.

### GetId

`func (o *Webhook) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Webhook) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *Webhook) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *Webhook) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetName

`func (o *Webhook) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Webhook) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *Webhook) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *Webhook) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetSecret

`func (o *Webhook) GetSecret() string`

GetSecret returns the Secret field if non-nil, zero value otherwise.

### GetSecretOk

`func (o *Webhook) GetSecretOk() (string, bool)`

GetSecretOk returns a tuple with the Secret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSecret

`func (o *Webhook) HasSecret() bool`

HasSecret returns a boolean if a field has been set.

### SetSecret

`func (o *Webhook) SetSecret(v string)`

SetSecret gets a reference to the given string and assigns it to the Secret field.

### GetUrl

`func (o *Webhook) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *Webhook) GetUrlOk() (string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasUrl

`func (o *Webhook) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### SetUrl

`func (o *Webhook) SetUrl(v string)`

SetUrl gets a reference to the given string and assigns it to the Url field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


