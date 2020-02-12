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

// OrgSafetyScoresResponseData struct for OrgSafetyScoresResponseData
type OrgSafetyScoresResponseData struct {
	// Crash count
	CrashCount *int64 `json:"crashCount,omitempty"`
	// Driver Id
	DriverId *int64 `json:"driverId,omitempty"`
	// Harsh accel count
	HarshAccelCount *int64 `json:"harshAccelCount,omitempty"`
	// Harsh braking count
	HarshBrakingCount     *int64                                          `json:"harshBrakingCount,omitempty"`
	HarshEventIdentifiers *[]OrgSafetyScoresResponseHarshEventIdentifiers `json:"harshEventIdentifiers,omitempty"`
	// Harsh turning count
	HarshTurningCount *int64 `json:"harshTurningCount,omitempty"`
	// Vehicle/Driver Safety Score
	SafetyScore *int64 `json:"safetyScore,omitempty"`
	// Vehicle/Driver Safety Rank
	SafetyScoreRank *int64 `json:"safetyScoreRank,omitempty"`
	// Overspeed limit time, specified in milliseconds UNIX time.
	TimeOverSpeedLimitMs *int64 `json:"timeOverSpeedLimitMs,omitempty"`
	// Total distance driven meters
	TotalDistanceDrivenMeters *int64 `json:"totalDistanceDrivenMeters,omitempty"`
	// Total harsh event count
	TotalHarshEventCount *int64 `json:"totalHarshEventCount,omitempty"`
	// Total driver time, specified in milliseconds UNIX time.
	TotalTimeDrivenMs *int64 `json:"totalTimeDrivenMs,omitempty"`
	// Vehicle Id
	VehicleId *int64 `json:"vehicleId,omitempty"`
}

// GetCrashCount returns the CrashCount field value if set, zero value otherwise.
func (o *OrgSafetyScoresResponseData) GetCrashCount() int64 {
	if o == nil || o.CrashCount == nil {
		var ret int64
		return ret
	}
	return *o.CrashCount
}

// GetCrashCountOk returns a tuple with the CrashCount field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *OrgSafetyScoresResponseData) GetCrashCountOk() (int64, bool) {
	if o == nil || o.CrashCount == nil {
		var ret int64
		return ret, false
	}
	return *o.CrashCount, true
}

// HasCrashCount returns a boolean if a field has been set.
func (o *OrgSafetyScoresResponseData) HasCrashCount() bool {
	if o != nil && o.CrashCount != nil {
		return true
	}

	return false
}

// SetCrashCount gets a reference to the given int64 and assigns it to the CrashCount field.
func (o *OrgSafetyScoresResponseData) SetCrashCount(v int64) {
	o.CrashCount = &v
}

// GetDriverId returns the DriverId field value if set, zero value otherwise.
func (o *OrgSafetyScoresResponseData) GetDriverId() int64 {
	if o == nil || o.DriverId == nil {
		var ret int64
		return ret
	}
	return *o.DriverId
}

// GetDriverIdOk returns a tuple with the DriverId field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *OrgSafetyScoresResponseData) GetDriverIdOk() (int64, bool) {
	if o == nil || o.DriverId == nil {
		var ret int64
		return ret, false
	}
	return *o.DriverId, true
}

// HasDriverId returns a boolean if a field has been set.
func (o *OrgSafetyScoresResponseData) HasDriverId() bool {
	if o != nil && o.DriverId != nil {
		return true
	}

	return false
}

// SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.
func (o *OrgSafetyScoresResponseData) SetDriverId(v int64) {
	o.DriverId = &v
}

// GetHarshAccelCount returns the HarshAccelCount field value if set, zero value otherwise.
func (o *OrgSafetyScoresResponseData) GetHarshAccelCount() int64 {
	if o == nil || o.HarshAccelCount == nil {
		var ret int64
		return ret
	}
	return *o.HarshAccelCount
}

// GetHarshAccelCountOk returns a tuple with the HarshAccelCount field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *OrgSafetyScoresResponseData) GetHarshAccelCountOk() (int64, bool) {
	if o == nil || o.HarshAccelCount == nil {
		var ret int64
		return ret, false
	}
	return *o.HarshAccelCount, true
}

// HasHarshAccelCount returns a boolean if a field has been set.
func (o *OrgSafetyScoresResponseData) HasHarshAccelCount() bool {
	if o != nil && o.HarshAccelCount != nil {
		return true
	}

	return false
}

// SetHarshAccelCount gets a reference to the given int64 and assigns it to the HarshAccelCount field.
func (o *OrgSafetyScoresResponseData) SetHarshAccelCount(v int64) {
	o.HarshAccelCount = &v
}

// GetHarshBrakingCount returns the HarshBrakingCount field value if set, zero value otherwise.
func (o *OrgSafetyScoresResponseData) GetHarshBrakingCount() int64 {
	if o == nil || o.HarshBrakingCount == nil {
		var ret int64
		return ret
	}
	return *o.HarshBrakingCount
}

// GetHarshBrakingCountOk returns a tuple with the HarshBrakingCount field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *OrgSafetyScoresResponseData) GetHarshBrakingCountOk() (int64, bool) {
	if o == nil || o.HarshBrakingCount == nil {
		var ret int64
		return ret, false
	}
	return *o.HarshBrakingCount, true
}

// HasHarshBrakingCount returns a boolean if a field has been set.
func (o *OrgSafetyScoresResponseData) HasHarshBrakingCount() bool {
	if o != nil && o.HarshBrakingCount != nil {
		return true
	}

	return false
}

// SetHarshBrakingCount gets a reference to the given int64 and assigns it to the HarshBrakingCount field.
func (o *OrgSafetyScoresResponseData) SetHarshBrakingCount(v int64) {
	o.HarshBrakingCount = &v
}

// GetHarshEventIdentifiers returns the HarshEventIdentifiers field value if set, zero value otherwise.
func (o *OrgSafetyScoresResponseData) GetHarshEventIdentifiers() []OrgSafetyScoresResponseHarshEventIdentifiers {
	if o == nil || o.HarshEventIdentifiers == nil {
		var ret []OrgSafetyScoresResponseHarshEventIdentifiers
		return ret
	}
	return *o.HarshEventIdentifiers
}

// GetHarshEventIdentifiersOk returns a tuple with the HarshEventIdentifiers field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *OrgSafetyScoresResponseData) GetHarshEventIdentifiersOk() ([]OrgSafetyScoresResponseHarshEventIdentifiers, bool) {
	if o == nil || o.HarshEventIdentifiers == nil {
		var ret []OrgSafetyScoresResponseHarshEventIdentifiers
		return ret, false
	}
	return *o.HarshEventIdentifiers, true
}

// HasHarshEventIdentifiers returns a boolean if a field has been set.
func (o *OrgSafetyScoresResponseData) HasHarshEventIdentifiers() bool {
	if o != nil && o.HarshEventIdentifiers != nil {
		return true
	}

	return false
}

// SetHarshEventIdentifiers gets a reference to the given []OrgSafetyScoresResponseHarshEventIdentifiers and assigns it to the HarshEventIdentifiers field.
func (o *OrgSafetyScoresResponseData) SetHarshEventIdentifiers(v []OrgSafetyScoresResponseHarshEventIdentifiers) {
	o.HarshEventIdentifiers = &v
}

// GetHarshTurningCount returns the HarshTurningCount field value if set, zero value otherwise.
func (o *OrgSafetyScoresResponseData) GetHarshTurningCount() int64 {
	if o == nil || o.HarshTurningCount == nil {
		var ret int64
		return ret
	}
	return *o.HarshTurningCount
}

// GetHarshTurningCountOk returns a tuple with the HarshTurningCount field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *OrgSafetyScoresResponseData) GetHarshTurningCountOk() (int64, bool) {
	if o == nil || o.HarshTurningCount == nil {
		var ret int64
		return ret, false
	}
	return *o.HarshTurningCount, true
}

// HasHarshTurningCount returns a boolean if a field has been set.
func (o *OrgSafetyScoresResponseData) HasHarshTurningCount() bool {
	if o != nil && o.HarshTurningCount != nil {
		return true
	}

	return false
}

// SetHarshTurningCount gets a reference to the given int64 and assigns it to the HarshTurningCount field.
func (o *OrgSafetyScoresResponseData) SetHarshTurningCount(v int64) {
	o.HarshTurningCount = &v
}

// GetSafetyScore returns the SafetyScore field value if set, zero value otherwise.
func (o *OrgSafetyScoresResponseData) GetSafetyScore() int64 {
	if o == nil || o.SafetyScore == nil {
		var ret int64
		return ret
	}
	return *o.SafetyScore
}

// GetSafetyScoreOk returns a tuple with the SafetyScore field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *OrgSafetyScoresResponseData) GetSafetyScoreOk() (int64, bool) {
	if o == nil || o.SafetyScore == nil {
		var ret int64
		return ret, false
	}
	return *o.SafetyScore, true
}

// HasSafetyScore returns a boolean if a field has been set.
func (o *OrgSafetyScoresResponseData) HasSafetyScore() bool {
	if o != nil && o.SafetyScore != nil {
		return true
	}

	return false
}

// SetSafetyScore gets a reference to the given int64 and assigns it to the SafetyScore field.
func (o *OrgSafetyScoresResponseData) SetSafetyScore(v int64) {
	o.SafetyScore = &v
}

// GetSafetyScoreRank returns the SafetyScoreRank field value if set, zero value otherwise.
func (o *OrgSafetyScoresResponseData) GetSafetyScoreRank() int64 {
	if o == nil || o.SafetyScoreRank == nil {
		var ret int64
		return ret
	}
	return *o.SafetyScoreRank
}

// GetSafetyScoreRankOk returns a tuple with the SafetyScoreRank field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *OrgSafetyScoresResponseData) GetSafetyScoreRankOk() (int64, bool) {
	if o == nil || o.SafetyScoreRank == nil {
		var ret int64
		return ret, false
	}
	return *o.SafetyScoreRank, true
}

// HasSafetyScoreRank returns a boolean if a field has been set.
func (o *OrgSafetyScoresResponseData) HasSafetyScoreRank() bool {
	if o != nil && o.SafetyScoreRank != nil {
		return true
	}

	return false
}

// SetSafetyScoreRank gets a reference to the given int64 and assigns it to the SafetyScoreRank field.
func (o *OrgSafetyScoresResponseData) SetSafetyScoreRank(v int64) {
	o.SafetyScoreRank = &v
}

// GetTimeOverSpeedLimitMs returns the TimeOverSpeedLimitMs field value if set, zero value otherwise.
func (o *OrgSafetyScoresResponseData) GetTimeOverSpeedLimitMs() int64 {
	if o == nil || o.TimeOverSpeedLimitMs == nil {
		var ret int64
		return ret
	}
	return *o.TimeOverSpeedLimitMs
}

// GetTimeOverSpeedLimitMsOk returns a tuple with the TimeOverSpeedLimitMs field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *OrgSafetyScoresResponseData) GetTimeOverSpeedLimitMsOk() (int64, bool) {
	if o == nil || o.TimeOverSpeedLimitMs == nil {
		var ret int64
		return ret, false
	}
	return *o.TimeOverSpeedLimitMs, true
}

// HasTimeOverSpeedLimitMs returns a boolean if a field has been set.
func (o *OrgSafetyScoresResponseData) HasTimeOverSpeedLimitMs() bool {
	if o != nil && o.TimeOverSpeedLimitMs != nil {
		return true
	}

	return false
}

// SetTimeOverSpeedLimitMs gets a reference to the given int64 and assigns it to the TimeOverSpeedLimitMs field.
func (o *OrgSafetyScoresResponseData) SetTimeOverSpeedLimitMs(v int64) {
	o.TimeOverSpeedLimitMs = &v
}

// GetTotalDistanceDrivenMeters returns the TotalDistanceDrivenMeters field value if set, zero value otherwise.
func (o *OrgSafetyScoresResponseData) GetTotalDistanceDrivenMeters() int64 {
	if o == nil || o.TotalDistanceDrivenMeters == nil {
		var ret int64
		return ret
	}
	return *o.TotalDistanceDrivenMeters
}

// GetTotalDistanceDrivenMetersOk returns a tuple with the TotalDistanceDrivenMeters field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *OrgSafetyScoresResponseData) GetTotalDistanceDrivenMetersOk() (int64, bool) {
	if o == nil || o.TotalDistanceDrivenMeters == nil {
		var ret int64
		return ret, false
	}
	return *o.TotalDistanceDrivenMeters, true
}

// HasTotalDistanceDrivenMeters returns a boolean if a field has been set.
func (o *OrgSafetyScoresResponseData) HasTotalDistanceDrivenMeters() bool {
	if o != nil && o.TotalDistanceDrivenMeters != nil {
		return true
	}

	return false
}

// SetTotalDistanceDrivenMeters gets a reference to the given int64 and assigns it to the TotalDistanceDrivenMeters field.
func (o *OrgSafetyScoresResponseData) SetTotalDistanceDrivenMeters(v int64) {
	o.TotalDistanceDrivenMeters = &v
}

// GetTotalHarshEventCount returns the TotalHarshEventCount field value if set, zero value otherwise.
func (o *OrgSafetyScoresResponseData) GetTotalHarshEventCount() int64 {
	if o == nil || o.TotalHarshEventCount == nil {
		var ret int64
		return ret
	}
	return *o.TotalHarshEventCount
}

// GetTotalHarshEventCountOk returns a tuple with the TotalHarshEventCount field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *OrgSafetyScoresResponseData) GetTotalHarshEventCountOk() (int64, bool) {
	if o == nil || o.TotalHarshEventCount == nil {
		var ret int64
		return ret, false
	}
	return *o.TotalHarshEventCount, true
}

// HasTotalHarshEventCount returns a boolean if a field has been set.
func (o *OrgSafetyScoresResponseData) HasTotalHarshEventCount() bool {
	if o != nil && o.TotalHarshEventCount != nil {
		return true
	}

	return false
}

// SetTotalHarshEventCount gets a reference to the given int64 and assigns it to the TotalHarshEventCount field.
func (o *OrgSafetyScoresResponseData) SetTotalHarshEventCount(v int64) {
	o.TotalHarshEventCount = &v
}

// GetTotalTimeDrivenMs returns the TotalTimeDrivenMs field value if set, zero value otherwise.
func (o *OrgSafetyScoresResponseData) GetTotalTimeDrivenMs() int64 {
	if o == nil || o.TotalTimeDrivenMs == nil {
		var ret int64
		return ret
	}
	return *o.TotalTimeDrivenMs
}

// GetTotalTimeDrivenMsOk returns a tuple with the TotalTimeDrivenMs field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *OrgSafetyScoresResponseData) GetTotalTimeDrivenMsOk() (int64, bool) {
	if o == nil || o.TotalTimeDrivenMs == nil {
		var ret int64
		return ret, false
	}
	return *o.TotalTimeDrivenMs, true
}

// HasTotalTimeDrivenMs returns a boolean if a field has been set.
func (o *OrgSafetyScoresResponseData) HasTotalTimeDrivenMs() bool {
	if o != nil && o.TotalTimeDrivenMs != nil {
		return true
	}

	return false
}

// SetTotalTimeDrivenMs gets a reference to the given int64 and assigns it to the TotalTimeDrivenMs field.
func (o *OrgSafetyScoresResponseData) SetTotalTimeDrivenMs(v int64) {
	o.TotalTimeDrivenMs = &v
}

// GetVehicleId returns the VehicleId field value if set, zero value otherwise.
func (o *OrgSafetyScoresResponseData) GetVehicleId() int64 {
	if o == nil || o.VehicleId == nil {
		var ret int64
		return ret
	}
	return *o.VehicleId
}

// GetVehicleIdOk returns a tuple with the VehicleId field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *OrgSafetyScoresResponseData) GetVehicleIdOk() (int64, bool) {
	if o == nil || o.VehicleId == nil {
		var ret int64
		return ret, false
	}
	return *o.VehicleId, true
}

// HasVehicleId returns a boolean if a field has been set.
func (o *OrgSafetyScoresResponseData) HasVehicleId() bool {
	if o != nil && o.VehicleId != nil {
		return true
	}

	return false
}

// SetVehicleId gets a reference to the given int64 and assigns it to the VehicleId field.
func (o *OrgSafetyScoresResponseData) SetVehicleId(v int64) {
	o.VehicleId = &v
}

type NullableOrgSafetyScoresResponseData struct {
	Value        OrgSafetyScoresResponseData
	ExplicitNull bool
}

func (v NullableOrgSafetyScoresResponseData) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableOrgSafetyScoresResponseData) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}
