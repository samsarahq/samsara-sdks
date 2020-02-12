/*
 * Samsara API
 *
 * <style type=\"text/css\"> n {     padding: 1em;     width: 100%;     display: block;     margin: 28px 0; } n.info {     background-color: rgba(0, 51, 160, 0.1); } n.warning {     background-color: #fdf6e3; } i:before {     margin-right: 6px; } nh {     font-size: 1.5rem;     font-weight: 700;     line-height: 1.1;     display: block; } nb {     margin-top: 10px;     padding-left: 22px;     display: block; } </style>  # Overview  <n class=\"info\"> <nh> <i class=\"fa fa-info-circle\"></i> Something new! </nh> <nb> Welcome Samsara's new and improved API. Check out our FAQ [here](https://developers.samsara.com/docs/introducing-our-next-generation-api) to see what's changed and learn how to get started.<br> <br> Want to access the legacy API docs? You can find them [here](https://www.samsara.com/api-legacy).<br> <br> *Note: Because this is a new set of APIs, we have not transitioned all endpoints over to this standard. Endpoints that still use the legacy standards are indicated in the reference documentation. If you can't find an API that you're looking for, we encourage you to look for it in our [legacy API docs](https://www.samsara.com/api-legacy) as we continue to transition all endpoints over. Check back here for updates!*<br> <br> Submit your feedback [here](https://forms.gle/r4bs6HQshQAvBuwv6)! </nb> </n>  Samsara provides API endpoints so that you can build powerful applications and custom solutions with sensor data. Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets.  The Samsara API is a [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer). It uses standard [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) authentication, verbs, and response codes, and it returns [JSON](http://www.json.org/) response bodies. If you're familiar with what you can build with a REST API, then this will be your go-to API reference.  Visit [developers.samsara.com](https://developers.samsara.com) to find getting started guides and an API overview.  If you have any questions, reach out to us at [support@samsara.com](mailto:support@samsara.com).  ## Endpoints  All our APIs can be accessed through HTTP requests to URLs like:  ``` https://api.samsara.com/<endpoint> ```  For EU customers, this URL will be:  ``` https://api.eu.samsara.com/<endpoint> ```  <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> Note </nh> <nb> Legacy endpoints will have the URL: `https://api.samsara.com/v1/<endpoint>` or `https://api.eu.samsara.com/v1/<endpoint>` </nb> </n>  ## Authentication  To authenticate your API request you will need to include your secret token. You can manage your API tokens in the [Dashboard](https://cloud.samsara.com). They are visible under `Settings->Organization->API Tokens`.  Your API tokens carry many privileges, so be sure to keep them secure. Do not share your secret API tokens in publicly accessible areas such as GitHub, client-side code, and so on.  Authentication to the API is performed via Bearer Token in the HTTP Authorization header. Provide your API token as the `access_token` value in an `Authorization: Bearer` header. You do not need to provide a password:  ```curl Authorization: Bearer {access_token} ```  All API requests must be made over [HTTPS](https://en.wikipedia.org/wiki/HTTPS). Calls made over plain HTTP or without authentication will fail.  ## Common Patterns  You can find more info about request methods, response codes, error codes, versioning, pagination, timestamps, and mini-objects [here](https://developers.samsara.com/docs/common-structures).
 *
 * API version: 2019-12-12
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package goapiclient

import (
	"bytes"
	"encoding/json"
)

// DocumentCreateFields item
type DocumentCreateFields struct {
	// The type of the field in the document.
	FieldType *string `json:"fieldType,omitempty"`
	// Descriptive name of this field.
	Label *string `json:"label,omitempty"`
	// The shape of the value property depends on the fieldType selected.  - fieldType `string`: returns a string (e.g. `\"hello\"`).  - fieldType `number`: returns a number (e.g. `100`).  - fieldType `signature`: returns an array of signature objects where each object contains the `name`, `signedAtTime`, and `signatureUrl` properties for a signature. Example:  ```json [   {     \"name\": \"John Smith\",     \"signedAtTime\": \"2006-01-02T15:04:05Z07:00\",     \"signatureUrl\": \"https://www.samsara.com/signature1\"   } ] ```  The `name` property returns the name of the signee in string format (e.g. John Smith). The `signedAtTime` property returns the time the signature was created in string format, following RFC 3339 standard (e.g. `\"2006-01-02T15:04:05Z07:00\"`). The `signatureUrl` property returns a string URL to get the signature data in base64 format (e.g. `\"https://www.samsara.com/signature1\"`).  - fieldType `photo`: returns an array of photo objects where each object contains a `url` property for a photo. The `url` property returns a string URL for a JPG image (e.g. `\"https://www.samsara.com/photo1\"`).  - fieldType `multipleChoice`: returns an array of multiple choice objects where each object contains the `selected` and `label` properties for a multiple choice field item. The `selected` property indicates whether the multiple choice field is selected and returns a boolean value (e.g. `false`). The `label` property describes the multiple choice field and returns a string value (e.g. `\"Answer choice 1\"`).  - fieldType `dateTime`: returns a string with the timestamp in RFC 3339 format.
	Value *string `json:"value,omitempty"`
}

// GetFieldType returns the FieldType field value if set, zero value otherwise.
func (o *DocumentCreateFields) GetFieldType() string {
	if o == nil || o.FieldType == nil {
		var ret string
		return ret
	}
	return *o.FieldType
}

// GetFieldTypeOk returns a tuple with the FieldType field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DocumentCreateFields) GetFieldTypeOk() (string, bool) {
	if o == nil || o.FieldType == nil {
		var ret string
		return ret, false
	}
	return *o.FieldType, true
}

// HasFieldType returns a boolean if a field has been set.
func (o *DocumentCreateFields) HasFieldType() bool {
	if o != nil && o.FieldType != nil {
		return true
	}

	return false
}

// SetFieldType gets a reference to the given string and assigns it to the FieldType field.
func (o *DocumentCreateFields) SetFieldType(v string) {
	o.FieldType = &v
}

// GetLabel returns the Label field value if set, zero value otherwise.
func (o *DocumentCreateFields) GetLabel() string {
	if o == nil || o.Label == nil {
		var ret string
		return ret
	}
	return *o.Label
}

// GetLabelOk returns a tuple with the Label field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DocumentCreateFields) GetLabelOk() (string, bool) {
	if o == nil || o.Label == nil {
		var ret string
		return ret, false
	}
	return *o.Label, true
}

// HasLabel returns a boolean if a field has been set.
func (o *DocumentCreateFields) HasLabel() bool {
	if o != nil && o.Label != nil {
		return true
	}

	return false
}

// SetLabel gets a reference to the given string and assigns it to the Label field.
func (o *DocumentCreateFields) SetLabel(v string) {
	o.Label = &v
}

// GetValue returns the Value field value if set, zero value otherwise.
func (o *DocumentCreateFields) GetValue() string {
	if o == nil || o.Value == nil {
		var ret string
		return ret
	}
	return *o.Value
}

// GetValueOk returns a tuple with the Value field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DocumentCreateFields) GetValueOk() (string, bool) {
	if o == nil || o.Value == nil {
		var ret string
		return ret, false
	}
	return *o.Value, true
}

// HasValue returns a boolean if a field has been set.
func (o *DocumentCreateFields) HasValue() bool {
	if o != nil && o.Value != nil {
		return true
	}

	return false
}

// SetValue gets a reference to the given string and assigns it to the Value field.
func (o *DocumentCreateFields) SetValue(v string) {
	o.Value = &v
}

type NullableDocumentCreateFields struct {
	Value        DocumentCreateFields
	ExplicitNull bool
}

func (v NullableDocumentCreateFields) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableDocumentCreateFields) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}
