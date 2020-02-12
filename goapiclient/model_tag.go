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

// Tag struct for Tag
type Tag struct {
	// Unique Samsara ID of this tag.
	Id *string `json:"id,omitempty"`
	// Name of this tag.
	Name *string `json:"name,omitempty"`
	// The addresses that belong to this tag.
	Addresses *[]TaggedObject `json:"addresses,omitempty"`
	// The trailers, unpowered, and powered assets that belong to this tag.
	Assets *[]TaggedObject `json:"assets,omitempty"`
	// The drivers that belong to this tag.
	Drivers *[]TaggedObject `json:"drivers,omitempty"`
	// The machines that belong to thistag.
	Machines  *[]TaggedObject `json:"machines,omitempty"`
	ParentTag *ParentTag      `json:"parentTag,omitempty"`
	// The sensors that belong to this tag.
	Sensors *[]TaggedObject `json:"sensors,omitempty"`
	// The vehicles that belong to this tag.
	Vehicles *[]TaggedObject `json:"vehicles,omitempty"`
}

// GetId returns the Id field value if set, zero value otherwise.
func (o *Tag) GetId() string {
	if o == nil || o.Id == nil {
		var ret string
		return ret
	}
	return *o.Id
}

// GetIdOk returns a tuple with the Id field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Tag) GetIdOk() (string, bool) {
	if o == nil || o.Id == nil {
		var ret string
		return ret, false
	}
	return *o.Id, true
}

// HasId returns a boolean if a field has been set.
func (o *Tag) HasId() bool {
	if o != nil && o.Id != nil {
		return true
	}

	return false
}

// SetId gets a reference to the given string and assigns it to the Id field.
func (o *Tag) SetId(v string) {
	o.Id = &v
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *Tag) GetName() string {
	if o == nil || o.Name == nil {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Tag) GetNameOk() (string, bool) {
	if o == nil || o.Name == nil {
		var ret string
		return ret, false
	}
	return *o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *Tag) HasName() bool {
	if o != nil && o.Name != nil {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *Tag) SetName(v string) {
	o.Name = &v
}

// GetAddresses returns the Addresses field value if set, zero value otherwise.
func (o *Tag) GetAddresses() []TaggedObject {
	if o == nil || o.Addresses == nil {
		var ret []TaggedObject
		return ret
	}
	return *o.Addresses
}

// GetAddressesOk returns a tuple with the Addresses field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Tag) GetAddressesOk() ([]TaggedObject, bool) {
	if o == nil || o.Addresses == nil {
		var ret []TaggedObject
		return ret, false
	}
	return *o.Addresses, true
}

// HasAddresses returns a boolean if a field has been set.
func (o *Tag) HasAddresses() bool {
	if o != nil && o.Addresses != nil {
		return true
	}

	return false
}

// SetAddresses gets a reference to the given []TaggedObject and assigns it to the Addresses field.
func (o *Tag) SetAddresses(v []TaggedObject) {
	o.Addresses = &v
}

// GetAssets returns the Assets field value if set, zero value otherwise.
func (o *Tag) GetAssets() []TaggedObject {
	if o == nil || o.Assets == nil {
		var ret []TaggedObject
		return ret
	}
	return *o.Assets
}

// GetAssetsOk returns a tuple with the Assets field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Tag) GetAssetsOk() ([]TaggedObject, bool) {
	if o == nil || o.Assets == nil {
		var ret []TaggedObject
		return ret, false
	}
	return *o.Assets, true
}

// HasAssets returns a boolean if a field has been set.
func (o *Tag) HasAssets() bool {
	if o != nil && o.Assets != nil {
		return true
	}

	return false
}

// SetAssets gets a reference to the given []TaggedObject and assigns it to the Assets field.
func (o *Tag) SetAssets(v []TaggedObject) {
	o.Assets = &v
}

// GetDrivers returns the Drivers field value if set, zero value otherwise.
func (o *Tag) GetDrivers() []TaggedObject {
	if o == nil || o.Drivers == nil {
		var ret []TaggedObject
		return ret
	}
	return *o.Drivers
}

// GetDriversOk returns a tuple with the Drivers field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Tag) GetDriversOk() ([]TaggedObject, bool) {
	if o == nil || o.Drivers == nil {
		var ret []TaggedObject
		return ret, false
	}
	return *o.Drivers, true
}

// HasDrivers returns a boolean if a field has been set.
func (o *Tag) HasDrivers() bool {
	if o != nil && o.Drivers != nil {
		return true
	}

	return false
}

// SetDrivers gets a reference to the given []TaggedObject and assigns it to the Drivers field.
func (o *Tag) SetDrivers(v []TaggedObject) {
	o.Drivers = &v
}

// GetMachines returns the Machines field value if set, zero value otherwise.
func (o *Tag) GetMachines() []TaggedObject {
	if o == nil || o.Machines == nil {
		var ret []TaggedObject
		return ret
	}
	return *o.Machines
}

// GetMachinesOk returns a tuple with the Machines field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Tag) GetMachinesOk() ([]TaggedObject, bool) {
	if o == nil || o.Machines == nil {
		var ret []TaggedObject
		return ret, false
	}
	return *o.Machines, true
}

// HasMachines returns a boolean if a field has been set.
func (o *Tag) HasMachines() bool {
	if o != nil && o.Machines != nil {
		return true
	}

	return false
}

// SetMachines gets a reference to the given []TaggedObject and assigns it to the Machines field.
func (o *Tag) SetMachines(v []TaggedObject) {
	o.Machines = &v
}

// GetParentTag returns the ParentTag field value if set, zero value otherwise.
func (o *Tag) GetParentTag() ParentTag {
	if o == nil || o.ParentTag == nil {
		var ret ParentTag
		return ret
	}
	return *o.ParentTag
}

// GetParentTagOk returns a tuple with the ParentTag field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Tag) GetParentTagOk() (ParentTag, bool) {
	if o == nil || o.ParentTag == nil {
		var ret ParentTag
		return ret, false
	}
	return *o.ParentTag, true
}

// HasParentTag returns a boolean if a field has been set.
func (o *Tag) HasParentTag() bool {
	if o != nil && o.ParentTag != nil {
		return true
	}

	return false
}

// SetParentTag gets a reference to the given ParentTag and assigns it to the ParentTag field.
func (o *Tag) SetParentTag(v ParentTag) {
	o.ParentTag = &v
}

// GetSensors returns the Sensors field value if set, zero value otherwise.
func (o *Tag) GetSensors() []TaggedObject {
	if o == nil || o.Sensors == nil {
		var ret []TaggedObject
		return ret
	}
	return *o.Sensors
}

// GetSensorsOk returns a tuple with the Sensors field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Tag) GetSensorsOk() ([]TaggedObject, bool) {
	if o == nil || o.Sensors == nil {
		var ret []TaggedObject
		return ret, false
	}
	return *o.Sensors, true
}

// HasSensors returns a boolean if a field has been set.
func (o *Tag) HasSensors() bool {
	if o != nil && o.Sensors != nil {
		return true
	}

	return false
}

// SetSensors gets a reference to the given []TaggedObject and assigns it to the Sensors field.
func (o *Tag) SetSensors(v []TaggedObject) {
	o.Sensors = &v
}

// GetVehicles returns the Vehicles field value if set, zero value otherwise.
func (o *Tag) GetVehicles() []TaggedObject {
	if o == nil || o.Vehicles == nil {
		var ret []TaggedObject
		return ret
	}
	return *o.Vehicles
}

// GetVehiclesOk returns a tuple with the Vehicles field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Tag) GetVehiclesOk() ([]TaggedObject, bool) {
	if o == nil || o.Vehicles == nil {
		var ret []TaggedObject
		return ret, false
	}
	return *o.Vehicles, true
}

// HasVehicles returns a boolean if a field has been set.
func (o *Tag) HasVehicles() bool {
	if o != nil && o.Vehicles != nil {
		return true
	}

	return false
}

// SetVehicles gets a reference to the given []TaggedObject and assigns it to the Vehicles field.
func (o *Tag) SetVehicles(v []TaggedObject) {
	o.Vehicles = &v
}

type NullableTag struct {
	Value        Tag
	ExplicitNull bool
}

func (v NullableTag) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableTag) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}
