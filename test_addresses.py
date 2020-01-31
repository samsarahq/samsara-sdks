import samsara_test

with open('token', 'r') as f:
    token = f.read()
# Create an ApiClient with an API access `token`. You can provide your access token to the variable `token` below.
client = samsara_test.ApiClient(header_name='Authorization', header_value='Bearer {token}'.format(token=token))

# Create an instance of the Api
api = samsara_test.AddressesApi(api_client=client)

# Create Address
address = samsara_test.CreateAddressRequest(
    external_ids={
        "system1": "1234",
        "system2": "5678"
    },
    geofence=samsara_test.AddressGeofence(
        circle=samsara_test.AddressGeofenceCircle(
            radius_meters=25
        )
    ),
    address_types=[
        "yard"
    ],
    formatted_address="350 Rhode Island St, San Francisco, CA",
    name="Testing SDK",
    notes="Testing SDK",
    contact_ids=[
        "146128"
    ],
    tag_ids=[
        "967208"
    ]
)
resp = api.create_address(address)
address_id = resp.data.id

# Get Address
api.get_address(address_id)

# List Addresses
api.list_addresses()

# Update Address
address_updates = samsara_test.UpdateAddressRequest(
    external_ids={
        "system3": "0987"
    }
)
api.update_address(address_id, address_updates)

# Delete Address
api.delete_address(address_id)
