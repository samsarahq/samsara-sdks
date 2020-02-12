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

// V1VehicleHarshEventResponseLocation struct for V1VehicleHarshEventResponseLocation
type V1VehicleHarshEventResponseLocation struct {
	// Address of location where the harsh event occurred
	Address *string `json:"address,omitempty"`
	// Latitude of location where the harsh event occurred
	Latitude *float32 `json:"latitude,omitempty"`
	// Longitude of location where the harsh event occurred
	Longitude *float32 `json:"longitude,omitempty"`
}

// GetAddress returns the Address field value if set, zero value otherwise.
func (o *V1VehicleHarshEventResponseLocation) GetAddress() string {
	if o == nil || o.Address == nil {
		var ret string
		return ret
	}
	return *o.Address
}

// GetAddressOk returns a tuple with the Address field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1VehicleHarshEventResponseLocation) GetAddressOk() (string, bool) {
	if o == nil || o.Address == nil {
		var ret string
		return ret, false
	}
	return *o.Address, true
}

// HasAddress returns a boolean if a field has been set.
func (o *V1VehicleHarshEventResponseLocation) HasAddress() bool {
	if o != nil && o.Address != nil {
		return true
	}

	return false
}

// SetAddress gets a reference to the given string and assigns it to the Address field.
func (o *V1VehicleHarshEventResponseLocation) SetAddress(v string) {
	o.Address = &v
}

// GetLatitude returns the Latitude field value if set, zero value otherwise.
func (o *V1VehicleHarshEventResponseLocation) GetLatitude() float32 {
	if o == nil || o.Latitude == nil {
		var ret float32
		return ret
	}
	return *o.Latitude
}

// GetLatitudeOk returns a tuple with the Latitude field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1VehicleHarshEventResponseLocation) GetLatitudeOk() (float32, bool) {
	if o == nil || o.Latitude == nil {
		var ret float32
		return ret, false
	}
	return *o.Latitude, true
}

// HasLatitude returns a boolean if a field has been set.
func (o *V1VehicleHarshEventResponseLocation) HasLatitude() bool {
	if o != nil && o.Latitude != nil {
		return true
	}

	return false
}

// SetLatitude gets a reference to the given float32 and assigns it to the Latitude field.
func (o *V1VehicleHarshEventResponseLocation) SetLatitude(v float32) {
	o.Latitude = &v
}

// GetLongitude returns the Longitude field value if set, zero value otherwise.
func (o *V1VehicleHarshEventResponseLocation) GetLongitude() float32 {
	if o == nil || o.Longitude == nil {
		var ret float32
		return ret
	}
	return *o.Longitude
}

// GetLongitudeOk returns a tuple with the Longitude field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1VehicleHarshEventResponseLocation) GetLongitudeOk() (float32, bool) {
	if o == nil || o.Longitude == nil {
		var ret float32
		return ret, false
	}
	return *o.Longitude, true
}

// HasLongitude returns a boolean if a field has been set.
func (o *V1VehicleHarshEventResponseLocation) HasLongitude() bool {
	if o != nil && o.Longitude != nil {
		return true
	}

	return false
}

// SetLongitude gets a reference to the given float32 and assigns it to the Longitude field.
func (o *V1VehicleHarshEventResponseLocation) SetLongitude(v float32) {
	o.Longitude = &v
}

type NullableV1VehicleHarshEventResponseLocation struct {
	Value        V1VehicleHarshEventResponseLocation
	ExplicitNull bool
}

func (v NullableV1VehicleHarshEventResponseLocation) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableV1VehicleHarshEventResponseLocation) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}
