from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint


# Create an instance of the API class
#api_instance = openapi_client.AddressesApi(openapi_client.ApiClient(configuration=None, header_name="Authorization", header_value="Bearer <REDACTED>"))
api_instance = openapi_client.VehiclesApi(openapi_client.ApiClient(configuration=None, header_name="Authorization", header_value="Bearer <REDACTED>"))
#api_instance = openapi_client.UsersApi(openapi_client.ApiClient(configuration=None, header_name="Authorization", header_value="Bearer <REDACTED>"))
#api_instance = openapi_client.DriversApi(openapi_client.ApiClient(configuration=None, header_name="Authorization", header_value="Bearer <REDACTED>"))
#api_instance = openapi_client.TagsApi(openapi_client.ApiClient(configuration=None, header_name="Authorization", header_value="Bearer <REDACTED>"))
#api_instance = openapi_client.RoutesApi(openapi_client.ApiClient(configuration=None, header_name="Authorization", header_value="Bearer <REDACTED>"))

# try:
#     # List all addresses
#     api_response = api_instance.get_addresses()
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling AddressesApi->get_addresses: %s\n" % e)

# try:
#     # List all user roles
#     api_response = api_instance.get_user_roles()
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling UsersApi->get_user_roles: %s\n" % e)

# try:
#     # List all Routes
#     api_response = api_instance.v1fetch_all_dispatch_routes()
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling RoutesApi->v1_fetch_all_dispatch_routes: %s\n" % e)

try:
    # Get all vehicle stats
    api_response = api_instance.get_vehicle_stats_feed(types="engineStates")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->get_vehicle_stats_feed: %s\n" % e)

# try:
#     # Get all vehicle stats
#     api_response = api_instance.get_vehicle_locations()
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling VehiclesApi->get_vehicle_locations: %s\n" % e)


# try:
#     # Get 1137933 driver.
#     api_response = api_instance.get_driver_by_id(id="1137933")
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling DriversApi->get_drivers: %s\n" % e)

# try:
#     # Get all tags.
#     api_response = api_instance.get_all_tags()
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling TagsApi->get_all_tags: %s\n" % e)

# try:
#     # Update an address
#     address = openapi_client.AddressPatch(name="hey new address")
#     api_response = api_instance.update_address_by_id(id="7232585", address=address)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling AddressesApi->create_addresses: %s\n" % e)