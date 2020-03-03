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

# Get the last the last known location for each vehicle
cursor = None
has_next_page = True
while has_next_page:
    res = api.get_vehicle_locations(after=cursor)
    for vehicle in res.data:
        print('''
            {vehicle.name}:
                latitude: {vehicle.location.latitude}
                longitude: {vehicle.location.longitude}
                heading: {vehicle.location.heading}
                speed: {vehicle.location.speed}
                reverse_geo: {vehicle.location.reverse_geo.formatted_location}
                time: {vehicle.location.time}
                ==============================================================
        '''.format(vehicle=vehicle))
    cursor = res.pagination.end_cursor
    has_next_page = res.pagination.has_next_page
