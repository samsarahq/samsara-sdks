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

# Define a new Tag object.
ca_tag = samsara.CreateTagRequest(
    name="California"
)
# Call the API
res = api.create_tag(ca_tag)
# Save the new tag's Samsara ID
ca_tag_id = res.data.id
print("created {name} tag".format(name=res.data.name))

# Define some child Tags
sf_tag = samsara.CreateTagRequest(
    name="San Francisco",
    parent_tag_id=ca_tag_id
)
sj_tag = samsara.CreateTagRequest(
    name="San Jose",
    parent_tag_id=ca_tag_id
)
# Call the API and save the new tag IDs
res = api.create_tag(sf_tag)
sf_tag_id = res.data.id
print("created {name} tag".format(name=res.data.name))
res = api.create_tag(sj_tag)
sj_tag_id = res.data.id
print("created {name} tag".format(name=res.data.name))

# Add some vehicles to the tags using the replace_tag function
print("getting list of vehicles...")
vehicle_ids = []
cursor = None
has_next_page = True
while has_next_page:
    res = api.list_vehicles(after=cursor)
    for vehicle in res.data:
        vehicle_ids.append(vehicle.id)
    cursor = res.pagination.end_cursor
    has_next_page = res.pagination.has_next_page

sf_vehicles = vehicle_ids[:len(vehicle_ids)//2]
sj_vehicles = vehicle_ids[len(vehicle_ids)//2:]

sf_tag = api.get_tag(sf_tag_id).data
sj_tag = api.get_tag(sj_tag_id).data

sf_tag.vehicles = sf_vehicles
sj_tag.vehicles = sj_vehicles

res = api.replace_tag(sf_tag_id, sf_tag)
print("Added {name} vehicles to {name} tag".format(name=res.data.name))
res = api.replace_tag(sj_tag_id, sj_tag)
print("Added {name} vehicles to {name} tag".format(name=res.data.name))

# Create an address and add it to a tag
tag_address = samsara.CreateAddressRequest(
    name="Tag Address",
    formatted_address="350 Rhode Island Street, Suite 300s San Francisco, CA 94103",
    geofence=samsara.AddressGeofence(
        circle=samsara.AddressGeofenceCircle(
            radius_meters=25
        )
    ),
    tag_ids=[sf_tag_id]
)
# Call API
res = api.create_address(tag_address)
# Save address ID
tag_address_id = res.data.id

# List all tags
print("Tags:")
cursor = None
has_next_page = True
while has_next_page:
    res = api.list_tags(after=cursor)
    for tag in res.data:
        print("""
            {name}:
                Number of vehicles: {vehicles}
                Number of assets: {assets}
                Number of drivers: {drivers}
                Number of addresses: {addresses}
                Number of sensors: {sensors}
                Number of machines: {machines}
        """.format(
            name=tag.name,
            vehicles=len(tag.vehicles),
            assets=len(tag.assets),
            drivers=len(tag.drivers),
            addresses=len(tag.addresses),
            sensors=len(tag.sensors),
            machines=len(tag.machines)))
    cursor = res.pagination.end_cursor
    has_next_page = res.pagination.has_next_page

# Delete tags
res = api.delete_tag(ca_tag_id)
if res is None:
    print("Deleted California tag")
res = api.delete_tag(sf_tag_id)
if res is None:
    print("Deleted San Francisco tag")
res = api.delete_tag(sj_tag_id)
if res is None:
    print("Deleted San Jose tag")

# Delete demo address
res = api.delete_address(tag_address_id)
if res is None:
    print("Deleted demo address")
