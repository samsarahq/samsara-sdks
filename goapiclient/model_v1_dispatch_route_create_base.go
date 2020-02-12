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

// V1DispatchRouteCreateBase struct for V1DispatchRouteCreateBase
type V1DispatchRouteCreateBase struct {
	// ID of the driver assigned to the dispatch route. Note that driver_id and vehicle_id are mutually exclusive. If neither is specified, then the route is unassigned.
	DriverId *int64 `json:"driver_id,omitempty"`
	// Descriptive name of this route.
	Name string `json:"name"`
	// Notes regarding the details of this route; maximum of 2000 characters; newline characters ('\\n')can be used for formatting.
	Notes *string `json:"notes,omitempty"`
	// The time in Unix epoch milliseconds that the last job in the route is scheduled to end.
	ScheduledEndMs *int64 `json:"scheduled_end_ms,omitempty"`
	// The distance expected to be traveled for this route in meters.
	ScheduledMeters *int64 `json:"scheduled_meters,omitempty"`
	// The time in Unix epoch milliseconds that the route is scheduled to start.
	ScheduledStartMs int64 `json:"scheduled_start_ms"`
	// The address of the route's starting location, as it would be recognized if provided to maps.google.com. Optional if a valid start location address ID is provided.
	StartLocationAddress *string `json:"start_location_address,omitempty"`
	// ID of the start location associated with an address book entry. Optional if valid values are provided for start location address and latitude/longitude. If a valid start location address ID is provided, address/latitude/longitude will be used from the address book entry. Name of the address book entry will only be used if the start location name is not provided.
	StartLocationAddressId *int64 `json:"start_location_address_id,omitempty"`
	// Latitude of the start location in decimal degrees. Optional if a valid start location address ID is provided.
	StartLocationLat *float64 `json:"start_location_lat,omitempty"`
	// Longitude of the start location in decimal degrees. Optional if a valid start location address ID is provided.
	StartLocationLng *float64 `json:"start_location_lng,omitempty"`
	// The name of the route's starting location. If provided, it will take precedence over the name of the address book entry.
	StartLocationName *string `json:"start_location_name,omitempty"`
	// ID of the trailer assigned to the dispatch route. Note that trailers can only be assigned to routes that have a Vehicle or Driver assigned to them.
	TrailerId *int64 `json:"trailer_id,omitempty"`
	// ID of the vehicle assigned to the dispatch route. Note that vehicle_id and driver_id are mutually exclusive. If neither is specified, then the route is unassigned.
	VehicleId *int64 `json:"vehicle_id,omitempty"`
}

// GetDriverId returns the DriverId field value if set, zero value otherwise.
func (o *V1DispatchRouteCreateBase) GetDriverId() int64 {
	if o == nil || o.DriverId == nil {
		var ret int64
		return ret
	}
	return *o.DriverId
}

// GetDriverIdOk returns a tuple with the DriverId field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1DispatchRouteCreateBase) GetDriverIdOk() (int64, bool) {
	if o == nil || o.DriverId == nil {
		var ret int64
		return ret, false
	}
	return *o.DriverId, true
}

// HasDriverId returns a boolean if a field has been set.
func (o *V1DispatchRouteCreateBase) HasDriverId() bool {
	if o != nil && o.DriverId != nil {
		return true
	}

	return false
}

// SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.
func (o *V1DispatchRouteCreateBase) SetDriverId(v int64) {
	o.DriverId = &v
}

// GetName returns the Name field value
func (o *V1DispatchRouteCreateBase) GetName() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Name
}

// SetName sets field value
func (o *V1DispatchRouteCreateBase) SetName(v string) {
	o.Name = v
}

// GetNotes returns the Notes field value if set, zero value otherwise.
func (o *V1DispatchRouteCreateBase) GetNotes() string {
	if o == nil || o.Notes == nil {
		var ret string
		return ret
	}
	return *o.Notes
}

// GetNotesOk returns a tuple with the Notes field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1DispatchRouteCreateBase) GetNotesOk() (string, bool) {
	if o == nil || o.Notes == nil {
		var ret string
		return ret, false
	}
	return *o.Notes, true
}

// HasNotes returns a boolean if a field has been set.
func (o *V1DispatchRouteCreateBase) HasNotes() bool {
	if o != nil && o.Notes != nil {
		return true
	}

	return false
}

// SetNotes gets a reference to the given string and assigns it to the Notes field.
func (o *V1DispatchRouteCreateBase) SetNotes(v string) {
	o.Notes = &v
}

// GetScheduledEndMs returns the ScheduledEndMs field value if set, zero value otherwise.
func (o *V1DispatchRouteCreateBase) GetScheduledEndMs() int64 {
	if o == nil || o.ScheduledEndMs == nil {
		var ret int64
		return ret
	}
	return *o.ScheduledEndMs
}

// GetScheduledEndMsOk returns a tuple with the ScheduledEndMs field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1DispatchRouteCreateBase) GetScheduledEndMsOk() (int64, bool) {
	if o == nil || o.ScheduledEndMs == nil {
		var ret int64
		return ret, false
	}
	return *o.ScheduledEndMs, true
}

// HasScheduledEndMs returns a boolean if a field has been set.
func (o *V1DispatchRouteCreateBase) HasScheduledEndMs() bool {
	if o != nil && o.ScheduledEndMs != nil {
		return true
	}

	return false
}

// SetScheduledEndMs gets a reference to the given int64 and assigns it to the ScheduledEndMs field.
func (o *V1DispatchRouteCreateBase) SetScheduledEndMs(v int64) {
	o.ScheduledEndMs = &v
}

// GetScheduledMeters returns the ScheduledMeters field value if set, zero value otherwise.
func (o *V1DispatchRouteCreateBase) GetScheduledMeters() int64 {
	if o == nil || o.ScheduledMeters == nil {
		var ret int64
		return ret
	}
	return *o.ScheduledMeters
}

// GetScheduledMetersOk returns a tuple with the ScheduledMeters field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1DispatchRouteCreateBase) GetScheduledMetersOk() (int64, bool) {
	if o == nil || o.ScheduledMeters == nil {
		var ret int64
		return ret, false
	}
	return *o.ScheduledMeters, true
}

// HasScheduledMeters returns a boolean if a field has been set.
func (o *V1DispatchRouteCreateBase) HasScheduledMeters() bool {
	if o != nil && o.ScheduledMeters != nil {
		return true
	}

	return false
}

// SetScheduledMeters gets a reference to the given int64 and assigns it to the ScheduledMeters field.
func (o *V1DispatchRouteCreateBase) SetScheduledMeters(v int64) {
	o.ScheduledMeters = &v
}

// GetScheduledStartMs returns the ScheduledStartMs field value
func (o *V1DispatchRouteCreateBase) GetScheduledStartMs() int64 {
	if o == nil {
		var ret int64
		return ret
	}

	return o.ScheduledStartMs
}

// SetScheduledStartMs sets field value
func (o *V1DispatchRouteCreateBase) SetScheduledStartMs(v int64) {
	o.ScheduledStartMs = v
}

// GetStartLocationAddress returns the StartLocationAddress field value if set, zero value otherwise.
func (o *V1DispatchRouteCreateBase) GetStartLocationAddress() string {
	if o == nil || o.StartLocationAddress == nil {
		var ret string
		return ret
	}
	return *o.StartLocationAddress
}

// GetStartLocationAddressOk returns a tuple with the StartLocationAddress field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1DispatchRouteCreateBase) GetStartLocationAddressOk() (string, bool) {
	if o == nil || o.StartLocationAddress == nil {
		var ret string
		return ret, false
	}
	return *o.StartLocationAddress, true
}

// HasStartLocationAddress returns a boolean if a field has been set.
func (o *V1DispatchRouteCreateBase) HasStartLocationAddress() bool {
	if o != nil && o.StartLocationAddress != nil {
		return true
	}

	return false
}

// SetStartLocationAddress gets a reference to the given string and assigns it to the StartLocationAddress field.
func (o *V1DispatchRouteCreateBase) SetStartLocationAddress(v string) {
	o.StartLocationAddress = &v
}

// GetStartLocationAddressId returns the StartLocationAddressId field value if set, zero value otherwise.
func (o *V1DispatchRouteCreateBase) GetStartLocationAddressId() int64 {
	if o == nil || o.StartLocationAddressId == nil {
		var ret int64
		return ret
	}
	return *o.StartLocationAddressId
}

// GetStartLocationAddressIdOk returns a tuple with the StartLocationAddressId field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1DispatchRouteCreateBase) GetStartLocationAddressIdOk() (int64, bool) {
	if o == nil || o.StartLocationAddressId == nil {
		var ret int64
		return ret, false
	}
	return *o.StartLocationAddressId, true
}

// HasStartLocationAddressId returns a boolean if a field has been set.
func (o *V1DispatchRouteCreateBase) HasStartLocationAddressId() bool {
	if o != nil && o.StartLocationAddressId != nil {
		return true
	}

	return false
}

// SetStartLocationAddressId gets a reference to the given int64 and assigns it to the StartLocationAddressId field.
func (o *V1DispatchRouteCreateBase) SetStartLocationAddressId(v int64) {
	o.StartLocationAddressId = &v
}

// GetStartLocationLat returns the StartLocationLat field value if set, zero value otherwise.
func (o *V1DispatchRouteCreateBase) GetStartLocationLat() float64 {
	if o == nil || o.StartLocationLat == nil {
		var ret float64
		return ret
	}
	return *o.StartLocationLat
}

// GetStartLocationLatOk returns a tuple with the StartLocationLat field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1DispatchRouteCreateBase) GetStartLocationLatOk() (float64, bool) {
	if o == nil || o.StartLocationLat == nil {
		var ret float64
		return ret, false
	}
	return *o.StartLocationLat, true
}

// HasStartLocationLat returns a boolean if a field has been set.
func (o *V1DispatchRouteCreateBase) HasStartLocationLat() bool {
	if o != nil && o.StartLocationLat != nil {
		return true
	}

	return false
}

// SetStartLocationLat gets a reference to the given float64 and assigns it to the StartLocationLat field.
func (o *V1DispatchRouteCreateBase) SetStartLocationLat(v float64) {
	o.StartLocationLat = &v
}

// GetStartLocationLng returns the StartLocationLng field value if set, zero value otherwise.
func (o *V1DispatchRouteCreateBase) GetStartLocationLng() float64 {
	if o == nil || o.StartLocationLng == nil {
		var ret float64
		return ret
	}
	return *o.StartLocationLng
}

// GetStartLocationLngOk returns a tuple with the StartLocationLng field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1DispatchRouteCreateBase) GetStartLocationLngOk() (float64, bool) {
	if o == nil || o.StartLocationLng == nil {
		var ret float64
		return ret, false
	}
	return *o.StartLocationLng, true
}

// HasStartLocationLng returns a boolean if a field has been set.
func (o *V1DispatchRouteCreateBase) HasStartLocationLng() bool {
	if o != nil && o.StartLocationLng != nil {
		return true
	}

	return false
}

// SetStartLocationLng gets a reference to the given float64 and assigns it to the StartLocationLng field.
func (o *V1DispatchRouteCreateBase) SetStartLocationLng(v float64) {
	o.StartLocationLng = &v
}

// GetStartLocationName returns the StartLocationName field value if set, zero value otherwise.
func (o *V1DispatchRouteCreateBase) GetStartLocationName() string {
	if o == nil || o.StartLocationName == nil {
		var ret string
		return ret
	}
	return *o.StartLocationName
}

// GetStartLocationNameOk returns a tuple with the StartLocationName field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1DispatchRouteCreateBase) GetStartLocationNameOk() (string, bool) {
	if o == nil || o.StartLocationName == nil {
		var ret string
		return ret, false
	}
	return *o.StartLocationName, true
}

// HasStartLocationName returns a boolean if a field has been set.
func (o *V1DispatchRouteCreateBase) HasStartLocationName() bool {
	if o != nil && o.StartLocationName != nil {
		return true
	}

	return false
}

// SetStartLocationName gets a reference to the given string and assigns it to the StartLocationName field.
func (o *V1DispatchRouteCreateBase) SetStartLocationName(v string) {
	o.StartLocationName = &v
}

// GetTrailerId returns the TrailerId field value if set, zero value otherwise.
func (o *V1DispatchRouteCreateBase) GetTrailerId() int64 {
	if o == nil || o.TrailerId == nil {
		var ret int64
		return ret
	}
	return *o.TrailerId
}

// GetTrailerIdOk returns a tuple with the TrailerId field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1DispatchRouteCreateBase) GetTrailerIdOk() (int64, bool) {
	if o == nil || o.TrailerId == nil {
		var ret int64
		return ret, false
	}
	return *o.TrailerId, true
}

// HasTrailerId returns a boolean if a field has been set.
func (o *V1DispatchRouteCreateBase) HasTrailerId() bool {
	if o != nil && o.TrailerId != nil {
		return true
	}

	return false
}

// SetTrailerId gets a reference to the given int64 and assigns it to the TrailerId field.
func (o *V1DispatchRouteCreateBase) SetTrailerId(v int64) {
	o.TrailerId = &v
}

// GetVehicleId returns the VehicleId field value if set, zero value otherwise.
func (o *V1DispatchRouteCreateBase) GetVehicleId() int64 {
	if o == nil || o.VehicleId == nil {
		var ret int64
		return ret
	}
	return *o.VehicleId
}

// GetVehicleIdOk returns a tuple with the VehicleId field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1DispatchRouteCreateBase) GetVehicleIdOk() (int64, bool) {
	if o == nil || o.VehicleId == nil {
		var ret int64
		return ret, false
	}
	return *o.VehicleId, true
}

// HasVehicleId returns a boolean if a field has been set.
func (o *V1DispatchRouteCreateBase) HasVehicleId() bool {
	if o != nil && o.VehicleId != nil {
		return true
	}

	return false
}

// SetVehicleId gets a reference to the given int64 and assigns it to the VehicleId field.
func (o *V1DispatchRouteCreateBase) SetVehicleId(v int64) {
	o.VehicleId = &v
}

type NullableV1DispatchRouteCreateBase struct {
	Value        V1DispatchRouteCreateBase
	ExplicitNull bool
}

func (v NullableV1DispatchRouteCreateBase) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableV1DispatchRouteCreateBase) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}
