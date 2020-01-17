# UserUpdate

The user update arguments
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | The authentication type the user uses to authenticate. To use SAML this organization must have a configured SAML integration. | [optional] 
**name** | **str** | The first and last name of the user. | [optional] 
**roles** | [**list[UserRoleInput]**](UserRoleInput.md) | The roles for this user. Users must have at least a single role to be a part of an organization. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


