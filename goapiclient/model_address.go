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

// Address An Address object.
type Address struct {
	// Reporting location type associated with the address (used for ELD reporting purposes).
	AddressTypes *[]string `json:"addressTypes,omitempty"`
	// An array Contact mini-objects that are associated the Address.
	Contacts *[]ContactTinyResponse `json:"contacts,omitempty"`
	// User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (`\"\"`). An external ID can be used as a path parameter to retrieve or update that resource.
	ExternalIds *map[string]string `json:"externalIds,omitempty"`
	// The full street address for this address/geofence, as it might be recognized by Google Maps.
	FormattedAddress string          `json:"formattedAddress"`
	Geofence         AddressGeofence `json:"geofence"`
	// ID of the Address.
	Id string `json:"id"`
	// Latitude of the address. Will be geocoded from `formattedAddress` if not provided.
	Latitude *float64 `json:"latitude,omitempty"`
	// Longitude of the address. Will be geocoded from `formattedAddress` if not provided.
	Longitude *float64 `json:"longitude,omitempty"`
	// Name of the address.
	Name string `json:"name"`
	// Notes about the address.
	Notes *string `json:"notes,omitempty"`
	// An array of all tag mini-objects that are associated with the given address entry.
	Tags *[]TagTinyResponse `json:"tags,omitempty"`
}

// GetAddressTypes returns the AddressTypes field value if set, zero value otherwise.
func (o *Address) GetAddressTypes() []string {
	if o == nil || o.AddressTypes == nil {
		var ret []string
		return ret
	}
	return *o.AddressTypes
}

// GetAddressTypesOk returns a tuple with the AddressTypes field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Address) GetAddressTypesOk() ([]string, bool) {
	if o == nil || o.AddressTypes == nil {
		var ret []string
		return ret, false
	}
	return *o.AddressTypes, true
}

// HasAddressTypes returns a boolean if a field has been set.
func (o *Address) HasAddressTypes() bool {
	if o != nil && o.AddressTypes != nil {
		return true
	}

	return false
}

// SetAddressTypes gets a reference to the given []string and assigns it to the AddressTypes field.
func (o *Address) SetAddressTypes(v []string) {
	o.AddressTypes = &v
}

// GetContacts returns the Contacts field value if set, zero value otherwise.
func (o *Address) GetContacts() []ContactTinyResponse {
	if o == nil || o.Contacts == nil {
		var ret []ContactTinyResponse
		return ret
	}
	return *o.Contacts
}

// GetContactsOk returns a tuple with the Contacts field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Address) GetContactsOk() ([]ContactTinyResponse, bool) {
	if o == nil || o.Contacts == nil {
		var ret []ContactTinyResponse
		return ret, false
	}
	return *o.Contacts, true
}

// HasContacts returns a boolean if a field has been set.
func (o *Address) HasContacts() bool {
	if o != nil && o.Contacts != nil {
		return true
	}

	return false
}

// SetContacts gets a reference to the given []ContactTinyResponse and assigns it to the Contacts field.
func (o *Address) SetContacts(v []ContactTinyResponse) {
	o.Contacts = &v
}

// GetExternalIds returns the ExternalIds field value if set, zero value otherwise.
func (o *Address) GetExternalIds() map[string]string {
	if o == nil || o.ExternalIds == nil {
		var ret map[string]string
		return ret
	}
	return *o.ExternalIds
}

// GetExternalIdsOk returns a tuple with the ExternalIds field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Address) GetExternalIdsOk() (map[string]string, bool) {
	if o == nil || o.ExternalIds == nil {
		var ret map[string]string
		return ret, false
	}
	return *o.ExternalIds, true
}

// HasExternalIds returns a boolean if a field has been set.
func (o *Address) HasExternalIds() bool {
	if o != nil && o.ExternalIds != nil {
		return true
	}

	return false
}

// SetExternalIds gets a reference to the given map[string]string and assigns it to the ExternalIds field.
func (o *Address) SetExternalIds(v map[string]string) {
	o.ExternalIds = &v
}

// GetFormattedAddress returns the FormattedAddress field value
func (o *Address) GetFormattedAddress() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.FormattedAddress
}

// SetFormattedAddress sets field value
func (o *Address) SetFormattedAddress(v string) {
	o.FormattedAddress = v
}

// GetGeofence returns the Geofence field value
func (o *Address) GetGeofence() AddressGeofence {
	if o == nil {
		var ret AddressGeofence
		return ret
	}

	return o.Geofence
}

// SetGeofence sets field value
func (o *Address) SetGeofence(v AddressGeofence) {
	o.Geofence = v
}

// GetId returns the Id field value
func (o *Address) GetId() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Id
}

// SetId sets field value
func (o *Address) SetId(v string) {
	o.Id = v
}

// GetLatitude returns the Latitude field value if set, zero value otherwise.
func (o *Address) GetLatitude() float64 {
	if o == nil || o.Latitude == nil {
		var ret float64
		return ret
	}
	return *o.Latitude
}

// GetLatitudeOk returns a tuple with the Latitude field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Address) GetLatitudeOk() (float64, bool) {
	if o == nil || o.Latitude == nil {
		var ret float64
		return ret, false
	}
	return *o.Latitude, true
}

// HasLatitude returns a boolean if a field has been set.
func (o *Address) HasLatitude() bool {
	if o != nil && o.Latitude != nil {
		return true
	}

	return false
}

// SetLatitude gets a reference to the given float64 and assigns it to the Latitude field.
func (o *Address) SetLatitude(v float64) {
	o.Latitude = &v
}

// GetLongitude returns the Longitude field value if set, zero value otherwise.
func (o *Address) GetLongitude() float64 {
	if o == nil || o.Longitude == nil {
		var ret float64
		return ret
	}
	return *o.Longitude
}

// GetLongitudeOk returns a tuple with the Longitude field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Address) GetLongitudeOk() (float64, bool) {
	if o == nil || o.Longitude == nil {
		var ret float64
		return ret, false
	}
	return *o.Longitude, true
}

// HasLongitude returns a boolean if a field has been set.
func (o *Address) HasLongitude() bool {
	if o != nil && o.Longitude != nil {
		return true
	}

	return false
}

// SetLongitude gets a reference to the given float64 and assigns it to the Longitude field.
func (o *Address) SetLongitude(v float64) {
	o.Longitude = &v
}

// GetName returns the Name field value
func (o *Address) GetName() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Name
}

// SetName sets field value
func (o *Address) SetName(v string) {
	o.Name = v
}

// GetNotes returns the Notes field value if set, zero value otherwise.
func (o *Address) GetNotes() string {
	if o == nil || o.Notes == nil {
		var ret string
		return ret
	}
	return *o.Notes
}

// GetNotesOk returns a tuple with the Notes field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Address) GetNotesOk() (string, bool) {
	if o == nil || o.Notes == nil {
		var ret string
		return ret, false
	}
	return *o.Notes, true
}

// HasNotes returns a boolean if a field has been set.
func (o *Address) HasNotes() bool {
	if o != nil && o.Notes != nil {
		return true
	}

	return false
}

// SetNotes gets a reference to the given string and assigns it to the Notes field.
func (o *Address) SetNotes(v string) {
	o.Notes = &v
}

// GetTags returns the Tags field value if set, zero value otherwise.
func (o *Address) GetTags() []TagTinyResponse {
	if o == nil || o.Tags == nil {
		var ret []TagTinyResponse
		return ret
	}
	return *o.Tags
}

// GetTagsOk returns a tuple with the Tags field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Address) GetTagsOk() ([]TagTinyResponse, bool) {
	if o == nil || o.Tags == nil {
		var ret []TagTinyResponse
		return ret, false
	}
	return *o.Tags, true
}

// HasTags returns a boolean if a field has been set.
func (o *Address) HasTags() bool {
	if o != nil && o.Tags != nil {
		return true
	}

	return false
}

// SetTags gets a reference to the given []TagTinyResponse and assigns it to the Tags field.
func (o *Address) SetTags(v []TagTinyResponse) {
	o.Tags = &v
}

type NullableAddress struct {
	Value        Address
	ExplicitNull bool
}

func (v NullableAddress) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableAddress) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}
