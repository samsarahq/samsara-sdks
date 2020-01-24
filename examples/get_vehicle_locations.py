from __future__ import print_function
import time
import samsara
import sys

try:
    token = sys.argv[1]
except IndexError as e:
    print('Please provide an access token. For example:')
    print(f'python {sys.argv[0]} 2YotnFZFEjr1zCsicMWpAA')
    sys.exit()

# Create an ApiClient
client = samsara.ApiClient(header_name='Authorization', header_value=f'Bearer {token}')

# Create an instance of the VehiclesAPI
api = samsara.VehiclesApi(api_client=client)

# Get vehicle locations
cursor = None
for i in range(5):
    resp = api.get_vehicle_locations_feed(after=cursor)
    for vehicle in resp.data:
        print(f'New data available for: {vehicle.name}!')
        for location in vehicle.locations:
            print(f'    latitude: {location.latitude}')
            print(f'    longitude: {location.longitude}')
            print(f'    heading: {location.heading}')
            print(f'    speed: {location.speed}')
            print(f'    time: {location.time}')
            print('====================================')
    cursor = resp.pagination.end_cursor
    if not resp.pagination.has_next_page:
        print('Waiting for new data...')
        time.sleep(5)
