from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException

# Create an instance of the openapi_client
# configuration = openapi_client.Configuration()
with open('token', 'r') as f:
    # configuration.api_key_prefix["Authorization"] = "Bearer"
    # configuration.api_key["Authorization"] = token.read()
    token = f.read()
client = openapi_client.ApiClient(header_name='Authorization', header_value=f'Bearer {token}')

# Create an instance of the VehiclesAPI
api = openapi_client.VehiclesApi(api_client=client)

# Get vehicle locations
try:
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
except ApiException as e:
    print(e)