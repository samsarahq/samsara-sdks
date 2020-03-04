from __future__ import print_function
import sys
import samsara
from datetime import datetime, timedelta
from dateutil.tz import tzlocal

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

# Get vehicle locations for the last hour
end_time = datetime.now(tzlocal())
start_time = end_time - timedelta(hours=1)
cursor = None
has_next_page = True
while has_next_page:
    res = api.get_vehicle_locations_history(
        start_time=start_time,
        end_time=end_time,
        after=cursor)
    for vehicle in res.data:
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
    has_next_page = res.pagination.has_next_page
