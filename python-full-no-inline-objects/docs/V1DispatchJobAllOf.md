# V1DispatchJobAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrived_at_ms** | **int** | The time at which the driver arrived at the job destination. | [optional] 
**completed_at_ms** | **int** | The time at which the job was marked complete (e.g. started driving to the next destination). | [optional] 
**dispatch_route_id** | **int** | ID of the route that this job belongs to. | 
**documents** | [**list[V1DispatchJobDocumentInfo]**](V1DispatchJobDocumentInfo.md) | Document submissions associated with this job. | [optional] 
**driver_id** | **int** | ID of the driver assigned to the dispatch job. | [optional] 
**en_route_at_ms** | **int** | The time at which the assigned driver started fulfilling the job (e.g. started driving to the destination). | [optional] 
**estimated_arrival_ms** | **int** | The time at which the assigned driver is estimated to arrive at the job destination. Only valid for en-route jobs. | [optional] 
**fleet_viewer_url** | **str** | Fleet viewer url of the dispatch job. | [optional] 
**group_id** | **int** | Deprecated. | [optional] 
**id** | **int** | ID of the Samsara dispatch job. | 
**job_state** | [**V1jobStatus**](V1jobStatus.md) |  | 
**skipped_at_ms** | **int** | The time at which the job was marked skipped. | [optional] 
**vehicle_id** | **int** | ID of the vehicle used for the dispatch job. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


