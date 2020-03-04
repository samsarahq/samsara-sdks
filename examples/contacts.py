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

# Define a new Contact object
new_contact = samsara.CreateContactRequest(
    first_name="Sam",
    last_name="Saurus",
    email="sam.saurus@email.com",
    phone="1234567890"
)
# Call API
res = api.create_contact(new_contact)
# Save new contact ID
new_contact_id = res.data.id
print("Created new contact {id}: {first_name} {last_name}, {email}, {phone}".format(
    id=res.data.id,
    first_name=res.data.first_name,
    last_name=res.data.last_name,
    email=res.data.email,
    phone=res.data.phone
))

# List all contacts
print("Contacts:")
cursor = None
has_next_page = True
while has_next_page:
    res = api.list_contacts(after=cursor)
    for contact in res.data:
        print("{first_name} {last_name}, {email}, {phone}".format(
            first_name=contact.first_name,
            last_name=contact.last_name,
            email=contact.email,
            phone=contact.phone
        ))
    cursor = res.pagination.end_cursor
    has_next_page = res.pagination.has_next_page

# Update the new contact
# This example unsets the email for the contact
contact_updates = samsara.UpdateContactRequest(
    email=""
)
# Call the API
res = api.update_contact(new_contact_id, contact_updates)
print("Updated contact {id} by unsetting email to: {email}".format(
    id=res.data.id,
    email=res.data.email
))

# Get the contact
res = api.get_contact(new_contact_id)
print("Contact {id}: {first_name} {last_name}, {email}, {phone}".format(
    id=res.data.id,
    first_name=res.data.first_name,
    last_name=res.data.last_name,
    email=res.data.email,
    phone=res.data.phone
))

# Delete the contact
res = api.delete_contact(new_contact_id)
if res is None:
    print("Deleted the contact")
