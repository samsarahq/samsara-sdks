from __future__ import print_function
import sys
import samsara
import time

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

# Follow a feed of vehicle locations indefinitely
cursor = None
while True:
    res = api.get_vehicle_locations_feed(after=cursor)
    for vehicle in res.data:
        print('New data available for: {vehicle.name}!'.format(vehicle=vehicle))
        for location in vehicle.locations:
            print('''
                latitude: {location.latitude}
                longitude: {location.longitude}
                heading: {location.heading}
                speed: {location.speed}
                reverse_geo: {location.reverse_geo.formatted_location}
                time: {location.time}
                ======================================================
            '''.format(location=location))
    cursor = res.pagination.end_cursor
    if not res.pagination.has_next_page:
        print('Waiting for new data...')
        time.sleep(5)
