# V1TrailerAssignmentsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int64** | ID of the trailer | 
**Name** | Pointer to **string** | Assignment trailer name (given when creating trailer via the trailer portal) | 
**TrailerAssignments** | Pointer to [**[]V1TrailerAssignmentResponse**](V1TrailerAssignmentResponse.md) |  | [optional] 

## Methods

### GetId

`func (o *V1TrailerAssignmentsResponse) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1TrailerAssignmentsResponse) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1TrailerAssignmentsResponse) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1TrailerAssignmentsResponse) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetName

`func (o *V1TrailerAssignmentsResponse) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *V1TrailerAssignmentsResponse) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *V1TrailerAssignmentsResponse) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *V1TrailerAssignmentsResponse) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetTrailerAssignments

`func (o *V1TrailerAssignmentsResponse) GetTrailerAssignments() []V1TrailerAssignmentResponse`

GetTrailerAssignments returns the TrailerAssignments field if non-nil, zero value otherwise.

### GetTrailerAssignmentsOk

`func (o *V1TrailerAssignmentsResponse) GetTrailerAssignmentsOk() ([]V1TrailerAssignmentResponse, bool)`

GetTrailerAssignmentsOk returns a tuple with the TrailerAssignments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerAssignments

`func (o *V1TrailerAssignmentsResponse) HasTrailerAssignments() bool`

HasTrailerAssignments returns a boolean if a field has been set.

### SetTrailerAssignments

`func (o *V1TrailerAssignmentsResponse) SetTrailerAssignments(v []V1TrailerAssignmentResponse)`

SetTrailerAssignments gets a reference to the given []V1TrailerAssignmentResponse and assigns it to the TrailerAssignments field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


