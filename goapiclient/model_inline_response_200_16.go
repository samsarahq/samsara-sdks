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

// InlineResponse20016 struct for InlineResponse20016
type InlineResponse20016 struct {
	Assets     *[]V1AssetCurrentLocationsResponse `json:"assets,omitempty"`
	Pagination *V1Pagination                      `json:"pagination,omitempty"`
}

// GetAssets returns the Assets field value if set, zero value otherwise.
func (o *InlineResponse20016) GetAssets() []V1AssetCurrentLocationsResponse {
	if o == nil || o.Assets == nil {
		var ret []V1AssetCurrentLocationsResponse
		return ret
	}
	return *o.Assets
}

// GetAssetsOk returns a tuple with the Assets field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *InlineResponse20016) GetAssetsOk() ([]V1AssetCurrentLocationsResponse, bool) {
	if o == nil || o.Assets == nil {
		var ret []V1AssetCurrentLocationsResponse
		return ret, false
	}
	return *o.Assets, true
}

// HasAssets returns a boolean if a field has been set.
func (o *InlineResponse20016) HasAssets() bool {
	if o != nil && o.Assets != nil {
		return true
	}

	return false
}

// SetAssets gets a reference to the given []V1AssetCurrentLocationsResponse and assigns it to the Assets field.
func (o *InlineResponse20016) SetAssets(v []V1AssetCurrentLocationsResponse) {
	o.Assets = &v
}

// GetPagination returns the Pagination field value if set, zero value otherwise.
func (o *InlineResponse20016) GetPagination() V1Pagination {
	if o == nil || o.Pagination == nil {
		var ret V1Pagination
		return ret
	}
	return *o.Pagination
}

// GetPaginationOk returns a tuple with the Pagination field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *InlineResponse20016) GetPaginationOk() (V1Pagination, bool) {
	if o == nil || o.Pagination == nil {
		var ret V1Pagination
		return ret, false
	}
	return *o.Pagination, true
}

// HasPagination returns a boolean if a field has been set.
func (o *InlineResponse20016) HasPagination() bool {
	if o != nil && o.Pagination != nil {
		return true
	}

	return false
}

// SetPagination gets a reference to the given V1Pagination and assigns it to the Pagination field.
func (o *InlineResponse20016) SetPagination(v V1Pagination) {
	o.Pagination = &v
}

type NullableInlineResponse20016 struct {
	Value        InlineResponse20016
	ExplicitNull bool
}

func (v NullableInlineResponse20016) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableInlineResponse20016) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}
