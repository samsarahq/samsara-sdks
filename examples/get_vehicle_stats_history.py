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

# Stat mappings
stat_mappings = {
    'engineStates': 'engine_states',
    'fuelPercents': 'fuel_percents',
    'obdOdometerMeters': 'obd_odometer_meters',
    'gpsOdometerMeters': 'gps_odometer_meters',
    'obdEngineSeconds': 'obd_engine_seconds',
    'gpsDistanceMeters': 'gps_distance_meters'
}

# Get desired stat type
stat_type = ''
while stat_type not in ['engineStates', 'fuelPercents', 'obdOdometerMeters', 'gpsOdometerMeters', 'obdEngineSeconds', 'gpsDistanceMeters']:
    print('Please enter one of the following stat types:')
    print('''
        - engineStates
        - fuelPercents
        - obdOdometerMeters
        - gpsOdometerMeters
        - obdEngineSeconds
        - gpsDistanceMeters
    ''')
    stat_type = input('--> ')

# Create an ApiClient
client = samsara.ApiClient(
    header_name='Authorization',
    header_value='Bearer {token}'.format(token=token))

# Create an instance of the API
api = samsara.DefaultApi(api_client=client)

# Get vehicle stats for the last 24 hours
end_time = datetime.now(tzlocal())
start_time = end_time - timedelta(days=1)
cursor = None
has_next_page = True
while has_next_page:
    res = api.get_vehicle_stats_history(
        types=[stat_type],
        start_time=start_time,
        end_time=end_time,
        after=cursor)
    for vehicle in res.data:
        for stat_point in getattr(vehicle, stat_mappings[stat_type]):
            print('''
                value: {stat_point.value}
                time: {stat_point.time}
                ======================================================
            '''.format(stat_point=stat_point))
    cursor = res.pagination.end_cursor
    has_next_page = res.pagination.has_next_page
