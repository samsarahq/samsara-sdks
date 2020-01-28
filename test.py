import samsara

with open('token', 'r') as f:
    # configuration.api_key_prefix["Authorization"] = "Bearer"
    # configuration.api_key["Authorization"] = token.read()
    token = f.read()
client = samsara.ApiClient(header_name='Authorization', header_value=f'Bearer {token}')

# Create an instance of the VehiclesAPI
api = samsara.VehiclesApi(api_client=client)

print(api.get_vehicle_stats_feed(types="engineStates"))
