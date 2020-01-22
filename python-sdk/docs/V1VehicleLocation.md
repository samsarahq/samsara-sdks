# V1VehicleLocation

Contains the location, in latitude and longitude, of a vehicle.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver_id** | **int** | The ID of the driver currently assigned to this vehicle. | [optional] 
**heading** | **float** | Heading in degrees. | [optional] 
**id** | **int** | ID of the vehicle. | 
**latitude** | **float** | Latitude in decimal degrees. | [optional] 
**location** | **str** | Text representation of nearest identifiable location to (latitude, longitude) coordinates. | [optional] 
**longitude** | **float** | Longitude in decimal degrees. | [optional] 
**name** | **str** | Name of the vehicle. | [optional] 
**odometer_meters** | **int** | The number of meters reported by the odometer. | [optional] 
**odometer_type** | **str** | The source of data for odometerMeters. Will be either GPS or OBD | [optional] 
**on_trip** | **bool** | Whether or not a trip is currently in progress for this vehicle. More information available via /fleet/trips endpoint. | [optional] 
**route_ids** | **list[int]** | A list of currently active route IDs that the vehicle is in. | [optional] 
**speed** | **float** | Speed in miles per hour. | [optional] 
**time** | **int** | The time the reported location was logged, reported as a UNIX timestamp in milliseconds. | [optional] 
**vin** | **str** | Vehicle Identification Number (VIN) of the vehicle. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


