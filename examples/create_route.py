from __future__ import print_function
import datetime
import time
import samsara
import sys

try:
    token = sys.argv[1]
except IndexError as e:
    print('Please provide an access token. For example:')
    print('python {program} <access token>'.format(program=sys.argv[0]))
    sys.exit()

# Create an ApiClient
client = samsara.ApiClient(header_name='Authorization', header_value='Bearer {token}'.format(token=token))

# Create an instance of some APIs
routes_api = samsara.RoutesApi(api_client=client)
addresses_api = samsara.AddressesApi(api_client=client)

# Create some addresses for use in a route
address_ids = {}
sf6 = samsara.AddressCreate(
    name="SF6",
    formatted_address="350 Rhode Island St, San Francisco, CA",
    geofence=samsara.AddressGeofenceRequest(
        circle=samsara.AddressGeofenceRequestCircle(
            radius_meters=25
        )
    )
)
resp = addresses_api.create_address(address=sf6)
address_ids['SF6'] = resp.data.id

sj1 = samsara.AddressCreate(
    name="SJ1",
    formatted_address="99 S Almaden Blvd, San Jose, CA",
    geofence=samsara.AddressGeofenceRequest(
        circle=samsara.AddressGeofenceRequestCircle(
            radius_meters=25
        )
    )
)
resp = addresses_api.create_address(address=sj1)
address_ids['SJ1'] = resp.data.id

# Create a route from SF6 to SJ1 and then delete everything for cleanup
route = samsara.V1DispatchRouteCreate(
    name="SF6 to SJ1",
    start_location_address_id=address_ids['SF6'],
    scheduled_start_ms=(time.time() + datetime.timedelta(days=1).total_seconds())*1000,
    dispatch_jobs=[
        samsara.V1DispatchJobCreate(
            destination_address_id=address_ids['SJ1'],
            scheduled_arrival_time_ms=(time.time() + datetime.timedelta(days=1, hours=1).total_seconds())*1000
        )
    ],
)
resp = routes_api.v1create_dispatch_route(route)
print(resp)
routes_api.v1delete_dispatch_route_by_id(resp.id)
addresses_api.delete_address_by_id(address_ids['SF6'])
addresses_api.delete_address_by_id(address_ids['SJ1'])
