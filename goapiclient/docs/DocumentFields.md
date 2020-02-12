# DocumentFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FieldType** | Pointer to **string** | The type of the field in the document. | [optional] 
**Label** | Pointer to **string** | Descriptive name of this field. | [optional] 
**Value** | Pointer to **string** | The shape of the value property depends on the fieldType selected.  - fieldType &#x60;string&#x60;: returns a string (e.g. &#x60;\&quot;hello\&quot;&#x60;).  - fieldType &#x60;number&#x60;: returns a number (e.g. &#x60;100&#x60;).  - fieldType &#x60;signature&#x60;: returns an array of signature objects where each object contains the &#x60;name&#x60;, &#x60;signedAtTime&#x60;, and &#x60;signatureUrl&#x60; properties for a signature. Example:  &#x60;&#x60;&#x60;json [   {     \&quot;name\&quot;: \&quot;John Smith\&quot;,     \&quot;signedAtTime\&quot;: \&quot;2006-01-02T15:04:05Z07:00\&quot;,     \&quot;signatureUrl\&quot;: \&quot;https://www.samsara.com/signature1\&quot;   } ] &#x60;&#x60;&#x60;  The &#x60;name&#x60; property returns the name of the signee in string format (e.g. John Smith). The &#x60;signedAtTime&#x60; property returns the time the signature was created in string format, following RFC 3339 standard (e.g. &#x60;\&quot;2006-01-02T15:04:05Z07:00\&quot;&#x60;). The &#x60;signatureUrl&#x60; property returns a string URL to get the signature data in base64 format (e.g. &#x60;\&quot;https://www.samsara.com/signature1\&quot;&#x60;).  - fieldType &#x60;photo&#x60;: returns an array of photo objects where each object contains a &#x60;url&#x60; property for a photo. The &#x60;url&#x60; property returns a string URL for a JPG image (e.g. &#x60;\&quot;https://www.samsara.com/photo1\&quot;&#x60;).  - fieldType &#x60;multipleChoiceField&#x60;: returns an array of multiple choice objects where each object contains the &#x60;selected&#x60; and &#x60;label&#x60; properties for a multiple choice field item. The &#x60;selected&#x60; property indicates whether the multiple choice field is selected and returns a boolean value (e.g. &#x60;false&#x60;). The &#x60;label&#x60; property describes the multiple choice field and returns a string value (e.g. &#x60;\&quot;Answer choice 1\&quot;&#x60;). | [optional] 

## Methods

### GetFieldType

`func (o *DocumentFields) GetFieldType() string`

GetFieldType returns the FieldType field if non-nil, zero value otherwise.

### GetFieldTypeOk

`func (o *DocumentFields) GetFieldTypeOk() (string, bool)`

GetFieldTypeOk returns a tuple with the FieldType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasFieldType

`func (o *DocumentFields) HasFieldType() bool`

HasFieldType returns a boolean if a field has been set.

### SetFieldType

`func (o *DocumentFields) SetFieldType(v string)`

SetFieldType gets a reference to the given string and assigns it to the FieldType field.

### GetLabel

`func (o *DocumentFields) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *DocumentFields) GetLabelOk() (string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLabel

`func (o *DocumentFields) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### SetLabel

`func (o *DocumentFields) SetLabel(v string)`

SetLabel gets a reference to the given string and assigns it to the Label field.

### GetValue

`func (o *DocumentFields) GetValue() string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *DocumentFields) GetValueOk() (string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasValue

`func (o *DocumentFields) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValue

`func (o *DocumentFields) SetValue(v string)`

SetValue gets a reference to the given string and assigns it to the Value field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


