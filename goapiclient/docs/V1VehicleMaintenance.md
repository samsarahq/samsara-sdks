# V1VehicleMaintenance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int64** | ID of the vehicle. | 
**J1939** | Pointer to [**V1VehicleMaintenanceJ1939**](V1VehicleMaintenance_j1939.md) |  | [optional] 
**Passenger** | Pointer to [**V1VehicleMaintenancePassenger**](V1VehicleMaintenance_passenger.md) |  | [optional] 

## Methods

### GetId

`func (o *V1VehicleMaintenance) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1VehicleMaintenance) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1VehicleMaintenance) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1VehicleMaintenance) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetJ1939

`func (o *V1VehicleMaintenance) GetJ1939() V1VehicleMaintenanceJ1939`

GetJ1939 returns the J1939 field if non-nil, zero value otherwise.

### GetJ1939Ok

`func (o *V1VehicleMaintenance) GetJ1939Ok() (V1VehicleMaintenanceJ1939, bool)`

GetJ1939Ok returns a tuple with the J1939 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasJ1939

`func (o *V1VehicleMaintenance) HasJ1939() bool`

HasJ1939 returns a boolean if a field has been set.

### SetJ1939

`func (o *V1VehicleMaintenance) SetJ1939(v V1VehicleMaintenanceJ1939)`

SetJ1939 gets a reference to the given V1VehicleMaintenanceJ1939 and assigns it to the J1939 field.

### GetPassenger

`func (o *V1VehicleMaintenance) GetPassenger() V1VehicleMaintenancePassenger`

GetPassenger returns the Passenger field if non-nil, zero value otherwise.

### GetPassengerOk

`func (o *V1VehicleMaintenance) GetPassengerOk() (V1VehicleMaintenancePassenger, bool)`

GetPassengerOk returns a tuple with the Passenger field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasPassenger

`func (o *V1VehicleMaintenance) HasPassenger() bool`

HasPassenger returns a boolean if a field has been set.

### SetPassenger

`func (o *V1VehicleMaintenance) SetPassenger(v V1VehicleMaintenancePassenger)`

SetPassenger gets a reference to the given V1VehicleMaintenancePassenger and assigns it to the Passenger field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


