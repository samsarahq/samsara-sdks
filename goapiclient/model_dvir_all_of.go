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

// DvirAllOf struct for DvirAllOf
type DvirAllOf struct {
	AuthorSignature *map[string]interface{} `json:"authorSignature,omitempty"`
	EndTime         *map[string]interface{} `json:"endTime,omitempty"`
	// Unique Samsara ID for the DVIR.
	Id string `json:"id"`
	// The license plate of this vehicle.
	LicensePlate *string `json:"licensePlate,omitempty"`
	// Optional string if your jurisdiction requires a location of the DVIR.
	Location *string `json:"location,omitempty"`
	// The mechanics notes on the DVIR.
	MechanicNotes *string `json:"mechanicNotes,omitempty"`
	// The odometer reading in meters.
	OdometerMeters *int32 `json:"odometerMeters,omitempty"`
	// The condition of vechile on which DVIR was done.
	SafetyStatus    *string                 `json:"safetyStatus,omitempty"`
	SecondSignature *map[string]interface{} `json:"secondSignature,omitempty"`
	StartTime       *map[string]interface{} `json:"startTime,omitempty"`
	ThirdSignature  *map[string]interface{} `json:"thirdSignature,omitempty"`
	Trailer         *map[string]interface{} `json:"trailer,omitempty"`
	// Defects registered for the trailer which was part of the DVIR.
	TrailerDefects *[]DvirAllOf0TrailerDefectsItems `json:"trailerDefects,omitempty"`
	// The name of the trailer the DVIR was submitted for.  Only included for tractor+trailer DVIRs.
	TrailerName *string `json:"trailerName,omitempty"`
	// Inspection type of the DVIR.
	Type    *string                 `json:"type,omitempty"`
	Vehicle *map[string]interface{} `json:"vehicle,omitempty"`
	// Defects registered for the vehicle which was part of the DVIR.
	VehicleDefects *[]DvirAllOf0TrailerDefectsItems `json:"vehicleDefects,omitempty"`
}

// GetAuthorSignature returns the AuthorSignature field value if set, zero value otherwise.
func (o *DvirAllOf) GetAuthorSignature() map[string]interface{} {
	if o == nil || o.AuthorSignature == nil {
		var ret map[string]interface{}
		return ret
	}
	return *o.AuthorSignature
}

// GetAuthorSignatureOk returns a tuple with the AuthorSignature field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetAuthorSignatureOk() (map[string]interface{}, bool) {
	if o == nil || o.AuthorSignature == nil {
		var ret map[string]interface{}
		return ret, false
	}
	return *o.AuthorSignature, true
}

// HasAuthorSignature returns a boolean if a field has been set.
func (o *DvirAllOf) HasAuthorSignature() bool {
	if o != nil && o.AuthorSignature != nil {
		return true
	}

	return false
}

// SetAuthorSignature gets a reference to the given map[string]interface{} and assigns it to the AuthorSignature field.
func (o *DvirAllOf) SetAuthorSignature(v map[string]interface{}) {
	o.AuthorSignature = &v
}

// GetEndTime returns the EndTime field value if set, zero value otherwise.
func (o *DvirAllOf) GetEndTime() map[string]interface{} {
	if o == nil || o.EndTime == nil {
		var ret map[string]interface{}
		return ret
	}
	return *o.EndTime
}

// GetEndTimeOk returns a tuple with the EndTime field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetEndTimeOk() (map[string]interface{}, bool) {
	if o == nil || o.EndTime == nil {
		var ret map[string]interface{}
		return ret, false
	}
	return *o.EndTime, true
}

// HasEndTime returns a boolean if a field has been set.
func (o *DvirAllOf) HasEndTime() bool {
	if o != nil && o.EndTime != nil {
		return true
	}

	return false
}

// SetEndTime gets a reference to the given map[string]interface{} and assigns it to the EndTime field.
func (o *DvirAllOf) SetEndTime(v map[string]interface{}) {
	o.EndTime = &v
}

// GetId returns the Id field value
func (o *DvirAllOf) GetId() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Id
}

// SetId sets field value
func (o *DvirAllOf) SetId(v string) {
	o.Id = v
}

// GetLicensePlate returns the LicensePlate field value if set, zero value otherwise.
func (o *DvirAllOf) GetLicensePlate() string {
	if o == nil || o.LicensePlate == nil {
		var ret string
		return ret
	}
	return *o.LicensePlate
}

// GetLicensePlateOk returns a tuple with the LicensePlate field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetLicensePlateOk() (string, bool) {
	if o == nil || o.LicensePlate == nil {
		var ret string
		return ret, false
	}
	return *o.LicensePlate, true
}

// HasLicensePlate returns a boolean if a field has been set.
func (o *DvirAllOf) HasLicensePlate() bool {
	if o != nil && o.LicensePlate != nil {
		return true
	}

	return false
}

// SetLicensePlate gets a reference to the given string and assigns it to the LicensePlate field.
func (o *DvirAllOf) SetLicensePlate(v string) {
	o.LicensePlate = &v
}

// GetLocation returns the Location field value if set, zero value otherwise.
func (o *DvirAllOf) GetLocation() string {
	if o == nil || o.Location == nil {
		var ret string
		return ret
	}
	return *o.Location
}

// GetLocationOk returns a tuple with the Location field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetLocationOk() (string, bool) {
	if o == nil || o.Location == nil {
		var ret string
		return ret, false
	}
	return *o.Location, true
}

// HasLocation returns a boolean if a field has been set.
func (o *DvirAllOf) HasLocation() bool {
	if o != nil && o.Location != nil {
		return true
	}

	return false
}

// SetLocation gets a reference to the given string and assigns it to the Location field.
func (o *DvirAllOf) SetLocation(v string) {
	o.Location = &v
}

// GetMechanicNotes returns the MechanicNotes field value if set, zero value otherwise.
func (o *DvirAllOf) GetMechanicNotes() string {
	if o == nil || o.MechanicNotes == nil {
		var ret string
		return ret
	}
	return *o.MechanicNotes
}

// GetMechanicNotesOk returns a tuple with the MechanicNotes field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetMechanicNotesOk() (string, bool) {
	if o == nil || o.MechanicNotes == nil {
		var ret string
		return ret, false
	}
	return *o.MechanicNotes, true
}

// HasMechanicNotes returns a boolean if a field has been set.
func (o *DvirAllOf) HasMechanicNotes() bool {
	if o != nil && o.MechanicNotes != nil {
		return true
	}

	return false
}

// SetMechanicNotes gets a reference to the given string and assigns it to the MechanicNotes field.
func (o *DvirAllOf) SetMechanicNotes(v string) {
	o.MechanicNotes = &v
}

// GetOdometerMeters returns the OdometerMeters field value if set, zero value otherwise.
func (o *DvirAllOf) GetOdometerMeters() int32 {
	if o == nil || o.OdometerMeters == nil {
		var ret int32
		return ret
	}
	return *o.OdometerMeters
}

// GetOdometerMetersOk returns a tuple with the OdometerMeters field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetOdometerMetersOk() (int32, bool) {
	if o == nil || o.OdometerMeters == nil {
		var ret int32
		return ret, false
	}
	return *o.OdometerMeters, true
}

// HasOdometerMeters returns a boolean if a field has been set.
func (o *DvirAllOf) HasOdometerMeters() bool {
	if o != nil && o.OdometerMeters != nil {
		return true
	}

	return false
}

// SetOdometerMeters gets a reference to the given int32 and assigns it to the OdometerMeters field.
func (o *DvirAllOf) SetOdometerMeters(v int32) {
	o.OdometerMeters = &v
}

// GetSafetyStatus returns the SafetyStatus field value if set, zero value otherwise.
func (o *DvirAllOf) GetSafetyStatus() string {
	if o == nil || o.SafetyStatus == nil {
		var ret string
		return ret
	}
	return *o.SafetyStatus
}

// GetSafetyStatusOk returns a tuple with the SafetyStatus field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetSafetyStatusOk() (string, bool) {
	if o == nil || o.SafetyStatus == nil {
		var ret string
		return ret, false
	}
	return *o.SafetyStatus, true
}

// HasSafetyStatus returns a boolean if a field has been set.
func (o *DvirAllOf) HasSafetyStatus() bool {
	if o != nil && o.SafetyStatus != nil {
		return true
	}

	return false
}

// SetSafetyStatus gets a reference to the given string and assigns it to the SafetyStatus field.
func (o *DvirAllOf) SetSafetyStatus(v string) {
	o.SafetyStatus = &v
}

// GetSecondSignature returns the SecondSignature field value if set, zero value otherwise.
func (o *DvirAllOf) GetSecondSignature() map[string]interface{} {
	if o == nil || o.SecondSignature == nil {
		var ret map[string]interface{}
		return ret
	}
	return *o.SecondSignature
}

// GetSecondSignatureOk returns a tuple with the SecondSignature field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetSecondSignatureOk() (map[string]interface{}, bool) {
	if o == nil || o.SecondSignature == nil {
		var ret map[string]interface{}
		return ret, false
	}
	return *o.SecondSignature, true
}

// HasSecondSignature returns a boolean if a field has been set.
func (o *DvirAllOf) HasSecondSignature() bool {
	if o != nil && o.SecondSignature != nil {
		return true
	}

	return false
}

// SetSecondSignature gets a reference to the given map[string]interface{} and assigns it to the SecondSignature field.
func (o *DvirAllOf) SetSecondSignature(v map[string]interface{}) {
	o.SecondSignature = &v
}

// GetStartTime returns the StartTime field value if set, zero value otherwise.
func (o *DvirAllOf) GetStartTime() map[string]interface{} {
	if o == nil || o.StartTime == nil {
		var ret map[string]interface{}
		return ret
	}
	return *o.StartTime
}

// GetStartTimeOk returns a tuple with the StartTime field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetStartTimeOk() (map[string]interface{}, bool) {
	if o == nil || o.StartTime == nil {
		var ret map[string]interface{}
		return ret, false
	}
	return *o.StartTime, true
}

// HasStartTime returns a boolean if a field has been set.
func (o *DvirAllOf) HasStartTime() bool {
	if o != nil && o.StartTime != nil {
		return true
	}

	return false
}

// SetStartTime gets a reference to the given map[string]interface{} and assigns it to the StartTime field.
func (o *DvirAllOf) SetStartTime(v map[string]interface{}) {
	o.StartTime = &v
}

// GetThirdSignature returns the ThirdSignature field value if set, zero value otherwise.
func (o *DvirAllOf) GetThirdSignature() map[string]interface{} {
	if o == nil || o.ThirdSignature == nil {
		var ret map[string]interface{}
		return ret
	}
	return *o.ThirdSignature
}

// GetThirdSignatureOk returns a tuple with the ThirdSignature field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetThirdSignatureOk() (map[string]interface{}, bool) {
	if o == nil || o.ThirdSignature == nil {
		var ret map[string]interface{}
		return ret, false
	}
	return *o.ThirdSignature, true
}

// HasThirdSignature returns a boolean if a field has been set.
func (o *DvirAllOf) HasThirdSignature() bool {
	if o != nil && o.ThirdSignature != nil {
		return true
	}

	return false
}

// SetThirdSignature gets a reference to the given map[string]interface{} and assigns it to the ThirdSignature field.
func (o *DvirAllOf) SetThirdSignature(v map[string]interface{}) {
	o.ThirdSignature = &v
}

// GetTrailer returns the Trailer field value if set, zero value otherwise.
func (o *DvirAllOf) GetTrailer() map[string]interface{} {
	if o == nil || o.Trailer == nil {
		var ret map[string]interface{}
		return ret
	}
	return *o.Trailer
}

// GetTrailerOk returns a tuple with the Trailer field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetTrailerOk() (map[string]interface{}, bool) {
	if o == nil || o.Trailer == nil {
		var ret map[string]interface{}
		return ret, false
	}
	return *o.Trailer, true
}

// HasTrailer returns a boolean if a field has been set.
func (o *DvirAllOf) HasTrailer() bool {
	if o != nil && o.Trailer != nil {
		return true
	}

	return false
}

// SetTrailer gets a reference to the given map[string]interface{} and assigns it to the Trailer field.
func (o *DvirAllOf) SetTrailer(v map[string]interface{}) {
	o.Trailer = &v
}

// GetTrailerDefects returns the TrailerDefects field value if set, zero value otherwise.
func (o *DvirAllOf) GetTrailerDefects() []DvirAllOf0TrailerDefectsItems {
	if o == nil || o.TrailerDefects == nil {
		var ret []DvirAllOf0TrailerDefectsItems
		return ret
	}
	return *o.TrailerDefects
}

// GetTrailerDefectsOk returns a tuple with the TrailerDefects field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetTrailerDefectsOk() ([]DvirAllOf0TrailerDefectsItems, bool) {
	if o == nil || o.TrailerDefects == nil {
		var ret []DvirAllOf0TrailerDefectsItems
		return ret, false
	}
	return *o.TrailerDefects, true
}

// HasTrailerDefects returns a boolean if a field has been set.
func (o *DvirAllOf) HasTrailerDefects() bool {
	if o != nil && o.TrailerDefects != nil {
		return true
	}

	return false
}

// SetTrailerDefects gets a reference to the given []DvirAllOf0TrailerDefectsItems and assigns it to the TrailerDefects field.
func (o *DvirAllOf) SetTrailerDefects(v []DvirAllOf0TrailerDefectsItems) {
	o.TrailerDefects = &v
}

// GetTrailerName returns the TrailerName field value if set, zero value otherwise.
func (o *DvirAllOf) GetTrailerName() string {
	if o == nil || o.TrailerName == nil {
		var ret string
		return ret
	}
	return *o.TrailerName
}

// GetTrailerNameOk returns a tuple with the TrailerName field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetTrailerNameOk() (string, bool) {
	if o == nil || o.TrailerName == nil {
		var ret string
		return ret, false
	}
	return *o.TrailerName, true
}

// HasTrailerName returns a boolean if a field has been set.
func (o *DvirAllOf) HasTrailerName() bool {
	if o != nil && o.TrailerName != nil {
		return true
	}

	return false
}

// SetTrailerName gets a reference to the given string and assigns it to the TrailerName field.
func (o *DvirAllOf) SetTrailerName(v string) {
	o.TrailerName = &v
}

// GetType returns the Type field value if set, zero value otherwise.
func (o *DvirAllOf) GetType() string {
	if o == nil || o.Type == nil {
		var ret string
		return ret
	}
	return *o.Type
}

// GetTypeOk returns a tuple with the Type field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetTypeOk() (string, bool) {
	if o == nil || o.Type == nil {
		var ret string
		return ret, false
	}
	return *o.Type, true
}

// HasType returns a boolean if a field has been set.
func (o *DvirAllOf) HasType() bool {
	if o != nil && o.Type != nil {
		return true
	}

	return false
}

// SetType gets a reference to the given string and assigns it to the Type field.
func (o *DvirAllOf) SetType(v string) {
	o.Type = &v
}

// GetVehicle returns the Vehicle field value if set, zero value otherwise.
func (o *DvirAllOf) GetVehicle() map[string]interface{} {
	if o == nil || o.Vehicle == nil {
		var ret map[string]interface{}
		return ret
	}
	return *o.Vehicle
}

// GetVehicleOk returns a tuple with the Vehicle field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetVehicleOk() (map[string]interface{}, bool) {
	if o == nil || o.Vehicle == nil {
		var ret map[string]interface{}
		return ret, false
	}
	return *o.Vehicle, true
}

// HasVehicle returns a boolean if a field has been set.
func (o *DvirAllOf) HasVehicle() bool {
	if o != nil && o.Vehicle != nil {
		return true
	}

	return false
}

// SetVehicle gets a reference to the given map[string]interface{} and assigns it to the Vehicle field.
func (o *DvirAllOf) SetVehicle(v map[string]interface{}) {
	o.Vehicle = &v
}

// GetVehicleDefects returns the VehicleDefects field value if set, zero value otherwise.
func (o *DvirAllOf) GetVehicleDefects() []DvirAllOf0TrailerDefectsItems {
	if o == nil || o.VehicleDefects == nil {
		var ret []DvirAllOf0TrailerDefectsItems
		return ret
	}
	return *o.VehicleDefects
}

// GetVehicleDefectsOk returns a tuple with the VehicleDefects field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *DvirAllOf) GetVehicleDefectsOk() ([]DvirAllOf0TrailerDefectsItems, bool) {
	if o == nil || o.VehicleDefects == nil {
		var ret []DvirAllOf0TrailerDefectsItems
		return ret, false
	}
	return *o.VehicleDefects, true
}

// HasVehicleDefects returns a boolean if a field has been set.
func (o *DvirAllOf) HasVehicleDefects() bool {
	if o != nil && o.VehicleDefects != nil {
		return true
	}

	return false
}

// SetVehicleDefects gets a reference to the given []DvirAllOf0TrailerDefectsItems and assigns it to the VehicleDefects field.
func (o *DvirAllOf) SetVehicleDefects(v []DvirAllOf0TrailerDefectsItems) {
	o.VehicleDefects = &v
}

type NullableDvirAllOf struct {
	Value        DvirAllOf
	ExplicitNull bool
}

func (v NullableDvirAllOf) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableDvirAllOf) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}
