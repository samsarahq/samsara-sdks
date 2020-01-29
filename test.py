import samsara_test

with open('token', 'r') as f:
    token = f.read()
# Create an ApiClient with an API access `token`. You can provide your access token to the variable `token` below.
client = samsara_test.ApiClient(header_name='Authorization', header_value='Bearer {token}'.format(token=token))

# Create an instance of the Api
api = samsara_test.DefaultApi(api_client=client)

print("=======================================================================")

# List Addresses
resp = api.get_addresses()
print("List Addresses Response:")
print(resp)
print("=======================================================================")

# Create Address
new_address = samsara_test.NewAddress(
    external_ids={
        "system1": "1234",
        "system2": "5678"
    },
    geofence=samsara_test.AddressCoreGeofence(
        circle=samsara_test.AddressCoreGeofenceCircle(
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
print(new_address)
resp = api.create_address(address=new_address)
new_address_id = resp.data.id
print("Create Address Response:")
print(resp)
print("=======================================================================")

# Read Address
resp = api.get_address_by_id(new_address_id)
print("Read Address Response:")
print(resp)
print("=======================================================================")

# Update Address
address_updates = samsara_test.AddressUpdates(
    external_ids={
        "system3": "0987"
    }
)
resp = api.update_address_by_id(new_address_id, address=address_updates)
print("Update Address Response:")
print(resp)
print("=======================================================================")

# Delete Address
resp = api.delete_address_by_id(new_address_id)
print("Delete Address Response:")
print(resp)
print("=======================================================================")
