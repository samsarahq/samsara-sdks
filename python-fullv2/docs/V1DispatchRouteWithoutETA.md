# V1DispatchRouteWithoutETA

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispatch_jobs** | [**list[V1DispatchJobWithoutETA]**](V1DispatchJobWithoutETA.md) | The dispatch jobs associated with this route. | [optional] 
**id** | **int** | ID of the Samsara dispatch route. | [optional] 
**actual_end_ms** | **int** | The time in Unix epoch milliseconds that the route actually ended. | [optional] 
**actual_start_ms** | **int** | The time in Unix epoch milliseconds that the route actually started. | [optional] 
**driver_id** | **int** | ID of the driver assigned to the dispatch route. Note that driver_id and vehicle_id are mutually exclusive. If neither is specified, then the route is unassigned. | [optional] 
**group_id** | **int** | Deprecated. | [optional] 
**name** | **str** | Descriptive name of this route. | [optional] 
**notes** | **str** | Notes regarding the details of this route; maximum of 2000 characters; newline characters (&#39;\\n&#39;)can be used for formatting. | [optional] 
**odometer_end_meters** | **int** | Odometer reading at the end of the route. Will not be returned if Route is not completed or if Odometer information is not available for the relevant vehicle. | [optional] 
**odometer_start_meters** | **int** | Odometer reading at the start of the route. Will not be returned if Route has not started or if Odometer information is not available for the relevant vehicle. | [optional] 
**scheduled_end_ms** | **int** | The time in Unix epoch milliseconds that the last job in the route is scheduled to end. | [optional] 
**scheduled_meters** | **int** | The distance expected to be traveled for this route in meters. | [optional] 
**scheduled_start_ms** | **int** | The time in Unix epoch milliseconds that the route is scheduled to start. | [optional] 
**start_location_address** | **str** | The address of the route&#39;s starting location, as it would be recognized if provided to maps.google.com. Optional if a valid start location address ID is provided. | [optional] 
**start_location_address_id** | **int** | ID of the start location associated with an address book entry. Optional if valid values are provided for start location address and latitude/longitude. If a valid start location address ID is provided, address/latitude/longitude will be used from the address book entry. Name of the address book entry will only be used if the start location name is not provided. | [optional] 
**start_location_lat** | **float** | Latitude of the start location in decimal degrees. Optional if a valid start location address ID is provided. | [optional] 
**start_location_lng** | **float** | Longitude of the start location in decimal degrees. Optional if a valid start location address ID is provided. | [optional] 
**start_location_name** | **str** | The name of the route&#39;s starting location. If provided, it will take precedence over the name of the address book entry. | [optional] 
**trailer_id** | **int** | ID of the trailer assigned to the dispatch route. Note that trailers can only be assigned to routes that have a Vehicle or Driver assigned to them. | [optional] 
**vehicle_id** | **int** | ID of the vehicle assigned to the dispatch route. Note that vehicle_id and driver_id are mutually exclusive. If neither is specified, then the route is unassigned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

