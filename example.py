from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint


# Authorization info
with open("token", "r") as f:
    token = f.read()
# Create an ApiClient
api_client = samsara.ApiClient(header_name="Authorization",
    header_value="Bearer "+token)

# Create an instance of the Addresses API class
api_instance = samsara.AddressesApi(api_client)

# Create an address 
address = samsara.AddressCreate()

try:
    # Create an address
    api_response = api_instance.create_address()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->create_address: %s\n" % e)