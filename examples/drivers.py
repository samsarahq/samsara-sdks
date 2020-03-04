################################################################################
## NOTE: DRIVERS CANNOT BE DELETED. THEY CAN ONLY BE MADE 'INACTIVE'.         ##
##       ONLY RUN THIS PROGRAM IF YOU TRULY WISH TO CREATE A DRIVER.          ##
################################################################################

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

# Define the new Driver object.
new_driver = samsara.CreateDriverRequest(
    name='Driver Danielle',
    username='driver.danielle',
    password='hideyourpassword',
    license_number='A1234567', # optional
    license_state='CA', # optional
    phone='1234567890', # optional
    timezone='America/Los_Angeles', # optional
    external_ids={ # optional list of external identifier (key, value) pairs
        'email': 'driver.danielle@email.com'
    }
)
# Call the API
# NOTE: THE DRIVER CANNOT BE DELETED. It can only be deactivated.
res = api.create_driver(new_driver)
# Save the new driver's Samsara ID and email
new_driver_id = res.data.id
new_driver_email = res.data.external_ids['email']
print("CREATED NEW DRIVER WITH ID: {id}".format(id=new_driver_id))

# List all driver names and emails if they exist
print("PRINTING ALL DRIVERS NAMES AND EMAILS:")
cursor = None
has_next_page = True
while has_next_page:
    res = api.list_drivers(after=cursor)
    for driver in res.data:
        if driver.external_ids is not None:
            email = driver.external_ids.get('email', None)
        else:
            email = None
        print('{name}, email: {email}'.format(
            name=driver.name, 
            email=email))
    cursor = res.pagination.end_cursor
    has_next_page = res.pagination.has_next_page

# Retrieve the newly created driver
res = api.get_driver(new_driver_id)
print("NEWLY CREATED DRIVER:")
print(res.data)

# Retrieve the newly created driver by their external ID
res = api.get_driver('email:{email}'.format(email=new_driver_email))
print("NEWLY CREATED DRIVER EMAIL:")
print(res.data.external_ids['email'])

# Define an update to the newly created driver
# This update changes the driver's name and adds another external ID
driver_updates = samsara.UpdateDriverRequest(
    name="Captain Danielle",
    external_ids={
        'mysystem': 'ABC123'
    }
)
# Call the API to update the driver
res = api.update_driver(new_driver_id, driver_updates)
print("DRIVER NAME CHANGED TO: {driver.name} UDPATED AT {driver.updated_at_time} WITH EXTERNAL IDS:".format(driver=res.data))
print(res.data.external_ids)