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

// EquipmentStatsSnapshotResponseAllOf struct for EquipmentStatsSnapshotResponseAllOf
type EquipmentStatsSnapshotResponseAllOf struct {
	EngineRpm      *EquipmentEngineRpm      `json:"engineRpm,omitempty"`
	EngineSeconds  *EquipmentEngineSeconds  `json:"engineSeconds,omitempty"`
	EngineState    *EquipmentEngineState    `json:"engineState,omitempty"`
	FuelPercent    *EquipmentFuelPercent    `json:"fuelPercent,omitempty"`
	OdometerMeters *EquipmentOdometerMeters `json:"odometerMeters,omitempty"`
}

// GetEngineRpm returns the EngineRpm field value if set, zero value otherwise.
func (o *EquipmentStatsSnapshotResponseAllOf) GetEngineRpm() EquipmentEngineRpm {
	if o == nil || o.EngineRpm == nil {
		var ret EquipmentEngineRpm
		return ret
	}
	return *o.EngineRpm
}

// GetEngineRpmOk returns a tuple with the EngineRpm field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *EquipmentStatsSnapshotResponseAllOf) GetEngineRpmOk() (EquipmentEngineRpm, bool) {
	if o == nil || o.EngineRpm == nil {
		var ret EquipmentEngineRpm
		return ret, false
	}
	return *o.EngineRpm, true
}

// HasEngineRpm returns a boolean if a field has been set.
func (o *EquipmentStatsSnapshotResponseAllOf) HasEngineRpm() bool {
	if o != nil && o.EngineRpm != nil {
		return true
	}

	return false
}

// SetEngineRpm gets a reference to the given EquipmentEngineRpm and assigns it to the EngineRpm field.
func (o *EquipmentStatsSnapshotResponseAllOf) SetEngineRpm(v EquipmentEngineRpm) {
	o.EngineRpm = &v
}

// GetEngineSeconds returns the EngineSeconds field value if set, zero value otherwise.
func (o *EquipmentStatsSnapshotResponseAllOf) GetEngineSeconds() EquipmentEngineSeconds {
	if o == nil || o.EngineSeconds == nil {
		var ret EquipmentEngineSeconds
		return ret
	}
	return *o.EngineSeconds
}

// GetEngineSecondsOk returns a tuple with the EngineSeconds field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *EquipmentStatsSnapshotResponseAllOf) GetEngineSecondsOk() (EquipmentEngineSeconds, bool) {
	if o == nil || o.EngineSeconds == nil {
		var ret EquipmentEngineSeconds
		return ret, false
	}
	return *o.EngineSeconds, true
}

// HasEngineSeconds returns a boolean if a field has been set.
func (o *EquipmentStatsSnapshotResponseAllOf) HasEngineSeconds() bool {
	if o != nil && o.EngineSeconds != nil {
		return true
	}

	return false
}

// SetEngineSeconds gets a reference to the given EquipmentEngineSeconds and assigns it to the EngineSeconds field.
func (o *EquipmentStatsSnapshotResponseAllOf) SetEngineSeconds(v EquipmentEngineSeconds) {
	o.EngineSeconds = &v
}

// GetEngineState returns the EngineState field value if set, zero value otherwise.
func (o *EquipmentStatsSnapshotResponseAllOf) GetEngineState() EquipmentEngineState {
	if o == nil || o.EngineState == nil {
		var ret EquipmentEngineState
		return ret
	}
	return *o.EngineState
}

// GetEngineStateOk returns a tuple with the EngineState field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *EquipmentStatsSnapshotResponseAllOf) GetEngineStateOk() (EquipmentEngineState, bool) {
	if o == nil || o.EngineState == nil {
		var ret EquipmentEngineState
		return ret, false
	}
	return *o.EngineState, true
}

// HasEngineState returns a boolean if a field has been set.
func (o *EquipmentStatsSnapshotResponseAllOf) HasEngineState() bool {
	if o != nil && o.EngineState != nil {
		return true
	}

	return false
}

// SetEngineState gets a reference to the given EquipmentEngineState and assigns it to the EngineState field.
func (o *EquipmentStatsSnapshotResponseAllOf) SetEngineState(v EquipmentEngineState) {
	o.EngineState = &v
}

// GetFuelPercent returns the FuelPercent field value if set, zero value otherwise.
func (o *EquipmentStatsSnapshotResponseAllOf) GetFuelPercent() EquipmentFuelPercent {
	if o == nil || o.FuelPercent == nil {
		var ret EquipmentFuelPercent
		return ret
	}
	return *o.FuelPercent
}

// GetFuelPercentOk returns a tuple with the FuelPercent field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *EquipmentStatsSnapshotResponseAllOf) GetFuelPercentOk() (EquipmentFuelPercent, bool) {
	if o == nil || o.FuelPercent == nil {
		var ret EquipmentFuelPercent
		return ret, false
	}
	return *o.FuelPercent, true
}

// HasFuelPercent returns a boolean if a field has been set.
func (o *EquipmentStatsSnapshotResponseAllOf) HasFuelPercent() bool {
	if o != nil && o.FuelPercent != nil {
		return true
	}

	return false
}

// SetFuelPercent gets a reference to the given EquipmentFuelPercent and assigns it to the FuelPercent field.
func (o *EquipmentStatsSnapshotResponseAllOf) SetFuelPercent(v EquipmentFuelPercent) {
	o.FuelPercent = &v
}

// GetOdometerMeters returns the OdometerMeters field value if set, zero value otherwise.
func (o *EquipmentStatsSnapshotResponseAllOf) GetOdometerMeters() EquipmentOdometerMeters {
	if o == nil || o.OdometerMeters == nil {
		var ret EquipmentOdometerMeters
		return ret
	}
	return *o.OdometerMeters
}

// GetOdometerMetersOk returns a tuple with the OdometerMeters field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *EquipmentStatsSnapshotResponseAllOf) GetOdometerMetersOk() (EquipmentOdometerMeters, bool) {
	if o == nil || o.OdometerMeters == nil {
		var ret EquipmentOdometerMeters
		return ret, false
	}
	return *o.OdometerMeters, true
}

// HasOdometerMeters returns a boolean if a field has been set.
func (o *EquipmentStatsSnapshotResponseAllOf) HasOdometerMeters() bool {
	if o != nil && o.OdometerMeters != nil {
		return true
	}

	return false
}

// SetOdometerMeters gets a reference to the given EquipmentOdometerMeters and assigns it to the OdometerMeters field.
func (o *EquipmentStatsSnapshotResponseAllOf) SetOdometerMeters(v EquipmentOdometerMeters) {
	o.OdometerMeters = &v
}

type NullableEquipmentStatsSnapshotResponseAllOf struct {
	Value        EquipmentStatsSnapshotResponseAllOf
	ExplicitNull bool
}

func (v NullableEquipmentStatsSnapshotResponseAllOf) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableEquipmentStatsSnapshotResponseAllOf) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}
