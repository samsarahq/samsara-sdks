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

// RouteStop A single route stop for a route.
type RouteStop struct {
	// Actual arrival time, if it exists, for the route stop in RFC 3339 format.
	ActualArrivalTime *string `json:"actualArrivalTime,omitempty"`
	// Actual departure time, if it exists, for the route stop in RFC 3339 format.
	ActualDepartureTime *string `json:"actualDepartureTime,omitempty"`
	// The documents associated with the stop.
	Documents *[]RouteStopDocuments `json:"documents,omitempty"`
	// Unique identifier for the route stop.
	Id *string `json:"id,omitempty"`
	// The live share URL for the stop.
	LiveShareUrl *string `json:"liveShareUrl,omitempty"`
	// Route stop notes.
	Notes *string `json:"notes,omitempty"`
	// Scheduled arrival time for the route stop in RFC 3339 format.
	ScheduledArrivalTime *string `json:"scheduledArrivalTime,omitempty"`
	// Scheduled departure time for the route stop in RFC 3339 format.
	ScheduledDepartureTime *string `json:"scheduledDepartureTime,omitempty"`
	// Skipped time, if it exists, for the route stop in RFC 3339 format.
	SkippedTime *string `json:"skippedTime,omitempty"`
	// The current state of the route stop.
	State        *string        `json:"state,omitempty"`
	StopLocation *RouteLocation `json:"stopLocation,omitempty"`
}

// GetActualArrivalTime returns the ActualArrivalTime field value if set, zero value otherwise.
func (o *RouteStop) GetActualArrivalTime() string {
	if o == nil || o.ActualArrivalTime == nil {
		var ret string
		return ret
	}
	return *o.ActualArrivalTime
}

// GetActualArrivalTimeOk returns a tuple with the ActualArrivalTime field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *RouteStop) GetActualArrivalTimeOk() (string, bool) {
	if o == nil || o.ActualArrivalTime == nil {
		var ret string
		return ret, false
	}
	return *o.ActualArrivalTime, true
}

// HasActualArrivalTime returns a boolean if a field has been set.
func (o *RouteStop) HasActualArrivalTime() bool {
	if o != nil && o.ActualArrivalTime != nil {
		return true
	}

	return false
}

// SetActualArrivalTime gets a reference to the given string and assigns it to the ActualArrivalTime field.
func (o *RouteStop) SetActualArrivalTime(v string) {
	o.ActualArrivalTime = &v
}

// GetActualDepartureTime returns the ActualDepartureTime field value if set, zero value otherwise.
func (o *RouteStop) GetActualDepartureTime() string {
	if o == nil || o.ActualDepartureTime == nil {
		var ret string
		return ret
	}
	return *o.ActualDepartureTime
}

// GetActualDepartureTimeOk returns a tuple with the ActualDepartureTime field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *RouteStop) GetActualDepartureTimeOk() (string, bool) {
	if o == nil || o.ActualDepartureTime == nil {
		var ret string
		return ret, false
	}
	return *o.ActualDepartureTime, true
}

// HasActualDepartureTime returns a boolean if a field has been set.
func (o *RouteStop) HasActualDepartureTime() bool {
	if o != nil && o.ActualDepartureTime != nil {
		return true
	}

	return false
}

// SetActualDepartureTime gets a reference to the given string and assigns it to the ActualDepartureTime field.
func (o *RouteStop) SetActualDepartureTime(v string) {
	o.ActualDepartureTime = &v
}

// GetDocuments returns the Documents field value if set, zero value otherwise.
func (o *RouteStop) GetDocuments() []RouteStopDocuments {
	if o == nil || o.Documents == nil {
		var ret []RouteStopDocuments
		return ret
	}
	return *o.Documents
}

// GetDocumentsOk returns a tuple with the Documents field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *RouteStop) GetDocumentsOk() ([]RouteStopDocuments, bool) {
	if o == nil || o.Documents == nil {
		var ret []RouteStopDocuments
		return ret, false
	}
	return *o.Documents, true
}

// HasDocuments returns a boolean if a field has been set.
func (o *RouteStop) HasDocuments() bool {
	if o != nil && o.Documents != nil {
		return true
	}

	return false
}

// SetDocuments gets a reference to the given []RouteStopDocuments and assigns it to the Documents field.
func (o *RouteStop) SetDocuments(v []RouteStopDocuments) {
	o.Documents = &v
}

// GetId returns the Id field value if set, zero value otherwise.
func (o *RouteStop) GetId() string {
	if o == nil || o.Id == nil {
		var ret string
		return ret
	}
	return *o.Id
}

// GetIdOk returns a tuple with the Id field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *RouteStop) GetIdOk() (string, bool) {
	if o == nil || o.Id == nil {
		var ret string
		return ret, false
	}
	return *o.Id, true
}

// HasId returns a boolean if a field has been set.
func (o *RouteStop) HasId() bool {
	if o != nil && o.Id != nil {
		return true
	}

	return false
}

// SetId gets a reference to the given string and assigns it to the Id field.
func (o *RouteStop) SetId(v string) {
	o.Id = &v
}

// GetLiveShareUrl returns the LiveShareUrl field value if set, zero value otherwise.
func (o *RouteStop) GetLiveShareUrl() string {
	if o == nil || o.LiveShareUrl == nil {
		var ret string
		return ret
	}
	return *o.LiveShareUrl
}

// GetLiveShareUrlOk returns a tuple with the LiveShareUrl field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *RouteStop) GetLiveShareUrlOk() (string, bool) {
	if o == nil || o.LiveShareUrl == nil {
		var ret string
		return ret, false
	}
	return *o.LiveShareUrl, true
}

// HasLiveShareUrl returns a boolean if a field has been set.
func (o *RouteStop) HasLiveShareUrl() bool {
	if o != nil && o.LiveShareUrl != nil {
		return true
	}

	return false
}

// SetLiveShareUrl gets a reference to the given string and assigns it to the LiveShareUrl field.
func (o *RouteStop) SetLiveShareUrl(v string) {
	o.LiveShareUrl = &v
}

// GetNotes returns the Notes field value if set, zero value otherwise.
func (o *RouteStop) GetNotes() string {
	if o == nil || o.Notes == nil {
		var ret string
		return ret
	}
	return *o.Notes
}

// GetNotesOk returns a tuple with the Notes field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *RouteStop) GetNotesOk() (string, bool) {
	if o == nil || o.Notes == nil {
		var ret string
		return ret, false
	}
	return *o.Notes, true
}

// HasNotes returns a boolean if a field has been set.
func (o *RouteStop) HasNotes() bool {
	if o != nil && o.Notes != nil {
		return true
	}

	return false
}

// SetNotes gets a reference to the given string and assigns it to the Notes field.
func (o *RouteStop) SetNotes(v string) {
	o.Notes = &v
}

// GetScheduledArrivalTime returns the ScheduledArrivalTime field value if set, zero value otherwise.
func (o *RouteStop) GetScheduledArrivalTime() string {
	if o == nil || o.ScheduledArrivalTime == nil {
		var ret string
		return ret
	}
	return *o.ScheduledArrivalTime
}

// GetScheduledArrivalTimeOk returns a tuple with the ScheduledArrivalTime field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *RouteStop) GetScheduledArrivalTimeOk() (string, bool) {
	if o == nil || o.ScheduledArrivalTime == nil {
		var ret string
		return ret, false
	}
	return *o.ScheduledArrivalTime, true
}

// HasScheduledArrivalTime returns a boolean if a field has been set.
func (o *RouteStop) HasScheduledArrivalTime() bool {
	if o != nil && o.ScheduledArrivalTime != nil {
		return true
	}

	return false
}

// SetScheduledArrivalTime gets a reference to the given string and assigns it to the ScheduledArrivalTime field.
func (o *RouteStop) SetScheduledArrivalTime(v string) {
	o.ScheduledArrivalTime = &v
}

// GetScheduledDepartureTime returns the ScheduledDepartureTime field value if set, zero value otherwise.
func (o *RouteStop) GetScheduledDepartureTime() string {
	if o == nil || o.ScheduledDepartureTime == nil {
		var ret string
		return ret
	}
	return *o.ScheduledDepartureTime
}

// GetScheduledDepartureTimeOk returns a tuple with the ScheduledDepartureTime field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *RouteStop) GetScheduledDepartureTimeOk() (string, bool) {
	if o == nil || o.ScheduledDepartureTime == nil {
		var ret string
		return ret, false
	}
	return *o.ScheduledDepartureTime, true
}

// HasScheduledDepartureTime returns a boolean if a field has been set.
func (o *RouteStop) HasScheduledDepartureTime() bool {
	if o != nil && o.ScheduledDepartureTime != nil {
		return true
	}

	return false
}

// SetScheduledDepartureTime gets a reference to the given string and assigns it to the ScheduledDepartureTime field.
func (o *RouteStop) SetScheduledDepartureTime(v string) {
	o.ScheduledDepartureTime = &v
}

// GetSkippedTime returns the SkippedTime field value if set, zero value otherwise.
func (o *RouteStop) GetSkippedTime() string {
	if o == nil || o.SkippedTime == nil {
		var ret string
		return ret
	}
	return *o.SkippedTime
}

// GetSkippedTimeOk returns a tuple with the SkippedTime field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *RouteStop) GetSkippedTimeOk() (string, bool) {
	if o == nil || o.SkippedTime == nil {
		var ret string
		return ret, false
	}
	return *o.SkippedTime, true
}

// HasSkippedTime returns a boolean if a field has been set.
func (o *RouteStop) HasSkippedTime() bool {
	if o != nil && o.SkippedTime != nil {
		return true
	}

	return false
}

// SetSkippedTime gets a reference to the given string and assigns it to the SkippedTime field.
func (o *RouteStop) SetSkippedTime(v string) {
	o.SkippedTime = &v
}

// GetState returns the State field value if set, zero value otherwise.
func (o *RouteStop) GetState() string {
	if o == nil || o.State == nil {
		var ret string
		return ret
	}
	return *o.State
}

// GetStateOk returns a tuple with the State field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *RouteStop) GetStateOk() (string, bool) {
	if o == nil || o.State == nil {
		var ret string
		return ret, false
	}
	return *o.State, true
}

// HasState returns a boolean if a field has been set.
func (o *RouteStop) HasState() bool {
	if o != nil && o.State != nil {
		return true
	}

	return false
}

// SetState gets a reference to the given string and assigns it to the State field.
func (o *RouteStop) SetState(v string) {
	o.State = &v
}

// GetStopLocation returns the StopLocation field value if set, zero value otherwise.
func (o *RouteStop) GetStopLocation() RouteLocation {
	if o == nil || o.StopLocation == nil {
		var ret RouteLocation
		return ret
	}
	return *o.StopLocation
}

// GetStopLocationOk returns a tuple with the StopLocation field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *RouteStop) GetStopLocationOk() (RouteLocation, bool) {
	if o == nil || o.StopLocation == nil {
		var ret RouteLocation
		return ret, false
	}
	return *o.StopLocation, true
}

// HasStopLocation returns a boolean if a field has been set.
func (o *RouteStop) HasStopLocation() bool {
	if o != nil && o.StopLocation != nil {
		return true
	}

	return false
}

// SetStopLocation gets a reference to the given RouteLocation and assigns it to the StopLocation field.
func (o *RouteStop) SetStopLocation(v RouteLocation) {
	o.StopLocation = &v
}

type NullableRouteStop struct {
	Value        RouteStop
	ExplicitNull bool
}

func (v NullableRouteStop) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableRouteStop) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}
