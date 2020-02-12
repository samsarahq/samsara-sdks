# V1DispatchJobUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int64** | ID of the Samsara dispatch job to update | 
**DestinationAddress** | Pointer to **string** | The address of the job destination, as it would be recognized if provided to maps.google.com. Optional if a valid destination address ID is provided. | [optional] 
**DestinationAddressId** | Pointer to **int64** | ID of the job destination associated with an address book entry. Optional if valid values are provided for destination address and latitude/longitude. If a valid destination address ID is provided, address/latitude/longitude will be used from the address book entry. Name of the address book entry will only be used if the destination name is not provided. | [optional] 
**DestinationLat** | Pointer to **float64** | Latitude of the destination in decimal degrees. Optional if a valid destination address ID is provided. | [optional] 
**DestinationLng** | Pointer to **float64** | Longitude of the destination in decimal degrees. Optional if a valid destination address ID is provided. | [optional] 
**DestinationName** | Pointer to **string** | The name of the job destination. If provided, it will take precedence over the name of the address book entry. | [optional] 
**Notes** | Pointer to **string** | Notes regarding the details of this job, maximum of 2000 characters; newline characters (&#39;\\n&#39;)can be used for formatting. | [optional] 
**ScheduledArrivalTimeMs** | Pointer to **int64** | The time at which the assigned driver is scheduled to arrive at the job destination. | 
**ScheduledDepartureTimeMs** | Pointer to **int64** | The time at which the assigned driver is scheduled to depart from the job destination. | [optional] 

## Methods

### GetId

`func (o *V1DispatchJobUpdate) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1DispatchJobUpdate) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1DispatchJobUpdate) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1DispatchJobUpdate) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetDestinationAddress

`func (o *V1DispatchJobUpdate) GetDestinationAddress() string`

GetDestinationAddress returns the DestinationAddress field if non-nil, zero value otherwise.

### GetDestinationAddressOk

`func (o *V1DispatchJobUpdate) GetDestinationAddressOk() (string, bool)`

GetDestinationAddressOk returns a tuple with the DestinationAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationAddress

`func (o *V1DispatchJobUpdate) HasDestinationAddress() bool`

HasDestinationAddress returns a boolean if a field has been set.

### SetDestinationAddress

`func (o *V1DispatchJobUpdate) SetDestinationAddress(v string)`

SetDestinationAddress gets a reference to the given string and assigns it to the DestinationAddress field.

### GetDestinationAddressId

`func (o *V1DispatchJobUpdate) GetDestinationAddressId() int64`

GetDestinationAddressId returns the DestinationAddressId field if non-nil, zero value otherwise.

### GetDestinationAddressIdOk

`func (o *V1DispatchJobUpdate) GetDestinationAddressIdOk() (int64, bool)`

GetDestinationAddressIdOk returns a tuple with the DestinationAddressId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationAddressId

`func (o *V1DispatchJobUpdate) HasDestinationAddressId() bool`

HasDestinationAddressId returns a boolean if a field has been set.

### SetDestinationAddressId

`func (o *V1DispatchJobUpdate) SetDestinationAddressId(v int64)`

SetDestinationAddressId gets a reference to the given int64 and assigns it to the DestinationAddressId field.

### GetDestinationLat

`func (o *V1DispatchJobUpdate) GetDestinationLat() float64`

GetDestinationLat returns the DestinationLat field if non-nil, zero value otherwise.

### GetDestinationLatOk

`func (o *V1DispatchJobUpdate) GetDestinationLatOk() (float64, bool)`

GetDestinationLatOk returns a tuple with the DestinationLat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationLat

`func (o *V1DispatchJobUpdate) HasDestinationLat() bool`

HasDestinationLat returns a boolean if a field has been set.

### SetDestinationLat

`func (o *V1DispatchJobUpdate) SetDestinationLat(v float64)`

SetDestinationLat gets a reference to the given float64 and assigns it to the DestinationLat field.

### GetDestinationLng

`func (o *V1DispatchJobUpdate) GetDestinationLng() float64`

GetDestinationLng returns the DestinationLng field if non-nil, zero value otherwise.

### GetDestinationLngOk

`func (o *V1DispatchJobUpdate) GetDestinationLngOk() (float64, bool)`

GetDestinationLngOk returns a tuple with the DestinationLng field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationLng

`func (o *V1DispatchJobUpdate) HasDestinationLng() bool`

HasDestinationLng returns a boolean if a field has been set.

### SetDestinationLng

`func (o *V1DispatchJobUpdate) SetDestinationLng(v float64)`

SetDestinationLng gets a reference to the given float64 and assigns it to the DestinationLng field.

### GetDestinationName

`func (o *V1DispatchJobUpdate) GetDestinationName() string`

GetDestinationName returns the DestinationName field if non-nil, zero value otherwise.

### GetDestinationNameOk

`func (o *V1DispatchJobUpdate) GetDestinationNameOk() (string, bool)`

GetDestinationNameOk returns a tuple with the DestinationName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDestinationName

`func (o *V1DispatchJobUpdate) HasDestinationName() bool`

HasDestinationName returns a boolean if a field has been set.

### SetDestinationName

`func (o *V1DispatchJobUpdate) SetDestinationName(v string)`

SetDestinationName gets a reference to the given string and assigns it to the DestinationName field.

### GetNotes

`func (o *V1DispatchJobUpdate) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *V1DispatchJobUpdate) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *V1DispatchJobUpdate) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *V1DispatchJobUpdate) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetScheduledArrivalTimeMs

`func (o *V1DispatchJobUpdate) GetScheduledArrivalTimeMs() int64`

GetScheduledArrivalTimeMs returns the ScheduledArrivalTimeMs field if non-nil, zero value otherwise.

### GetScheduledArrivalTimeMsOk

`func (o *V1DispatchJobUpdate) GetScheduledArrivalTimeMsOk() (int64, bool)`

GetScheduledArrivalTimeMsOk returns a tuple with the ScheduledArrivalTimeMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledArrivalTimeMs

`func (o *V1DispatchJobUpdate) HasScheduledArrivalTimeMs() bool`

HasScheduledArrivalTimeMs returns a boolean if a field has been set.

### SetScheduledArrivalTimeMs

`func (o *V1DispatchJobUpdate) SetScheduledArrivalTimeMs(v int64)`

SetScheduledArrivalTimeMs gets a reference to the given int64 and assigns it to the ScheduledArrivalTimeMs field.

### GetScheduledDepartureTimeMs

`func (o *V1DispatchJobUpdate) GetScheduledDepartureTimeMs() int64`

GetScheduledDepartureTimeMs returns the ScheduledDepartureTimeMs field if non-nil, zero value otherwise.

### GetScheduledDepartureTimeMsOk

`func (o *V1DispatchJobUpdate) GetScheduledDepartureTimeMsOk() (int64, bool)`

GetScheduledDepartureTimeMsOk returns a tuple with the ScheduledDepartureTimeMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledDepartureTimeMs

`func (o *V1DispatchJobUpdate) HasScheduledDepartureTimeMs() bool`

HasScheduledDepartureTimeMs returns a boolean if a field has been set.

### SetScheduledDepartureTimeMs

`func (o *V1DispatchJobUpdate) SetScheduledDepartureTimeMs(v int64)`

SetScheduledDepartureTimeMs gets a reference to the given int64 and assigns it to the ScheduledDepartureTimeMs field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


