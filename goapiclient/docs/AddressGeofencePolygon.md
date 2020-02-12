# AddressGeofencePolygon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Vertices** | Pointer to [**[]AddressGeofencePolygonVertices**](AddressGeofence_polygon_vertices.md) | The vertices of the polygon geofence. These geofence vertices describe the perimeter of the polygon, and must consist of at least 3 vertices and less than 40. | 

## Methods

### GetVertices

`func (o *AddressGeofencePolygon) GetVertices() []AddressGeofencePolygonVertices`

GetVertices returns the Vertices field if non-nil, zero value otherwise.

### GetVerticesOk

`func (o *AddressGeofencePolygon) GetVerticesOk() ([]AddressGeofencePolygonVertices, bool)`

GetVerticesOk returns a tuple with the Vertices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVertices

`func (o *AddressGeofencePolygon) HasVertices() bool`

HasVertices returns a boolean if a field has been set.

### SetVertices

`func (o *AddressGeofencePolygon) SetVertices(v []AddressGeofencePolygonVertices)`

SetVertices gets a reference to the given []AddressGeofencePolygonVertices and assigns it to the Vertices field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


