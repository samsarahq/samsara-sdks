# TagUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**list[TaggedObjectId]**](TaggedObjectId.md) | The addresses that belong to this tag. | [optional] 
**assets** | [**list[TaggedObjectId]**](TaggedObjectId.md) | The trailers, unpowered, and powered assets that belong to this tag. | [optional] 
**drivers** | [**list[TaggedObjectId]**](TaggedObjectId.md) | The drivers that belong to this tag. | [optional] 
**machines** | [**list[TaggedObjectId]**](TaggedObjectId.md) | The machines that belong to this tag. | [optional] 
**name** | **str** | Name of this tag. Must be unique. | 
**parent_tag_id** | **str** | If this tag is part a hierarchical tag tree, this is the ID of the parent tag, otherwise this will be omitted. | [optional] 
**sensors** | [**list[TaggedObjectId]**](TaggedObjectId.md) | The sensors that belong to this tag. | [optional] 
**vehicles** | [**list[TaggedObjectId]**](TaggedObjectId.md) | The vehicles that belong to this tag. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

