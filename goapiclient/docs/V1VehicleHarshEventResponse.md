# V1VehicleHarshEventResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DownloadForwardVideoUrl** | Pointer to **string** | URL for downloading the forward facing video | [optional] 
**DownloadInwardVideoUrl** | Pointer to **string** | URL for downloading the inward facing video | [optional] 
**DownloadTrackedInwardVideoUrl** | Pointer to **string** | URL for downloading the tracked inward facing video | [optional] 
**HarshEventType** | Pointer to **string** | Type of the harsh event. One of: [Crash, Harsh Acceleration, Harsh Braking, Harsh Turn, ROP Engine, ROP Brake, YC Engine, YC Brake, Harsh Event] | 
**IncidentReportUrl** | Pointer to **string** | URL of the associated incident report page | 
**IsDistracted** | Pointer to **bool** | Whether the driver was deemed distracted during this harsh event | [optional] 
**Location** | Pointer to [**V1VehicleHarshEventResponseLocation**](V1VehicleHarshEventResponse_location.md) |  | [optional] 

## Methods

### GetDownloadForwardVideoUrl

`func (o *V1VehicleHarshEventResponse) GetDownloadForwardVideoUrl() string`

GetDownloadForwardVideoUrl returns the DownloadForwardVideoUrl field if non-nil, zero value otherwise.

### GetDownloadForwardVideoUrlOk

`func (o *V1VehicleHarshEventResponse) GetDownloadForwardVideoUrlOk() (string, bool)`

GetDownloadForwardVideoUrlOk returns a tuple with the DownloadForwardVideoUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDownloadForwardVideoUrl

`func (o *V1VehicleHarshEventResponse) HasDownloadForwardVideoUrl() bool`

HasDownloadForwardVideoUrl returns a boolean if a field has been set.

### SetDownloadForwardVideoUrl

`func (o *V1VehicleHarshEventResponse) SetDownloadForwardVideoUrl(v string)`

SetDownloadForwardVideoUrl gets a reference to the given string and assigns it to the DownloadForwardVideoUrl field.

### GetDownloadInwardVideoUrl

`func (o *V1VehicleHarshEventResponse) GetDownloadInwardVideoUrl() string`

GetDownloadInwardVideoUrl returns the DownloadInwardVideoUrl field if non-nil, zero value otherwise.

### GetDownloadInwardVideoUrlOk

`func (o *V1VehicleHarshEventResponse) GetDownloadInwardVideoUrlOk() (string, bool)`

GetDownloadInwardVideoUrlOk returns a tuple with the DownloadInwardVideoUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDownloadInwardVideoUrl

`func (o *V1VehicleHarshEventResponse) HasDownloadInwardVideoUrl() bool`

HasDownloadInwardVideoUrl returns a boolean if a field has been set.

### SetDownloadInwardVideoUrl

`func (o *V1VehicleHarshEventResponse) SetDownloadInwardVideoUrl(v string)`

SetDownloadInwardVideoUrl gets a reference to the given string and assigns it to the DownloadInwardVideoUrl field.

### GetDownloadTrackedInwardVideoUrl

`func (o *V1VehicleHarshEventResponse) GetDownloadTrackedInwardVideoUrl() string`

GetDownloadTrackedInwardVideoUrl returns the DownloadTrackedInwardVideoUrl field if non-nil, zero value otherwise.

### GetDownloadTrackedInwardVideoUrlOk

`func (o *V1VehicleHarshEventResponse) GetDownloadTrackedInwardVideoUrlOk() (string, bool)`

GetDownloadTrackedInwardVideoUrlOk returns a tuple with the DownloadTrackedInwardVideoUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDownloadTrackedInwardVideoUrl

`func (o *V1VehicleHarshEventResponse) HasDownloadTrackedInwardVideoUrl() bool`

HasDownloadTrackedInwardVideoUrl returns a boolean if a field has been set.

### SetDownloadTrackedInwardVideoUrl

`func (o *V1VehicleHarshEventResponse) SetDownloadTrackedInwardVideoUrl(v string)`

SetDownloadTrackedInwardVideoUrl gets a reference to the given string and assigns it to the DownloadTrackedInwardVideoUrl field.

### GetHarshEventType

`func (o *V1VehicleHarshEventResponse) GetHarshEventType() string`

GetHarshEventType returns the HarshEventType field if non-nil, zero value otherwise.

### GetHarshEventTypeOk

`func (o *V1VehicleHarshEventResponse) GetHarshEventTypeOk() (string, bool)`

GetHarshEventTypeOk returns a tuple with the HarshEventType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasHarshEventType

`func (o *V1VehicleHarshEventResponse) HasHarshEventType() bool`

HasHarshEventType returns a boolean if a field has been set.

### SetHarshEventType

`func (o *V1VehicleHarshEventResponse) SetHarshEventType(v string)`

SetHarshEventType gets a reference to the given string and assigns it to the HarshEventType field.

### GetIncidentReportUrl

`func (o *V1VehicleHarshEventResponse) GetIncidentReportUrl() string`

GetIncidentReportUrl returns the IncidentReportUrl field if non-nil, zero value otherwise.

### GetIncidentReportUrlOk

`func (o *V1VehicleHarshEventResponse) GetIncidentReportUrlOk() (string, bool)`

GetIncidentReportUrlOk returns a tuple with the IncidentReportUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasIncidentReportUrl

`func (o *V1VehicleHarshEventResponse) HasIncidentReportUrl() bool`

HasIncidentReportUrl returns a boolean if a field has been set.

### SetIncidentReportUrl

`func (o *V1VehicleHarshEventResponse) SetIncidentReportUrl(v string)`

SetIncidentReportUrl gets a reference to the given string and assigns it to the IncidentReportUrl field.

### GetIsDistracted

`func (o *V1VehicleHarshEventResponse) GetIsDistracted() bool`

GetIsDistracted returns the IsDistracted field if non-nil, zero value otherwise.

### GetIsDistractedOk

`func (o *V1VehicleHarshEventResponse) GetIsDistractedOk() (bool, bool)`

GetIsDistractedOk returns a tuple with the IsDistracted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasIsDistracted

`func (o *V1VehicleHarshEventResponse) HasIsDistracted() bool`

HasIsDistracted returns a boolean if a field has been set.

### SetIsDistracted

`func (o *V1VehicleHarshEventResponse) SetIsDistracted(v bool)`

SetIsDistracted gets a reference to the given bool and assigns it to the IsDistracted field.

### GetLocation

`func (o *V1VehicleHarshEventResponse) GetLocation() V1VehicleHarshEventResponseLocation`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *V1VehicleHarshEventResponse) GetLocationOk() (V1VehicleHarshEventResponseLocation, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocation

`func (o *V1VehicleHarshEventResponse) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### SetLocation

`func (o *V1VehicleHarshEventResponse) SetLocation(v V1VehicleHarshEventResponseLocation)`

SetLocation gets a reference to the given V1VehicleHarshEventResponseLocation and assigns it to the Location field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


