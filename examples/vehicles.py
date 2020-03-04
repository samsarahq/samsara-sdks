from __future__ import print_function
import sys
import samsara

try:
    token = sys.argv[1]
except IndexError as e:
    print('Please provide an access token. For example:')
    print('python {program} <access token>'.format(program=sys.argv[0]))
    sys.exit()

# Create an ApiClient
client = samsara.ApiClient(
    header_name='Authorization',
    header_value='Bearer {token}'.format(token=token))

# Create an instance of the API
api = samsara.DefaultApi(api_client=client)

# List all vehicles
# Save their Samsara IDs in a VIN:ID dictionary
# Save the Samsara IDs of any vehicles without VINs
vin_to_id = {}
vehicles_with_no_vins = []
cursor = None
has_next_page = True
while has_next_page:
    res = api.list_vehicles(after=cursor)
    for vehicle in res.data:
        print(vehicle.name)
        if vehicle.vin is not None:
            print("VIN: {vin}".format(vin=vehicle.vin))
            vin_to_id[vehicle.vin] = vehicle.id
        else:
            print("Vehicle does not have a VIN")
            vehicles_with_no_vins.append(vehicle.id)
        print("======================================")
    cursor = res.pagination.end_cursor
    has_next_page = res.pagination.has_next_page

# Update all the vehicles with VIN external IDs
for vin in vin_to_id:
    vehicle_update_request = samsara.UpdateVehicleRequest(
        external_ids={
            'vin': vin
        }
    )
    api.update_vehicle(vin_to_id[vin], vehicle_update_request)

# Retrieve a vehicle by its VIN
arbitrary_vin = list(vin_to_id)[0]
res = api.get_vehicle("vin:{vin}".format(vin=arbitrary_vin))
print(res.data)