from __future__ import print_function
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

# Create an instance of the VehiclesAPI
api = samsara.VehiclesApi(api_client=client)

# Get vehicle locations
cursor = None
while True:
    resp = api.get_vehicle_locations_feed(after=cursor)
    for vehicle in resp.data:
        print('New data available for: {vehicle.name}!'.format(vehicle=vehicle))
        for location in vehicle.locations:
            print('    latitude: {location.latitude}'.format(location=location))
            print('    longitude: {location.longitude}'.format(location=location))
            print('    heading: {location.heading}'.format(location=location))
            print('    speed: {location.speed}'.format(location=location))
            print('    time: {location.time}'.format(location=location))
            print('====================================')
    cursor = resp.pagination.end_cursor
    if not resp.pagination.has_next_page:
        print('Waiting for new data...')
        time.sleep(5)
