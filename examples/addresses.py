from __future__ import print_function
import sys
import samsara

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

# Define a new Address object.
new_address = samsara.CreateAddressRequest(
    name="SF6",
    formatted_address="350 Rhode Island Street, Suite 300s San Francisco, CA 94103",
    geofence=samsara.AddressGeofence(
        circle=samsara.AddressGeofenceCircle(
            radius_meters=25
        )
    ),
    external_ids={
        'externalsystem': 'ABC123'
    }
)
# Call the API
res = api.create_address(new_address)
# Save the new address's Samsara ID
new_address_id = res.data.id
print("CREATED NEW ADDRESS WITH ID: {id}".format(id=new_address_id))

# List all addresses
print("ALL ADDRESSES:")
cursor = None
has_next_page = True
while has_next_page:
    res = api.list_addresses(after=cursor)
    for address in res.data:
        print(address.name)
        print(address.formatted_address)
        print("=======================")
    cursor = res.pagination.end_cursor
    has_next_page = res.pagination.has_next_page

# Retrieve the newly created address
res = api.get_address(new_address_id)
print("NEWLY CREATED ADDRESS:")
print(res.data)

# Define an update to the newly created address
# This update adds another external ID
address_updates = samsara.UpdateAddressRequest(
    external_ids={
        'routeplanning': '123ABC'
    }
)
# Call the API to update the address,
# using the `mysystem` external ID to indicate which address to update
res = api.update_address("externalsystem:ABC123", address_updates)
print("ADDRESS UPDATED. NEW LIST OF EXTERNAL IDS:")
print(res.data.external_ids)

# Delete the newly created address by its new external ID
res = api.delete_address("routeplanning:123ABC")
if res is None:
    print("Successfully deleted new address.")