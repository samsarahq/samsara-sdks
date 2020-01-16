from __future__ import print_function
import datetime
import openapi_client
from openapi_client.rest import ApiException


# Create an instance of the openapi_client
# configuration = openapi_client.Configuration()
with open('token', 'r') as f:
    # configuration.api_key_prefix["Authorization"] = "Bearer"
    # configuration.api_key["Authorization"] = token.read()
    token = f.read()
client = openapi_client.ApiClient(header_name='Authorization', header_value=f'Bearer {token}')

# Create an instance of some APIs
routes_api = openapi_client.RoutesApi(api_client=client)
addresses_api = openapi_client.AddressesApi(api_client=client)

# Get addresses
addresses = []
try:
    cursor = None
    has_next_page = True
    while has_next_page:
        resp = addresses_api.get_addresses(after=cursor)
        addresses.extend(resp["data"])
        cursor = resp["pagination"]["endCursor"]
        has_next_page = resp["pagination"]["hasNextPage"]
except ApiException as e:
    print(e)

# Search for addresses function
def find_address_id(name, addresses):
    return list(filter(lambda address: address["name"] == name, addresses))[0]["id"]

# Convert to from datetime to milliseconds
def ms(datetime):
    return int(datetime.timestamp()*1000)

# Create a route from SF6 to SJ1 and then delete it
try:
    route = openapi_client.V1DispatchRouteCreate(
        dispatch_jobs=[
            openapi_client.V1DispatchJobCreate(
                destination_address_id=find_address_id('SF6', addresses),
                scheduled_arrival_time_ms=ms(datetime.datetime.now() + datetime.timedelta(days=1, hours=1))
            )
        ],
        name="SF6 to SJ1",
        scheduled_start_ms=ms(datetime.datetime.now() + datetime.timedelta(days=1)),
        start_location_address_id=find_address_id('SJ1', addresses)
    )
    resp = routes_api.v1create_dispatch_route(route)
    print(resp)
    resp = routes_api.v1delete_dispatch_route_by_id(resp.id)
    print(resp)
except ApiException as e:
    print(e)
