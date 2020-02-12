# WebhookCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EventType** | Pointer to **string** | The eventType that will trigger this webhook. | 
**Name** | Pointer to **string** | The name of the webhook. | 
**Url** | Pointer to **string** | The URL of the webserver endpoint that the webhook payload should be sent to. Must be a https URL. | 

## Methods

### GetEventType

`func (o *WebhookCreate) GetEventType() string`

GetEventType returns the EventType field if non-nil, zero value otherwise.

### GetEventTypeOk

`func (o *WebhookCreate) GetEventTypeOk() (string, bool)`

GetEventTypeOk returns a tuple with the EventType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasEventType

`func (o *WebhookCreate) HasEventType() bool`

HasEventType returns a boolean if a field has been set.

### SetEventType

`func (o *WebhookCreate) SetEventType(v string)`

SetEventType gets a reference to the given string and assigns it to the EventType field.

### GetName

`func (o *WebhookCreate) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *WebhookCreate) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *WebhookCreate) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *WebhookCreate) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetUrl

`func (o *WebhookCreate) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *WebhookCreate) GetUrlOk() (string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasUrl

`func (o *WebhookCreate) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### SetUrl

`func (o *WebhookCreate) SetUrl(v string)`

SetUrl gets a reference to the given string and assigns it to the Url field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


