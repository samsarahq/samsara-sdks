from __future__ import print_function
import sys
import samsara

try:
    token = sys.argv[1]
except IndexError as e:
    print('Please provide an access token. For example:')
    print('python {program} <access token>'.format(program=sys.argv[0]))
    sys.exit()

# Stat mappings
stat_mappings = {
    'engineStates': 'engine_state',
    'fuelPercents': 'fuel_percent',
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

# Get the last the last known location for each vehicle
cursor = None
has_next_page = True
while has_next_page:
    res = api.get_vehicle_stats(types=[stat_type], after=cursor)
    for vehicle in res.data:
        print('''
            {vehicle.name}:
                {stat_type}: {stat_point.value}
                {stat_point.time}
                ==============================================================
        '''.format(vehicle=vehicle, stat_type=stat_mappings[stat_type], stat_point=getattr(vehicle, stat_mappings[stat_type])))
    cursor = res.pagination.end_cursor
    has_next_page = res.pagination.has_next_page
