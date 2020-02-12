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

// V1CargoResponseSensors struct for V1CargoResponseSensors
type V1CargoResponseSensors struct {
	// Flag indicating whether the current cargo is empty or loaded.
	CargoEmpty *bool `json:"cargoEmpty,omitempty"`
	// The timestamp of reported cargo status, specified in RFC 3339 time.
	CargoStatusTime *string `json:"cargoStatusTime,omitempty"`
	// ID of the sensor.
	Id *int64 `json:"id,omitempty"`
	// Name of the sensor.
	Name *string `json:"name,omitempty"`
	// ID of the trailer associated with the sensor for the data point. If no trailer is connected, this parameter will not be reported.
	TrailerId *int32 `json:"trailerId,omitempty"`
	// ID of the vehicle associated with the sensor for the data point. If no vehicle is connected, this parameter will not be reported.
	VehicleId *int32 `json:"vehicleId,omitempty"`
}

// GetCargoEmpty returns the CargoEmpty field value if set, zero value otherwise.
func (o *V1CargoResponseSensors) GetCargoEmpty() bool {
	if o == nil || o.CargoEmpty == nil {
		var ret bool
		return ret
	}
	return *o.CargoEmpty
}

// GetCargoEmptyOk returns a tuple with the CargoEmpty field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1CargoResponseSensors) GetCargoEmptyOk() (bool, bool) {
	if o == nil || o.CargoEmpty == nil {
		var ret bool
		return ret, false
	}
	return *o.CargoEmpty, true
}

// HasCargoEmpty returns a boolean if a field has been set.
func (o *V1CargoResponseSensors) HasCargoEmpty() bool {
	if o != nil && o.CargoEmpty != nil {
		return true
	}

	return false
}

// SetCargoEmpty gets a reference to the given bool and assigns it to the CargoEmpty field.
func (o *V1CargoResponseSensors) SetCargoEmpty(v bool) {
	o.CargoEmpty = &v
}

// GetCargoStatusTime returns the CargoStatusTime field value if set, zero value otherwise.
func (o *V1CargoResponseSensors) GetCargoStatusTime() string {
	if o == nil || o.CargoStatusTime == nil {
		var ret string
		return ret
	}
	return *o.CargoStatusTime
}

// GetCargoStatusTimeOk returns a tuple with the CargoStatusTime field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1CargoResponseSensors) GetCargoStatusTimeOk() (string, bool) {
	if o == nil || o.CargoStatusTime == nil {
		var ret string
		return ret, false
	}
	return *o.CargoStatusTime, true
}

// HasCargoStatusTime returns a boolean if a field has been set.
func (o *V1CargoResponseSensors) HasCargoStatusTime() bool {
	if o != nil && o.CargoStatusTime != nil {
		return true
	}

	return false
}

// SetCargoStatusTime gets a reference to the given string and assigns it to the CargoStatusTime field.
func (o *V1CargoResponseSensors) SetCargoStatusTime(v string) {
	o.CargoStatusTime = &v
}

// GetId returns the Id field value if set, zero value otherwise.
func (o *V1CargoResponseSensors) GetId() int64 {
	if o == nil || o.Id == nil {
		var ret int64
		return ret
	}
	return *o.Id
}

// GetIdOk returns a tuple with the Id field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1CargoResponseSensors) GetIdOk() (int64, bool) {
	if o == nil || o.Id == nil {
		var ret int64
		return ret, false
	}
	return *o.Id, true
}

// HasId returns a boolean if a field has been set.
func (o *V1CargoResponseSensors) HasId() bool {
	if o != nil && o.Id != nil {
		return true
	}

	return false
}

// SetId gets a reference to the given int64 and assigns it to the Id field.
func (o *V1CargoResponseSensors) SetId(v int64) {
	o.Id = &v
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *V1CargoResponseSensors) GetName() string {
	if o == nil || o.Name == nil {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1CargoResponseSensors) GetNameOk() (string, bool) {
	if o == nil || o.Name == nil {
		var ret string
		return ret, false
	}
	return *o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *V1CargoResponseSensors) HasName() bool {
	if o != nil && o.Name != nil {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *V1CargoResponseSensors) SetName(v string) {
	o.Name = &v
}

// GetTrailerId returns the TrailerId field value if set, zero value otherwise.
func (o *V1CargoResponseSensors) GetTrailerId() int32 {
	if o == nil || o.TrailerId == nil {
		var ret int32
		return ret
	}
	return *o.TrailerId
}

// GetTrailerIdOk returns a tuple with the TrailerId field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1CargoResponseSensors) GetTrailerIdOk() (int32, bool) {
	if o == nil || o.TrailerId == nil {
		var ret int32
		return ret, false
	}
	return *o.TrailerId, true
}

// HasTrailerId returns a boolean if a field has been set.
func (o *V1CargoResponseSensors) HasTrailerId() bool {
	if o != nil && o.TrailerId != nil {
		return true
	}

	return false
}

// SetTrailerId gets a reference to the given int32 and assigns it to the TrailerId field.
func (o *V1CargoResponseSensors) SetTrailerId(v int32) {
	o.TrailerId = &v
}

// GetVehicleId returns the VehicleId field value if set, zero value otherwise.
func (o *V1CargoResponseSensors) GetVehicleId() int32 {
	if o == nil || o.VehicleId == nil {
		var ret int32
		return ret
	}
	return *o.VehicleId
}

// GetVehicleIdOk returns a tuple with the VehicleId field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1CargoResponseSensors) GetVehicleIdOk() (int32, bool) {
	if o == nil || o.VehicleId == nil {
		var ret int32
		return ret, false
	}
	return *o.VehicleId, true
}

// HasVehicleId returns a boolean if a field has been set.
func (o *V1CargoResponseSensors) HasVehicleId() bool {
	if o != nil && o.VehicleId != nil {
		return true
	}

	return false
}

// SetVehicleId gets a reference to the given int32 and assigns it to the VehicleId field.
func (o *V1CargoResponseSensors) SetVehicleId(v int32) {
	o.VehicleId = &v
}

type NullableV1CargoResponseSensors struct {
	Value        V1CargoResponseSensors
	ExplicitNull bool
}

func (v NullableV1CargoResponseSensors) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableV1CargoResponseSensors) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}
